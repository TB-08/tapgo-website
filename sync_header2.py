import re

with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/home_website.html', 'r', encoding='utf-8') as f:
    home_html = f.read()

# Using find to precisely extract the header block
idx_topbar = home_html.find('<!-- MAIN HEADER -->')
idx_main = home_html.find('<main class=')

if idx_topbar != -1 and idx_main != -1:
    header_block = home_html[idx_topbar:idx_main]
    
    with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/product_detail.html', 'r', encoding='utf-8') as f:
        prod_html = f.read()
        
    idx_topbar_prod = prod_html.find('<!-- MAIN HEADER -->')
    idx_main_prod = prod_html.find('<main class=')
    
    new_prod_html = prod_html[:idx_topbar_prod] + header_block + prod_html[idx_main_prod:]
    
    if '<!-- Dùng Ngay Modal -->' not in new_prod_html:
        modal_match = re.search(r'<!-- Dùng Ngay Modal -->.*?</body>', home_html, re.DOTALL)
        if modal_match:
            new_prod_html = new_prod_html.replace('</body>', '\n' + modal_match.group(0))

    with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/product_detail.html', 'w', encoding='utf-8') as f:
        f.write(new_prod_html)
    print("Header sync successful by index slicing.")
else:
    print("Header tags not found.")
