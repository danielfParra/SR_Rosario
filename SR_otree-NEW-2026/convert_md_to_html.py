#!/usr/bin/env python
"""Convert markdown file to HTML (can be printed to PDF from browser)"""

import markdown
from pathlib import Path

# Input and output files
md_file = Path(__file__).parent / "protocol_SR_v2.md"
html_file = Path(__file__).parent / "protocol_SR_v2.html"

# Read markdown file
with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML with extensions
html_content = markdown.markdown(
    md_content, 
    extensions=['toc', 'tables', 'fenced_code', 'codehilite']
)

# Create complete HTML document with styling
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Protocol SR v2</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
            padding: 20px;
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        
        h1 {{
            color: #1a5490;
            border-bottom: 3px solid #1a5490;
            padding-bottom: 15px;
            margin: 40px 0 20px 0;
            font-size: 32px;
        }}
        
        h2 {{
            color: #2c5aa0;
            border-left: 5px solid #2c5aa0;
            padding-left: 15px;
            margin: 30px 0 15px 0;
            font-size: 24px;
        }}
        
        h3 {{
            color: #3d6bb3;
            margin: 20px 0 10px 0;
            font-size: 18px;
        }}
        
        h4 {{
            color: #555;
            margin: 15px 0 8px 0;
            font-size: 15px;
        }}
        
        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        
        ul, ol {{
            margin: 15px 0 15px 40px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            color: #d63384;
        }}
        
        pre {{
            background-color: #f4f4f4;
            border-left: 4px solid #e74c3c;
            padding: 15px;
            margin: 15px 0;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }}
        
        pre code {{
            color: #333;
            padding: 0;
            background-color: transparent;
            font-size: 12px;
        }}
        
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        th {{
            background-color: #2c5aa0;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
        }}
        
        td {{
            border: 1px solid #ddd;
            padding: 12px;
        }}
        
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        tr:hover {{
            background-color: #f0f0f0;
        }}
        
        blockquote {{
            border-left: 4px solid #ddd;
            margin: 20px 0;
            padding-left: 20px;
            color: #666;
            font-style: italic;
        }}
        
        a {{
            color: #1a5490;
            text-decoration: none;
            border-bottom: 1px dotted #1a5490;
        }}
        
        a:hover {{
            border-bottom: 1px solid #1a5490;
            background-color: #f0f7ff;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #ddd;
            margin: 30px 0;
        }}
        
        .toc {{
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 20px;
            margin: 20px 0;
        }}
        
        .toc ul {{
            list-style: none;
            margin-left: 0;
        }}
        
        .toc li {{
            margin: 5px 0;
            margin-left: 20px;
        }}
        
        .toc a {{
            color: #1a5490;
        }}
        
        @media print {{
            body {{
                background-color: white;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
                padding: 0;
                max-width: 100%;
            }}
            
            a {{
                color: #1a5490;
            }}
            
            a:visited {{
                color: #1a5490;
            }}
            
            h1, h2, h3, h4, h5, h6 {{
                page-break-after: avoid;
            }}
            
            ul, ol {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_content}
    </div>
    <script>
        // Optional: Add print functionality
        console.log('To save as PDF: Press Ctrl+P (or Cmd+P on Mac) and select "Save as PDF"');
    </script>
</body>
</html>
"""

# Save HTML
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"✓ Successfully converted to HTML: {html_file}")
print(f"  To save as PDF:")
print(f"  1. Open the HTML file in your browser")
print(f"  2. Press Ctrl+P (or Cmd+P on Mac)")
print(f"  3. Select 'Save as PDF'")
print(f"  4. Choose location and save")
