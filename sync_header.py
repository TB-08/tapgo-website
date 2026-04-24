import re

# Sync Header from home_website.html to product_detail.html
with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/home_website.html', 'r', encoding='utf-8') as f:
    home_html = f.read()

# Extract from <header> to the closing </div> of the category nav
header_pattern = re.compile(r'<!-- MAIN HEADER -->\s*<header class="bg-white/95 backdrop-blur-md sticky top-0 z-50 relative.*?<div class="bg-white/95 border-t border-gray-100 shadow-sm relative z-40">.*?</div>\s*</div>\s*</div>', re.DOTALL)
header_match = header_pattern.search(home_html)

if header_match:
    header_block = header_match.group(0)
    
    with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/product_detail.html', 'r', encoding='utf-8') as f:
        prod_html = f.read()
        
    old_header_pattern = re.compile(r'<!-- MAIN HEADER -->\s*<header class="bg-white.*?</header>.*?<div class="bg-white/95 border-t border-gray-200.*?</div>\s*</div>\s*</div>', re.DOTALL)
    
    # Alternatively simply find <main class-...> in product_detail and slice everything between `<!-- TOP BAR -->` and `<main>`
    idx_topbar = prod_html.find('<!-- MAIN HEADER -->')
    idx_main = prod_html.find('<main class="')
    
    new_prod_html = prod_html[:idx_topbar] + header_block + '\n\n    ' + prod_html[idx_main:]
    
    # Also add the Modal to body end
    if '<!-- Dùng Ngay Modal -->' not in new_prod_html:
        modal_match = re.search(r'<!-- Dùng Ngay Modal -->.*?</body>', home_html, re.DOTALL)
        if modal_match:
            new_prod_html = new_prod_html.replace('</body>', '\n' + modal_match.group(0))

    with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/product_detail.html', 'w', encoding='utf-8') as f:
        f.write(new_prod_html)
    print("Header successfully synced to product_detail.html")
else:
    print("Could not extract header from home_website.html")
