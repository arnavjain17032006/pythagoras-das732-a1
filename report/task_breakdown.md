# Task Breakdown — EM-DAT Natural Disasters

**Dataset fields:** Year, Country, ISO, Disaster Group, Disaster Subgroup, Disaster Type, Disaster Subtype, Total Events, Total Affected, Total Deaths, Total Damage (USD, original), Total Damage (USD, adjusted), CPI.

**Guiding question:** How have natural disasters evolved in frequency, geographic distribution, and human/economic impact over the last century, and which disaster types and regions demand the most attention today?

## Visualization guidance from TAs/instructor (Sep 10 2026 announcement)
- Up to **15 visualizations per person** may be submitted, but the report should only feature a **curated subset** that serves the narrative — not every chart generated.
- Visualizations are ranked by **how informative** they are: a chart combining **3-4+ variables** (e.g. color + size + position encodings) ranks higher than a simple 2-variable bar chart. Simple charts are fine when they genuinely serve the question, but shouldn't dominate the submission.
- Use a **variety of visualization types** per person — don't repeat the same chart type across all 15.
- Every figure included in the report must have: a **figure number** (e.g. Figure 1), a **caption**, an **in-text reference**, and a written **interpretation/significance** of what it shows. Subfigures/subimages are allowed within one numbered figure.

**Practical implication for each task set below:** build more than needed in Tableau (explore freely), then pick ~4-6 best per person that (a) cover a spread of chart types and (b) lean toward multi-variable encodings, not just single-variable bar/line charts.

---

## Task Set A — Temporal Trends (Arnav Jain)
Variables: Year, Disaster Type/Subtype, Total Events

- **Overview**: total disaster events per year/decade, 1900–2023
- **Trends**: which disaster types have grown or declined in frequency over time (e.g. storms/floods vs earthquakes)
- **Comparison**: pre-1950 vs post-1950 event rates (data reporting improved after WWII — worth flagging as a caveat)
- Chart types: stacked area chart (events by type over time), line chart (yearly totals), small multiples per disaster type
- **Multi-variable options** (rank higher per TA guidance): stacked area chart encoding Year × Disaster Type × Total Events (3 vars); a bubble/heatmap grid of Decade × Disaster Type with color+size = event count (3 vars); small multiples of Year × Total Events trellised by Disaster Type with Reporting Era as a highlighted band (3-4 vars)

## Task Set B — Geographic Distribution (Kalpit Phogat)
Variables: Country, ISO, Disaster Type, Total Events

- **Overview**: choropleth map of total disaster events by country
- **Search/filter**: which countries are most exposed to which disaster type (e.g. earthquakes in Japan/Turkey, floods in India/Bangladesh)
- **Comparison**: regional/continental disaster-type profiles
- Chart types: choropleth map, filterable bar chart by country, heatmap (country x disaster type)
- **Multi-variable options**: choropleth encoding Country × Total Events with a size/color split by dominant Disaster Type (3 vars); heatmap of Country × Disaster Type with color = Total Events and a Year filter (3-4 vars); symbol map with position (lat/lon via Country) × size = events × color = disaster type (3 vars)

## Task Set C — Impact Severity (Lakshya Jain)
Variables: Total Deaths, Total Affected, Total Damage (USD, adjusted), CPI

- **Overview**: top-10 deadliest and costliest disaster types/countries
- **Trends**: economic damage over time (CPI-adjusted to normalize for inflation)
- **Correlation**: relationship between event frequency and severity (does more frequent = more deadly, or are rare events more catastrophic?)
- Chart types: ranked bar charts, scatterplot (events vs deaths), dual-axis time series (damage vs deaths)
- **Multi-variable options**: scatterplot of Total Events × Total Deaths with size = Total Damage (adjusted) and color = Disaster Type (4 vars); dual-axis time series of Year × Damage (adjusted) × Deaths trellised by Disaster Type (3-4 vars); ranked bar chart of Country × Total Deaths with color = Disaster Type and a Total Affected tooltip/size encoding (3-4 vars)

---

## Data caveats to mention in the report
- Missingness: Total Affected (2,845 missing), Total Deaths (3,056), Damage original (6,597), Damage adjusted (6,601) — pre-1980s entries especially sparse
- Disaster Subtype has 2,133 missing rows
- All 13 disaster types fall under the single "Natural" group (no man-made disasters in this dataset)
- Reporting bias: earlier 20th-century events are undercounted vs recent decades due to improved global monitoring/reporting infrastructure over time — not necessarily a real increase in disaster frequency
