import re

with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html', 'r', encoding='utf-8') as f:
    cat_text = f.read()

# 1. Avatar circle fix
avatar_pattern = r'class="w-full h-full object-cover rounded-full"'
cat_text = cat_text.replace(avatar_pattern, 'class="w-full h-full object-cover rounded-full aspect-square"')
cat_text = cat_text.replace('class="absolute -top-5 left-4 w-[42px] h-[42px]', 'class="absolute -top-5 left-4 w-10 h-10')

# 2. Sticky Tab
cat_text = cat_text.replace('top-[140px]', 'top-[75px]')

# 3. Pagination centering
cat_text = cat_text.replace('</template>\n                    </div></div>\n                        <!-- Pagination Buttons -->', '</template>\n                    </div>\n                        <!-- Pagination Buttons -->')

with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html', 'w', encoding='utf-8') as f:
    f.write(cat_text)


new_modal = """
    <!-- Dùng Ngay Modal -->
    <div x-show="openQr" x-transition style="display: none;" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/70 backdrop-blur-sm" @click.away="openQr = false">
        <div class="bg-white rounded-[2rem] shadow-2xl w-[340px] text-center relative overflow-hidden flex flex-col items-center" @click.stop>
            <!-- Orange header -->
            <div class="h-24 bg-brand absolute top-0 inset-x-0 z-0"></div>
            <button @click="openQr = false" class="absolute top-4 right-4 text-white hover:text-gray-200 w-8 h-8 rounded-full bg-white/20 flex items-center justify-center transition z-20 backdrop-blur-sm shadow-sm"><i class="fas fa-times text-sm"></i></button>
            
            <!-- Brand Avatar -->
            <div class="relative z-10 pt-6 px-6 flex flex-col items-center w-full">
                <div class="w-16 h-16 bg-white rounded-2xl shadow-md border-4 border-white overflow-hidden flex items-center justify-center mb-3">
                    <img src="https://images.unsplash.com/photo-1544148103-0773bf10d330?q=80&w=200" class="w-full h-full object-cover">
                </div>
                <h3 class="font-bold text-[17px] text-white mb-1">Yakimono - Thịt Nướng</h3>
                <p class="text-[12px] text-white/90 font-medium mb-5">Combo Gia Đình 4 Người</p>
            </div>
            
            <!-- Ticket Notches -->
            <div class="absolute -left-3 top-[108px] w-6 h-6 bg-black/70 rounded-full z-20" style="box-shadow: inset -3px 0px 5px rgba(0,0,0,0.1)"></div>
            <div class="absolute -right-3 top-[108px] w-6 h-6 bg-black/70 rounded-full z-20" style="box-shadow: inset 3px 0 5px rgba(0,0,0,0.1)"></div>
            
            <!-- Ticket body -->
            <div class="bg-white relative z-10 px-8 pb-8 pt-6 w-full border-t-[2px] border-dashed border-gray-200 mt-2">
                <p class="text-[12px] text-gray-500 mb-4 font-bold uppercase tracking-wider">Đưa mã QR cho thu ngân</p>
                <div class="bg-gray-50 p-4 rounded-2xl mb-5 pb-5 border border-brand/20 w-fit mx-auto shadow-inner group">
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=TAPGO12345" class="w-[180px] h-[180px] mx-auto mix-blend-multiply group-hover:scale-105 transition duration-500">
                </div>
                <p class="text-3xl font-bold tracking-[0.2em] text-gray-900 mb-5 font-mono drop-shadow-sm">TPG-X8A2M</p>
                <div class="flex items-center justify-center gap-2 text-danger bg-red-50 py-3 rounded-xl font-bold text-[14px] w-full border border-red-100 shadow-sm animate-pulse">
                    <i class="fas fa-clock text-lg"></i> Hết hạn sau: 01:59:59
                </div>
            </div>
        </div>
    </div>
</body>"""

for fpath in ['c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/home_website.html', 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html', 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/product_detail.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'p-6 md:p-8 shadow-xl bg-gradient' in html:
        html = re.sub(r'p-6 md:p-8 shadow-xl bg-gradient', 'p-6 md:p-8 pb-12 shadow-xl bg-gradient', html)
    modal_match = re.search(r'<!-- Dùng Ngay Modal -->.*?</body>', html, re.DOTALL)
    if modal_match:
        html = html.replace(modal_match.group(0), new_modal)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
print("Fixes applied successfully to all files.")
