import glob, re
import os

html_files = glob.glob("*.html")
pattern = re.compile(r"<h1 class=""text-3xl font-bold italic tracking-tighter drop-shadow-sm text-gray-900"">\s*TAP\s*<span\s*class=""text-brand"">GO</span>\s*</h1>")

replacement = """<img src="assets/logo.png" alt="TAPGO" class="h-10 md:h-12 object-contain drop-shadow-sm">"""

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = pattern.sub(replacement, content)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)
        
print("Replaced logo in", len(html_files), "files")
