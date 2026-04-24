const getTapgoData = () => {
    return {
        cartCount: 0,
        openCart: false,
        openQr: false,
        showBuyModal: false,
        currentSortTab: 'eVoucher',
        loc: 'Toàn quốc',
        openLoc: false,
        activeCat: localStorage.getItem('tapgo_activeCat') || 'Flash Deal',

        // Gọi khi click danh mục từ trang chủ → chuyển sang category_website.html
        // Riêng Flash Deal → về trang chủ và scroll mượt tới section Flash Deals
        goToCat(name) {
            localStorage.setItem('tapgo_activeCat', name);
            if (name === 'Flash Deal') {
                const isHome = window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || window.location.pathname.endsWith('home_website.html');
                if (isHome) {
                    // Đã ở trang chủ → scroll smooth xuống Flash Deals
                    const el = document.getElementById('flash-deals');
                    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                } else {
                    window.location.href = 'index.html#flash-deals';
                }
            } else {
                window.location.href = 'category_website.html';
            }
        },

        // Gọi khi click danh mục trong chính trang category (đổi active + scroll về đầu trang)
        switchCat(name) {
            this.activeCat = name;
            localStorage.setItem('tapgo_activeCat', name);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },

        cats: [
            { name: 'Tất cả', i: 'th-large', bg: 'bg-orange-50', col: 'text-brand' },
            { name: 'Vui chơi Giải trí', i: 'gamepad', bg: 'bg-pink-50', col: 'text-pink-500' },
            { name: 'Nhà hàng Ăn uống', i: 'utensils', bg: 'bg-red-50', col: 'text-red-500' },
            { name: 'Spa & Làm đẹp', i: 'spa', bg: 'bg-teal-50', col: 'text-teal-500' },
            { name: 'Khách sạn & Tour', i: 'plane', bg: 'bg-blue-50', col: 'text-blue-500' },
            { name: 'Làm đẹp & Skincare', i: 'face-smile', bg: 'bg-purple-50', col: 'text-purple-500' },
            { name: 'Thể thao & Fitness', i: 'dumbbell', bg: 'bg-green-50', col: 'text-green-500' },
            { name: 'Mua sắm', i: 'shopping-bag', bg: 'bg-yellow-50', col: 'text-yellow-600' },
            { name: 'Sức khỏe & Y tế', i: 'heart', bg: 'bg-rose-50', col: 'text-rose-500' },
            { name: 'Giáo dục & Kỹ năng', i: 'graduation-cap', bg: 'bg-indigo-50', col: 'text-indigo-500' },
            { name: 'Thú cưng', i: 'paw', bg: 'bg-amber-50', col: 'text-amber-600' },
            { name: 'Xe & Di chuyển', i: 'car', bg: 'bg-slate-100', col: 'text-slate-500' }
        ],

        // Danh mục phụ theo từng danh mục chính
        subCats: {
            'Tất cả':                  [ { name: 'Tất cả deal', n: 845 }, { name: 'Mới nhất', n: 120 }, { name: 'Bán chạy nhất', n: 310 }, { name: 'Giảm giá sốc', n: 95 }, { name: 'Độc quyền TAPGO', n: 42 } ],
            'Vui chơi Giải trí':       [ { name: 'Rạp chiếu phim', n: 156 }, { name: 'Khu vui chơi & Công viên', n: 98 }, { name: 'Karaoke & Bar', n: 73 }, { name: 'Bowling & Bi-a', n: 42 }, { name: 'Escape Room & Board Game', n: 35 } ],
            'Nhà hàng Ăn uống':        [ { name: 'Buffet & Lẩu', n: 203 }, { name: 'Nhà hàng Á', n: 187 }, { name: 'Đồ uống & Trà sữa', n: 142 }, { name: 'Nhà hàng Âu – Mỹ', n: 65 }, { name: 'Ăn vặt & Street Food', n: 88 } ],
            'Spa & Làm đẹp':           [ { name: 'Massage & Thư giãn', n: 178 }, { name: 'Chăm sóc da mặt', n: 134 }, { name: 'Làm nail', n: 96 }, { name: 'Triệt lông', n: 57 }, { name: 'Cắt & Tạo kiểu tóc', n: 112 } ],
            'Khách sạn & Tour':        [ { name: 'Khách sạn 3–5 sao', n: 245 }, { name: 'Tour trong nước', n: 189 }, { name: 'Tour nước ngoài', n: 76 }, { name: 'Resort & Nghỉ dưỡng', n: 103 }, { name: 'Homestay & Airbnb', n: 58 } ],
            'Làm đẹp & Skincare':      [ { name: 'Serum & Kem dưỡng', n: 321 }, { name: 'Tẩy da chết & Mask', n: 154 }, { name: 'Kem chống nắng', n: 98 }, { name: 'Nước tẩy trang', n: 67 }, { name: 'Bộ kit dưỡng da', n: 84 } ],
            'Thể thao & Fitness':      [ { name: 'Gym & Cardio', n: 167 }, { name: 'Yoga & Pilates', n: 89 }, { name: 'Bơi lội', n: 54 }, { name: 'Cầu lông & Tennis', n: 73 }, { name: 'Thể thao ngoài trời', n: 48 } ],
            'Mua sắm':                 [ { name: 'Siêu thị & Tiện lợi', n: 213 }, { name: 'Thời trang', n: 178 }, { name: 'Điện tử & Thiết bị', n: 95 }, { name: 'Đồ gia dụng & Nội thất', n: 67 }, { name: 'Sách & Văn phòng phẩm', n: 44 } ],
            'Sức khỏe & Y tế':         [ { name: 'Khám sức khỏe tổng quát', n: 143 }, { name: 'Xét nghiệm & Chuẩn đoán', n: 87 }, { name: 'Nha khoa', n: 112 }, { name: 'Dinh dưỡng & Meal Prep', n: 64 }, { name: 'Vật lý trị liệu', n: 39 } ],
            'Giáo dục & Kỹ năng':      [ { name: 'Ngoại ngữ', n: 198 }, { name: 'Lập trình & Công nghệ', n: 134 }, { name: 'Nghệ thuật & Âm nhạc', n: 76 }, { name: 'Kỹ năng mềm', n: 89 }, { name: 'Dạy nghề & Workshop', n: 57 } ],
            'Thú cưng':                [ { name: 'Tắm & Grooming', n: 123 }, { name: 'Thú y & Khám bệnh', n: 86 }, { name: 'Thức ăn & Dinh dưỡng', n: 94 }, { name: 'Đồ chơi & Phụ kiện', n: 57 }, { name: 'Trông giữ & Khách sạn thú cưng', n: 38 } ],
            'Xe & Di chuyển':          [ { name: 'Đặt xe công nghệ', n: 167 }, { name: 'Thuê xe tự lái', n: 78 }, { name: 'Rửa xe & Chăm sóc', n: 112 }, { name: 'Bảo dưỡng & Sửa chữa', n: 95 }, { name: 'Vé xe & Limousine', n: 53 } ],
        },

        // Getter: trả về danh mục phụ theo activeCat
        get currentSubCats() {
            return this.subCats[this.activeCat] || this.subCats['Tất cả'];
        },

        // Dữ liệu sản phẩm theo từng danh mục
        catProducts: {
            'Vui chơi Giải trí': [
                { brand:'CGV Cinemas', img:'https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=600', title:'Vé Xem Phim 2D Cuối Tuần – Tất Cả Cụm Rạp', rating:4.9, sold:312, discount:30, price:630 },
                { brand:'Lotte Cinema', img:'https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=600', title:'Combo Phim + Bắp Nước Siêu Tiết Kiệm', rating:4.8, sold:1024, discount:25, price:750 },
                { brand:'Galaxy Bowling', img:'https://images.unsplash.com/photo-1511882150382-421056c89033?q=80&w=600', title:'Trọn Gói Bowling 2 Giờ Cuối Tuần', rating:4.7, sold:520, discount:20, price:500 },
                { brand:'KidZania', img:'https://images.unsplash.com/photo-1534567153574-2b12153a87f0?q=80&w=600', title:'Vé Trải Nghiệm KidZania Cho Trẻ Em', rating:4.9, sold:890, discount:14, price:900 },
                { brand:'VinKE', img:'https://images.unsplash.com/photo-1560624052-449f5ddf0c31?q=80&w=600', title:'Vé Vào Cổng Khu Vui Chơi VinKE Times City', rating:4.7, sold:2400, discount:21, price:660 },
                { brand:'Escape Room', img:'https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?q=80&w=600', title:'Vé Escape Room Nhóm 4-6 Người', rating:4.8, sold:380, discount:35, price:450 },
                { brand:'Board Game Café', img:'https://images.unsplash.com/photo-1606503825008-909a67e63c3d?q=80&w=600', title:'Combo Board Game Café Cả Ngày', rating:4.6, sold:210, discount:20, price:400 },
                { brand:'Karaoke VIP', img:'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?q=80&w=600', title:'Karaoke 3 Giờ Phòng VIP – Miễn Phí Nước', rating:4.7, sold:670, discount:40, price:550 },
            ],
            'Nhà hàng Ăn uống': [
                { brand:'Yakimono', img:'https://images.unsplash.com/photo-1544148103-0773bf10d330?q=80&w=600', title:'Thịt Nướng Nhật Bản Bao Gồm Cả Lẩu Chào Mừng', rating:4.8, sold:312, discount:28, price:640 },
                { brand:'Shang Chi Lẩu', img:'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?q=80&w=600', title:'Buffet Lẩu Ngon Đỉnh Cao Giảm 35% Hóa Đơn', rating:5.0, sold:5200, discount:35, price:990 },
                { brand:'Phúc Long', img:'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?q=80&w=600', title:'Combo 2 Ly Trà Sữa Phúc Long Size L Đủ Vị', rating:4.7, sold:670, discount:34, price:237 },
                { brand:'Tokbokki 247', img:'https://images.unsplash.com/photo-1498654896293-37aacf113fd9?q=80&w=600', title:'Set Ăn Vặt Hàn Quốc Đường Phố Cho 2 Người', rating:4.5, sold:233, discount:40, price:357 },
                { brand:'Highlands Coffee', img:'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?q=80&w=600', title:'Combo 2 Ly Cà Phê Highlands Coffee Size L + Bánh Mì', rating:4.6, sold:3200, discount:34, price:297 },
                { brand:'Pizza 4P\'s', img:'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?q=80&w=600', title:'Voucher Pizza 4P\'s – Set Ăn 2 Người Cao Cấp', rating:4.9, sold:1800, discount:20, price:800 },
                { brand:'The Coffee House', img:'https://images.unsplash.com/photo-1442512595331-e89e73853f31?q=80&w=600', title:'Combo Cà Phê + Bánh Ngọt The Coffee House', rating:4.6, sold:920, discount:25, price:180 },
                { brand:'Gà Rán Lotteria', img:'https://images.unsplash.com/photo-1551782450-a2132b4ba21d?q=80&w=600', title:'Combo Gà Rán Lotteria Set Gia Đình 4 Người', rating:4.5, sold:1500, discount:30, price:450 },
            ],
            'Spa & Làm đẹp': [
                { brand:'Beauty Center', img:'https://images.unsplash.com/photo-1560750588-73207b1ef5b8?q=80&w=600', title:'Gói Chăm Sóc Da Mặt + Massage Thư Giãn 90 Phút', rating:4.9, sold:341, discount:45, price:897 },
                { brand:'Cocoon Spa', img:'https://images.unsplash.com/photo-1544161515-4ab6ce6db874?q=80&w=600', title:'Liệu Trình Spa Toàn Thân Cao Cấp 120 Phút', rating:5.0, sold:210, discount:50, price:1200 },
                { brand:'ZEN Nails', img:'https://images.unsplash.com/photo-1604654894610-df63bc536371?q=80&w=600', title:'Combo Làm Nail + Pedicure Nghệ Thuật', rating:4.8, sold:480, discount:30, price:350 },
                { brand:'Rose Spa', img:'https://images.unsplash.com/photo-1519823551278-64ac92734fb1?q=80&w=600', title:'Massage Thư Giãn 60 Phút Kiểu Thái', rating:4.7, sold:620, discount:40, price:480 },
                { brand:'Wax & Beauty', img:'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?q=80&w=600', title:'Triệt Lông Công Nghệ Laser Cao Cấp 5 Vùng', rating:4.9, sold:280, discount:60, price:1800 },
                { brand:'Tóc Xinh Studio', img:'https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?q=80&w=600', title:'Combo Cắt + Uốn + Nhuộm Tóc Tại Studio', rating:4.8, sold:540, discount:35, price:750 },
                { brand:'Aroma Massage', img:'https://images.unsplash.com/photo-1540555700478-4be289fbecef?q=80&w=600', title:'Massage Tinh Dầu Thảo Mộc 90 Phút Khử Căng Cơ', rating:4.9, sold:390, discount:38, price:660 },
                { brand:'Glowing Skin', img:'https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?q=80&w=600', title:'Căng Bóng Da Mặt Collagen + Dưỡng Ẩm Chuyên Sâu', rating:4.7, sold:175, discount:45, price:900 },
            ],
            'Khách sạn & Tour': [
                { brand:'Mường Thanh', img:'https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=600', title:'Phòng Deluxe Mường Thanh Đà Nẵng – Bao Ăn Sáng', rating:4.8, sold:890, discount:25, price:1500 },
                { brand:'Vinpearl Resort', img:'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?q=80&w=600', title:'Combo 2N1Đ Vinpearl Resort + Vé Vui Chơi', rating:5.0, sold:1200, discount:30, price:3200 },
                { brand:'Tour Hội An', img:'https://images.unsplash.com/photo-1559592413-7cec4d0cae2b?q=80&w=600', title:'Tour Hội An Cổ Phố + Thả Đèn Hoa Đăng 1 Ngày', rating:4.9, sold:560, discount:20, price:680 },
                { brand:'Tour Bà Nà Hills', img:'https://images.unsplash.com/photo-1503220317375-aaad61436b1b?q=80&w=600', title:'Vé Cáp Treo Bà Nà Hills – Cầu Vàng Nổi Tiếng', rating:4.9, sold:3400, discount:15, price:850 },
                { brand:'Furama Resort', img:'https://images.unsplash.com/photo-1571896349842-33c89424de2d?q=80&w=600', title:'Nghỉ Dưỡng Furama Resort 5 Sao Bãi Mỹ Khê', rating:4.8, sold:420, discount:35, price:4800 },
                { brand:'Tour Sa Pa', img:'https://images.unsplash.com/photo-1516483638261-f4dbaf036963?q=80&w=600', title:'Tour Sa Pa 3N2Đ Chinh Phục Fansipan', rating:4.7, sold:310, discount:22, price:2200 },
                { brand:'Tour Phú Quốc', img:'https://images.unsplash.com/photo-1559494007-9f5847c49d94?q=80&w=600', title:'Combo Phú Quốc 3N2Đ Nghỉ Resort 4 Sao', rating:4.9, sold:780, discount:28, price:3600 },
                { brand:'Tour Đà Lạt', img:'https://images.unsplash.com/photo-1583417319070-4a69db38a482?q=80&w=600', title:'Tour Đà Lạt 2N1Đ Săn Mây + Cà Phê Vườn', rating:4.8, sold:960, discount:20, price:1400 },
            ],
            'Làm đẹp & Skincare': [
                { brand:'Innisfree', img:'https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?q=80&w=600', title:'Bộ Dưỡng Ẩm Innisfree Green Tea Chăm Sóc Da', rating:4.8, sold:1200, discount:40, price:540 },
                { brand:'The Ordinary', img:'https://images.unsplash.com/photo-1556228852-6d35a585d566?q=80&w=600', title:'Set Serum Dưỡng Da The Ordinary Cao Cấp 5 Chai', rating:4.9, sold:870, discount:35, price:720 },
                { brand:'Laneige', img:'https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?q=80&w=600', title:'Bộ Dưỡng Đêm Laneige Sleeping Mask Đầy Đủ', rating:4.7, sold:560, discount:30, price:890 },
                { brand:'Klairs', img:'https://images.unsplash.com/photo-1631390894029-cb62aa3f4b36?q=80&w=600', title:'Vitamin C Klairs + Kem Chống Nắng SPF50 Combo', rating:4.9, sold:2100, discount:45, price:630 },
                { brand:'Cetaphil', img:'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?q=80&w=600', title:'Bộ Rửa Mặt + Kem Dưỡng Ẩm Cetaphil Da Nhạy Cảm', rating:4.8, sold:3400, discount:25, price:450 },
                { brand:'Paula\'s Choice', img:'https://images.unsplash.com/photo-1607006483224-a51f3f3f0e40?q=80&w=600', title:'BHA Tẩy Da Chết Paula\'s Choice 2% BHA Liquid', rating:4.9, sold:1560, discount:20, price:810 },
                { brand:'Sulwhasoo', img:'https://images.unsplash.com/photo-1625772452859-1c03d884dcd7?q=80&w=600', title:'Bộ Dưỡng Da Trắng Sáng Sulwhasoo Cao Cấp Hàn Quốc', rating:5.0, sold:290, discount:38, price:2400 },
                { brand:'Bioderma', img:'https://images.unsplash.com/photo-1522338242992-e1a54906a8da?q=80&w=600', title:'Nước Tẩy Trang Bioderma Sensibio H2O 500ml', rating:4.8, sold:4800, discount:22, price:270 },
            ],
            'Thể thao & Fitness': [
                { brand:'Fit24 Gym', img:'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=600', title:'Thẻ Tập Gym Fit24 – 1 Tháng Không Giới Hạn', rating:4.8, sold:620, discount:40, price:480 },
                { brand:'California Fitness', img:'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?q=80&w=600', title:'Gói Gym + Yoga California Fitness 3 Tháng', rating:4.9, sold:380, discount:35, price:2100 },
                { brand:'Yoga Zen', img:'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=600', title:'Khóa Học Yoga 20 Buổi Cùng HLV Chuyên Nghiệp', rating:5.0, sold:210, discount:30, price:900 },
                { brand:'Swimming Center', img:'https://images.unsplash.com/photo-1530549387789-4c1017266635?q=80&w=600', title:'Vé Bơi Lội 10 Lần Tại Bể Bơi Tiêu Chuẩn Olympic', rating:4.7, sold:840, discount:25, price:350 },
                { brand:'Badminton Club', img:'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?q=80&w=600', title:'Thuê Sân Cầu Lông 2 Giờ + Cầu Miễn Phí', rating:4.6, sold:1200, discount:20, price:160 },
                { brand:'Tennis Court', img:'https://images.unsplash.com/photo-1554068865-24cecd4e34b8?q=80&w=600', title:'Thuê Sân Tennis 2 Giờ Cao Cấp + HLV 1-1', rating:4.8, sold:290, discount:30, price:350 },
                { brand:'Cycling Tour', img:'https://images.unsplash.com/photo-1571188654248-7a89213915f7?q=80&w=600', title:'Tour Đạp Xe Khám Phá Đồng Quê Vùng Ven', rating:4.9, sold:180, discount:15, price:270 },
                { brand:'Rock Climbing', img:'https://images.unsplash.com/photo-1504671914553-18c8ff5d7f22?q=80&w=600', title:'Trải Nghiệm Leo Núi Nhân Tạo – Thách Thức Giới Hạn', rating:4.7, sold:160, discount:25, price:220 },
            ],
            'Mua sắm': [
                { brand:'Vinmart+', img:'https://images.unsplash.com/photo-1601924994987-69e26d50dc26?q=80&w=600', title:'Voucher Mua Sắm Vinmart 200.000đ Giảm Còn 130.000đ', rating:4.7, sold:3200, discount:35, price:390 },
                { brand:'Fahasa Books', img:'https://images.unsplash.com/photo-1512820790803-83ca734da794?q=80&w=600', title:'Voucher Mua Sách Fahasa 300.000đ Ưu Đãi 40%', rating:4.8, sold:890, discount:40, price:540 },
                { brand:'Circle K', img:'https://images.unsplash.com/photo-1542838132-92c53300491e?q=80&w=600', title:'Combo Đồ Uống + Snack Circle K Yêu Thích', rating:4.5, sold:5600, discount:20, price:120 },
                { brand:'The Body Shop', img:'https://images.unsplash.com/photo-1607083206869-4c7672e72a8a?q=80&w=600', title:'Set Quà Tặng The Body Shop Cao Cấp Dưỡng Da', rating:4.9, sold:420, discount:45, price:1080 },
                { brand:'Shopee Mall', img:'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?q=80&w=600', title:'Voucher Shopee Mall 500.000đ Cho Mọi Gian Hàng', rating:4.8, sold:9800, discount:10, price:450 },
                { brand:'TGDĐ', img:'https://images.unsplash.com/photo-1610945264803-c22b62d2a7b3?q=80&w=600', title:'Phiếu Giảm 2 Triệu Khi Mua Điện Thoại Tại TGDĐ', rating:4.8, sold:1230, discount:10, price:1800 },
                { brand:'Muji', img:'https://images.unsplash.com/photo-1493946820527-c61f4a4f0066?q=80&w=600', title:'Voucher Muji 300.000đ Mua Đồ Gia Dụng Văn Phòng', rating:4.7, sold:560, discount:30, price:630 },
                { brand:'Uniqlo', img:'https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?q=80&w=600', title:'Voucher Uniqlo 500.000đ Thời Trang Nhật Bản', rating:4.8, sold:740, discount:25, price:1125 },
            ],
            'Sức khỏe & Y tế': [
                { brand:'Vinmec Hospital', img:'https://images.unsplash.com/photo-1631217868264-e6f75c354d01?q=80&w=600', title:'Gói Khám Sức Khỏe Tổng Quát Vinmec Cao Cấp', rating:4.9, sold:560, discount:30, price:2100 },
                { brand:'Medlatec Lab', img:'https://images.unsplash.com/photo-1579684385127-1ef15d508118?q=80&w=600', title:'Xét Nghiệm Bộ 30 Chỉ Số Máu Tổng Quát Tại Nhà', rating:4.8, sold:1200, discount:40, price:720 },
                { brand:'Nutricare', img:'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=600', title:'Gói Dinh Dưỡng Healthy Meal 1 Tuần Giao Tận Nơi', rating:4.7, sold:380, discount:25, price:675 },
                { brand:'DrNow GPs', img:'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?q=80&w=600', title:'Tư Vấn Bác Sĩ Online 24/7 – Gói 3 Tháng', rating:5.0, sold:840, discount:50, price:450 },
                { brand:'Gym & Wellness', img:'https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=600', title:'Gói Meal Prep Ăn Sạch Giảm Cân 7 Ngày', rating:4.8, sold:290, discount:35, price:630 },
                { brand:'Dental House', img:'https://images.unsplash.com/photo-1606811841689-23dfddce3e95?q=80&w=600', title:'Cạo Vôi Răng + Đánh Bóng Chuyên Nghiệp Tại Nhà', rating:4.9, sold:1560, discount:55, price:270 },
                { brand:'Massage Therapy', img:'https://images.unsplash.com/photo-1515377905703-c4788e51af15?q=80&w=600', title:'Vật Lý Trị Liệu Xương Khớp 60 Phút HLV Chuyên Gia', rating:4.7, sold:210, discount:30, price:540 },
                { brand:'Eye Care Center', img:'https://images.unsplash.com/photo-1574170609306-b4f8e6e2e888?q=80&w=600', title:'Khám Mắt + Đo Thị Lực + Tư Vấn Kính Mắt', rating:4.8, sold:670, discount:40, price:270 },
            ],
            'Giáo dục & Kỹ năng': [
                { brand:'IELTS UP', img:'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?q=80&w=600', title:'Khóa Luyện Thi IELTS 6.5+ Trọn Gói 3 Tháng', rating:4.9, sold:680, discount:40, price:3600 },
                { brand:'Udemy VN', img:'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=600', title:'Combo 5 Khóa Học Lập Trình Python + Data Science', rating:4.8, sold:2100, discount:85, price:270 },
                { brand:'English Now', img:'https://images.unsplash.com/photo-1503676260728-1c00da094a0b?q=80&w=600', title:'Khóa Tiếng Anh Giao Tiếp Online 1-1 Với GV Bản Ngữ', rating:5.0, sold:340, discount:30, price:1260 },
                { brand:'Design Academy', img:'https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?q=80&w=600', title:'Khóa Thiết Kế Đồ Họa Từ A-Z Adobe CC', rating:4.8, sold:520, discount:50, price:900 },
                { brand:'Chef School', img:'https://images.unsplash.com/photo-1466637574441-749b8f19452f?q=80&w=600', title:'Workshop Nấu Ăn Chuyên Nghiệp 4 Buổi Cuối Tuần', rating:4.9, sold:180, discount:25, price:675 },
                { brand:'Music Center', img:'https://images.unsplash.com/photo-1511192336575-5a79af67a629?q=80&w=600', title:'Khóa Học Đàn Guitar Cơ Bản 10 Buổi Cùng HLV', rating:4.7, sold:290, discount:30, price:630 },
                { brand:'Kids Academy', img:'https://images.unsplash.com/photo-1473492201326-7c01dd2e596b?q=80&w=600', title:'Lớp Vẽ Sáng Tạo Cho Trẻ 4-12 Tuổi 8 Buổi', rating:4.9, sold:410, discount:20, price:720 },
                { brand:'Marketing Pro', img:'https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?q=80&w=600', title:'Khóa Digital Marketing Thực Chiến 30 Bài Học', rating:4.8, sold:760, discount:60, price:900 },
            ],
            'Thú cưng': [
                { brand:'Pet Spa', img:'https://images.unsplash.com/photo-1587300003388-59208cc962cb?q=80&w=600', title:'Tắm Gội + Cắt Tỉa Lông Cho Chó Mèo Dưới 10kg', rating:4.9, sold:540, discount:35, price:390 },
                { brand:'VetCare Clinic', img:'https://images.unsplash.com/photo-1612531386530-97286d97c2d2?q=80&w=600', title:'Gói Tiêm Phòng + Khám Sức Khỏe Thú Cưng Toàn Diện', rating:5.0, sold:380, discount:40, price:720 },
                { brand:'PetMart', img:'https://images.unsplash.com/photo-1601979031925-424e53b6caaa?q=80&w=600', title:'Voucher PetMart 300.000đ Mua Đồ Cho Thú Cưng', rating:4.7, sold:650, discount:25, price:675 },
                { brand:'Dog Hotel', img:'https://images.unsplash.com/photo-1560743641-3914f2c45636?q=80&w=600', title:'Dịch Vụ Trông Giữ Chó/Mèo 5 Ngày Tại Khách Sạn Thú Cưng', rating:4.8, sold:210, discount:20, price:960 },
                { brand:'Pet Training', img:'https://images.unsplash.com/photo-1450778869180-41d0601e046e?q=80&w=600', title:'Khóa Huấn Luyện Chó 10 Buổi Cùng Chuyên Gia', rating:4.9, sold:180, discount:30, price:1260 },
                { brand:'Aqua World', img:'https://images.unsplash.com/photo-1496942299866-9e7ab403e614?q=80&w=600', title:'Voucher Mua Cá Cảnh + Bể Thủy Sinh Trọn Gói', rating:4.6, sold:290, discount:25, price:540 },
                { brand:'Pet Food Premium', img:'https://images.unsplash.com/photo-1583336663277-620dc1996580?q=80&w=600', title:'Thức Ăn Hữu Cơ Cao Cấp Cho Mèo Royal Canin 2kg', rating:4.8, sold:1200, discount:30, price:630 },
                { brand:'Cat Paradise', img:'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?q=80&w=600', title:'Dịch Vụ Grooming Mèo Cao Cấp + Nhuộm Móng Nghệ Thuật', rating:4.8, sold:160, discount:40, price:450 },
            ],
            'Xe & Di chuyển': [
                { brand:'Grab Car', img:'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=600', title:'Voucher Grab 100.000đ Cho 3 Chuyến Đi Nội Thành', rating:4.8, sold:12000, discount:50, price:150 },
                { brand:'Renting Go', img:'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?q=80&w=600', title:'Thuê Xe Máy 3 Ngày Khám Phá Đà Nẵng – Hội An', rating:4.7, sold:880, discount:25, price:450 },
                { brand:'Car Spa', img:'https://images.unsplash.com/photo-1520340356584-f9917d1eea6f?q=80&w=600', title:'Gói Rửa + Vệ Sinh Nội Thất Xe Ô Tô Cao Cấp', rating:4.8, sold:1560, discount:40, price:480 },
                { brand:'Bike Share', img:'https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?q=80&w=600', title:'Thuê Xe Đạp Điện Khám Phá Thành Phố 1 Ngày', rating:4.6, sold:670, discount:30, price:210 },
                { brand:'Car Rental VIP', img:'https://images.unsplash.com/photo-1544636331-e26879cd4d9b?q=80&w=600', title:'Thuê Xe 7 Chỗ Đưa Đón Sân Bay Hạng Sang', rating:4.9, sold:340, discount:20, price:1200 },
                { brand:'Engine Care', img:'https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?q=80&w=600', title:'Thay Dầu + Kiểm Tra Xe Định Kỳ 15 Hạng Mục', rating:4.8, sold:2100, discount:35, price:390 },
                { brand:'Limousine VN', img:'https://images.unsplash.com/photo-1590080875515-8a3a8dc5735e?q=80&w=600', title:'Vé Xe Limousine Hà Nội – Hạ Long Ghế Nằm VIP', rating:4.9, sold:760, discount:25, price:540 },
                { brand:'Parking App', img:'https://images.unsplash.com/photo-1506521781263-d8422e82f27a?q=80&w=600', title:'Phiếu Giữ Xe Tháng Bãi Đỗ Cao Cấp Vị Trí Đắc Địa', rating:4.7, sold:430, discount:20, price:720 },
            ],
            'Tất cả': [
                { brand:'CGV Cinemas', img:'https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=600', title:'Vé Xem Phim 2D Cuối Tuần – Tất Cả Cụm Rạp', rating:4.9, sold:312, discount:30, price:630 },
                { brand:'Yakimono', img:'https://images.unsplash.com/photo-1544148103-0773bf10d330?q=80&w=600', title:'Thịt Nướng Nhật Bản Bao Gồm Cả Lẩu', rating:4.8, sold:1024, discount:28, price:640 },
                { brand:'Beauty Center', img:'https://images.unsplash.com/photo-1560750588-73207b1ef5b8?q=80&w=600', title:'Gói Chăm Sóc Da Mặt + Massage 90 Phút', rating:4.9, sold:341, discount:45, price:897 },
                { brand:'Vinpearl Resort', img:'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?q=80&w=600', title:'Combo 2N1Đ Vinpearl Resort + Vé Vui Chơi', rating:5.0, sold:1200, discount:30, price:3200 },
                { brand:'Fit24 Gym', img:'https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=600', title:'Thẻ Tập Gym Fit24 – 1 Tháng Không Giới Hạn', rating:4.8, sold:620, discount:40, price:480 },
                { brand:'Grab Car', img:'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=600', title:'Voucher Grab 100.000đ Cho 3 Chuyến Đi', rating:4.8, sold:12000, discount:50, price:150 },
                { brand:'Pet Spa', img:'https://images.unsplash.com/photo-1587300003388-59208cc962cb?q=80&w=600', title:'Tắm Gội + Cắt Tỉa Lông Cho Chó Mèo', rating:4.9, sold:540, discount:35, price:390 },
                { brand:'IELTS UP', img:'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?q=80&w=600', title:'Khóa Luyện Thi IELTS 6.5+ Trọn Gói 3 Tháng', rating:4.9, sold:680, discount:40, price:3600 },
                { brand:'Vinmec', img:'https://images.unsplash.com/photo-1631217868264-e6f75c354d01?q=80&w=600', title:'Gói Khám Sức Khỏe Tổng Quát Vinmec', rating:4.9, sold:560, discount:30, price:2100 },
                { brand:'Pizza 4P\'s', img:'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?q=80&w=600', title:'Set Ăn Đôi Pizza 4P\'s Cao Cấp', rating:4.9, sold:1800, discount:20, price:800 },
                { brand:'Innisfree', img:'https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?q=80&w=600', title:'Bộ Dưỡng Ẩm Innisfree Green Tea', rating:4.8, sold:1200, discount:40, price:540 },
                { brand:'Tour Bà Nà Hills', img:'https://images.unsplash.com/photo-1503220317375-aaad61436b1b?q=80&w=600', title:'Vé Cáp Treo Bà Nà Hills – Cầu Vàng', rating:4.9, sold:3400, discount:15, price:850 },
            ],
        },

        // Getter: trả về danh sách sản phẩm theo activeCat
        get currentCatProducts() {
            return this.catProducts[this.activeCat] || this.catProducts['Tất cả'];
        },

        flashDeals: [
            { brand: 'Le Monde Steak', img: 'https://images.unsplash.com/photo-1544148103-0773bf10d330?q=80&w=600', title: 'Thịt Nướng Nhật Bản Bao Gồm Cả Lẩu Chào Mừng', tag: 'MUA 1 TẶNG 1', remain: 5, total: 100, out: false, originalPrice: '450.000đ', salePrice: '320.000đ', discount: '28%', rating: 4.8, reviews: 312 },
            { brand: 'Yakimono', img: 'https://images.unsplash.com/photo-1550547660-d9450f859349?q=80&w=600', title: 'Set Nướng Bò Fuji Thượng Hạng Cực Ngon', tag: '-50% BẠCH KIM', remain: 30, total: 150, out: false, originalPrice: '750.000đ', salePrice: '375.000đ', discount: '50%', rating: 5.0, reviews: 1024 },
            { brand: 'Granden Charm', img: 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?q=80&w=600', title: 'Tặng 01 lọ nước hoa size mini cao cấp khi mua hóa đơn trên 1 triệu', tag: 'TẶNG QUÀ', remain: 55, total: 100, out: false, originalPrice: '200.000đ', salePrice: '0đ', discount: '100%', rating: 4.6, reviews: 88 },
            { brand: 'Shang Chi', img: 'https://images.unsplash.com/photo-1600891964092-4316c288032e?q=80&w=600', title: 'E-Coupon giảm 100k áp dụng cho Lẩu Băng Chuyền Shang Chi', tag: '-25% H.VÀNG', remain: 2, total: 50, out: false, originalPrice: '100.000đ', salePrice: '75.000đ', discount: '25%', rating: 4.9, reviews: 200 },
            { brand: 'bTaskee', img: 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=600', title: 'Voucher dọn dẹp nhà cửa toàn diện 4 giờ siêu sạch', tag: 'GIẢM GIÁ SỐC', remain: 0, total: 100, out: true, originalPrice: '320.000đ', salePrice: '150.000đ', discount: '53%', rating: 4.7, reviews: 900 },
            { brand: 'CGV Cinemas', img: 'https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=600', title: 'Vé xem phim 2D tất cả các cụm rạp trên toàn quốc', tag: '-30%', remain: 80, total: 200, out: false, originalPrice: '130.000đ', salePrice: '90.000đ', discount: '30%', rating: 4.8, reviews: 512 },
            { brand: 'Phúc Long', img: 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?q=80&w=600', title: 'Combo 2 ly trà sữa Phúc Long size L đủ vị', tag: 'HOT', remain: 40, total: 100, out: false, originalPrice: '120.000đ', salePrice: '79.000đ', discount: '34%', rating: 4.7, reviews: 670 },
            { brand: 'Tokbokki 247', img: 'https://images.unsplash.com/photo-1498654896293-37aacf113fd9?q=80&w=600', title: 'Set ăn vặt Hàn Quốc đường phố cho 2 người', tag: '-40%', remain: 20, total: 80, out: false, originalPrice: '200.000đ', salePrice: '119.000đ', discount: '40%', rating: 4.5, reviews: 233 },
            { brand: 'Beauty Center', img: 'https://images.unsplash.com/photo-1560750588-73207b1ef5b8?q=80&w=600', title: 'Gói chăm sóc da mặt + massage thư giãn 90 phút', tag: '-45%', remain: 15, total: 60, out: false, originalPrice: '550.000đ', salePrice: '299.000đ', discount: '45%', rating: 4.9, reviews: 341 },
            { brand: 'Lotte Cinema', img: 'https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=600', title: 'Vé xem phim tại Hệ thống Lotte Cinema toàn quốc', tag: '-15%', remain: 100, total: 300, out: false, originalPrice: '105.000đ', salePrice: '89.000đ', discount: '15%', rating: 4.8, reviews: 989 }
        ],
        vouchersNH: [
            { brand: 'Yakimono', logo: 'https://cdn.dealtoday.vn/img/s150x150/cgv_13032026142551.jpg?sign=9jYod5UnyYijJYC3ZBfNfw', img: 'https://images.unsplash.com/photo-1544148103-0773bf10d330?q=80&w=600', title: 'Thịt Nướng Nhật Bản Bao Gồm Cả Lẩu Chào Mừng', loc: 'Hồ Chí Minh', originalPrice: '230.000đ', salePrice: '189.000đ', discount: '18%', rating: 4.8, reviews: '89 đánh giá' },
            { brand: 'Shang Chi', logo: 'https://upload.wikimedia.org/wikipedia/vi/thumb/d/d3/Starbucks_Corporation_Logo_2011.svg/1280px-Starbucks_Corporation_Logo_2011.svg.png', img: 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?q=80&w=600', title: 'Buffet Lẩu Ngon Đỉnh Cao Giảm Ngay Cho Hóa Đơn Lớn', loc: 'Toàn quốc', originalPrice: '510.000đ', salePrice: '331.100đ', discount: '35%', rating: 5.0, reviews: '5k đã bán' }
        ],
        vouchersDV: [
            { brand: 'CGV Cinemas', logo: 'https://cdn.dealtoday.vn/img/s150x150/cgv_13032026142551.jpg?sign=9jYod5UnyYijJYC3ZBfNfw', img: 'https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=600', title: 'Vé xem phim 2D tất cả các cụm rạp trên toàn quốc cuối tuần', loc: 'Toàn quốc', originalPrice: '130.000đ', salePrice: '90.000đ', discount: '30%', rating: 4.8, reviews: '10k+ đã bán' },
            { brand: 'VinKE & Aquarium', logo: 'https://cdn.dealtoday.vn/img/s150x150/vinke-aquarium_16122024094725.jpg?sign=2_XGoQF_keva19HsaC8Iow', img: 'https://images.unsplash.com/photo-1560624052-449f5ddf0c31?q=80&w=600', title: 'Vé vào cổng khu vui chơi giải trí giáo dục VinKE Times City', loc: 'Hà Nội', originalPrice: '280.000đ', salePrice: '220.000đ', discount: '21%', rating: 4.7, reviews: '2.4k đánh giá' },
            { brand: 'KidZania', logo: 'https://cdn.dealtoday.vn/img/s150x150/KIDZANIA-LOTTE-MALL-logo_28062024112152.jpg?sign=JYuvv8Nc_ueUYK-jm62Jng', img: 'https://images.unsplash.com/photo-1534567153574-2b12153a87f0?q=80&w=600', title: 'Vé trải nghiệm hướng nghiệp KidZania Lotte Mall Tây Hồ', loc: 'Hà Nội', originalPrice: '350.000đ', salePrice: '299.000đ', discount: '14%', rating: 4.9, reviews: '900+ đã bán' },
            { brand: 'Lotte Cinema', logo: 'https://cdn.dealtoday.vn/img/s150x150/lotte-cinema-Logo_13112023171611.jpg?sign=dgb-aeD0hxDUwvwtDP818g', img: 'https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=600', title: 'Vé xem phim tại Hệ thống Lotte Cinema', loc: 'Toàn quốc', originalPrice: '105.000đ', salePrice: '89.000đ', discount: '15%', rating: 4.8, reviews: '541 đánh giá' },
            { brand: 'Highlands Coffee', logo: 'https://www.highlandscoffee.com.vn/vnt_upload/weblink/red_BG_logo800.png', img: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?q=80&w=600', title: 'Combo 2 ly cà phê Highlands Coffee size L + bánh mình', loc: 'Toàn quốc', originalPrice: '150.000đ', salePrice: '99.000đ', discount: '34%', rating: 4.6, reviews: '3.2k đã bán' }
        ],
        brands: [
            'https://www.highlandscoffee.com.vn/vnt_upload/weblink/red_BG_logo800.png',
            'https://upload.wikimedia.org/wikipedia/vi/thumb/d/d3/Starbucks_Corporation_Logo_2011.svg/1280px-Starbucks_Corporation_Logo_2011.svg.png',
            'https://cdn.dealtoday.vn/img/s150x150/cgv_13032026142551.jpg?sign=9jYod5UnyYijJYC3ZBfNfw',
            'https://cdn.dealtoday.vn/img/s150x150/vinke-aquarium_16122024094725.jpg?sign=2_XGoQF_keva19HsaC8Iow',
            'https://cdn.dealtoday.vn/img/s150x150/KIDZANIA-LOTTE-MALL-logo_28062024112152.jpg?sign=JYuvv8Nc_ueUYK-jm62Jng',
            'https://cdn.dealtoday.vn/img/s150x150/lotte-cinema-Logo_13112023171611.jpg?sign=dgb-aeD0hxDUwvwtDP818g',
            'https://cdn.dealtoday.vn/img/s150x150/b033a8f8238a481794293f8e1752c67d.png?sign=5Y5vPFS6D-RnNlsmD3_W-A'
        ],
        press: [
            'https://upload.wikimedia.org/wikipedia/commons/f/fd/VnExpress_logo.png',
            'https://static.thanhnien.com.vn/thanhnien.vn/image/logo-footer-mb.png',
            'https://upload.wikimedia.org/wikipedia/vi/e/e1/Logo_baomoi.png',
            'https://upload.wikimedia.org/wikipedia/commons/1/1f/Tu%E1%BB%95i_Tr%E1%BA%BB_Logo.svg',
            'https://media-cdn-v2.laodong.vn/storage/newsportal/2018/12/19/647577/Bao-Gia-Quang-Cao-Ba.png?w=526&h=314&crop=auto&scale=both',
            'https://static.wikia.nocookie.net/logos/images/d/d8/KTDT.png/revision/latest/scale-to-width-down/2000?cb=20250823112035&path-prefix=vi'
        ]
    };
}
