import re

with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('<!-- Alpine rendered remaining vouchers -->')
idx_end = text.find('<!-- Pagination Buttons -->', idx_start)

if idx_end != -1 and idx_start != -1:
    template_loop = r'''<!-- Alpine rendered remaining vouchers -->
                    <template x-for="(v, vi) in Array.from({length: 16})" :key="vi">
                        <a href="product_detail.html"
                            class="bg-white rounded-[1.2rem] flex flex-col relative shadow-[0_2px_12px_rgba(0,0,0,0.04)] border border-gray-100 group overflow-visible w-full hover:-translate-y-1 hover:shadow-[0_20px_40px_-10px_rgba(244,129,51,0.15)] transition-all duration-300">
                            <div class="absolute top-3 left-3 z-20 flex gap-2">
                                <span class="bg-gradient-to-r from-orange-500 to-danger text-white text-[10px] font-bold px-2 py-1 rounded shadow-sm" x-show="vi < 4">🔥 HOT DEAL</span>
                            </div>
                            <div class="absolute top-3 right-3 z-20" x-show="vi % 2 === 0">
                                <span class="font-bold text-[9px] px-2 py-1 rounded shadow-md" style="background:#FBBF24;color:#7C3B00">
                                    <i class="fas fa-crown text-[8px]"></i> GOLD
                                </span>
                            </div>
                            <div class="relative overflow-hidden aspect-[4/3] rounded-t-[1.2rem] bg-gray-100 z-10 w-full">
                                <img :src="['https://images.unsplash.com/photo-1544148103-0773bf10d330?q=80&w=600&auto=format&fit=crop','https://images.unsplash.com/photo-1550547660-d9450f859349?q=80&w=600&auto=format&fit=crop','https://images.unsplash.com/photo-1560624052-449f5ddf0c31?q=80&w=600&auto=format&fit=crop','https://images.unsplash.com/photo-1542314831-c6a4d14d8373?q=80&w=600&auto=format&fit=crop','https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=600&auto=format&fit=crop'][vi%5]" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                            </div>
                            <div class="relative h-0 z-30">
                                <div class="absolute -top-5 left-4 w-[42px] h-[42px] bg-white rounded-full flex items-center justify-center p-1 shadow-md border border-gray-100">
                                    <img :src="['https://images.unsplash.com/photo-1560624052-449f5ddf0c31?q=80&w=80','https://images.unsplash.com/photo-1512418490979-9ce792d5e1dc?q=80&w=80'][vi%2]" class="w-full h-full object-cover rounded-full">
                                </div>
                            </div>
                            <div class="px-5 pt-7 pb-5 flex-1 flex flex-col relative z-20 bg-transparent rounded-b-[1.2rem]">
                                <span class="text-[10px] text-gray-500 font-bold uppercase" x-text="['MỘC SPA', 'YAKIMONO', 'GRANDVIEW', 'THE COFFEE HOUSE', 'VOUCHER DU LỊCH'][vi%5] + ' &middot; ĐÀ NẴNG'"></span>
                                <h3 class="font-bold text-[15px] text-gray-900 leading-snug mt-1.5 mb-2 group-hover:text-brand transition" x-text="'Gói Trải Nghiệm ' + (vi+1) + ' Cao Cấp – Ưu Đãi Độc Quyền'"></h3>
                                <div class="flex items-center gap-1.5 mb-3">
                                    <i class="fas fa-star text-yellow-500 text-[11px]"></i>
                                    <span class="text-[12px] font-bold text-gray-700">4.9</span>
                                    <span class="text-gray-300 mx-0.5">&middot;</span>
                                    <span class="text-[11px] text-gray-500 font-medium" x-text="(150 + vi*14) + ' đã bán'"></span>
                                </div>
                                <div class="flex flex-col mt-auto pt-3 border-t border-gray-100/80 gap-2">
                                    <div class="flex justify-between items-center w-full">
                                        <span class="bg-red-50 text-danger font-bold text-[11px] px-2 py-0.5 rounded" x-text="'Giảm ' + (20 + (vi%4)*10) + '%'"></span>
                                        <span class="text-gray-400 text-[11px] line-through decoration-gray-300 font-medium">1,200 TapCoin</span>
                                    </div>
                                    <div class="flex justify-between items-end w-full">
                                        <span class="text-[11px] text-gray-500 font-medium">Chỉ còn</span>
                                        <span class="text-brand font-bold text-[16px]"><i class="fas fa-coins text-yellow-500 mr-1 text-[12px]"></i><span x-text="(500 + vi*50) + ''"></span></span>
                                    </div>
                                </div>
                                <!-- Hover Reveal CTA -->
                                <div class="absolute inset-x-0 bottom-0 translate-y-full opacity-0 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 rounded-b-[1.2rem] overflow-hidden bg-brand z-50">
                                    <button class="w-full bg-brand hover:bg-brand-hover text-white font-bold py-3.5 text-[14px] tracking-wide">XEM CHI TIẾT DEAL</button>
                                </div>
                            </div>
                        </a>
                    </template>
                    <!-- Pagination Buttons -->'''
    
    new_text = text[:idx_start] + template_loop + text[idx_end+len('<!-- Pagination Buttons -->'):]
    with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Successfully applied beautifully redesigned 16 cards!')
