import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

physician_scientists = [
    "Dennis Slamon",
    "Jeffrey R Curtis",
    "Reshma Jagsi",
    "Kenneth Mandl",
    "Nancy Lane",
    "Juan Pablo Wisnivesky",
    "Joseph Goldstein",
    "Jean-Pierre Issa",
    "Jasmohan Singh Bajaj",
    "Vineet M Arora",
    "Allan Detsky",
    "Karl Y Bilimoria",
    "Ash Arash Alizadeh",
    "Ching-Hon Pui",
    "Robert Couch",
    "Naftali Kaminski",
    "Peter Macklem",
    "Andrew David Auerbach",
    "William Tap",
    "Robert Eaton",
    "Douglas Sawyer",
    "Wonder Puryear Drake",
    "Maximilian Diehn",
    "Soumya Raychaudhuri",
    "Stephen Gottschalk",
    "Beth Diane Kirkpatrick",
    "Orlando Gutierrez",
    "Margaret Koziel",
    "Peter Dobbs Crompton",
    "Brent Hollenbeck",
    "Claude Piantadosi",
    "Sarat Chandarlapaty",
    "Randall Urban",
    "Peter Cram",
    "Louise Laurent",
    "Anna Diehl",
    "Catherine A Blish",
    "Aida Habtezion",
    "Sudhir Shah",
    "Alexander Sasha Krupnick",
    "Barry Sherman",
    "Norman Edelman",
    "Oscar Ratnoff",
    "Jack Tsao",
    "Robert William Baloh",
    "Alessia Fornoni",
    "Anna Greka",
    "Warren Gold",
    "Joseph Bloomer",
    "Trever Grant Bivona",
    "Shyamasundaran Kottilil",
    "Keith Adam Choate",
    "Alexander A. Soukas",
    "Stephen Desiderio",
    "Sanford Shattil",
    "Rasheed Adebayo Gbadegesin",
    "Ganesh Raj",
    "Stephen Baum",
    "William Hwang",
    "Aaron Martin Cypess",
    "Alan Kopin",
    "Bernhard Kühn",
    "Koji Yasutomo",
    "Euan Ashley",
    "Maria Basil",
    "Susan Wall",
    "Agata Smogorzewska",
    "James Lemos",
    "Ronald Rieder",
    "Don Nelson",
    "G.R. Budinger",
    "Harvey Marver",
    "Conrad Weihl",
    "Margaret Feeney",
]

# ==========================
# Setup
# ==========================

tier_categories = ['Tier 1: Knowledge Production', 'Tier 2: Translational Pipeline', 'Tier 3: Patient and Population Reach',
                   'Tier 4: Leadership and Systemic Influence']
dim_categories = ['Publications', 'Research Grants', 'Clinical Trial Leadership',
                  'Patents and Licensing', 'Commercialization', 'Clinical Guidelines',
                  'Executive Leadership', 'Government and Policy Leadership',
                  'Research and Education Leadership']


def graph_scientist_tier(t1, t2, t3, t4, tier_weights):
    """
    Graphs the given physician scientist as a radar chart showing their overall impact score with tiers
    """
    max_range = max(tier_weights) * 100
    fig = go.Figure(data=go.Scatterpolar(
        r=[t1 * tier_weights[0], t2 * tier_weights[1],
            t3 * tier_weights[2], t4 * tier_weights[3]],
        theta=tier_categories,
        fill='toself'
    ))

    fig.update_layout(
        title={'text':
               'Tier Score with Weighting'},
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max_range]
            ),
        ),
        showlegend=False
    )
    return fig


def graph_scientist_dim(d):
    """
    Graphs the given physician scientist as a radar chart showing their overall impact score with
    a list of dimensions
    """
    fig = go.Figure(data=go.Scatterpolar(
        r=[d[0], d[1], d[2], d[3], d[4], d[5],
           d[6], d[7], d[8]],
        theta=dim_categories,
        fill='toself'
    ))

    fig.update_layout(
        title={
            'text': 'Dimension Scores without weighting'
        },
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            ),
        ),
        showlegend=False
    )
    return fig


def compare_scientist_tier(tier_dict, tier_weights):
    """Compares scientists' tier using layered radar charts and a dictionary with keys being the scientist's
    name and values being a list of their tier values"""
    fig = go.Figure()
    custom_colors = [
        '#EF553B',  # red
        '#636EFA',  # blue
        '#00CC96',  # green
        '#AB63FA',  # purple
        '#FFA15A',  # orange
        '#19D3F3',  # cyan
        '#FF6692',  # pink
        '#B6E880',  # light green
        '#FF97FF',  # light purple
        '#636EFA',  # repeat/reuse if more scientists than colors
    ]

    maximum_range = max(tier_weights) * 100

    for i, (name, tier_scores) in enumerate(tier_dict.items()):
        color = custom_colors[i % len(custom_colors)]
        fig.add_trace(go.Scatterpolar(
            r=[tier_scores[0] * tier_weights[0],
               tier_scores[1] * tier_weights[1],
               tier_scores[2] * tier_weights[2],
               tier_scores[3] * tier_weights[3]],
            theta=tier_categories,
            fill='toself',
            name=f'{name}',
            line=dict(color=color),
            fillcolor=color,
            opacity=0.5
        ))

    fig.update_layout(
        title={'text': 'Tier Comparison with Weighing'},
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, maximum_range]
            )),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.15,
            xanchor="center",
            x=0.5
        )
    )

    return fig


def compare_scientist_dim(dim_dict):
    """Compares  scientists' dimensions using layered radar charts and a dictionary with keys being the scientist's
    name and values being a list of their tier values"""
    fig = go.Figure()
    custom_colors = [
        '#EF553B',  # red
        '#636EFA',  # blue
        '#00CC96',  # green
        '#AB63FA',  # purple
        '#FFA15A',  # orange
        '#19D3F3',  # cyan
        '#FF6692',  # pink
        '#B6E880',  # light green
        '#FF97FF',  # light purple
        '#636EFA',  # repeat/reuse if more scientists than colors
    ]
    for i, (name, d) in enumerate(dim_dict.items()):
        color = custom_colors[i % len(custom_colors)]
        fig.add_trace(go.Scatterpolar(
            r=[d[0], d[1], d[2], d[3], d[4], d[5],
               d[6], d[7], d[8]],
            theta=dim_categories,
            fill='toself',
            name=f'{name}',
            line=dict(color=color),
            fillcolor=color,
            opacity=0.5
        ))

    fig.update_layout(
        title={'text': 'Dimension Comparison Without Weighing'},
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.15,
            xanchor="center",
            x=0.5
        )
    )
    return fig


def get_tier_dim_info(name, tier_df, dim_df):
    """Gets the tier and dimension scores from the dataframes."""
    if name is None:
        return None

    tier_info = tier_df.loc[
        tier_df['name'] == name
    ].drop(columns=['name', 'rank'])

    dim_info = dim_df.loc[
        dim_df['name'] == name
    ].drop(columns=['name'])

    if tier_info.empty:
        return None

    if dim_info.empty:
        return None

    t1, t2, t3, t4, final = tier_info.iloc[0].tolist()

    dimensions = dim_info[
        [
            "Dimension 1",
            "Dimension 2",
            "Dimension 4",
            "Dimension 5",
            "Dimension 6",
            "Dimension 8",
            "Dimension 10",
            "Dimension 11",
            "Dimension 12"
        ]
    ].iloc[0].tolist()

    return t1, t2, t3, t4, final, dimensions


def expander_scores(container, final, t1, t2, t3, t4, dimensions):
    container.write(f'**Final Score**: {round(final, 2)}')
    container.write(f'**Tier 1**: {round(t1, 2)}')
    container.write(f'**Tier 2**: {round(t2, 2)}')
    container.write(f'**Tier 3**: {round(t3, 2)}')
    container.write(f'**Tier 4**: {round(t4, 2)}')
    for dim_name, dimension in zip(dim_categories, dimensions):
        container.write(f'**{dim_name}**: {round(dimension, 2)}')


dim_df = pd.read_csv(
    '/Users/serenalu/physician_scientist_dash/dimension_score_breakdown.csv')
tier_df = pd.read_csv(
    '/Users/serenalu/physician_scientist_dash/final_score-3.csv')
tier_weights = []

# ==========================
# Main Page
# ==========================
st.set_page_config(layout='wide')

st.title('Dashboard for Physician Scientist Research Group')

n_scientists = st.sidebar.number_input(
    'Please input how many scientists you\'d like to observe scores:',
    min_value=0, max_value=len(physician_scientists), value=1, step=1
)

n_comparisons = st.sidebar.number_input(
    'Please input how many scientists you\'d like to compare:',
    min_value=0, max_value=len(physician_scientists), value=0, step=1
)

t1 = st.sidebar.number_input(
    'Tier 1 Weight:', min_value=0.00, max_value=1.00, value=0.20, step=0.05, key='t1'
)
t2 = st.sidebar.number_input(
    'Tier 2 Weight:', min_value=0.00, max_value=1.00, value=0.20, step=0.05, key='t2'
)
t3 = st.sidebar.number_input(
    'Tier 3 Weight:', min_value=0.00, max_value=1.00, value=0.30, step=0.05, key='t3'
)
t4 = st.sidebar.number_input(
    'Tier 4 Weight:', min_value=0.00, max_value=1.00, value=0.30, step=0.05, key='t4'
)
tier_weights.extend([t1, t2, t3, t4])

for i in range(n_scientists):
    selected_physician = st.selectbox(
        "Select a physician-scientist to **observe**",
        options=physician_scientists,
        index=None,
        placeholder="Type a name or select from the list...",
        key=f'observe_id_{i}'
    )

    if selected_physician:
        try:
            t1, t2, t3, t4, final, dimensions = get_tier_dim_info(
                selected_physician, tier_df, dim_df)

            tier_radar = graph_scientist_tier(t1, t2, t3, t4, tier_weights)
            dim_radar = graph_scientist_dim(dimensions)

            results = st.container(border=True)

            results.header(f'Impact score for {selected_physician}')
            left, right = results.columns(2)
            left.plotly_chart(tier_radar)
            right.plotly_chart(dim_radar)

            sci_stats = st.expander('Detailed Scoring')
            sci_stats.subheader('Scores Without Weighing')
            expander_scores(sci_stats, final, t1, t2, t3, t4, dimensions)

        except:
            st.subheader(':red[**Please pick a different scientist**]',)

if n_comparisons > 0:
    compare_physicians = []
    for n in range(n_comparisons):
        compare_physician = st.selectbox(
            "Select a physician-scientist to **compare**",
            options=physician_scientists,
            index=None,
            placeholder="Type a name or select from the list...",
            key=f'compare_id_{n}'
        )
        compare_physicians.append(compare_physician)

    # Stores tier scores and final score
    tier_dict = {}
    # Stores dimensions scores
    dim_dict = {}

    for scientist in compare_physicians:
        if scientist is None:
            continue
        result = get_tier_dim_info(
            scientist, tier_df, dim_df
        )
        if result is None:
            continue

        t1, t2, t3, t4, final, dimensions = result

        tier_dict[scientist] = [t1, t2, t3, t4, final]
        dim_dict[scientist] = dimensions

    if tier_dict:
        compare_tier_chart = compare_scientist_tier(tier_dict, tier_weights)
        compare_dim_chart = compare_scientist_dim(dim_dict)

        comparisons = st.container(border=True)
        comparisons.header('Impact Comparisons Results')
        left2, right2 = comparisons.columns(2)
        left2.plotly_chart(compare_tier_chart, width='stretch')
        right2.plotly_chart(compare_dim_chart, width='stretch')

        half = len(tier_dict) // 2
        compare_stats = st.expander('Scores per Scientist')
        left, right = compare_stats.columns(2)
        for name in list(tier_dict.keys())[0:half]:
            left.subheader(f'{name}\'s Scores')
            expander_scores(left, tier_dict[name][4], tier_dict[name][0], tier_dict[name][1],
                            tier_dict[name][2], tier_dict[name][3], dim_dict[name])
        for name in list(tier_dict.keys())[half:]:
            right.subheader(f'{name}\'s Scores')
            expander_scores(right, tier_dict[name][4], tier_dict[name][0], tier_dict[name][1],
                            tier_dict[name][2], tier_dict[name][3], dim_dict[name])
