import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');
    
    .main {
        background: linear-gradient(135deg, #1a1a1a 0%, #000000 100%);
        min-height: 100vh;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #000000 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .hero-section {
        text-align: center;
        padding: 120px 40px;
        background: radial-gradient(circle at center, rgba(255,255,255,0.03) 0%, transparent 70%);
        border-radius: 0;
        margin: 0;
    }
    
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 5rem;
        font-weight: 100;
        color: white;
        margin-bottom: 30px;
        letter-spacing: -3px;
        line-height: 0.9;
    }
    
    @media (max-width: 768px) {
        .hero-title {
            font-size: 3rem;
            letter-spacing: -2px;
        }
    }
    
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.3rem;
        font-weight: 300;
        color: rgba(255,255,255,0.7);
        margin-bottom: 60px;
        line-height: 1.6;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }
    
    @media (max-width: 768px) {
        .hero-subtitle {
            font-size: 1.1rem;
            padding: 0 20px;
        }
    }
    
    .keynote-style {
        background: #000000;
        padding: 80px 0;
        text-align: center;
    }
    
    .product-reveal {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 200;
        color: white;
        margin-bottom: 20px;
        letter-spacing: -2px;
    }
    
    @media (max-width: 768px) {
        .product-reveal {
            font-size: 2.5rem;
        }
    }
    
    .product-tagline {
        font-family: 'Inter', sans-serif;
        font-size: 1.5rem;
        font-weight: 300;
        color: #007AFF;
        margin-bottom: 40px;
    }
    
    .section-header {
        font-family: 'Inter', sans-serif;
        font-size: 3rem;
        font-weight: 200;
        color: white;
        text-align: center;
        margin: 80px 0 50px 0;
        letter-spacing: -1.5px;
    }
    
    @media (max-width: 768px) {
        .section-header {
            font-size: 2rem;
            margin: 40px 0 30px 0;
        }
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
    
    @media (max-width: 768px) {
        .product-card {
            padding: 25px;
            margin: 20px 0;
        }
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
    
    @media (max-width: 768px) {
        .product-card:hover {
            transform: translateY(-5px);
        }
    }
    
    .product-name {
        font-size: 2.2rem;
        font-weight: 300;
        color: white;
        margin-bottom: 15px;
        font-family: 'Inter', sans-serif;
        letter-spacing: -1px;
    }
    
    @media (max-width: 768px) {
        .product-name {
            font-size: 1.8rem;
        }
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
    
    @media (max-width: 768px) {
        .impact-metrics {
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }
    }
    
    .metric {
        text-align: center;
        padding: 15px;
        background: rgba(0,122,255,0.1);
        border-radius: 12px;
        border: 1px solid rgba(0,122,255,0.2);
        transition: transform 0.3s ease;
    }
    
    .metric:hover {
        transform: scale(1.05);
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 600;
        color: #007AFF;
        font-family: 'Inter', sans-serif;
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
    
    @media (max-width: 768px) {
        .jobs-quote {
            padding: 40px 20px;
            margin: 40px 0;
        }
    }
    
    .quote-text {
        font-family: 'Inter', sans-serif;
        font-size: 2.2rem;
        font-weight: 200;
        color: white;
        line-height: 1.4;
        margin-bottom: 30px;
        font-style: italic;
        letter-spacing: -0.5px;
    }
    
    @media (max-width: 768px) {
        .quote-text {
            font-size: 1.5rem;
        }
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
    
    @media (max-width: 768px) {
        .innovation-grid {
            grid-template-columns: 1fr;
            gap: 20px;
        }
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
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 10px 20px;
        color: rgba(255,255,255,0.7);
    }
    
    .stTabs [aria-selected="true"] {
        background-color: rgba(0,122,255,0.3);
        color: white;
    }
    
    /* Contact section styling */
    .contact-section {
        text-align: center;
        padding: 60px 20px;
        background: linear-gradient(135deg, rgba(0,122,255,0.1) 0%, rgba(0,199,190,0.1) 100%);
        border-radius: 20px;
        margin: 40px 0;
    }
    
    .contact-title {
        font-size: 2rem;
        color: white;
        margin-bottom: 20px;
        font-weight: 200;
    }
    
    .contact-subtitle {
        font-size: 1.1rem;
        color: rgba(255,255,255,0.8);
        margin-bottom: 30px;
    }
    
    .contact-links {
        display: flex;
        justify-content: center;
        gap: 30px;
        flex-wrap: wrap;
    }
    
    .contact-link {
        background: rgba(0,122,255,0.2);
        padding: 15px 30px;
        border-radius: 25px;
        border: 1px solid rgba(0,122,255,0.3);
        text-decoration: none;
        color: #007AFF;
        transition: all 0.3s ease;
    }
    
    .contact-link:hover {
        background: rgba(0,122,255,0.3);
        transform: translateY(-2px);
    }
    
    .contact-link-alt {
        background: rgba(0,199,190,0.2);
        border: 1px solid rgba(0,199,190,0.3);
        color: #00C7BE;
    }
    
    .contact-link-alt:hover {
        background: rgba(0,199,190,0.3);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def get_market_data():
    """Cache market data to improve performance"""
    return {
        'Segment': ['Urban Digital Natives', 'Emerging City Users', 'Small Town Adopters', 'Rural First-Time Users'],
        'Users (Millions)': [120, 180, 250, 350],
        'Growth Rate (%)': [15, 35, 55, 85],
        'Opportunity Score': [85, 92, 88, 95]
    }

@st.cache_data
def get_roadmap_data():
    """Cache roadmap data to improve performance"""
    return {
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

def create_hero_section():
    """Create hero section with improved accessibility"""
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
    """Create product showcase section"""
    st.markdown("""
    <div class="keynote-style">
        <div class="product-reveal">The Future of Indian Commerce</div>
        <div class="product-tagline">Revolutionary. Intuitive. Unmistakably Indian.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Product Vision</div>', unsafe_allow_html=True)
    
    # Product data for better maintainability
    products = [
        {
            'name': '🌟 Bharat Discovery',
            'description': '''A revolutionary AI-powered hyperlocal discovery platform that understands the unique pulse of every Indian neighborhood. 
            From the street vendor who makes the best gol gappa to the hidden gem restaurant in your locality—discover India like never before.''',
            'metrics': [
                {'value': '2.5M', 'label': 'Local Businesses'},
                {'value': '40%', 'label': 'Discovery Rate ↑'},
                {'value': '15s', 'label': 'Avg Search Time'},
                {'value': '95%', 'label': 'User Satisfaction'}
            ]
        },
        {
            'name': '💳 SmartCredit Bharat',
            'description': '''India's first behavioral credit scoring system that goes beyond traditional metrics. Using digital footprints, 
            social commerce patterns, and community trust scores to democratize credit access for 400 million underbanked Indians.''',
            'metrics': [
                {'value': '400M', 'label': 'Addressable Users'},
                {'value': '78%', 'label': 'Approval Rate'},
                {'value': '3min', 'label': 'Credit Decision'},
                {'value': '12%', 'label': 'Default Rate'}
            ]
        },
        {
            'name': '🎤 VoiceCart Pro',
            'description': '''The next frontier of Indian commerce. Shop in Hindi, Tamil, Bengali, and 10+ regional languages using natural conversation. 
            "Mumma ke liye diabetes ki dawai mangwao" becomes a seamless shopping experience powered by context-aware AI.''',
            'metrics': [
                {'value': '12', 'label': 'Languages'},
                {'value': '89%', 'label': 'Voice Accuracy'},
                {'value': '45%', 'label': 'Conversion ↑'},
                {'value': '70%', 'label': 'Rural Adoption'}
            ]
        }
    ]
    
    for product in products:
        metrics_html = ''.join([
            f'''
            <div class="metric">
                <div class="metric-value">{metric['value']}</div>
                <div class="metric-label">{metric['label']}</div>
            </div>
            ''' for metric in product['metrics']
        ])
        
        st.markdown(f"""
        <div class="product-card">
            <div class="product-name">{product['name']}</div>
            <div class="product-description">{product['description']}</div>
            <div class="impact-metrics">{metrics_html}</div>
        </div>
        """, unsafe_allow_html=True)

def create_innovation_philosophy():
    """Create innovation philosophy section"""
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
    
    principles = [
        {
            'title': '🇮🇳 India-First Design',
            'desc': '''Every product decision is made with India's unique cultural, linguistic, 
            and economic context at its core. From Tier-1 cities to rural villages.'''
        },
        {
            'title': '📊 Data-Driven Empathy',
            'desc': '''Combining quantitative insights with qualitative understanding. 
            Numbers tell us what, but empathy tells us why and how.'''
        },
        {
            'title': '🚀 Frugal Innovation',
            'desc': '''Maximum impact with optimal resources. Building products that work 
            flawlessly on a ₹5,000 smartphone and 2G network.'''
        },
        {
            'title': '🔄 Iterative Perfection',
            'desc': '''Ship fast, learn faster. Every user interaction is a lesson 
            in building something more beautiful and functional.'''
        },
        {
            'title': '🌐 Scale with Purpose',
            'desc': '''Technology that scales to millions while maintaining the warmth 
            and personal touch of local Indian businesses.'''
        },
        {
            'title': '🔮 Future-Ready',
            'desc': '''Building for tomorrow's India—voice-first, AI-native, 
            and seamlessly integrated with digital payments ecosystem.'''
        }
    ]
    
    principles_html = ''.join([
        f'''
        <div class="innovation-item">
            <div class="innovation-title">{principle['title']}</div>
            <div class="innovation-desc">{principle['desc']}</div>
        </div>
        ''' for principle in principles
    ])
    
    st.markdown(f'<div class="innovation-grid">{principles_html}</div>', unsafe_allow_html=True)

def create_market_vision():
    """Create market vision with improved chart"""
    st.markdown('<div class="section-header">The Indian Market Opportunity</div>', unsafe_allow_html=True)
    
    market_data = get_market_data()
    df = pd.DataFrame(market_data)
    
    fig = go.Figure()
    
    # Improved bubble chart with better styling
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
        textfont=dict(color='white', size=10, family='Inter'),
        hovertemplate='<b>%{text}</b><br>' +
                      'Users: %{x}M<br>' +
                      'Growth Rate: %{y}%<br>' +
                      'Opportunity Score: %{marker.size}<extra></extra>',
        name=''
    ))
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family='Inter'),
        xaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            showgrid=True,
            title='Market Size (Millions of Users)',
            titlefont=dict(size=14, family='Inter'),
            tickfont=dict(size=12, family='Inter')
        ),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            showgrid=True,
            title='Annual Growth Rate (%)',
            titlefont=dict(size=14, family='Inter'),
            tickfont=dict(size=12, family='Inter')
        ),
        height=500,
        margin=dict(t=20, b=20, l=20, r=20),
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True, key="market_vision_chart")

def create_competitive_advantage():
    """Create competitive advantage section"""
    st.markdown('<div class="section-header">Competitive Differentiation</div>', unsafe_allow_html=True)
    
    advantages = [
        {
            'title': '🧠 AI-Powered Localization',
            'description': 'Deep learning models trained on Indian consumer behavior, linguistic nuances, and cultural preferences.',
            'impact': '3x higher engagement vs. global platforms',
            'color': '#007AFF'
        },
        {
            'title': '📱 Omnichannel Excellence',
            'description': 'Seamless experience across voice, text, video, and AR interfaces optimized for Indian internet infrastructure.',
            'impact': '89% cross-platform retention rate',
            'color': '#00C7BE'
        },
        {
            'title': '🤝 Trust-First Approach',
            'description': 'Community-driven trust scores, local influencer partnerships, and vernacular customer support.',
            'impact': '92% user trust score vs 67% industry avg',
            'color': '#FF6B6B'
        },
        {
            'title': '⚡ Hyperlocal Intelligence',
            'description': 'Real-time inventory, pricing, and availability data from 2.5M+ local businesses across India.',
            'impact': '95% accurate local recommendations',
            'color': '#FFD60A'
        }
    ]
    
    for adv in advantages:
        st.markdown(f"""
        <div class="product-card">
            <div class="product-name" style="color: {adv['color']}; font-size: 1.5rem;">{adv['title']}</div>
            <div class="product-description">{adv['description']}</div>
            <div style="background: rgba(0,122,255,0.1); padding: 15px; border-radius: 10px; margin-top: 20px; border-left: 3px solid {adv['color']};">
                <strong style="color: {adv['color']};">Impact:</strong> <span style="color: rgba(255,255,255,0.9);">{adv['impact']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_roadmap():
    """Create roadmap with improved visualization"""
    st.markdown('<div class="section-header">Product Roadmap</div>', unsafe_allow_html=True)
    
    roadmap_data = get_roadmap_data()
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
        textfont=dict(color='white', size=12, family='Inter'),
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
        font=dict(color='white', family='Inter'),
        xaxis=dict(
            showgrid=False,
            title='Timeline',
            titlefont=dict(size=14, family='Inter'),
            tickfont=dict(size=12, family='Inter')
        ),
        yaxis=dict(
            showgrid=False,
            showticklabels=False,
            title='',
            range=[0.5, 5.5]
        ),
        height=300,
        margin=dict(t=50, b=20, l=20, r=20),
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True, key="roadmap_chart")

def create_closing_vision():
    """Create closing vision section"""
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
    <div class="contact-section">
        <div class="contact-title">Ready to revolutionize Indian commerce?</div>
        <div class="contact-subtitle">Let's build the future, one brilliant product at a time.</div>
        <div class="contact-links">
            <a href="mailto:anandnegi104@gmail.com" class="contact-link">
                <span>📧</span> anandnegi104@gmail.com
            </a>
            <a href="https://www.linkedin.com/in/anandnegi15/" class="contact-link contact-link-alt" target="_blank" rel="noopener noreferrer">
                <span>💼</span> linkedin.com/in/anand-negi
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main application function"""
    try:
        create_hero_section()
        
        # Navigation with improved UX
        tab_names = ["🚀 Product Vision", "💡 Innovation DNA", "📊 Market Analysis", "🛣️ Roadmap", "🌟 Philosophy"]
        tabs = st.tabs(tab_names)
        
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
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please refresh the page or contact support.")

if __name__ == "__main__":
    main()
