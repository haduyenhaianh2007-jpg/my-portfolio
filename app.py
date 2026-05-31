import streamlit as st

# Cấu hình trang web (Tên hiển thị trên tab trình duyệt và Icon)
st.set_page_config(
    page_title="Nguyễn Khánh Ngọc | Portfolio 🎀",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (Nơi biến hóa giao diện thành màu Hồng Bánh Bèo + Chuyên Nghiệp) ---
st.markdown("""
<style>
    /* Font chữ sang xịn mịn */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    
    .stApp {
        background-color: #FFF8FA; /* Section Background nhạt nhẹ nhàng */
        color: #2C2C2C;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Chỉnh màu thanh menu bên cạnh */
    [data-testid="stSidebar"] {
        background-color: #F4D7E1; /* Hồng nhạt My Melody */
    }
    
    /* Các tiêu đề lớn */
    h1, h2, h3 {
        color: #A64D79 !important; /* Accent Headline */
        font-family: 'Playfair Display', serif;
        font-weight: 700;
    }
    
    /* Thiết kế chiếc hộp thông tin (Cards) */
    .pink-card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        border: 2px dashed #D88CA3; /* Viền đứt nét đáng yêu */
        box-shadow: 0px 8px 16px rgba(216, 140, 163, 0.15);
        margin-bottom: 25px;
        transition: transform 0.3s;
    }
    .pink-card:hover {
        transform: translateY(-5px);
        border-style: solid;
    }
    
    /* Hiệu ứng chú cá bơi lội dễ thương */
    .swimming-fish {
        display: inline-block;
        font-size: 30px;
        animation: swim 4s ease-in-out infinite alternate;
    }
    @keyframes swim {
        0% { transform: translateX(0px) scaleX(1); }
        50% { transform: translateX(30px) scaleX(1); }
        51% { transform: translateX(30px) scaleX(-1); }
        100% { transform: translateX(0px) scaleX(-1); }
    }
    
    /* Tag kỹ năng điệu đà */
    .skill-tag {
        display: inline-block;
        background-color: #F4D7E1;
        color: #7A294F;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: bold;
        margin: 5px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (Thanh Menu bên trái) ---
with st.sidebar:
    st.markdown("<div style='text-align: center;'><h2>🎀 My Melody Navigation 🎀</h2></div>", unsafe_allow_html=True)
    st.write("---")
    
    # Thêm yếu tố mỹ phẩm/mỹ phân trang trí theo yêu cầu
    st.markdown("### 💄 Góc Mỹ Phân & Làm Đẹp")
    st.caption("Tư duy Marketing bắt nguồn từ sự thấu hiểu cái đẹp và phong cách sống.")
    st.info("✨ Tone màu chủ đạo: Pink Corporate (#D88CA3)")
    
    st.write("---")
    st.markdown("### 📞 Liên hệ với Ngọc")
    st.text("📧 kngocnguyen1506@gmail.com")
    st.text("📞 0824901827")
    st.text("📍 Hà Nội, Việt Nam")
    st.text("🎂 Sinh ngày: 15/06/2006")

# --- MAIN CONTENT (Nội dung chính của Portfolio) ---

# Header hoành tráng phong cách Hello Kitty kết hợp chuyên nghiệp
col_avatar, col_title = st.columns([1, 2.5])

with col_avatar:
    # Thay link ảnh Hello Kitty/Melody hoặc ảnh của Ngọc ở đây
    st.image("https://img.icons8.com/plasticine/200/hello-kitty.png", caption="Ngọc's Concept Mascot ✨")

with col_title:
    st.markdown("""
    <h1 style='font-size: 45px; margin-bottom: 0px;'>NGUYỄN KHÁNH NGỌC</h1>
    <p style='font-size: 18px; color: #7A294F; font-weight: 500; letter-spacing: 1px;'>
        International Business Student | Digital Marketing Enthusiast | Creative Storyteller
    </p>
    <p style='font-size: 16px; font-style: italic; color: #6B7280;'>
        "Turning ideas into stories and stories into impact." 🎀
    </p>
    """, unsafe_allow_html=True)

st.write("---")

# Layout chia 2 cột cho phần giới thiệu bản thân
col1, col2 = st.columns([1.8, 1.2])

with col1:
    st.markdown("## 🌸 Giới Thiệu Bản Thân (About Me)")
    st.markdown(
        """
        <div class="pink-card">
            Chào mọi người! Mình là <b>Khánh Ngọc</b>, hiện là sinh viên năm 2 ngành Kinh doanh Quốc tế 
            tại <b>Trường Đại học Ngoại thương (FTU)</b>.<br><br>
            Sự kết hợp giữa tư duy logic từ ngành học kinh tế cùng tâm hồn đam mê nghệ thuật, âm nhạc và làm đẹp (mỹ phân) 
            đã định hình nên một cá tính Marketing rất riêng trong mình: <b>Đầy chiến lược nhưng không thiếu phần sáng tạo bay bổng.</b>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown("## 🐠 Lý Do Chọn Ngành & Sở Thích")
    st.markdown(
        """
        <div class="pink-card">
            <h4>💡 Lý do chọn ngành Digital Marketing:</h4>
            Marketing là nơi mình được tự do kể những câu chuyện thương hiệu đầy cảm xúc, chạm đến insight khách hàng 
            giống như cách một bài hát hay hoặc một thỏi son đẹp làm lay động phái nữ.<br><br>
            <h4>🎀 Sở thích cá nhân:</h4>
            <ul>
                <li>🍉 Sưu tầm các ấn phẩm dễ thương như Hello Kitty, My Melody.</li>
                <li>💄 Nghiên cứu về ngành công nghiệp mỹ phẩm, skincare, makeup (Yếu tố mỹ phân nghệ thuật).</li>
                <li>🎵 Ca hát và biểu diễn âm nhạc biểu diễn nghệ thuật dưới ánh đèn sân khấu.</li>
            </ul>
            <div style='text-align: right;'><span class="swimming-fish">🐟</span></div>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown("## 🏫 Học Vấn (Education)")
    st.markdown(
        """
        <div class="pink-card" style="border-color: #A64D79;">
            <b>🎓 Đại học Ngoại thương (FTU)</b><br>
            <span style='color: #6B7280; font-size:13px;'>2024 – Hiện tại</span><br>
            Cử nhân Kinh doanh Quốc tế<br><br>
            <b>🏫 THPT Chuyên Lam Sơn</b><br>
            <span style='color: #6B7280; font-size:13px;'>Lớp chuyên Anh</span><br>
            🎯 <b>IELTS: 7.5</b>
        </div>
        """, unsafe_allow_html=True
    )

# Phần Hoạt động ngoại khóa & Thành tựu nổi bật
st.markdown("## 🏆 Thành Tựu & Hoạt Động Ngoại Khóa")
col_ach1, col_ach2, col_ach3 = st.columns(3)

with col_ach1:
    st.markdown(
        """
        <div class="pink-card" style="height: 250px;">
            <h3>🥇 Quán Quân</h3>
            <p><b>Now You See Me 2024</b></p>
            <span style='font-size: 13px; color: #555;'>Dẫn dắt đội nhóm xây dựng các chiến dịch truyền thông sáng tạo, nâng cao kỹ năng thuyết trình và làm việc nhóm dưới áp lực lớn.</span>
        </div>
        """, unsafe_allow_html=True
    )

with col_ach2:
    st.markdown(
        """
        <div class="pink-card" style="height: 250px;">
            <h3>🎤 Giải Ba</h3>
            <p><b>The Voice Kids Vietnam 2016</b></p>
            <span style='font-size: 13px; color: #555;'>Rèn luyện sự tự tin trước đám đông, tư duy sân khấu và khả năng giao tiếp, truyền tải năng lượng tích cực từ khi còn nhỏ.</span>
        </div>
        """, unsafe_allow_html=True
    )

with col_ach3:
    st.markdown(
        """
        <div class="pink-card" style="height: 250px;">
            <h3>🎸 Lam Son Music Club</h3>
            <p><b>Thành viên Ban Tổ Chức</b></p>
            <span style='font-size: 13px; color: #555;'>Lên ý tưởng truyền thông, thiết kế concept sự kiện âm nhạc học sinh, quản lý nội dung fanpage thu hút hàng ngàn lượt tương tác.</span>
        </div>
        """, unsafe_allow_html=True
    )

# Kỹ năng (Core Competencies) thiết kế dạng các hạt tag màu hồng xinh xắn
st.markdown("## 💅 Kỹ Năng Cốt Lõi (Core Competencies)")
st.markdown("""
<div class="pink-card" style="text-align: center;">
    <span class="skill-tag">💄 Content Creation</span>
    <span class="skill-tag">🎀 Social Media Marketing</span>
    <span class="skill-tag">✨ Brand Storytelling</span>
    <span class="skill-tag">🎀 Public Speaking</span>
    <span class="skill-tag">💄 Creative Campaign</span>
    <span class="skill-tag">✨ Consumer Insights</span>
    <span class="skill-tag">🐟 Presentation Design</span>
    <span class="skill-tag">🎀 English (IELTS 7.5)</span>
</div>
""", unsafe_allow_html=True)

# Footer chân trang web
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #A64D79;'>Made with 💖 by Nguyễn Khánh Ngọc © 2026 | Mang đậm phong cách Hello Kitty & Business Minded</div>", 
    unsafe_allow_html=True
)