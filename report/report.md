---
title: "DAS732 — Programming Assignment 1: Visual Exploration of Natural Disasters"
subtitle: "Team Pythagoras"
date: "September 2026"
---

# 1. Dataset Description

**Dataset:** EM-DAT Natural Disasters Emergency Events Database (Country Profiles)
**Source:** [kaggle.com/datasets/mexwell/natural-disasters-emergency-events-database](https://www.kaggle.com/datasets/mexwell/natural-disasters-emergency-events-database)
**Scope:** 10,431 records, 1900–2023, 225 countries, 13 natural disaster types.

**Fields:** Year, Country, ISO, Disaster Group, Disaster Subgroup, Disaster Type, Disaster Subtype, Total Events, Total Affected, Total Deaths, Total Damage (USD, original), Total Damage (USD, CPI-adjusted), CPI.

**Preprocessing:**

- Converted delimiter from `;` to `,` for tool compatibility.
- Fixed source typos ("Disaster Subroup" → "Disaster Subgroup", trailing space on "Extreme temperature").
- Corrected CPI field (was stored with comma decimal separators).
- Left Total Affected / Total Deaths / Damage fields as null where unreported — not imputed as zero, since "zero impact" and "not reported" are materially different in this dataset.
- Added a derived `Reporting Era` field (Pre-1980 vs 1980–present) to flag that pre-1980 records are undercounted due to sparser global disaster-reporting infrastructure at the time — a caveat for interpreting long-run trends.

**Missingness:** Total Affected (2,845 missing), Total Deaths (3,056), Damage original (6,597), Damage adjusted (6,601), Disaster Subtype (2,133, labeled "Not specified").

# 2. Guiding Question

*How have natural disasters evolved in frequency, geographic distribution, and human/economic impact over the last century, and which disaster types and regions demand the most attention today?*

This question is addressed through three complementary, non-overlapping task sets — one per team member — each covering a cohesive subset of variables.

# 3. Tasks and Visualizations

*Per TA/instructor guidance (Sep 10, 2026): visualizations favor multi-variable, informative encodings over simple 2-variable charts, across a variety of chart types. Fifteen figures are presented below (5 per task set), each referenced and interpreted in the text.*

## 3.1 Task Set A — Temporal Trends (Arnav Jain)

**Variables used:** Year, Disaster Type / Subtype, Total Events, Reporting Era

**Tasks:** Overview of events over time; trends by disaster type; pre-/post-1980 comparison accounting for the reporting-bias caveat.

![Figure 1](../images/Fig1.png)

**Figure 1.** Stacked area chart encoding Year × Disaster Type × Total Events (5-year rolling average). *Interpretation:* Recorded events rise sharply from the 1970s onward, dominated by floods and storms rather than geophysical events (earthquakes, volcanic activity), whose recorded rates stay comparatively flat. This is consistent with both a genuine rise in hydro-meteorological disasters and improved reporting infrastructure post-1980 (see Figure 4).

![Figure 2](../images/Fig2.png)

**Figure 2.** Heatmap of Disaster Type × Decade, color-encoding Total Events. *Interpretation:* The 2000s and 2010s stand out as the most disaster-dense decades across nearly every type, with floods showing the steepest decade-over-decade growth of any category.

![Figure 3](../images/Fig3.png)

**Figure 3.** Small multiples trellising Year × Total Events by Disaster Type, with the pre-1980 sparse-reporting era shaded. *Interpretation:* Each disaster type shows negligible activity in the shaded region, reinforcing that early-century figures are undercounts rather than a genuinely calmer era — a caveat carried into every temporal claim in this report.

![Figure 4](../images/Fig4.png)

**Figure 4.** Annualized event rate (events/year) compared pre-1980 vs. 1980-present, by disaster type. *Interpretation:* Every disaster type shows a higher annualized rate post-1980, but the increase is most extreme for floods and storms (roughly 8-10x) versus earthquakes (roughly 3x) — suggesting the flood/storm rise is not purely a reporting artifact, since geophysical events (less prone to reporting bias, as they are harder to miss) still show real growth, just smaller.

![Figure 5](../images/Fig5.png)

**Figure 5.** Overview line chart of total disaster events per year, 1900–2023. *Interpretation:* This is the simplest overview figure in the set — included to orient the reader before the more detailed multi-variable figures above — showing the same overall rise and a visible plateau/slight decline after ~2005.

## 3.2 Task Set B — Geographic Distribution (Kalpit Phogat)

**Variables used:** Country, ISO, Disaster Type, Total Events

**Tasks:** Overview of events by country; which countries are most exposed to which disaster type; regional disaster-type profiles.

![Figure 6](../images/Fig6.png)

**Figure 6.** Heatmap of Country × Disaster Type (top-15 countries by event count), color-encoding Total Events. *Interpretation:* The USA is dominated by storms, China and India by floods, the Philippines and Japan by a storm/earthquake mix — each country's disaster profile is visibly distinct rather than uniform, motivating country-specific mitigation policy rather than one-size-fits-all.

![Figure 7](../images/Fig7.png)

**Figure 7.** Stacked horizontal bar of disaster-type composition (share of events) per country. *Interpretation:* Normalizing by country total reveals that some lower-volume countries (e.g. Vietnam, Bangladesh) are almost entirely flood/storm-exposed, i.e. narrowly but severely at risk, versus larger countries like the USA whose totals are spread across several types.

![Figure 8](../images/Fig8.png)

**Figure 8.** Bubble chart: countries ranked by Total Events (x-axis), bubble size = event volume, color = dominant disaster type. *Interpretation:* This view highlights that flood-dominant countries (China, India, Bangladesh) cluster together, forming a visibly distinct exposure group from storm-dominant countries (USA, Philippines).

![Figure 9](../images/Fig9.png)

**Figure 9.** Overview bar chart of total events by country (top-15). *Interpretation:* A simple ranked view included for orientation — the USA, China, and India lead by raw volume, but Figure 7 shows this alone is misleading without the composition context.

![Figure 10](../images/Fig10.png)

**Figure 10.** Line chart of event trends (5-yr rolling average) for the top-5 countries by Year. *Interpretation:* The USA and China show the earliest and steepest rises, while India, Philippines, and Indonesia show more recent (post-1990s) acceleration — indicating the "hotspot" countries have changed composition over time, not just grown uniformly.

## 3.3 Task Set C — Impact Severity (Lakshya Jain)

**Variables used:** Total Deaths, Total Affected, Total Damage (USD, adjusted), CPI

**Tasks:** Top-10 deadliest/costliest; economic damage over time (CPI-adjusted); correlation between event frequency and severity.

![Figure 11](../images/Fig11.png)

**Figure 11.** Scatterplot of Total Events × Total Deaths (log-log, by country-type pair), point size = Total Damage, color = Disaster Type. *Interpretation:* Earthquakes sit above the general trend line — comparatively few events but disproportionately high deaths — while floods/storms cluster with high event counts but relatively lower deaths per event, confirming that frequency and lethality are driven by different disaster types.

![Figure 12](../images/Fig12.png)

**Figure 12.** Top-10 deadliest disaster types by cumulative deaths, 1900–2023. *Interpretation:* Despite floods and storms having far more recorded events (Figure 1), earthquakes and extreme temperature events claim comparable or higher cumulative death tolls — reinforcing Figure 11's finding that frequency does not predict lethality.

![Figure 13](../images/Fig13.png)

**Figure 13.** Dual-axis time series of Year × Damage (CPI-adjusted) and Year × Deaths. *Interpretation:* Economic damage has risen sharply since the 1980s (more infrastructure and assets exposed), while deaths have not risen proportionally and show more volatile year-to-year spikes tied to individual catastrophic events rather than a steady trend — a sign that mitigation/early-warning systems have decoupled death toll from raw economic exposure.

![Figure 14](../images/Fig14.png)

**Figure 14.** Top-10 costliest countries by cumulative CPI-adjusted damage, bar color intensity = Total Deaths. *Interpretation:* Several of the costliest countries (e.g. USA, Japan) show comparatively low death tolls relative to their damage ranking, consistent with high-value infrastructure loss but strong disaster-response capacity, while lower-damage countries can still show dark (high-death) bars, pointing to weaker response capacity per dollar of exposure.

![Figure 15](../images/Fig15.png)

**Figure 15.** Correlation matrix across Events, Deaths, Affected, and Damage (aggregated by Country-Year). *Interpretation:* Deaths correlate weakly with events (r ≈ 0.00) and only weakly with affected/damage (r ≈ 0.03), while damage correlates moderately with events (r ≈ 0.41) — quantitatively confirming the qualitative finding from Figures 11-12 that death toll is governed by disaster type/severity, not sheer event count, whereas economic damage scales more directly with how many events occur.

# 4. Overall Conclusions

Across all three task sets, a consistent picture emerges: recorded disaster activity has risen sharply since the 1970s-80s (Task Set A), driven disproportionately by floods and storms concentrated in a shifting set of exposed countries (Task Set B), while the human cost (deaths) is governed less by event frequency and more by disaster type and regional response capacity, even as economic damage has scaled closely with rising event counts (Task Set C). This suggests disaster policy should be disaggregated by both **type** and **country context** rather than treated as a single trend — flood/storm-prone nations need frequency-driven mitigation, while regions exposed to high-lethality but lower-frequency events (earthquakes, extreme temperature) need severity-driven early-warning investment regardless of event count.

# 5. Author Contributions

| Member | Roll Number | Task Set | Contribution |
|---|---|---|---|
| Arnav Jain | BT2024233 | A — Temporal Trends | Dataset selection, preprocessing, Task Set A analysis and Figures 1-5, repository setup |
| Kalpit Phogat | BT2024093 | B — Geographic Distribution | Task Set B analysis and Figures 6-10 |
| Lakshya Jain | BT2024044 | C — Impact Severity | Task Set C analysis and Figures 11-15 |

**Data preprocessing:** Arnav Jain (also covers the first minute of the video demo).

**Report writing/compilation:** Arnav Jain, with contributions from all members for their respective task sets.

# 6. AI Declaration

Separate AI declaration forms for each team member are included as an appendix (see `ai_declaration_form.md` / attached forms).
