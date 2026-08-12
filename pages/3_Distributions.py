import streamlit as st
import os
import pandas as pd
import plotly.graph_objects as go

tier_categories = ['Tier 1: Knowledge Production', 'Tier 2: Translational Pipeline', 'Tier 3: Patient and Population Reach',
                   'Tier 4: Leadership and Systemic Influence', 'Final Scores']
dim_categories = ['Publications', 'Research Grants', 'Clinical Trial Leadership',
                  'Patents and Licensing', 'Commercialization', 'Clinical Guidelines',
                  'Executive Leadership', 'Government and Policy Leadership',
                  'Research and Education Leadership']


def make_figure(column_name, df):
    """Makes a plotly histogram"""
    x = df[column_name]
    fig = go.Figure(data=[go.Histogram(x=x)])
    return fig


st.set_page_config(page_title='Distributions', layout='wide')

st.title('Physician Scientist Dashboard- Distributions')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

dim_df = pd.read_csv(os.path.join(BASE_DIR, "dimension_score_breakdown.csv"))
tier_df = pd.read_csv(os.path.join(BASE_DIR, "final_score-3.csv"))
dim_columns = dim_df.drop(
    columns=['name', 'Dimension 3', 'Dimension 7', 'Dimension 9']).columns.to_list()
tier_columns = tier_df.drop(columns=['name', 'rank']).columns.to_list()


st.header('Distributions')

for i, column in enumerate(tier_columns):
    expand = st.expander(tier_categories[i], key=column)
    histogram = make_figure(column, tier_df)
    expand.subheader(f'{tier_categories[i]} Distributions')
    expand.plotly_chart(histogram)

for i, column in enumerate(dim_columns):
    expand = st.expander(f'{column}: {dim_categories[i]}', key=column)
    histogram = make_figure(column, dim_df)
    expand.subheader(f'{column}: {dim_categories[i]} Distributions')
    expand.plotly_chart(histogram)
