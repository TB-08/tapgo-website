import re

def fix_home():
    path = 'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/home_website.html'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove overflow-hidden from section
    html = html.replace('overflow-hidden ring-1 ring-orange-400', 'ring-1 ring-orange-400')
    
    # We need to move the bottom pricing block inside the div with padding 
    # Current structure is:
    # </div> (closes the p-4 flex-1 div)
    # <div class="mt-3 pt-3 border-t border-gray-100"> ... </div>
    # </a>
    
    # Let's locate the flash deal a tag inside home_website.html and update it
    # We'll use a regex replacement that matches everything inside <a href="category_website.html" ... group border-0...
    # Actually, it's easier to just replace this exact block

    old_structure = """                        <div class="p-4 flex-1 flex flex-col justify-between z-20 bg-transparent rounded-b-[1.2rem]">
                            <div>
                                <span class="text-[10px] text-gray-500 font-bold uppercase truncate tracking-wider"
                                    x-text="fd.brand" :class="fd.out ? 'text-gray-400' : ''"></span>
                                <h3 class="font-bold text-[13px] text-gray-900 leading-snug my-1.5 truncate-2-lines group-hover:text-brand transition"
                                    x-text="fd.title" :class="fd.out ? '!text-gray-300' : ''"></h3>
                                <div class="flex items-center gap-1.5 text-gray-400">
                                    <i class="fas fa-star text-yellow-500 text-[10px]"></i>
                                    <span class="text-[11px] font-bold text-gray-700" x-text="fd.rating"
                                        :class="fd.out ? 'text-gray-500' : ''"></span>
                                </div>
                            </div>
                            <div class="mt-3 relative" x-show="!fd.out">
                                <div
                                    class="w-full bg-orange-100 rounded-full h-4 relative overflow-hidden shadow-inner hidden md:block">
                                    <div class="bg-gradient-to-r from-yellow-400 via-orange-500 to-red-600 h-full rounded-full absolute left-0 top-0 transition-all duration-1000"
                                        :style="`width: ${70 + (idx*6)}%`"></div>
                                    <div
                                        class="absolute inset-0 flex items-center justify-center text-white text-[9px] font-bold tracking-widest z-10 drop-shadow">
                                        ĐÃ BÁN <span x-text="fd.reviews"></span>
                                    </div>
                                </div>
                                <!-- Mobile simple bar version to save space if needed -->
                                <div
                                    class="w-full bg-orange-100 rounded-full h-3 relative overflow-hidden shadow-inner md:hidden">
                                    <div class="bg-gradient-to-r from-orange-400 to-red-600 h-full rounded-full"
                                        :style="`width: ${70 + (idx*6)}%`"></div>
                                </div>
                            </div>
                        </div>
                        <div class="mt-3 pt-3 border-t border-gray-100">
                            <div class="flex items-center gap-2 mb-2">
                                <span class="bg-danger/10 text-danger font-bold text-[13px] px-2.5 py-1 rounded-lg"
                                    x-text="'-' + fd.discount"></span>
                                <span class="text-gray-500 text-[11px] font-semibold">Giảm ngay</span>
                            </div>
                            <div class="text-brand font-bold text-[14px]"><i
                                    class="fas fa-coins mr-1 text-yellow-500"></i>Chỉ <span
                                    x-text="Math.round(parseFloat(fd.salePrice)*0.1)+' TapCoin'"></span></div>
                            <div class="w-full bg-orange-100 rounded-full h-1.5 mt-3 shadow-inner">
                                <div class="bg-gradient-to-r from-brand to-danger h-full rounded-full animate-pulse"
                                    :style="`width: ${Math.max(5,(fd.total-fd.remain)/fd.total*100)}%`"></div>
                            </div>
                            <p class="text-[9px] text-gray-500 mt-1 font-medium">Còn <span class="text-danger font-bold"
                                    x-text="fd.remain"></span> suất</p>
                        </div>"""

    new_structure = """                        <div class="p-4 flex-1 flex flex-col justify-between z-20 bg-transparent rounded-b-[1.2rem]">
                            <div>
                                <span class="text-[10px] text-gray-500 font-bold uppercase truncate tracking-wider"
                                    x-text="fd.brand" :class="fd.out ? 'text-gray-400' : ''"></span>
                                <h3 class="font-bold text-[13px] text-gray-900 leading-snug my-1.5 truncate-2-lines group-hover:text-brand transition min-h-[38px]"
                                    x-text="fd.title" :class="fd.out ? '!text-gray-300' : ''"></h3>
                                <div class="flex items-center gap-1.5 text-gray-400 mb-3">
                                    <i class="fas fa-star text-yellow-500 text-[10px]"></i>
                                    <span class="text-[11px] font-bold text-gray-700" x-text="fd.rating"
                                        :class="fd.out ? 'text-gray-500' : ''"></span>
                                </div>
                                <div class="relative mb-3" x-show="!fd.out">
                                    <div class="w-full bg-orange-50 rounded-full h-3 md:h-4 relative overflow-hidden shadow-inner border border-brand/10">
                                        <div class="bg-gradient-to-r from-orange-400 to-red-600 h-full rounded-full absolute left-0 top-0 transition-all duration-1000"
                                            :style="`width: ${70 + (idx*6)}%`"></div>
                                        <div class="absolute inset-0 flex items-center text-white text-[9px] font-bold tracking-widest drop-shadow-sm px-2 justify-center hidden md:flex">
                                            ĐÃ BÁN <span x-text="fd.reviews" class="ml-1"></span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- Bottom Info Moved Inside flex block -->
                            <div class="mt-auto pt-3 border-t border-gray-100 w-full flex flex-col justify-end">
                                <div class="flex items-center gap-2 mb-2">
                                    <span class="bg-danger/10 text-danger font-bold text-[13px] px-2.5 py-0.5 rounded-lg border border-danger/20"
                                        x-text="'-' + fd.discount"></span>
                                    <span class="text-gray-500 text-[11px] font-semibold tracking-wide uppercase">Giảm Ngay</span>
                                </div>
                                <div class="text-brand font-black text-[15px]"><i
                                        class="fas fa-coins mr-1 text-yellow-500"></i>Chỉ <span
                                        x-text="Math.round(parseFloat(fd.salePrice)*1)+' TapCoin'"></span></div>
                                <div class="w-full bg-red-100 rounded-full h-1 mt-2.5 shadow-inner">
                                    <div class="bg-gradient-to-r from-danger to-brand h-full rounded-full animate-pulse shadow-sm"
                                        :style="`width: ${Math.max(5,(fd.total-fd.remain)/fd.total*100)}%`"></div>
                                </div>
                                <p class="text-[10px] text-gray-500 mt-1 font-medium tracking-wide">Chỉ còn <strong class="text-danger font-bold"
                                        x-text="fd.remain"></strong> lượt</p>
                            </div>
                        </div>"""

    if old_structure in html:
        html = html.replace(old_structure, new_structure)
    else:
        print("Could not find old structure")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    fix_home()
    print("Flash deal structure updated")
