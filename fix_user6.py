import re

def fix_links_and_cart():
    for fpath in ['c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/home_website.html', 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html', 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/product_detail.html']:
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Update cart link
        html = html.replace('@click="openCart = !openCart"', 'onclick="window.location.href=\'cart_website.html\'"')
        html = html.replace('@click.away="openCart = false"', '') # remove the away click to avoid JS errors
        
        # Remove the cart dropdown from header because it now redirects immediately
        # Dropdown starts with `<div x-show="openCart"`
        html = re.sub(r'<!-- Cart Dropdown -->.*?</div>\s*</div>(?=\s*<div class="relative")', '</div>', html, flags=re.DOTALL)
        # Actually it's safer just to leave the dropdown dead or remove it entirely by replacing `<div x-show="openCart"` with empty
        html = re.sub(r'<div x-show="openCart".*?XEM GIỎ HÀNG</button>\s*</div>\s*</div>', '', html, flags=re.DOTALL)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)


def fix_home():
    path = 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/home_website.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove overflow-hidden from section
    html = re.sub(r'(<section class="rounded-\[2rem\].*?) overflow-hidden', r'\1', html)
    
    # Remove h-full and overflow-hidden from the <a> cards inside flash deals
    # Currently: class="bg-white rounded-[1.2rem] flex flex-col relative shadow-md overflow-hidden h-full group border border-gray-100/50 hover:-translate-y-1 hover:shadow-2xl transition duration-300"
    html = html.replace('shadow-md overflow-hidden h-full group', 'shadow-md group')
    
    # Adjust padding of content card
    html = html.replace('p-4 lg:p-5 flex-1 relative flex flex-col', 'px-4 pb-5 pt-4 flex-1 relative flex flex-col')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
        

def fix_category():
    path = 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    pagination_block = """
                        <!-- Pagination Buttons -->
                        <div class="flex justify-center items-center gap-2 mt-12 bg-white w-max mx-auto p-2 rounded-2xl shadow-sm border border-gray-200">
                            <button class="w-10 h-10 flex items-center justify-center rounded-xl hover:bg-gray-100 text-gray-400 font-medium transition"><i class="fas fa-chevron-left text-[12px]"></i></button>
                            <button class="w-10 h-10 flex items-center justify-center rounded-xl bg-brand text-white font-medium shadow-md text-[14px]">1</button>
                            <button class="w-10 h-10 flex items-center justify-center rounded-xl hover:bg-gray-100 hover:text-brand text-gray-600 font-medium transition text-[14px]">2</button>
                            <button class="w-10 h-10 flex items-center justify-center rounded-xl hover:bg-gray-100 text-gray-400 font-medium transition"><i class="fas fa-chevron-right text-[12px]"></i></button>
                        </div>
    """

    if '<!-- Pagination Buttons -->' not in html:
        # Insert before <!-- TAB CONTENT eGift -->
        html = html.replace('<!-- TAB CONTENT eGift -->', pagination_block + '\n<!-- TAB CONTENT eGift -->')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    fix_links_and_cart()
    fix_home()
    fix_category()
    print("Round 6 applied successfully.")
