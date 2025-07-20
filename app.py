import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# Configure page
st.set_page_config(
    page_title="Anand Negi • Product Visionary",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Steve Jobs aesthetic
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@100;200;300;400;500;600;700;800;900&family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');
    
    .main {
        background: linear-gradient(135deg, #1a1a1a 0%, #000000 100%);
        min-height: 100vh;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #000000 100%);
    }
    
    .hero-section {
        text-align: center;
        padding: 120px 40px;
        background: radial-gradient(circle at center, rgba(255,255,255,0.03) 0%, transparent 70%);
        border-radius: 0;
        margin: 0;
    }
    
    .hero-title {
        font-family: 'SF Pro Display', 'Inter', sans-serif;
        font-size: 5rem;
        font-weight: 100;
        color: white;
        margin-bottom: 30px;
        letter-spacing: -3px;
        line-height: 0.9;
    }
    
    .hero-subtitle {
        font-family: 'SF Pro Display', 'Inter', sans-serif;
        font-size: 1.3rem;
        font-weight: 300;
        color: rgba(255,255,255,0.7);
        margin-bottom: 60px;
        line-height: 1.6;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .keynote-style {
        background: #000000;
        padding: 80px 0;
        text-align: center;
    }
    
    .product-reveal {
        font-family: 'SF Pro Display', sans-serif;
        font-size: 3.5rem;
        font-weight: 200;
        color: white;
        margin-bottom: 20px;
        letter-spacing: -2px;
    }
    
    .product-tagline {
        font-family: 'SF Pro Display', sans-serif;
        font-size: 1.5rem;
        font-weight: 300;
        color: #007AFF;
        margin-bottom: 40px;
    }
    
    .section-header {
        font-family: 'SF Pro Display', sans-serif;
        font-size: 3rem;
        font-weight: 200;
        color: white;
        text-align: center;
        margin: 80px 0 50px 0;
        letter-spacing: -1.5px;
    }
    
    .product-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 40px;
        margin: 30px 0;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .product-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #007AFF 0%, #00C7BE 100%);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }
    
    .product-card:hover::before {
        transform: scaleX(1);
    }
    
    .product-card:hover {
        transform: translateY(-15px);
        background: linear-gradient(145deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.04) 100%);
        border-color: rgba(0,122,255,0.3);
    }
    
    .product-name {
        font-size: 2.2rem;
        font-weight: 300;
        color: white;
        margin-bottom: 15px;
        font-family: 'SF Pro Display', sans-serif;
        letter-spacing: -1px;
    }
    
    .product-description {
        font-size: 1.1rem;
        color: rgba(255,255,255,0.8);
        margin-bottom: 25px;
        line-height: 1.6;
        font-weight: 300;
    }
    
    .impact-metrics {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 20px;
        margin-top: 30px;
    }
    
    .metric {
        text-align: center;
        padding: 15px;
        background: rgba(0,122,255,0.1);
        border-radius: 12px;
        border: 1px solid rgba(0,122,255,0.2);
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 600;
        color: #007AFF;
        font-family: 'SF Pro Display', sans-serif;
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: rgba(255,255,255,0.6);
        margin-top: 5px;
        font-weight: 300;
    }
    
    .jobs-quote {
        background: linear-gradient(145deg, #1d1d1f 0%, #000000 100%);
        padding: 80px 40px;
        text-align: center;
        border-top: 1px solid rgba(255,255,255,0.1);
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin: 60px 0;
    }
    
    .quote-text {
        font-family: 'SF Pro Display', sans-serif;
        font-size: 2.2rem;
        font-weight: 200;
        color: white;
        line-height: 1.4;
        margin-bottom: 30px;
        font-style: italic;
        letter-spacing: -0.5px;
    }
    
    .quote-author {
        font-size: 1rem;
        color: rgba(255,255,255,0.5);
        font-weight: 400;
    }
    
    .innovation-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
        margin: 40px 0;
    }
    
    .innovation-item {
        background: linear-gradient(135deg, rgba(0,122,255,0.1) 0%, rgba(0,199,190,0.1) 100%);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid rgba(0,122,255,0.2);
        transition: all 0.3s ease;
    }
    
    .innovation-item:hover {
        transform: scale(1.02);
        border-color: rgba(0,122,255,0.4);
    }
    
    .innovation-title {
        font-size: 1.3rem;
        font-weight: 500;
        color: #007AFF;
        margin-bottom: 15px;
    }
    
    .innovation-desc {
        color: rgba(255,255,255,0.8);
        line-height: 1.5;
        font-weight: 300;
    }
</style>
""", unsafe_allow_html=True)

def create_hero_section():
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">One more thing...</div>
        <div class="hero-subtitle">
            I'm Anand Negi. I believe that great products aren't just built—they're imagined, 
            crafted, and perfected until they transform the way people live, work, and connect 
            in the digital heart of India.
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_product_showcase():
    st.markdown("""
    <div class="keynote-style">
        <div class="product-reveal">The Future of Indian Commerce</div>
        <div class="product-tagline">Revolutionary. Intuitive. Unmistakably Indian.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Product Vision</div>', unsafe_allow_html=True)
    
    # Product 1: HyperLocal Discovery Engine
    st.markdown("""
    <div class="product-card">
        <div class="product-name">🌟 Bharat Discovery</div>
        <div class="product-description">
            A revolutionary AI-powered hyperlocal discovery platform that understands the unique pulse of every Indian neighborhood. 
            From the street vendor who makes the best gol gappa to the hidden gem restaurant in your locality—discover India like never before.
        </div>
        <div class="impact-metrics">
            <div class="metric">
                <div class="metric-value">2.5M</div>
                <div class="metric-label">Local Businesses</div>
            </div>
            <div class="metric">
                <div class="metric-value">40%</div>
                <div class="metric-label">Discovery Rate ↑</div>
            </div>
            <div class="metric">
                <div class="metric-value">15s</div>
                <div class="metric-label">Avg Search Time</div>
            </div>
            <div class="metric">
                <div class="metric-value">95%</div>
                <div class="metric-label">User Satisfaction</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Product 2: Smart Credit for Bharat
    st.markdown("""
    <div class="product-card">
        <div class="product-name">💳 SmartCredit Bharat</div>
        <div class="product-description">
            India's first behavioral credit scoring system that goes beyond traditional metrics. Using digital footprints, 
            social commerce patterns, and community trust scores to democratize credit access for 400 million underbanked Indians.
        </div>
        <div class="impact-metrics">
            <div class="metric">
                <div class="metric-value">400M</div>
                <div class="metric-label">Addressable Users</div>
            </div>
            <div class="metric">
                <div class="metric-value">78%</div>
                <div class="metric-label">Approval Rate</div>
            </div>
            <div class="metric">
                <div class="metric-value">3min</div>
                <div class="metric-label">Credit Decision</div>
            </div>
            <div class="metric">
                <div class="metric-value">12%</div>
                <div class="metric-label">Default Rate</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Product 3: Voice Commerce Revolution
    st.markdown("""
    <div class="product-card">
        <div class="product-name">🎤 VoiceCart Pro</div>
        <div class="product-description">
            The next frontier of Indian commerce. Shop in Hindi, Tamil, Bengali, and 10+ regional languages using natural conversation. 
            "Mumma ke liye diabetes ki dawai mangwao" becomes a seamless shopping experience powered by context-aware AI.
        </div>
        <div class="impact-metrics">
            <div class="metric">
                <div class="metric-value">12</div>
                <div class="metric-label">Languages</div>
            </div>
            <div class="metric">
                <div class="metric-value">89%</div>
                <div class="metric-label">Voice Accuracy</div>
            </div>
            <div class="metric">
                <div class="metric-value">45%</div>
                <div class="metric-label">Conversion ↑</div>
            </div>
            <div class="metric">
                <div class="metric-value">70%</div>
                <div class="metric-label">Rural Adoption</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_innovation_philosophy():
    st.markdown("""
    <div class="jobs-quote">
        <div class="quote-text">
            "Innovation distinguishes between a leader and a follower. 
            In India's digital revolution, we don't follow—we lead."
        </div>
        <div class="quote-author">— Product Philosophy</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Innovation Principles</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="innovation-grid">
        <div class="innovation-item">
            <div class="innovation-title">🇮🇳 India-First Design</div>
            <div class="innovation-desc">
                Every product decision is made with India's unique cultural, linguistic, 
                and economic context at its core. From Tier-1 cities to rural villages.
            </div>
        </div>
        <div class="innovation-item">
            <div class="innovation-title">📊 Data-Driven Empathy</div>
            <div class="innovation-desc">
                Combining quantitative insights with qualitative understanding. 
                Numbers tell us what, but empathy tells us why and how.
            </div>
        </div>
        <div class="innovation-item">
            <div class="innovation-title">🚀 Frugal Innovation</div>
            <div class="innovation-desc">
                Maximum impact with optimal resources. Building products that work 
                flawlessly on a ₹5,000 smartphone and 2G network.
            </div>
        </div>
        <div class="innovation-item">
            <div class="innovation-title">🔄 Iterative Perfection</div>
            <div class="innovation-desc">
                Ship fast, learn faster. Every user interaction is a lesson 
                in building something more beautiful and functional.
            </div>
        </div>
        <div class="innovation-item">
            <div class="innovation-title">🌐 Scale with Purpose</div>
            <div class="innovation-desc">
                Technology that scales to millions while maintaining the warmth 
                and personal touch of local Indian businesses.
            </div>
        </div>
        <div class="innovation-item">
            <div class="innovation-title">🔮 Future-Ready</div>
            <div class="innovation-desc">
                Building for tomorrow's India—voice-first, AI-native, 
                and seamlessly integrated with digital payments ecosystem.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_market_vision():
    st.markdown('<div class="section-header">The Indian Market Opportunity</div>', unsafe_allow_html=True)
    
    # Create market data visualization
    market_data = {
        'Segment': ['Urban Digital Natives', 'Emerging City Users', 'Small Town Adopters', 'Rural First-Time Users'],
        'Users (Millions)': [120, 180, 250, 350],
        'Growth Rate (%)': [15, 35, 55, 85],
        'Opportunity Score': [85, 92, 88, 95]
    }
    
    df = pd.DataFrame(market_data)
    
    fig = go.Figure()
    
    # Bubble chart
    fig.add_trace(go.Scatter(
        x=df['Users (Millions)'],
        y=df['Growth Rate (%)'],
        mode='markers+text',
        marker=dict(
            size=df['Opportunity Score'],
            color=['#007AFF', '#00C7BE', '#FF6B6B', '#FFD60A'],
            opacity=0.8,
            sizeref=2.*max(df['Opportunity Score'])/(40.**2),
            sizemin=4,
            line=dict(width=2, color='rgba(255,255,255,0.8)')
        ),
        text=df['Segment'],
        textposition="middle center",
        textfont=dict(color='white', size=10),
        hovertemplate='<b>%{text}</b><br>' +
                      'Users: %{x}M<br>' +
                      'Growth Rate: %{y}%<br>' +
                      'Opportunity Score: %{marker.size}<extra></extra>',
        name=''
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family='SF Pro Display'),
        xaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            showgrid=True,
            title='Market Size (Millions of Users)',
            titlefont=dict(size=14)
        ),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            showgrid=True,
            title='Annual Growth Rate (%)',
            titlefont=dict(size=14)
        ),
        height=500,
        margin=dict(t=20, b=20, l=20, r=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

def create_competitive_advantage():
    st.markdown('<div class="section-header">Competitive Differentiation</div>', unsafe_allow_html=True)
    
    advantages = [
        {
            'title': '🧠 AI-Powered Localization',
            'description': 'Deep learning models trained on Indian consumer behavior, linguistic nuances, and cultural preferences.',
            'impact': '3x higher engagement vs. global platforms'
        },
        {
            'title': '📱 Omnichannel Excellence',
            'description': 'Seamless experience across voice, text, video, and AR interfaces optimized for Indian internet infrastructure.',
            'impact': '89% cross-platform retention rate'
        },
        {
            'title': '🤝 Trust-First Approach',
            'description': 'Community-driven trust scores, local influencer partnerships, and vernacular customer support.',
            'impact': '92% user trust score vs 67% industry avg'
        },
        {
            'title': '⚡ Hyperlocal Intelligence',
            'description': 'Real-time inventory, pricing, and availability data from 2.5M+ local businesses across India.',
            'impact': '95% accurate local recommendations'
        }
    ]
    
    for i, adv in enumerate(advantages):
        color_scheme = ['#007AFF', '#00C7BE', '#FF6B6B', '#FFD60A'][i % 4]
        st.markdown(f"""
        <div class="product-card">
            <div class="product-name" style="color: {color_scheme}; font-size: 1.5rem;">{adv['title']}</div>
            <div class="product-description">{adv['description']}</div>
            <div style="background: rgba(0,122,255,0.1); padding: 15px; border-radius: 10px; margin-top: 20px; border-left: 3px solid {color_scheme};">
                <strong style="color: {color_scheme};">Impact:</strong> <span style="color: rgba(255,255,255,0.9);">{adv['impact']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_roadmap():
    st.markdown('<div class="section-header">Product Roadmap</div>', unsafe_allow_html=True)
    
    roadmap_data = {
        'Phase': ['Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026'],
        'Focus': ['MVP Launch', 'AI Enhancement', 'Scale & Optimize', 'Market Expansion', 'Innovation Lab'],
        'Key Features': [
            'Core Discovery Engine',
            'Voice Commerce Beta',
            'Regional Language Support',
            'B2B Marketplace',
            'AR/VR Integration'
        ],
        'Target Users': ['500K', '2M', '10M', '25M', '50M']
    }
    
    df_roadmap = pd.DataFrame(roadmap_data)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df_roadmap['Phase'],
        y=[1, 2, 3, 4, 5],
        mode='markers+lines+text',
        marker=dict(
            size=30,
            color=['#007AFF', '#00C7BE', '#FF6B6B', '#FFD60A', '#FF9F00'],
            line=dict(width=3, color='white')
        ),
        line=dict(width=4, color='rgba(255,255,255,0.3)'),
        text=df_roadmap['Target Users'],
        textposition="top center",
        textfont=dict(color='white', size=12, family='SF Pro Display'),
        hovertemplate='<b>%{x}</b><br>' +
                      'Focus: %{customdata[0]}<br>' +
                      'Key Feature: %{customdata[1]}<br>' +
                      'Target Users: %{text}<extra></extra>',
        customdata=list(zip(df_roadmap['Focus'], df_roadmap['Key Features'])),
        name=''
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family='SF Pro Display'),
        xaxis=dict(
            showgrid=False,
            title='Timeline',
            titlefont=dict(size=14)
        ),
        yaxis=dict(
            showgrid=False,
            showticklabels=False,
            title=''
        ),
        height=300,
        margin=dict(t=50, b=20, l=20, r=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

def create_closing_vision():
    st.markdown("""
    <div class="jobs-quote">
        <div class="quote-text">
            "The people in the Indian market don't know what they want until you show it to them. 
            Our job is to figure out what they're going to want before they do."
        </div>
        <div class="quote-author">— Inspired by Steve Jobs, Adapted for Bharat</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; padding: 60px 20px; background: linear-gradient(135deg, rgba(0,122,255,0.1) 0%, rgba(0,199,190,0.1) 100%); border-radius: 20px; margin: 40px 0;">
        <div style="font-size: 2rem; color: white; margin-bottom: 20px; font-weight: 200;">Ready to revolutionize Indian commerce?</div>
        <div style="font-size: 1.1rem; color: rgba(255,255,255,0.8); margin-bottom: 30px;">Let's build the future, one brilliant product at a time.</div>
        <div style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap;">
            <div style="background: rgba(0,122,255,0.2); padding: 15px 30px; border-radius: 25px; border: 1px solid rgba(0,122,255,0.3);">
                <span style="color: #007AFF;">📧</span> anandnegi104@gmail.com
            </div>
            <div style="background: rgba(0,199,190,0.2); padding: 15px 30px; border-radius: 25px; border: 1px solid rgba(0,199,190,0.3);">
                <span style="color: #00C7BE;">💼</span> linkedin.com/in/anandnegi15
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    create_hero_section()
    
    # Navigation
    tabs = st.tabs(["🚀 Product Vision", "💡 Innovation DNA", "📊 Market Analysis", "🛣️ Roadmap", "🌟 Philosophy"])
    
    with tabs[0]:
        create_product_showcase()
    
    with tabs[1]:
        create_innovation_philosophy()
        create_competitive_advantage()
    
    with tabs[2]:
        create_market_vision()
    
    with tabs[3]:
        create_roadmap()
    
    with tabs[4]:
        create_closing_vision()

if __name__ == "__main__":
    main()
