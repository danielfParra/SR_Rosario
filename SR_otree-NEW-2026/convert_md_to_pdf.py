#!/usr/bin/env python
"""Convert markdown file to PDF using fpdf2"""

import markdown
import re
from fpdf import FPDF
from pathlib import Path

# Input and output files
md_file = Path(__file__).parent / "protocol_SR_v2.md"
pdf_file = Path(__file__).parent / "protocol_SR_v2.pdf"

# Read markdown file
with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Create PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set font
pdf.set_font("Helvetica", size=12)

# Process markdown content line by line
lines = md_content.split('\n')
for line in lines:
    line = line.rstrip()
    
    # Skip empty lines (but add spacing)
    if not line.strip():
        pdf.ln(4)
        continue
    
    # Handle headers
    if line.startswith('# '):
        pdf.set_font("Helvetica", 'B', size=18)
        pdf.ln(8)
        pdf.cell(0, 10, line[2:], ln=True)
        pdf.set_font("Helvetica", size=12)
        pdf.ln(4)
    elif line.startswith('## '):
        pdf.set_font("Helvetica", 'B', size=14)
        pdf.ln(6)
        pdf.cell(0, 10, line[3:], ln=True)
        pdf.set_font("Helvetica", size=12)
        pdf.ln(2)
    elif line.startswith('### '):
        pdf.set_font("Helvetica", 'B', size=12)
        pdf.cell(0, 9, line[4:], ln=True)
        pdf.set_font("Helvetica", size=12)
    elif line.startswith('- ') or line.startswith('* '):
        # Bullet point
        pdf.cell(6, 6, '•', ln=False)
        pdf.cell(0, 6, line[2:], ln=True)
    elif line.startswith('  - ') or line.startswith('  * '):
        # Sub-bullet point
        pdf.cell(12, 6, '◦', ln=False)
        pdf.cell(0, 6, line[4:], ln=True)
    elif line.startswith('```'):
        # Code block - skip for now in simple version
        continue
    elif line.startswith('[') or line.startswith('!'):
        # Skip links and images in simple version
        continue
    elif line.startswith('>'):
        # Blockquote
        pdf.set_font("Helvetica", 'I', size=11)
        pdf.cell(10, 6, '', ln=False)
        pdf.cell(0, 6, line[2:], ln=True)
        pdf.set_font("Helvetica", size=12)
    else:
        # Regular text
        # Wrap text if it's too long
        text = line.replace('**', '').replace('__', '').replace('`', '').replace('*', '').replace('_', '')
        
        # Check if line contains bold markers
        if '**' in line or '__' in line:
            # Simple bold handling
            text = re.sub(r'\*\*(.*?)\*\*', r'\1', line)
            text = re.sub(r'__(.*?)__', r'\1', text)
        
        # Remove other markdown
        text = text.replace('`', '').replace('*', '').replace('_', '').replace('[', '').replace(']', '')
        
        if text.strip():
            pdf.multi_cell(0, 6, text)

# Save PDF
pdf.output(str(pdf_file))

print(f"✓ Successfully converted to PDF: {pdf_file}")
print(f"  File size: {pdf_file.stat().st_size / 1024:.1f} KB")
