import streamlit as st

st.set_page_config(page_title='Methodology', layout='wide')

st.title('Physician Scientist Dashboard- Methodologies')

st.header("Data Methodology: Normalization, Data Sources, and Technical Stack")

# ─────────────────────────────────────────────────────────────
# NORMALIZATION
# ─────────────────────────────────────────────────────────────
st.subheader("Normalization Approach")
st.write("""
Every raw variable in the framework is normalized onto a common 0-100
scale before it is combined into a dimension score. All normalization is
done using a max-based approach, either linear max normalization or
logarithmic max normalization, rather than min-max normalization.
""")

st.write("""
**Linear vs. logarithmic normalization.** The choice between the two
methods depends on the shape of the underlying distribution. For data
that is right-skewed, where most physician-scientists have a low-to-
moderate value and a small number have an extremely high value (for
example, patent counts or number of clinical trials led), a logarithmic
max normalization is used:
""")

st.latex(r"""
100 \left( \frac{\ln(x_i + 1)}{\ln(x_{\max} + 1)} \right)
""")

st.write("""
The log transform compresses the influence of extreme outliers so that a
handful of very high-output physician-scientists don't dominate the
scale and flatten everyone else into the bottom of the range. For data
that is not heavily skewed, including most leadership-position counts, a
simple linear max normalization is used instead:
""")

st.latex(r"""
100 \left( \frac{x_i}{x_{\max}} \right)
""")

st.write("""
Leadership positions in particular were kept on a linear scale rather
than a log scale because these counts are already naturally small and
bounded (most physician-scientists hold zero to a handful of executive,
government, or research leadership roles), so there isn't the same
long-tail skew that log-transforming is meant to correct for, and a
linear scale keeps the relationship between, say, one versus two
leadership roles intuitive and directly proportional.
""")

st.write("""
**Why max normalization instead of min-max normalization.** Both formulas
above scale against x_max only, rather than rescaling against the full
range between a variable's minimum and maximum (traditional min-max
normalization). This was a deliberate choice: with true min-max
normalization, the lowest observed value in the cohort gets remapped to
0 and the scale is stretched between whatever the actual minimum and
maximum happen to be. That would mean a physician-scientist with zero
real output in a given area could still be assigned a nonzero normalized
score, and the meaning of "0" would shift depending on the specific
cohort being analyzed. Max normalization preserves a fixed, interpretable
floor: a true 0 in the raw data always maps to a 0 in the normalized
score, meaning "no impact in this area," regardless of what the rest of
the cohort looks like. This also allows normalized scores to be
compared consistently across different cohort slices, since the scale
isn't re-anchored every time the underlying data changes.
""")

# ─────────────────────────────────────────────────────────────
# COMPOSITE SCORING AND WEIGHTING
# ─────────────────────────────────────────────────────────────
st.subheader("Composite Scoring and Weighting")
st.write("""
Once individual dimension scores are normalized, they are combined into a
single score for each tier, and the four tier scores are combined into an
overall composite score. The current tier- and dimension-level weights
represent Version 1.0 of the framework.
""")

st.write("Tier I (Knowledge Production):")
st.latex(r"""
T_1 = 0.4\,D_1 + 0.6\,D_2
""")

st.write("Tier II (Translational Pipeline):")
st.latex(r"""
T_2 = 0.33\,D_4 + 0.33\,D_5 + 0.34\,D_6
""")

st.write("Tier III (Patient and Population Reach):")
st.latex(r"""
T_3 = D_8
""")

st.write("Tier IV (Leadership and Systemic Influence):")
st.latex(r"""
T_4 = 0.33\,D_{10} + 0.34\,D_{11} + 0.33\,D_{12}
""")

st.write("Overall Composite Score:")
st.latex(r"""
\text{Score} = 0.2\,T_1 + 0.2\,T_2 + 0.3\,T_3 + 0.4\,T_4
""")

st.write("""
**A note on these weights.** Every weight shown above, both at the
dimension level within each tier and at the tier level in the final
composite score, was set arbitrarily and reflects the research team's
subjective judgment about relative importance, not an empirically derived
or validated allocation. In particular, the greater weight placed on
Tiers III and IV reflects the team's opinion that patient-facing and
leadership impact should outweigh knowledge production and translational
activity, but this has not been tested or justified against outside
data. Further exploration and research, including sensitivity analysis,
expert elicitation, and validation against outcomes, is required before
these weights should be treated as settled.
""")

# ─────────────────────────────────────────────────────────────
# DATA SOURCING
# ─────────────────────────────────────────────────────────────
st.subheader("Data Sourcing")
st.write("""
The large majority of the framework's underlying data, covering Tier I
(Publications, Research Grants), Tier II Dimensions 4 and 5 (Clinical
Trial Leadership and Patents and Innovation), and Tier III Dimension 8
(Clinical Guidelines / Policy Documents), was pulled from the Dimensions
AI database.
""")

st.write("""
Two parts of the framework were sourced differently. Dimension 6
(Commercialization / Industry Positions) and the entirety of Tier IV
(Executive Leadership, Government and Policy Leadership, and Research
and Education Leadership) were not well covered by Dimensions AI, since
these are largely biographical, position-based facts rather than
publication or grant records. For these areas, information was instead
gathered using Claude Sonnet 5 through prompt engineering, querying the
model to quickly look up and summarize each physician-scientist's
industry, executive, government, and leadership positions. This let the
team populate these categorical, position-based dimensions at cohort
scale without the manual lookup that would otherwise have been required.
""")

# ─────────────────────────────────────────────────────────────
# TECHNICAL STACK
# ─────────────────────────────────────────────────────────────
st.subheader("Technical Stack")
st.write("""
The data processing pipeline was built in Python, using the pandas
library for data cleaning, transformation, and normalization. The final
dashboard used to explore and present the resulting scores was built
with Streamlit.
""")
