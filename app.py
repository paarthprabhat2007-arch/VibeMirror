import streamlit as st
import plotly.graph_objects as go
import html

from questions import QUESTIONS

from personality_engine import (
    analyse_personality,
    generate_personality_report
)


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="VibeMirror | Discover Your Personality",
    page_icon="🪞",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def safe_text(value):
    return html.escape(str(value))


def render_html(content):
    """Render HTML directly instead of displaying it as code."""
    st.html(content)


def render_score_card(dimension, score):

    score = max(0, min(100, float(score)))

    render_html(
        f"""
        <div class="score-card">

            <div class="score-top">

                <div class="score-name">
                    {safe_text(dimension)}
                </div>

                <div class="score-value">
                    {score:.0f}/100
                </div>

            </div>

            <div class="score-track">

                <div class="score-fill"
                     style="width:{score}%;">
                </div>

            </div>

        </div>
        """
    )


# =====================================================
# RESPONSIVE CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --purple: #a78bfa;
    --blue: #60a5fa;
    --cyan: #67e8f9;
    --white: #f8fafc;
}

html {
    scroll-behavior: smooth;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 5%, #252052 0%, transparent 38%),
        radial-gradient(ellipse at 90% 75%, #102b4c 0%, transparent 38%),
        #080b18;
    color: var(--white);
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

h1, h2, h3, h4, p, label {
    color: var(--white) !important;
}

p {
    line-height: 1.7;
}

.section-heading {
    font-size: 27px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 15px;
    letter-spacing: -0.7px;
}

/* HERO */

.hero-section {
    padding: 55px 30px;
    border-radius: 28px;
    background:
        radial-gradient(circle at 15% 20%, rgba(167,139,250,0.25), transparent 35%),
        linear-gradient(120deg, #211b4d, #102d4d);
    border: 1px solid rgba(255,255,255,0.13);
    text-align: center;
    margin-bottom: 28px;
    box-shadow: 0 15px 55px rgba(0,0,0,0.25);
}

.hero-logo {
    font-size: 55px;
}

.hero-title {
    font-size: 58px;
    font-weight: 900;
    letter-spacing: -2px;
    background: linear-gradient(90deg, #c4b5fd, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 19px;
    color: #cbd5e1;
}

.hero-description {
    color: #e2e8f0;
    margin-top: 20px;
}

/* GENERAL CARDS */

.info-card {
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 20px;
    padding: 23px;
    margin-bottom: 16px;
}

/* RESULT BANNER */

.result-banner {
    padding: 35px 20px;
    text-align: center;
    border-radius: 24px;
    background:
        radial-gradient(circle at 50% 0%, rgba(167,139,250,0.22), transparent 60%),
        rgba(255,255,255,0.045);
    border: 1px solid rgba(167,139,250,0.25);
    margin: 25px 0;
}

.result-banner-icon {
    font-size: 48px;
}

.result-banner-title {
    font-size: 32px;
    font-weight: 900;
    letter-spacing: -1px;
    background: linear-gradient(90deg, #c4b5fd, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.result-banner-subtitle {
    color: #a5b4c8;
    font-size: 14px;
}

/* ARCHETYPE */

.archetype-card {
    padding: 40px 25px;
    border-radius: 25px;
    text-align: center;
    background:
        radial-gradient(circle at 50% 0%, rgba(139,92,246,0.28), transparent 60%),
        linear-gradient(135deg, rgba(45,35,92,0.95), rgba(14,35,65,0.95));
    border: 1px solid rgba(167,139,250,0.4);
    box-shadow: 0 15px 50px rgba(124,58,237,0.12);
    margin: 20px 0;
}

.archetype-label {
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 3px;
    color: #c4b5fd;
}

.archetype {
    font-size: 39px;
    font-weight: 900;
    color: #ddd6fe;
    line-height: 1.25;
    margin: 15px 0;
}

.archetype-trait {
    color: #67e8f9;
    font-weight: 600;
    font-size: 16px;
}

.archetype-description {
    color: #dbeafe;
    max-width: 750px;
    margin: 18px auto 0;
    line-height: 1.8;
    font-size: 14px;
}

/* PERSONALITY PAIR */

.personality-pair {
    height: 100%;
    min-height: 155px;
    padding: 22px;
    border-radius: 19px;
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.11);
}

.pair-label {
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #94a3b8;
    margin-bottom: 12px;
}

.pair-name {
    font-size: 21px;
    font-weight: 800;
    color: #c4b5fd;
    margin-bottom: 10px;
}

.pair-trait {
    font-size: 13px;
    color: #cbd5e1;
    line-height: 1.6;
}

/* PATTERN */

.pattern-card {
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(
        120deg,
        rgba(14,165,233,0.12),
        rgba(124,58,237,0.15)
    );
    border: 1px solid rgba(103,232,249,0.22);
}

.pattern-label {
    color: #67e8f9;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
}

.pattern-title {
    font-size: 23px;
    font-weight: 800;
    margin: 12px 0;
    color: #e0e7ff;
}

.pattern-description {
    color: #cbd5e1;
    font-size: 14px;
    line-height: 1.7;
}

/* METRICS */

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 17px;
    padding: 18px;
}

div[data-testid="stMetricValue"] {
    font-weight: 800;
    color: #c4b5fd;
}

div[data-testid="stMetricLabel"] {
    color: #cbd5e1;
}

/* SCORE CARDS */

.score-card {
    padding: 17px 19px;
    border-radius: 16px;
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.09);
    margin-bottom: 13px;
}

.score-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    margin-bottom: 12px;
}

.score-name {
    font-size: 14px;
    font-weight: 700;
    color: #e2e8f0;
}

.score-value {
    font-size: 15px;
    font-weight: 800;
    color: #c4b5fd;
}

.score-track {
    width: 100%;
    height: 9px;
    border-radius: 20px;
    background: rgba(255,255,255,0.09);
    overflow: hidden;
}

.score-fill {
    height: 100%;
    border-radius: 20px;
    background: linear-gradient(90deg, #7c3aed, #38bdf8);
}

/* DIMENSION DETAILS */

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: rgba(255,255,255,0.12) !important;
    border-radius: 18px !important;
}

/* BUTTONS */

div.stButton > button,
div.stFormSubmitButton > button {
    width: 100%;
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    border: none;
    border-radius: 13px;
    padding: 14px;
    font-weight: 800;
    font-size: 14px;
    min-height: 49px;
    transition: 0.25s;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(124,92,237,0.35);
    color: white;
}

/* RADIO */

div[data-testid="stRadio"] label {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 13px;
    padding: 12px 14px;
    margin-bottom: 8px;
    transition: 0.2s;
}

div[data-testid="stRadio"] label:hover {
    background: rgba(124,58,237,0.15);
    border-color: rgba(167,139,250,0.5);
}

/* INPUT */

.stTextInput input {
    background: rgba(255,255,255,0.07);
    color: white;
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 12px;
    min-height: 45px;
}

/* TABS */

div[data-testid="stTabs"] {
    width: 100%;
}

button[data-baseweb="tab"] {
    font-weight: 700;
    padding: 13px 18px;
    white-space: nowrap;
}

div[data-testid="stTabs"] [role="tablist"] {
    gap: 5px;
}

/* PROGRESS */

div[data-testid="stProgressBar"] > div {
    background: rgba(255,255,255,0.10);
    border-radius: 20px;
}

hr {
    border-color: rgba(255,255,255,0.13);
}

/* FOOTER */

.footer-section {
    text-align: center;
    padding: 28px 15px;
    border-top: 1px solid rgba(255,255,255,0.08);
}

/* MOBILE */

@media screen and (max-width: 600px) {

    .block-container {
        padding-left: 13px !important;
        padding-right: 13px !important;
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }

    .hero-section {
        padding: 35px 13px !important;
        border-radius: 19px !important;
    }

    .hero-logo {
        font-size: 42px !important;
    }

    .hero-title {
        font-size: 38px !important;
        letter-spacing: -1.5px !important;
    }

    .hero-subtitle {
        font-size: 14px !important;
    }

    .hero-description {
        font-size: 12px !important;
    }

    .section-heading {
        font-size: 21px !important;
    }

    h1 {
        font-size: 25px !important;
    }

    h2 {
        font-size: 21px !important;
    }

    h3 {
        font-size: 18px !important;
    }

    .info-card {
        padding: 16px !important;
        border-radius: 15px !important;
    }

    .result-banner {
        padding: 27px 13px !important;
        border-radius: 19px !important;
    }

    .result-banner-icon {
        font-size: 40px !important;
    }

    .result-banner-title {
        font-size: 23px !important;
    }

    .result-banner-subtitle {
        font-size: 12px !important;
    }

    .archetype-card {
        padding: 28px 14px !important;
        border-radius: 19px !important;
    }

    .archetype-label {
        font-size: 10px !important;
        letter-spacing: 2px !important;
    }

    .archetype {
        font-size: 27px !important;
    }

    .archetype-trait {
        font-size: 14px !important;
    }

    .archetype-description {
        font-size: 13px !important;
    }

    .personality-pair {
        padding: 17px !important;
        min-height: auto !important;
        margin-bottom: 10px !important;
    }

    .pair-name {
        font-size: 18px !important;
    }

    .pattern-card {
        padding: 19px !important;
    }

    .pattern-title {
        font-size: 19px !important;
    }

    .pattern-description {
        font-size: 13px !important;
    }

    .score-card {
        padding: 15px !important;
    }

    .score-name {
        font-size: 12px !important;
    }

    .score-value {
        font-size: 13px !important;
    }

    div[data-testid="stMetric"] {
        padding: 12px !important;
        margin-bottom: 9px !important;
    }

    div[data-testid="stMetricValue"] {
        font-size: 21px !important;
    }

    div[data-testid="stMetricLabel"] {
        font-size: 11px !important;
    }

    div[data-testid="stTabs"] [role="tablist"] {
        overflow-x: auto !important;
        flex-wrap: nowrap !important;
        scrollbar-width: none;
    }

    div[data-testid="stTabs"] [role="tablist"]::-webkit-scrollbar {
        display: none;
    }

    button[data-baseweb="tab"] {
        padding: 10px 12px !important;
        font-size: 11px !important;
        flex-shrink: 0 !important;
    }

    div[data-testid="stPlotlyChart"] {
        width: 100% !important;
        overflow: hidden !important;
    }

    div[data-testid="stRadio"] label {
        padding: 11px 10px !important;
        font-size: 13px !important;
    }

    div.stButton > button,
    div.stFormSubmitButton > button {
        min-height: 50px !important;
        font-size: 13px !important;
    }

    p {
        font-size: 13px;
        line-height: 1.65;
    }

    .footer-section {
        padding: 20px 8px !important;
    }

}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HERO
# =====================================================

render_html("""
<div class="hero-section">

    <div class="hero-logo">🪞</div>

    <div class="hero-title">VibeMirror</div>

    <div class="hero-subtitle">
        Discover your vibe. Understand yourself.
    </div>

    <p class="hero-description">
        25 situations. 5 dimensions. 8 personality archetypes.
    </p>

</div>
""")


# =====================================================
# INTRODUCTION
# =====================================================

render_html("""
<div class="info-card">

    <h3>✨ Welcome to your self-discovery experience</h3>

    <p>
        Explore how you naturally think, react, communicate,
        make decisions and adapt to different situations.
    </p>

    <p>
        There are no right or wrong answers.
        Choose the option that genuinely reflects you.
    </p>

</div>
""")

st.info(
    "This is a fun self-discovery experience. "
    "Your responses are processed to generate your personality report. "
    "They are not saved permanently in this version."
)


# =====================================================
# PERSONAL DETAILS
# =====================================================

st.markdown(
    '<div class="section-heading">01 — Your Identity</div>',
    unsafe_allow_html=True
)

name = st.text_input(
    "What should we call you?",
    placeholder="Enter your name (optional)"
)


# =====================================================
# QUESTIONNAIRE
# =====================================================

st.markdown(
    '<div class="section-heading">02 — Explore Your Mind</div>',
    unsafe_allow_html=True
)

st.caption(
    "25 situations. Select the response that feels most like you."
)

categories = list(dict.fromkeys(
    q["category"] for q in QUESTIONS
))


with st.form("vibemirror_form"):

    answers = {}

    for category_index, category in enumerate(categories):

        st.markdown("---")

        st.markdown(
            f"### ✦ {category_index + 1:02d} — {safe_text(category)}"
        )

        category_questions = [
            q for q in QUESTIONS
            if q["category"] == category
        ]

        for q in category_questions:

            qid = q["id"]

            st.markdown(
                f"**Q{qid}. {safe_text(q['question'])}**"
            )

            selected = st.radio(
                "Choose your response:",
                options=[1, 2, 3, 4],
                format_func=lambda x, opts=q["options"]: opts[x - 1],
                key=f"mcq_{qid}",
                index=None
            )

            answers[qid] = selected

    submitted = st.form_submit_button(
        "✨ REVEAL MY PERSONALITY"
    )


# =====================================================
# VALIDATION AND ANALYSIS
# =====================================================

if submitted:

    incomplete = [
        qid for qid in range(1, 26)
        if answers.get(qid) is None
    ]

    if incomplete:

        st.error(
            "Please answer all 25 questions. "
            "Unanswered questions: "
            + ", ".join(map(str, incomplete))
        )

    else:

        results = analyse_personality(answers)

        report = generate_personality_report(
            answers,
            results
        )

        st.session_state["results"] = results
        st.session_state["report"] = report
        st.session_state["answers"] = answers
        st.session_state["name"] = name
        st.session_state["submitted"] = True


# =====================================================
# PERSONALITY REVEAL
# =====================================================

if st.session_state.get("submitted"):

    results = st.session_state["results"]
    report = st.session_state["report"]

    primary = report["primary"]
    secondary = report["secondary"]

    profile = report["primary_profile"]
    secondary_profile = report["secondary_profile"]

    sorted_dimensions = sorted(
        results.items(),
        key=lambda item: item[1],
        reverse=True
    )

    st.balloons()
    st.divider()


    # =================================================
    # RESULT HEADER
    # =================================================

    render_html("""
    <div class="result-banner">

        <div class="result-banner-icon">🪞</div>

        <div class="result-banner-title">
            YOUR PERSONALITY REVEAL
        </div>

        <p class="result-banner-subtitle">
            Your answers. Your patterns. Your personality snapshot.
        </p>

    </div>
    """)


    if st.session_state.get("name"):

        safe_name = safe_text(
            st.session_state["name"]
        )

        st.markdown(
            f"## Hey, {safe_name}! 👋"
        )


    # =================================================
    # PRIMARY ARCHETYPE
    # =================================================

    render_html(
        f"""
        <div class="archetype-card">

            <div class="archetype-label">
                YOUR PRIMARY ARCHETYPE
            </div>

            <div class="archetype">
                {safe_text(primary)}
            </div>

            <div class="archetype-trait">
                {safe_text(profile['trait'])}
            </div>

            <div class="archetype-description">
                {safe_text(profile['description'])}
            </div>

        </div>
        """
    )


    # =================================================
    # PERSONALITY COMBINATION
    # =================================================

    st.markdown("### 🧬 Your Personality Combination")

    col1, col2 = st.columns(2)

    with col1:

        render_html(
            f"""
            <div class="personality-pair">

                <div class="pair-label">
                    🥇 PRIMARY ARCHETYPE
                </div>

                <div class="pair-name">
                    {safe_text(primary)}
                </div>

                <div class="pair-trait">
                    {safe_text(profile['trait'])}
                </div>

            </div>
            """
        )

    with col2:

        render_html(
            f"""
            <div class="personality-pair">

                <div class="pair-label">
                    🥈 SECONDARY ARCHETYPE
                </div>

                <div class="pair-name">
                    {safe_text(secondary)}
                </div>

                <div class="pair-trait">
                    {safe_text(secondary_profile['trait'])}
                </div>

            </div>
            """
        )


    st.divider()


    # =================================================
    # RESULT TABS
    # =================================================

    overview_tab, breakdown_tab, behaviour_tab, growth_tab = st.tabs([
        "🌟 Overview",
        "📊 Deep Breakdown",
        "🧠 Behaviour",
        "💎 Growth"
    ])


    # =================================================
    # OVERVIEW
    # =================================================

    with overview_tab:

        st.markdown("### ✨ Your Personality at a Glance")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Personality Score",
            f"{report['average']}%"
        )

        col2.metric(
            "Strongest Dimension",
            report["strongest"][0],
            f"{report['strongest'][1]}%"
        )

        col3.metric(
            "Lowest Dimension",
            report["weakest"][0],
            f"{report['weakest'][1]}%"
        )


        # PERSONALITY PATTERN

        st.markdown("### 🧩 Your Personality Pattern")

        render_html(
            f"""
            <div class="pattern-card">

                <div class="pattern-label">
                    YOUR PERSONALITY PATTERN
                </div>

                <div class="pattern-title">
                    {safe_text(report['personality_pattern'])}
                </div>

                <div class="pattern-description">
                    {safe_text(report['pattern_description'])}
                </div>

            </div>
            """
        )


        # RADAR CHART

        st.markdown("### 🕸️ Your Personality Map")

        st.caption(
            "A visual snapshot of how your five personality dimensions compare."
        )

        dimensions = list(results.keys())
        scores = list(results.values())

        fig = go.Figure()

        fig.add_trace(
            go.Scatterpolar(
                r=scores,
                theta=dimensions,
                fill="toself",
                name="Your Personality",

                line=dict(
                    color="#a78bfa",
                    width=3
                ),

                fillcolor="rgba(139,92,246,0.25)",

                marker=dict(
                    size=9,
                    color="#67e8f9",
                    line=dict(
                        color="#ffffff",
                        width=1
                    )
                ),

                hovertemplate=(
                    "<b>%{theta}</b><br>"
                    "Score: %{r}/100"
                    "<extra></extra>"
                )
            )
        )

        fig.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",

                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickvals=[20, 40, 60, 80, 100],
                    gridcolor="rgba(255,255,255,0.12)",
                    linecolor="rgba(255,255,255,0.10)",
                    tickfont=dict(
                        size=10,
                        color="#94a3b8"
                    )
                ),

                angularaxis=dict(
                    gridcolor="rgba(255,255,255,0.10)",
                    linecolor="rgba(255,255,255,0.10)",
                    tickfont=dict(
                        size=11,
                        color="#e2e8f0"
                    )
                )
            ),

            paper_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="#f8fafc",
                family="Inter"
            ),

            showlegend=False,
            autosize=True,
            height=430,

            margin=dict(
                l=45,
                r=45,
                t=35,
                b=35
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "responsive": True,
                "displayModeBar": False
            }
        )


        # BAR CHART

        st.markdown("### 📈 Dimension Comparison")

        st.caption(
            "Compare the relative strength of each personality dimension."
        )

        chart_data = sorted_dimensions[::-1]

        bar_fig = go.Figure()

        bar_fig.add_trace(
            go.Bar(
                x=[item[1] for item in chart_data],
                y=[item[0] for item in chart_data],
                orientation="h",

                text=[
                    f"{item[1]}%"
                    for item in chart_data
                ],

                textposition="outside",

                marker=dict(
                    color=[
                        "#a78bfa",
                        "#8b9cf6",
                        "#60a5fa",
                        "#38bdf8",
                        "#67e8f9"
                    ]
                ),

                hovertemplate=(
                    "<b>%{y}</b><br>"
                    "Score: %{x}/100"
                    "<extra></extra>"
                )
            )
        )

        bar_fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="#e2e8f0",
                family="Inter"
            ),

            xaxis=dict(
                range=[0, 110],
                showgrid=True,
                gridcolor="rgba(255,255,255,0.10)",
                zeroline=False,
                title="Score out of 100"
            ),

            yaxis=dict(
                automargin=True,
                tickfont=dict(size=12)
            ),

            height=350,

            margin=dict(
                l=10,
                r=35,
                t=20,
                b=45
            ),

            showlegend=False
        )

        st.plotly_chart(
            bar_fig,
            use_container_width=True,
            config={
                "responsive": True,
                "displayModeBar": False
            }
        )


        # DIMENSION SCORE CARDS

        st.markdown("### 🎯 Your Five Dimensions")

        for dimension, score in sorted_dimensions:

            render_score_card(
                dimension,
                score
            )


    # =================================================
    # DEEP BREAKDOWN
    # =================================================

    with breakdown_tab:

        st.markdown("### 🔍 Understanding Your Personality")

        st.caption(
            "Explore what each dimension says about your behavioural tendencies."
        )

        for dimension, details in report["dimensions"].items():

            with st.container(border=True):

                st.markdown(
                    f"### {safe_text(dimension)}"
                )

                st.markdown(
                    f"**{safe_text(details['title'])}**"
                )

                score = max(
                    0,
                    min(100, int(details["score"]))
                )

                st.progress(score)

                st.write(
                    f"Score: {score}/100"
                )

                st.write(
                    details["description"]
                )

                st.success(
                    "💪 Strength: " + details["strength"]
                )

                st.info(
                    "🌱 Growth: " + details["growth"]
                )


    # =================================================
    # BEHAVIOURAL INSIGHTS
    # =================================================

    with behaviour_tab:

        st.markdown("### 🧠 Your Behavioural Blueprint")

        st.caption(
            "A look at how you may approach everyday situations."
        )

        render_html(
            f"""
            <div class="info-card">

                <h3>🤝 Social Interaction</h3>

                <p>{safe_text(report['social_style'])}</p>

            </div>
            """
        )

        render_html(
            f"""
            <div class="info-card">

                <h3>⚡ Under Pressure</h3>

                <p>{safe_text(report['pressure_style'])}</p>

            </div>
            """
        )

        render_html(
            f"""
            <div class="info-card">

                <h3>🎯 Decision Making</h3>

                <p>{safe_text(report['decision_style'])}</p>

            </div>
            """
        )

        st.markdown("### 🧩 Your Secondary Personality")

        render_html(
            f"""
            <div class="pattern-card">

                <div class="pattern-label">
                    YOUR SECONDARY ARCHETYPE
                </div>

                <div class="pattern-title">
                    {safe_text(secondary)}
                </div>

                <div class="pattern-description">
                    {safe_text(secondary_profile['description'])}
                </div>

            </div>
            """
        )


    # =================================================
    # STRENGTHS AND GROWTH
    # =================================================

    with growth_tab:

        st.markdown("### 💎 Your Natural Strengths")

        for strength in report["strengths"]:

            st.success(
                "✦ " + str(strength)
            )

        st.divider()

        st.markdown("### 🌱 Your Growth Areas")

        for growth in report["growth_areas"]:

            st.warning(
                "✦ " + str(growth)
            )

        st.divider()

        st.markdown("### 🚀 Your Personal Growth Blueprint")

        render_html(
            f"""
            <div class="pattern-card">

                <div class="pattern-label">
                    YOUR NEXT STEP
                </div>

                <div class="pattern-description">
                    {safe_text(report['advice'])}
                </div>

            </div>
            """
        )

        st.markdown("### 💭 A Final Thought")

        st.write(
            "Your personality is not a fixed identity. "
            "Your habits, experiences, environment and choices "
            "can influence how you respond to situations. "
            "Use this report as a starting point for self-discovery."
        )


    # =================================================
    # FOOTER
    # =================================================

    st.divider()

    render_html("""
    <div class="footer-section">

        <h2>🪞 VibeMirror</h2>

        <p style="color:#cbd5e1;">
            There is more to you than a score.
        </p>

        <p style="color:#94a3b8;font-size:12px;">
            A fun self-discovery experience.
            Not a scientifically validated psychological assessment.
        </p>

    </div>
    """)


    # =================================================
    # RESET
    # =================================================

    if st.button("🔄 Start a New Personality Test"):

        for key in list(st.session_state.keys()):

            del st.session_state[key]

        st.rerun()