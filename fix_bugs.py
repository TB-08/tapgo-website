import re
import os

def fix_html_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Fix search bar
    text = re.sub(
        r'class="bg-gray-50 h-full px-4 py-2.5 text-gray-700 cursor-pointer font-medium flex items-center justify-between min-w-\[120px\] hover:bg-gray-100 transition whitespace-nowrap rounded-l-lg"',
        'class="bg-gray-50 h-full px-4 py-2.5 text-gray-700 cursor-pointer font-medium flex items-center justify-between min-w-[120px] hover:bg-gray-100 transition whitespace-nowrap rounded-l-[10px]"',
        text
    )
    text = re.sub(
        r'<button class="bg-brand text-white px-7 hover:bg-brand-hover"><i class="fas fa-search"></i></button>',
        '<button class="bg-brand text-white px-7 hover:bg-brand-hover rounded-r-[10px]"><i class="fas fa-search"></i></button>',
        text
    )

    # Fix Notification Bell Overlap
    bell_pattern = r'<button @click="openNotif = !openNotif"\s*class="text-gray-600 relative hover:text-brand transition p-1">\s*<i class="fa-regular fa-bell text-2xl"></i>\s*<span\s*class="absolute -top-0\.5 -right-0\.5 bg-danger shadow border border-white text-white text-\[9px\] font-medium w-4 h-4 rounded-full flex items-center justify-center">3</span>\s*</button>'
    bell_replace = '''<button @click="openNotif = !openNotif" class="text-gray-600 hover:text-brand transition p-1">
                        <div class="relative inline-block">
                            <i class="fa-regular fa-bell text-2xl"></i>
                            <span class="absolute -top-1 -right-1.5 bg-danger shadow border border-white text-white text-[9px] font-medium w-4 h-4 rounded-full flex items-center justify-center">3</span>
                        </div>
                    </button>'''
    text = re.sub(re.compile(bell_pattern, re.MULTILINE), bell_replace, text)

    # Fix My Vouchers Overlap
    voucher_pattern = r'<button @click="openVoucher = !openVoucher"\s*class="flex items-center gap-2 text-gray-600 relative hover:text-brand transition">\s*<i class="fa-solid fa-ticket-alt text-\[26px\]"></i>\s*<span\s*class="absolute -top-1 -right-2 bg-black shadow border border-white text-white text-\[9px\] w-4 h-4 rounded-full flex items-center justify-center font-medium">5</span>\s*<span class="font-medium text-\[13px\] hidden xl:block leading-tight text-gray-700">Voucher<br>của\s*tôi</span>\s*</button>'
    voucher_replace = '''<button @click="openVoucher = !openVoucher" class="flex items-center gap-2 text-gray-600 hover:text-brand transition text-left">
                        <div class="relative">
                            <i class="fa-solid fa-ticket-alt text-[26px]"></i>
                            <span class="absolute -top-1 -right-2 bg-black shadow border border-white text-white text-[9px] w-4 h-4 rounded-full flex items-center justify-center font-medium">5</span>
                        </div>
                        <span class="font-medium text-[13px] hidden xl:block leading-tight text-gray-700">Voucher<br>của tôi</span>
                    </button>'''
    text = re.sub(re.compile(voucher_pattern, re.MULTILINE), voucher_replace, text)

    # Add `openQr = true` inside Dùng Ngay buttons inside dropdown
    text = re.sub(
        r'<button\s*class="self-center bg-brand text-white text-\[11px\] font-medium px-3 py-1\.5 rounded-lg hover:bg-brand-hover transition whitespace-nowrap">Dùng\s*ngay</button>',
        '<button @click="openQr = true; openVoucher = false" class="self-center bg-brand text-white text-[11px] font-medium px-3 py-1.5 rounded-lg hover:bg-brand-hover transition whitespace-nowrap">Dùng ngay</button>',
        text
    )

    # Add Modal layout right before </body> if not there
    if '<!-- Dùng Ngay Modal -->' not in text:
        modal_html = '''
    <!-- Dùng Ngay Modal -->
    <div x-show="openQr" x-transition style="display: none;" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/60 backdrop-blur-sm" @click.away="openQr = false">
        <div class="bg-white p-6 rounded-2xl shadow-xl w-[320px] text-center relative border border-gray-100" @click.stop>
            <button @click="openQr = false" class="absolute top-3 right-3 text-gray-400 hover:text-red-500 w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center transition"><i class="fas fa-times text-lg"></i></button>
            <h3 class="font-bold text-lg mb-1 text-gray-800">Mã Quét Voucher</h3>
            <p class="text-xs text-gray-500 mb-4">Cung cấp QR hoặc mã số cho nhân viên TAPGO để sử dụng dịch vụ</p>
            <div class="bg-gray-50 p-3 rounded-xl mb-4 border border-dashed border-brand max-w-[200px] mx-auto">
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=TAPGO12345" class="w-full h-auto mx-auto rounded-lg mix-blend-multiply opacity-90">
            </div>
            <p class="text-2xl font-bold tracking-[0.2em] text-gray-900 mb-2">TPG-X8A2M</p>
            <div class="flex items-center justify-center gap-2 text-danger bg-red-50 py-2.5 rounded-xl font-bold text-sm shadow-inner">
                <i class="fas fa-clock animate-pulse"></i> Hết hạn sau: 01:59:59
            </div>
        </div>
    </div>
</body>'''
        text = text.replace('</body>', modal_html)

    # In category_website.html, missing images
    if 'category_website.html' in file:
        img_replace = r"['https://images.unsplash.com/photo-1544148103-0773bf10d330?q=80&w=600&auto=format&fit=crop','https://images.unsplash.com/photo-1550547660-d9450f859349?q=80&w=600&auto=format&fit=crop','https://images.unsplash.com/photo-1560624052-449f5ddf0c31?q=80&w=600&auto=format&fit=crop','https://images.unsplash.com/photo-1555939594-58d7cb561ad1?q=80&w=600&auto=format&fit=crop','https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=600&auto=format&fit=crop'][vi%5]"
        text = re.sub(
            r"\['https://images.unsplash.com/photo-1544148103-0773bf10d330.*?\]\[vi%5\]",
            img_replace,
            text,
            flags=re.DOTALL
        )
        
        # Center pagination block
        pag_pattern = r'<div class="flex justify-center items-center gap-2 mt-12 bg-white w-max mx-auto p-2 rounded-2xl shadow-sm border border-gray-200">'
        text = text.replace(pag_pattern, '<div class="w-full flex justify-center mt-10"><div class="flex items-center gap-2 bg-white p-2 rounded-2xl shadow-sm border border-gray-100">')
        text = text.replace('<!-- Pagination Buttons -->', '</div></div>\n                        <!-- Pagination Buttons -->')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)

files = [
    'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/home_website.html',
    'c:/Users/ADMIN/.gemini/antigravity/scratch/TAPGO/category_website.html'
]
for file in files:
    fix_html_file(file)

print('Update successful.')
