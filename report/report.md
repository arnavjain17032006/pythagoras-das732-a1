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

This question is addressed through three complementary, non-overlapping task sets — one per team member — each covering a cohesive subset of variables, per the assignment's task-design guidance.

# 3. Tasks and Visualizations

*Per TA/instructor guidance (Sep 10, 2026): up to 15 visualizations may be built per person, but only a curated subset — favoring multi-variable, informative charts over simple 2-variable ones, across a variety of chart types — should appear below. Every figure has a number, caption, in-text reference, and interpretation.*

## 3.1 Task Set A — Temporal Trends (Arnav Jain)

**Variables used:** Year, Disaster Type / Subtype, Total Events, Reporting Era

**Tasks:**

- *Overview* — total disaster events per year/decade, 1900–2023.
- *Trends* — growth or decline in frequency by disaster type (e.g., storms/floods vs. earthquakes).
- *Comparison* — pre-1980 vs. 1980-present event rates, to account for the reporting-bias caveat.

**Planned chart types:** stacked area chart (events by type over time), line chart (yearly totals), small multiples per disaster type.

**Figure 1.** *[Chart title]* — image placeholder for `images/Fig1.png`.
*Caption:* [One or two sentences describing what the figure shows and which variables/encodings are used.]
*Interpretation:* [What this figure reveals in answer to the guiding question; reference it in prose as "As shown in Figure 1, ..."]

**Figure 2.** *[repeat pattern for each figure selected for this task set — aim for ~4-6, prioritizing multi-variable charts]*

## 3.2 Task Set B — Geographic Distribution (Kalpit Phogat)

**Variables used:** Country, ISO, Disaster Type, Total Events

**Tasks:**

- *Overview* — choropleth map of total disaster events by country.
- *Search/filter* — which countries are most exposed to which disaster type (e.g., earthquakes in Japan/Turkey, floods in India/Bangladesh).
- *Comparison* — regional/continental disaster-type profiles.

**Planned chart types:** choropleth map, filterable bar chart by country, heatmap (country × disaster type).

**Figure N.** *[Chart title]* — image placeholder for `images/FigN.png`.
*Caption:* [description + variables/encodings used.]
*Interpretation:* [finding, referenced in prose as "Figure N shows ..."]

**Figure N+1.** *[repeat for ~4-6 figures for this task set]*

## 3.3 Task Set C — Impact Severity (Lakshya Jain)

**Variables used:** Total Deaths, Total Affected, Total Damage (USD, adjusted), CPI

**Tasks:**

- *Overview* — top-10 deadliest and costliest disaster types/countries.
- *Trends* — economic damage over time (CPI-adjusted to normalize for inflation).
- *Correlation* — relationship between event frequency and severity.

**Planned chart types:** ranked bar charts, scatterplot (events vs. deaths), dual-axis time series (damage vs. deaths).

**Figure M.** *[Chart title]* — image placeholder for `images/FigM.png`.
*Caption:* [description + variables/encodings used.]
*Interpretation:* [finding, referenced in prose as "Figure M shows ..."]

**Figure M+1.** *[repeat for ~4-6 figures for this task set]*

# 4. Overall Conclusions

*[Synthesis across all three task sets — to be filled in once visualizations and inferences are complete. This section should tie Temporal, Geographic, and Impact findings back into a single data story answering the guiding question.]*

# 5. Author Contributions

| Member | Roll Number | Task Set | Contribution |
|---|---|---|---|
| Arnav Jain | BT2024233 | A — Temporal Trends | *[to be filled]* |
| Kalpit Phogat | BT2024093 | B — Geographic Distribution | *[to be filled]* |
| Lakshya Jain | BT2024044 | C — Impact Severity | *[to be filled]* |

**Data preprocessing:** *[name of member(s) who handled cleaning — also opens the first minute of the video demo]*

**Report writing/compilation:** *[to be filled]*

# 6. AI Declaration

Separate AI declaration forms for each team member are included as an appendix (see `ai_declaration_form.md` / attached forms).
