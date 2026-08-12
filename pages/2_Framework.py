import streamlit as st
import os

st.set_page_config(page_title='Framework', layout='wide')

st.title('Physician Scientist Dashboard- Framework')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

framework_img = os.path.join(BASE_DIR, "Framework.jpeg")

st.image(framework_img)

# ─────────────────────────────────────────────────────────────
# OVERVIEW
# ─────────────────────────────────────────────────────────────
st.subheader("Overview")
st.write("""
This framework was built to measure something the physician-scientist field
has never systematically quantified: what physician-scientist training
actually produces across an entire career, from the first publication to
the institutions a physician-scientist eventually leads. Rather than
relying on input metrics like raw grant counts or publication totals, the
framework tracks the full translational arc, basic discovery, clinical
translation, direct patient and population impact, and systemic
leadership, so the pipeline can be evaluated end to end rather than at a
single career snapshot.
""")

st.write("""
The twelve dimensions are organized into four tiers, and each dimension is
built from a small set of underlying variables meant to represent that
dimension as concretely and fairly as possible.
""")

st.subheader("Note on Unimplemented Dimensions")
st.write("""
Dimensions 3 (Trainee Pipeline), 7 (FDA Approvals), and 9 (Payer Coverage)
are not yet implemented in the current version of the framework. This is
due to a current lack of resources to reliably locate and attribute this
information at cohort scale, not a decision to exclude these dimensions
from the framework. They remain part of the twelve-dimension structure and
are intended to be built out as resources allow.
""")

# ─────────────────────────────────────────────────────────────
# TIER I
# ─────────────────────────────────────────────────────────────
st.subheader("Tier I: Knowledge Production")
st.write("""
Tier I is the foundation of the framework and the best-developed tier in
existing workforce literature. It establishes the physician-scientist as
an active contributor to biomedical knowledge, serving as the baseline
from which the more impact-oriented downstream tiers are distinguished.
""")

st.write("""
**Dimension 1 — Publications (m-index).** This dimension is represented by
the m-index, a career-length-adjusted version of the h-index (h-index
divided by years since first publication). It was chosen over a raw
publication count or a plain h-index because physician-scientists enter
research at very different career stages and take career interruptions
for clinical training that a raw count would unfairly penalize. The
m-index lets a physician-scientist's output be compared on a level footing
regardless of how long they've been publishing.
""")

st.write("""
**Dimension 2 — Research Grants (funding per grant).** This dimension is
represented by average funding per grant. It was chosen instead of total
dollars raised because total funding tends to simply reward physician-
scientists who have accumulated many grants over a long career, whereas
funding per grant is a better proxy for the scale and competitiveness of
any individual award a physician-scientist has been able to secure.
""")

st.write("""
**Dimension 3 — Trainee Pipeline.** This dimension is intended to track the
graduate students, fellows, and junior faculty a physician-scientist has
mentored across their career, capturing contribution to the next
generation of the workforce, not just a physician-scientist's own output.
This dimension is currently unimplemented.
""")

# ─────────────────────────────────────────────────────────────
# TIER II
# ─────────────────────────────────────────────────────────────
st.subheader("Tier II: Translational Pipeline")
st.write("""
Tier II marks the first point at which patient-facing potential becomes
directly attributable to an individual physician-scientist. It captures
the movement of discoveries out of the laboratory and toward clinical
investigation and commercialization.
""")

st.write("""
**Dimension 4 — Clinical Trial Leadership.** This dimension is represented
by the number of distinct clinical trials a physician-scientist has led,
along with the number of distinct research fields represented across
those trials. Trial count was chosen because leading a clinical trial is
the clearest available signal that a physician-scientist is directly
running human-subjects research, rather than just contributing to it.
Field breadth was added alongside it because volume alone can't
distinguish a physician-scientist who has run many trials in one narrow
area from one whose trial leadership spans multiple disease areas, and
breadth of field is itself a meaningful signal of translational range.
""")

st.write("""
**Dimension 5 — Patents and Innovation.** This dimension is represented by
four measures: the number of distinct patents a physician-scientist
holds, the number of citations those patents have received, the share of
the physician-scientist's total publications that are linked to a patent,
and the number of distinct patent fields represented. Patent count
captures raw inventive output. Patent citations were added because a
patent that is heavily cited by later patents is a stronger signal of
real influence on subsequent innovation than an uncited one. The share of
publications linked to patents captures translation efficiency, what
portion of a physician-scientist's overall publication record actually
converted into patented innovation, rather than crediting people simply
for being highly published. Patent field breadth captures diversity of
innovation, mirroring the field-breadth logic used in Dimension 4.
""")

st.write("""
**Dimension 6 — Industry Positions.** This dimension is represented by the
number of industry positions a physician-scientist has held. It was
chosen as a direct, countable marker of a physician-scientist's
involvement in translating research into industry application, alongside
patenting activity in Dimension 5.
""")

# ─────────────────────────────────────────────────────────────
# TIER III
# ─────────────────────────────────────────────────────────────
st.subheader("Tier III: Patient and Population Reach")
st.write("""
Tier III addresses the question that most directly justifies physician-
scientist training investment: did the work actually reach patients? It
is the most technically demanding tier to populate, since it requires
linking individual physician-scientists to regulatory, guideline, and
coverage records rather than just their own outputs.
""")

st.write("""
**Dimension 7 — FDA Approvals.** This dimension is intended to attribute
FDA approvals and clearances to physician-scientists through trial
records and regulatory documentation. It is treated as the most direct
patient-facing impact measure in the framework, since an FDA approval is
the clearest possible marker that a discovery reached real patients. This
dimension is currently unimplemented.
""")

st.write("""
**Dimension 8 — Clinical Guidelines / Policy Documents.** This dimension
is represented by four measures: the number of policy documents linked
to a physician-scientist's publications, the share of the physician-
scientist's total publications that are linked to a policy document, the
number of distinct policy document fields represented, and the number of
distinct publisher organizations involved. Policy document count directly
captures how often a physician-scientist's work is cited in practice
guidelines or policy documents, capturing evidence-to-guideline linkage.
The share of publications linked to policy documents, like the analogous
measure in Dimension 5, captures what portion of a physician-scientist's
total publication record has actually influenced guidelines, rather than
just rewarding overall publication volume. Field breadth captures
diversity of clinical domains influenced, and publisher breadth captures
how many distinct organizations (specialty societies, government bodies,
etc.) have adopted the physician-scientist's work, which distinguishes
broad, cross-institutional influence from citation by a single publisher.
""")

st.write("""
**Dimension 9 — Payer Coverage.** This dimension is intended to track
physician-scientist work cited in coverage determinations and payer
medical policies, connecting research output to population-level
coverage decisions. This dimension is currently unimplemented.
""")

# ─────────────────────────────────────────────────────────────
# TIER IV
# ─────────────────────────────────────────────────────────────
st.subheader("Tier IV: Leadership and Systemic Influence")
st.write("""
Tier IV treats physician-scientists as architects of institutions, not
only producers of knowledge, reflecting the outsized influence a single
leader can have on medicine, research, industry, and policy at scale.
""")

st.write("""
**Dimension 10 — Executive Leadership.** This dimension is represented by
the number of executive positions (CEO, CMO, CSO, President) a physician-
scientist has held at biopharma companies, health systems, or academic
medical centers. A direct count of these roles was chosen because
executive titles are unambiguous, externally verifiable, and each one
represents a physician-scientist directly shaping the strategy of an
entire organization.
""")

st.write("""
**Dimension 11 — Government and Policy Leadership.** This dimension is
represented by the number of government and policy positions held (e.g.
NIH Director, FDA Commissioner, Surgeon General, HHS, or international
regulatory leadership). Like Dimension 10, a direct position count was
chosen because these roles are discrete, verifiable, and each carries
national or international scope of influence over medicine and research
policy.
""")

st.write("""
**Dimension 12 — Research and Education Leadership.** This dimension is
represented by the number of research and leadership positions held (e.g.
university executive roles such as dean, provost, or president; NIH study
section service; editorial leadership of major journals). This variable
was chosen for the same reason as Dimensions 10 and 11: it is a concrete,
countable signal of a physician-scientist's role in governing the
institutions, universities, funding bodies, and journals, that structure
how research and training happen at a systemic level.
""")

# ─────────────────────────────────────────────────────────────
# HOW IT TIES TOGETHER
# ─────────────────────────────────────────────────────────────
st.subheader("How the Framework Encapsulates the Full Pipeline")
st.write("""
Together, the four tiers trace a physician-scientist's contribution along
the entire translational spectrum rather than at one point in time. Tier
I documents that a physician-scientist is producing knowledge. Tier II
shows that knowledge moving toward clinical and commercial application.
Tier III captures the moment that work reaches patients and populations
directly, through regulatory approval, clinical guidelines, or coverage
decisions. Tier IV captures a physician-scientist's ultimate influence as
a builder and leader of the institutions, companies, agencies,
universities, and journals, that shape medicine at a systemic level.
""")

st.write("""
Because this progression is layered onto each individual's longitudinal
career arc rather than measured cross-sectionally, the framework can also
capture how physician-scientists move through the pipeline: whether they
sustain a single translational focus over a career ("Marathon") or
transition across multiple stages ("Relay"), and how long it takes for
early investment in training to surface as measurable, patient-facing
impact.
""")
