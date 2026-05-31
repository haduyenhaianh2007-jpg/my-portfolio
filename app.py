import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Nguyen Khanh Ngoc | Portfolio 🎀",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (Pink Corporate & Aesthetic Theme) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    
    .stApp {
        background-color: #FFF8FA; /* Soft Section Background */
        color: #2C2C2C;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #F4D7E1; /* My Melody Light Pink */
    }
    
    /* Headings styling */
    h1, h2, h3 {
        color: #A64D79 !important; /* Deep Rose Accent */
        font-family: 'Playfair Display', serif;
        font-weight: 700;
    }
    
    /* Professional Card Layout */
    .pink-card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        border: 2px dashed #D88CA3; /* Playful dashed border */
        box-shadow: 0px 8px 16px rgba(216, 140, 163, 0.15);
        margin-bottom: 25px;
        transition: transform 0.3s, border-style 0.3s;
    }
    .pink-card:hover {
        transform: translateY(-5px);
        border-style: solid;
    }
    
    /* Swimming Fish Animation */
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
    
    /* Cute Skill Tags */
    .skill-tag {
        display: inline-block;
        background-color: #F4D7E1;
        color: #7A294F;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 600;
        margin: 5px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<div style='text-align: center;'><h2>🎀 My Melody Nav 🎀</h2></div>", unsafe_allow_html=True)
    st.write("---")
    
    # Cosmetics & Aesthetics Corner
    st.markdown("### 💄 Aesthetics & Vision")
    st.caption("Strategic marketing thinking rooted in the ultimate appreciation of beauty, culture, and lifestyle.")
    st.info("✨ Theme: Pink Corporate (#D88CA3)")
    
    st.write("---")
    st.markdown("### 📞 Contact Me")
    st.text("📧 kngocnguyen1506@gmail.com")
    st.text("📞 0824901827")
    st.text("📍 Hanoi, Vietnam")
    st.text("🎂 Born: June 15, 2006")

# --- MAIN HERO SECTION ---
col_avatar, col_title = st.columns([1, 2.5])

with col_avatar:
    # Mascot placeholder - Can be replaced with Ngoc's actual portrait URL later
    st.image("https://img.icons8.com/plasticine/200/hello-kitty.png", caption="Creative Mascot ✨")

with col_title:
    st.markdown("""
    <h1 style='font-size: 45px; margin-bottom: 0px;'>NGUYỄN KHÁNH NGỌC</h1>
    <p style='font-size: 18px; color: #7A294F; font-weight: 500; letter-spacing: 1px;'>
        International Business Student | Digital Marketing Enthusiast | Creative Storyteller
    </p>
    <p style='font-size: 16px; font-style: italic; color: #6B7280; font-family: "Playfair Display", serif;'>
        "Turning ideas into stories and stories into impact." 🎀
    </p>
    """, unsafe_allow_html=True)

st.write("---")

# --- ABOUT ME & INTERESTS ---
col1, col2 = st.columns([1.8, 1.2])

with col1:
    st.markdown("## 🌸 About Me")
    st.markdown(
        """
        <div class="pink-card">
            I am a second-year International Business student at <b>Foreign Trade University (FTU)</b> 
            with a profound interest in Digital Marketing, Branding, and Creative Communication.<br><br>
            My academic background, combined with experiences in music performance and extracurricular activities, 
            has helped me develop a unique blend of <b>analytical thinking and artistic creativity</b>. I thrive on 
            transforming raw ideas into compelling brand narratives that build meaningful connections.
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown("## 🐠 Why Marketing & My Passions")
    st.markdown(
        """
        <div class="pink-card">
            <h4>💡 Why Digital Marketing?</h4>
            Marketing is the perfect playground where business logic meets artistic expression. It allows me to deconstruct 
            consumer insights and weave them into impactful stories—much like how the perfect lipstick shade 
            or a beautiful melody instantly captivates a crowd.<br><br>
            <h4>🎀 Personal Passions:</h4>
            <ul>
                <li>🍉 Collecting cute aesthetic items (Hello Kitty & My Melody enthusiast).</li>
                <li>💄 Exploring cosmetics, skincare trends, and visual makeup arts (The science of aesthetics).</li>
                <li>🎵 Music, live performance, and public speaking under the spotlight.</li>
            </ul>
            <div style='text-align: right;'><span class="swimming-fish">🐟</span></div>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown("## 🏫 Education")
    st.markdown(
        """
        <div class="pink-card" style="border-color: #A64D79;">
            <b>🎓 Foreign Trade University (FTU)</b><br>
            <span style='color: #6B7280; font-size:13px;'>2024 – Present</span><br>
            Bachelor of International Business<br><br>
            <b>🏫 Lam Son High School for the Gifted</b><br>
            <span style='color: #6B7280; font-size:13px;'>English Specialized Class</span><br>
            🎯 <b>IELTS Score: 7.5</b>
        </div>
        """, unsafe_allow_html=True
    )

# --- ACHIEVEMENTS & EXPERIENCE ---
st.markdown("## 🏆 Key Achievements & Experience")
col_ach1, col_ach2, col_ach3 = st.columns(3)

with col_ach1:
    st.markdown(
        """
        <div class="pink-card" style="height: 260px;">
            <h3>🥇 Champion</h3>
            <p><b>Now You See Me 2024</b></p>
            <span style='font-size: 13px; color: #555;'>Led a cross-functional team to develop creative communication strategies, delivering high-impact marketing solutions and sharpening project execution skills under pressure.</span>
        </div>
        """, unsafe_allow_html=True
    )

with col_ach2:
    st.markdown(
        """
        <div class="pink-card" style="height: 260px;">
            <h3>🎤 Third Prize</h3>
            <p><b>The Voice Kids Vietnam 2016</b></p>
            <span style='font-size: 13px; color: #555;'>Cultivated immense confidence in public performance, stage presentation, and audience emotional engagement from an early age.</span>
        </div>
        """, unsafe_allow_html=True
    )

with col_ach3:
    st.markdown(
        """
        <div class="pink-card" style="height: 260px;">
            <h3>🎸 Lam Son Music Club</h3>
            <p><b>Event Organizing Team</b></p>
            <span style='font-size: 13px; color: #555;'>Brainstormed distinct promotional concepts, curated social media content, and coordinated logistics for flagship community music events.</span>
        </div>
        """, unsafe_allow_html=True
    )

# --- CORE COMPETENCIES ---
st.markdown("## 💅 Core Competencies")
st.markdown("""
<div class="pink-card" style="text-align: center;">
    <span class="skill-tag">💄 Content Creation</span>
    <span class="skill-tag">🎀 Social Media Marketing</span>
    <span class="skill-tag">✨ Brand Storytelling</span>
    <span class="skill-tag">🎀 Public Speaking</span>
    <span class="skill-tag">💄 Creative Campaigns</span>
    <span class="skill-tag">✨ Consumer Insights</span>
    <span class="skill-tag">🐟 Presentation Design</span>
    <span class="skill-tag">🎀 Copywriting</span>
    <span class="skill-tag">💄 Team Collaboration</span>
    <span class="skill-tag">✨ Critical Thinking</span>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #A64D79;'>Made with 💖 by Nguyen Khanh Ngoc © 2026 | Perfectly blending Hello Kitty aesthetics with a Business Mindset</div>", 
    unsafe_allow_html=True
)
