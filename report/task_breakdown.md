# Task Breakdown — EM-DAT Natural Disasters

**Dataset fields:** Year, Country, ISO, Disaster Group, Disaster Subgroup, Disaster Type, Disaster Subtype, Total Events, Total Affected, Total Deaths, Total Damage (USD, original), Total Damage (USD, adjusted), CPI.

**Guiding question:** How have natural disasters evolved in frequency, geographic distribution, and human/economic impact over the last century, and which disaster types and regions demand the most attention today?

---

## Task Set A — Temporal Trends (Arnav Jain)
Variables: Year, Disaster Type/Subtype, Total Events

- **Overview**: total disaster events per year/decade, 1900–2023
- **Trends**: which disaster types have grown or declined in frequency over time (e.g. storms/floods vs earthquakes)
- **Comparison**: pre-1950 vs post-1950 event rates (data reporting improved after WWII — worth flagging as a caveat)
- Chart types: stacked area chart (events by type over time), line chart (yearly totals), small multiples per disaster type

## Task Set B — Geographic Distribution (KAlpit)
Variables: Country, ISO, Disaster Type, Total Events

- **Overview**: choropleth map of total disaster events by country
- **Search/filter**: which countries are most exposed to which disaster type (e.g. earthquakes in Japan/Turkey, floods in India/Bangladesh)
- **Comparison**: regional/continental disaster-type profiles
- Chart types: choropleth map, filterable bar chart by country, heatmap (country x disaster type)

## Task Set C — Impact Severity (3rd member, TBD)
Variables: Total Deaths, Total Affected, Total Damage (USD, adjusted), CPI

- **Overview**: top-10 deadliest and costliest disaster types/countries
- **Trends**: economic damage over time (CPI-adjusted to normalize for inflation)
- **Correlation**: relationship between event frequency and severity (does more frequent = more deadly, or are rare events more catastrophic?)
- Chart types: ranked bar charts, scatterplot (events vs deaths), dual-axis time series (damage vs deaths)

---

## Data caveats to mention in the report
- Missingness: Total Affected (2,845 missing), Total Deaths (3,056), Damage original (6,597), Damage adjusted (6,601) — pre-1980s entries especially sparse
- Disaster Subtype has 2,133 missing rows
- All 13 disaster types fall under the single "Natural" group (no man-made disasters in this dataset)
- Reporting bias: earlier 20th-century events are undercounted vs recent decades due to improved global monitoring/reporting infrastructure over time — not necessarily a real increase in disaster frequency
