import streamlit as st

st.set_page_config(page_title="Home")

st.title('Dashboard for Physician Scientist Research Group')

st.header('About the MIT Physician Scientist Research Group')
st.write(
    """
    The MIT Physician Scientist Research Group investigates how physician-scientists shape biomedical discovery, innovation,
    and the health economy. Trained in both clinical medicine and scientific research, physician-scientists play a critical role in
    translating clinical insights into research questions—and research findings into new diagnostics, therapeutics, and technologies.
    We study the evolution, segmentation, and long-term impact of the physician-scientist workforce across generations, institutions, and
    innovation domains. Our work focuses on how physician-scientists contribute to different stages of the translational pipeline;
    how their roles have changed as biomedical innovation becomes more specialized and collaborative; and how systemic pressures,
    funding structures, and institutional models influence their career trajectories. As the number of physician-scientists continues
    to decline, and as their roles become increasingly fragmented across stages of innovation, understanding these dynamics
    has never been more urgent. We provide actionable insights that inform training pathways, workforce policy, and translational
    strategy—ensuring physician-scientists are supported, retained, and empowered to drive impact across the continuum of biomedical
    research.
    """
)

st.header('About the Data Output Summer 2026 Subgroup')
st.write(
    """
    This project analyzes how physician-scientists have contributed to research translation and commercialization across generations.
    We assess trends in patenting, startup formation, clinical trial leadership, and translational grant activity to understand how
    physician-scientists operate within the full pipeline—from ideation to implementation. We investigate how generational shifts,
    institutional environments, and training pathways have led to increased segmentation, and identify the profiles of physician-scientists
    who operate across multiple stages versus those siloed within a single phase.
    """
)
st.write(
    """
    The Summer 2026 subgroup has worked hard to develop a new scoring framework inspired by previous Data Output groups. This scoring system
    now integrates 12 different dimensions across 4 tiers and has been applied to a dataset of 74 scientists. This dashboard is a portfolio
    of the progress our subgroup made this semester containing our methodologies, distributions, and personalized scores for each
    physician scientist.
    """
)

st.header('Navigation')
st.write(
    """
    To begin, please open the side bar if it's not already opened and navigate to any one of our pages.
    """
)
st.write(
    '**Methodology:** A summary of our scoring methodologies and the statistical decisions that went into normalizing and weighing metrics'
)
st.write(
    '**Framework:** A description of our 4 tiers and 12 dimensions that would hopefully capture most of the Physician Scientist Pipeline'
)
st.write(
    '**Distributions:** Histograms displaying the distribution and frequency of the physician scientists\' scores across all parameters'
)
st.write(
    '**Impact Scores:** A tool to view and visualize each physician scientist\'s impact scores across our domains'
)
