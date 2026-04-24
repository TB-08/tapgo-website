import re

with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('<!-- Static Sample Data (Miền Trung deals) -->')
idx_end = text.find('<!-- Pagination Buttons -->', idx_start)

if idx_end != -1 and idx_start != -1:
    template_loop = r'''<!-- Alpine rendered remaining vouchers -->
                    <template x-for="(v, vi) in Array.from({length: 16})" :key="vi">
                        <a href="product_detail.html"
                            class="ticket-card bg-white rounded-2xl flex flex-col relative border border-gray-100 shadow-sm group overflow-visible w-full"
                            style="transition:all 0.3s ease"
                            onmouseenter="this.style.transform='translateY(-8px)';this.style.boxShadow='0 20px 40px -10px rgba(244,129,51,0.2)'"
                            onmouseleave="this.style.transform='';this.style.boxShadow=''">
                            <div class="absolute top-3 left-3 z-10 flex gap-2">
                                <span class="bg-gradient-to-r from-red-600 to-danger text-white text-[10px] font-bold px-2 py-1 rounded-lg shadow" x-show="vi < 4">🔥 HOT HÍT</span>
                            </div>
                            <div class="absolute top-3 right-3 z-10" x-show="vi % 3 === 0">
                                <span class="font-bold text-[9px] px-2 py-1 rounded-lg shadow-md" style="background:#FBBF24;color:#7C3B00">
                                    <i class="fas fa-crown text-[8px]"></i> GOLD
                                </span>
                            </div>
                            <div class="relative overflow-hidden aspect-[4/3] rounded-t-2xl bg-gray-100 z-20">
                                <img :src="'https://images.unsplash.com/photo-1544148103-0773bf10d330?q=80&w=600&auto=format&fit=crop&sig=' + vi" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                            </div>
                            <div class="relative h-0">
                                <div class="absolute -top-4 left-4 w-[38px] h-[38px] bg-white rounded-xl flex items-center justify-center p-1 shadow-md z-30 border border-gray-100">
                                    <img src="https://images.unsplash.com/photo-1560624052-449f5ddf0c31?q=80&w=80" class="w-full h-full object-cover rounded-lg">
                                </div>
                            </div>
                            <div class="ticket-divider mx-3 mt-0 !border-gray-200"></div>
                            <div class="px-4 pt-3 pb-4 flex-1 flex flex-col relative z-20 bg-white rounded-b-2xl">
                                <span class="text-[10px] text-gray-400 font-bold uppercase" x-text="['MỘC SPA', 'YAKIMONO', 'GRANDVIEW', 'THE COFFEE HOUSE'][vi%4] + ' &middot; ĐÀ NẴNG'"></span>
                                <h3 class="font-bold text-[14px] text-gray-900 leading-snug mt-1.5 mb-2 group-hover:text-brand transition" x-text="'Gói Trải Nghiệm ' + (vi+1) + ' Cao Cấp – Đà Nẵng'"></h3>
                                <div class="flex items-center gap-1 mb-3">
                                    <i class="fas fa-star text-brand text-[10px]"></i>
                                    <span class="text-[11px] font-bold text-gray-700">4.9</span>
                                    <span class="text-gray-300 mx-1">&middot;</span>
                                    <span class="text-[11px] text-gray-500" x-text="(200 + vi*14) + ' đánh giá'"></span>
                                </div>
                                <div class="flex items-center justify-between mt-auto">
                                    <span class="bg-danger/10 text-danger font-bold text-[13px] px-3 py-1 rounded-lg" x-text="'Giảm ' + (20 + (vi%4)*10) + '%'"></span>
                                    <span class="text-brand font-bold text-[13px]"><i class="fas fa-coins text-yellow-500 mr-0.5"></i><span x-text="(500 + vi*50) + ' TapCoin'"></span></span>
                                </div>
                                <!-- Hover Reveal CTA -->
                                <div class="absolute inset-x-0 bottom-0 translate-y-full group-hover:translate-y-0 transition-transform duration-300 rounded-b-2xl overflow-hidden bg-brand z-50">
                                    <button class="w-full bg-brand hover:bg-brand-hover text-white font-bold py-3.5 text-[13px] tracking-wide">XEM CHI TIẾT DEAL</button>
                                </div>
                            </div>
                        </a>
                    </template>
                    <!-- Pagination Buttons -->'''
    
    new_text = text[:idx_start] + template_loop + text[idx_end+len('<!-- Pagination Buttons -->'):]
    with open('c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Successfully applied 16 cards!')
