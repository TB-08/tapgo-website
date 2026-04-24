import re

def update_header():
    cart_button = """
                <!-- Cart Header Icon -->
                <div class="relative z-50">
                    <button @click="openCart = !openCart" class="text-gray-400 hover:text-brand transition w-10 h-10 rounded-full hover:bg-gray-50 flex items-center justify-center -mr-2">
                        <div class="relative">
                            <i class="fas fa-shopping-cart text-[20px]"></i>
                            <span x-show="cartCount > 0" class="absolute -top-2 -right-2 bg-brand border border-white text-white text-[10px] font-bold w-4 h-4 rounded-full flex items-center justify-center z-10" x-text="cartCount"></span>
                        </div>
                    </button>
                    <!-- Cart Dropdown -->
                    <div x-show="openCart" @click.away="openCart = false" x-transition style="display: none;" class="absolute right-0 top-12 w-80 bg-white rounded-2xl shadow-xl border border-gray-100 z-50 overflow-hidden transform origin-top-right">
                        <div class="px-5 py-3 border-b border-gray-100 bg-gray-50 flex justify-between">
                            <h4 class="font-bold text-sm">Giỏ hàng của bạn</h4>
                            <span class="text-xs font-bold text-brand" x-text="cartCount + ' sản phẩm'"></span>
                        </div>
                        <div class="p-8 text-center text-gray-400" x-show="cartCount === 0">
                            <i class="fas fa-shopping-basket text-4xl mb-3 opacity-20"></i>
                            <p class="text-sm font-medium">Chưa có deal nào</p>
                        </div>
                        <div x-show="cartCount > 0" class="max-h-[300px] overflow-y-auto">
                            <!-- Dummy Item logic -->
                            <template x-for="i in cartCount">
                                <div class="px-5 py-3 border-b border-gray-50 flex gap-3">
                                    <div class="w-12 h-12 bg-gray-100 rounded-lg flex-shrink-0">
                                        <img src="https://images.unsplash.com/photo-1544148103-0773bf10d330?q=80&w=200" class="w-full h-full object-cover rounded-lg">
                                    </div>
                                    <div class="flex-1 text-left">
                                        <p class="text-[12px] font-bold text-gray-800 line-clamp-1">Combo Thịt Nướng Yakimono</p>
                                        <p class="text-[12px] font-bold text-brand mt-1"><i class="fas fa-coins text-yellow-500 mr-1"></i>300</p>
                                    </div>
                                </div>
                            </template>
                        </div>
                        <div class="p-3" x-show="cartCount > 0">
                            <button class="w-full py-2.5 bg-brand text-white font-bold rounded-xl shadow-md text-sm">XEM GIỎ HÀNG</button>
                        </div>
                    </div>
                </div>
    """
    
    for fpath in ['c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/home_website.html', 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html', 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/product_detail.html']:
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Inject Cart Button before Notif Bell
        # Original: <!-- Notifiction Bell --> or <button class="relative text-gray-400 hover:text-brand transition w-10 h-10 rounded-full hover:bg-gray-50 flex items-center justify-center">
        html = re.sub(r'(<button class="relative text-gray-400 hover:text-brand transition w-10 h-10 rounded-full hover:bg-gray-50 flex items-center justify-center">.*?<i class="fas bg-transparent fa-bell)', cart_button + r'\1', html, flags=re.DOTALL)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)

def update_home():
    path = 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/home_website.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Rebalance Flash Deal Aspect Ratio
    html = html.replace('aspect-[4/3] bg-gray-100', 'aspect-[16/9] bg-gray-100')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

def update_product():
    path = 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/product_detail.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # 1. Add to Cart button logic
    html = html.replace('<button class="flex-1 py-4 border-2 border-brand text-brand hover:bg-orange-50 font-bold rounded-2xl flex items-center justify-center gap-2 transition text-[15px]">', 
                        '<button @click.prevent="cartCount++; showBuyModal=true" class="flex-1 py-4 border-2 border-brand text-brand hover:bg-orange-50 font-bold rounded-2xl flex items-center justify-center gap-2 transition text-[15px]">')
    
    html = html.replace('<button class="flex-1 py-4 bg-brand hover:bg-brand-hover text-white font-bold rounded-2xl flex items-center justify-center gap-2 transition text-[15px] shadow-[0_8px_20px_rgba(244,129,51,0.3)] hover:shadow-[0_12px_25px_rgba(244,129,51,0.4)] hover:-translate-y-0.5">',
                        '<button @click.prevent="showBuyModal=true" class="flex-1 py-4 bg-brand hover:bg-brand-hover text-white font-bold rounded-2xl flex items-center justify-center gap-2 transition text-[15px] shadow-[0_8px_20px_rgba(244,129,51,0.3)] hover:shadow-[0_12px_25px_rgba(244,129,51,0.4)] hover:-translate-y-0.5">')

    buy_modal = """
    <!-- Success / Buy Modal -->
    <div x-show="showBuyModal" x-transition x-cloak style="display:none;" class="fixed inset-0 z-[110] flex items-center justify-center bg-black/60 backdrop-blur-sm" @click.away="showBuyModal=false">
        <div class="bg-white rounded-3xl shadow-2xl w-[360px] text-center p-8 relative transform transition-all">
            <button @click="showBuyModal=false" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600"><i class="fas fa-times"></i></button>
            <div class="w-20 h-20 bg-green-50 text-green-500 rounded-full flex items-center justify-center mx-auto mb-5">
                <i class="fas fa-check-circle text-4xl"></i>
            </div>
            <h3 class="font-bold text-2xl text-gray-900 mb-2">Thành Công!</h3>
            <p class="text-sm text-gray-500 mb-6 leading-relaxed">Bạn đã thêm Deal vào giỏ hàng thành công. Tiến hành thanh toán bằng TapCoin?</p>
            <div class="space-y-3">
                <button @click="showBuyModal=false; window.location.href='category_website.html'" class="w-full bg-brand text-white font-bold py-3.5 rounded-xl shadow-md"><i class="fas fa-wallet mr-2"></i>Thanh Toán Bằng TapCoin</button>
                <button @click="showBuyModal=false" class="w-full bg-gray-100 text-gray-600 font-bold py-3.5 rounded-xl hover:bg-gray-200 transition">Tiếp Tục Lướt Deal</button>
            </div>
        </div>
    </div>
</body>"""
    html = re.sub(r'</body>', buy_modal, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

def update_category():
    path = 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Change Tab buttons
    html = html.replace('''<button
                        class="bg-brand-bg md:flex-1 border border-brand text-brand px-8 py-3 rounded-xl text-[14px] font-bold flex items-center justify-center gap-2 shadow-inner whitespace-nowrap"><i
                            class="fas fa-ticket-alt text-lg shadow-sm w-8 h-8 flex items-center justify-center bg-brand text-white rounded-md"></i>
                        e-Voucher</button>''', 
                        '''<button @click="currentSortTab = 'eVoucher'"
                        :class="currentSortTab === 'eVoucher' ? 'bg-brand text-white shadow-brand/30' : 'bg-transparent text-gray-500 border border-transparent hover:border-brand/30'"
                        class="flex-1 px-8 py-3 rounded-xl text-[14px] font-bold flex items-center justify-center gap-2 transition whitespace-nowrap"><i
                            class="fas fa-ticket-alt text-lg shadow-sm w-8 h-8 flex items-center justify-center rounded-md" :class="currentSortTab === 'eVoucher' ? 'bg-white text-brand' : 'bg-gray-100 text-gray-400'"></i>
                        e-Voucher</button>''')
    
    html = html.replace('''<button
                        class="bg-transparent md:flex-1 border-2 border-transparent text-gray-500 hover:text-brand hover:border-brand/30 px-8 py-3 rounded-xl text-[14px] font-medium flex items-center justify-center gap-2 transition whitespace-nowrap"><i
                            class="fas fa-gift text-lg w-8 h-8 flex items-center justify-center bg-gray-100 text-gray-400 rounded-md"></i>
                        e-Gift</button>''',
                        '''<button @click="currentSortTab = 'eGift'"
                        :class="currentSortTab === 'eGift' ? 'bg-brand text-white shadow-brand/30' : 'bg-transparent text-gray-500 border border-transparent hover:border-brand/30'"
                        class="flex-1 px-8 py-3 rounded-xl text-[14px] font-bold flex items-center justify-center gap-2 transition whitespace-nowrap"><i
                            class="fas fa-gift text-lg w-8 h-8 flex items-center justify-center rounded-md" :class="currentSortTab === 'eGift' ? 'bg-white text-brand' : 'bg-gray-100 text-gray-400'"></i>
                        e-Gift</button>''')
    
    html = html.replace('''<button
                        class="bg-transparent md:flex-1 border-2 border-transparent text-gray-500 hover:text-brand hover:border-brand/30 px-8 py-3 rounded-xl text-[14px] font-medium flex items-center justify-center gap-2 transition whitespace-nowrap"><i
                            class="fas fa-qrcode text-lg w-8 h-8 flex items-center justify-center bg-gray-100 text-gray-400 rounded-md"></i>
                        Scan Tab</button>''',
                        '''<button @click="currentSortTab = 'scanTab'"
                        :class="currentSortTab === 'scanTab' ? 'bg-brand text-white shadow-brand/30' : 'bg-transparent text-gray-500 border border-transparent hover:border-brand/30'"
                        class="flex-1 px-8 py-3 rounded-xl text-[14px] font-bold flex items-center justify-center gap-2 transition whitespace-nowrap"><i
                            class="fas fa-qrcode text-lg w-8 h-8 flex items-center justify-center rounded-md" :class="currentSortTab === 'scanTab' ? 'bg-white text-brand' : 'bg-gray-100 text-gray-400'"></i>
                        Scan Tab</button>''')

    # Wrap the entire tools and grid in x-show="currentSortTab === 'eVoucher'"
    # Wait, tools + grid + pagination are all below the sorting tabs.
    # The SORTING TABS div ends at line 666 (roughly) -> "Scan Tab</button>\n                </div>\n"
    # Then there is <!-- Tools -->
    
    html = html.replace('<!-- Tools -->', '<!-- TAB CONTENT eVoucher -->\n<div x-show="currentSortTab === \'eVoucher\'" x-transition>\n<!-- Tools -->')
    # Pagination Buttons closes at `</div>`. After it, there's `</div>` for Right Column Grid.
    html = html.replace('<!-- Pagination Buttons -->', '<!-- Pagination Buttons -->\n</div>\n')
    
    # Actually wait. The div structure is delicate. I should wrap it carefully using regex.
    # I'll just append the mock tabs at the end of the col-span-9 div before the closing `</div>`.
    
    mock_tabs = """
                </div> <!-- End eVoucher block -->
                
                <!-- TAB CONTENT eGift -->
                <div x-show="currentSortTab === 'eGift'" x-cloak x-transition>
                    <div class="flex flex-col items-center justify-center py-20 bg-pink-50/50 rounded-2xl border border-pink-100 border-dashed mb-8">
                        <i class="fas fa-gift text-6xl text-pink-300 mb-6 animate-pulse"></i>
                        <h3 class="font-bold text-xl text-gray-800 mb-2">Trung tâm e-Gift Tặng Quà</h3>
                        <p class="text-sm text-gray-500 mb-8 max-w-sm text-center">Gửi tặng Voucher bất ngờ tới bạn bè và người thân qua tính năng e-Gift độc đáo.</p>
                        <button class="bg-pink-500 text-white font-bold py-3 px-8 rounded-xl shadow-md hover:bg-pink-600">Khám Phá E-Gift</button>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <!-- Gift card mock -->
                        <div class="bg-white rounded-[1.2rem] shadow p-5 border-t-8 border-t-pink-400 relative overflow-hidden group">
                           <div class="flex items-center gap-3 mb-4">
                                <div class="w-12 h-12 bg-pink-100 text-pink-500 rounded-full flex justify-center items-center"><i class="fas fa-birthday-cake text-xl"></i></div>
                                <div><p class="font-bold text-gray-800">Set Quà Sinh Nhật</p><p class="text-xs text-brand font-bold">1200 TapCoin</p></div>
                           </div>
                           <button class="w-full py-2 bg-gray-100 text-gray-600 font-bold rounded-lg text-sm hover:bg-pink-50 hover:text-pink-600">Gửi tặng ngay</button>
                        </div>
                    </div>
                </div>
                
                <!-- TAB CONTENT scanTab -->
                <div x-show="currentSortTab === 'scanTab'" x-cloak x-transition>
                    <div class="flex flex-col items-center justify-center py-10 bg-white rounded-2xl shadow-sm border border-gray-100">
                        <img src="https://media.giphy.com/media/xUPGcmNe85ElIbroS4/giphy.gif" class="w-32 h-32 rounded-full object-cover mb-4 opacity-50" style="filter:grayscale(1)">
                        <h3 class="font-bold text-xl text-gray-800 mb-2">Thanh Toán & Quét Tại Chỗ</h3>
                        <p class="text-sm text-gray-500 mb-6">Mở Camera TAPGO APP để quét mã QR tại bàn (Table QR) của cửa hàng đối tác để nhận giảm giá bí mật lập tức!</p>
                        <button class="bg-gray-900 text-white font-bold py-3 px-8 rounded-xl shadow-md hover:bg-black"><i class="fas fa-expand mr-2"></i>Mở Camera Scan</button>
                    </div>
                </div>
    """
    
    # Replace the close of pagination with the injected code
    html = re.sub(r'<!-- Pagination Buttons -->.*?</div>\s*</div>\s*(?=</div>\s*</main>)', r'<!-- Pagination Buttons block ends -->\n\n' + mock_tabs + r'\n</div>', html, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    update_header()
    update_home()
    update_product()
    update_category()
    print("Files patched successfully!")
