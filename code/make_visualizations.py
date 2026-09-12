"""Generate 45 figures (15 per task set) for EM-DAT Natural Disasters, Team Pythagoras.

Task Set A (Arnav Jain)    - Temporal trends        -> Fig1-Fig15
Task Set B (Kalpit Phogat) - Geographic distribution -> Fig16-Fig30
Task Set C (Lakshya Jain)  - Impact severity         -> Fig31-Fig45
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

plt.rcParams["figure.dpi"] = 150
plt.rcParams["font.size"] = 10

df = pd.read_csv("data/emdat_cleaned.csv")
OUT = "images"

TOP_TYPES = df["Disaster Type"].value_counts().head(6).index.tolist()
ALL_TYPES = df["Disaster Type"].value_counts().index.tolist()
df["Decade"] = (df["Year"] // 10) * 10

def cmap(name, n):
    return plt.get_cmap(name, n)

# ============================================================
# TASK SET A - TEMPORAL TRENDS (Fig1-Fig15)
# ============================================================

# Fig1: stacked area, Year x Disaster Type x Total Events (3 vars)
pivot = df[df["Disaster Type"].isin(TOP_TYPES)].pivot_table(
    index="Year", columns="Disaster Type", values="Total Events", aggfunc="sum"
).fillna(0)
pivot_smooth = pivot.rolling(5, min_periods=1).mean()
fig, ax = plt.subplots(figsize=(9, 5))
ax.stackplot(pivot_smooth.index, pivot_smooth.T.values, labels=pivot_smooth.columns, alpha=0.85)
ax.set_title("Figure 1. Disaster Events by Type Over Time (5-yr rolling avg)")
ax.set_xlabel("Year"); ax.set_ylabel("Total Events")
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig1.png"); plt.close(fig)

# Fig2: heatmap, Decade x Disaster Type, color = Total Events (3 vars)
heat = df[df["Disaster Type"].isin(TOP_TYPES)].pivot_table(
    index="Disaster Type", columns="Decade", values="Total Events", aggfunc="sum"
).fillna(0)
fig, ax = plt.subplots(figsize=(10, 4))
im = ax.imshow(heat.values, aspect="auto", cmap="YlOrRd")
ax.set_xticks(range(len(heat.columns))); ax.set_xticklabels(heat.columns, rotation=45)
ax.set_yticks(range(len(heat.index))); ax.set_yticklabels(heat.index)
ax.set_title("Figure 2. Event Intensity Heatmap: Disaster Type x Decade")
fig.colorbar(im, ax=ax, label="Total Events")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig2.png"); plt.close(fig)

# Fig3: small multiples, Year x Total Events trellised by Disaster Type
fig, axes = plt.subplots(2, 3, figsize=(12, 6), sharex=True)
for ax, dtype in zip(axes.flat, TOP_TYPES):
    sub = df[df["Disaster Type"] == dtype].groupby("Year")["Total Events"].sum()
    ax.plot(sub.index, sub.values, color="steelblue")
    ax.axvspan(1900, 1980, color="grey", alpha=0.15)
    ax.set_title(dtype, fontsize=9)
fig.suptitle("Figure 3. Per-Type Trends (grey = pre-1980 sparse-reporting era)")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig3.png"); plt.close(fig)

# Fig4: pre/post-1980 annualized rate comparison bar
era_pivot = df[df["Disaster Type"].isin(TOP_TYPES)].pivot_table(
    index="Disaster Type", columns="Reporting Era", values="Total Events", aggfunc="sum"
).fillna(0)
era_pivot["annualized_pre"] = era_pivot.get("Pre-1980 (sparse reporting)", 0) / 80
era_pivot["annualized_post"] = era_pivot.get("1980-present", 0) / 44
fig, ax = plt.subplots(figsize=(8, 5))
x = np.arange(len(era_pivot))
ax.bar(x - 0.2, era_pivot["annualized_pre"], width=0.4, label="Pre-1980 (per yr)")
ax.bar(x + 0.2, era_pivot["annualized_post"], width=0.4, label="1980-present (per yr)")
ax.set_xticks(x); ax.set_xticklabels(era_pivot.index, rotation=30, ha="right")
ax.set_ylabel("Avg Events / Year")
ax.set_title("Figure 4. Annualized Event Rate: Pre- vs Post-1980 by Type")
ax.legend()
fig.tight_layout(); fig.savefig(f"{OUT}/Fig4.png"); plt.close(fig)

# Fig5: overview line, total events per year
yearly = df.groupby("Year")["Total Events"].sum()
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(yearly.index, yearly.values, color="darkred")
ax.axvspan(1900, 1980, color="grey", alpha=0.15, label="Sparse reporting era")
ax.set_title("Figure 5. Total Disaster Events per Year, 1900-2023 (Overview)")
ax.set_xlabel("Year"); ax.set_ylabel("Total Events"); ax.legend()
fig.tight_layout(); fig.savefig(f"{OUT}/Fig5.png"); plt.close(fig)

# Fig6: 100% stacked area - Year x Disaster Type x Share of events (3 vars)
share = pivot_smooth.div(pivot_smooth.sum(axis=1), axis=0).fillna(0)
fig, ax = plt.subplots(figsize=(9, 5))
ax.stackplot(share.index, share.T.values, labels=share.columns, alpha=0.85)
ax.set_title("Figure 6. Share of Events by Type Over Time (100% Stacked)")
ax.set_xlabel("Year"); ax.set_ylabel("Share of Total Events")
ax.legend(loc="upper left", fontsize=8, ncol=2)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig6.png"); plt.close(fig)

# Fig7: cumulative events over time by type, multi-line (3 vars)
cumulative = pivot.cumsum()
fig, ax = plt.subplots(figsize=(9, 5))
for col in cumulative.columns:
    ax.plot(cumulative.index, cumulative[col], label=col)
ax.set_title("Figure 7. Cumulative Events by Type, 1900-2023")
ax.set_xlabel("Year"); ax.set_ylabel("Cumulative Events"); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig7.png"); plt.close(fig)

# Fig8: Flood subtype breakdown, stacked area (Year x Flood Subtype x Events) (3 vars)
flood = df[df["Disaster Type"] == "Flood"]
flood_pivot = flood.pivot_table(index="Year", columns="Disaster Subtype", values="Total Events", aggfunc="sum").fillna(0)
flood_pivot = flood_pivot.rolling(5, min_periods=1).mean()
fig, ax = plt.subplots(figsize=(9, 5))
ax.stackplot(flood_pivot.index, flood_pivot.T.values, labels=flood_pivot.columns, alpha=0.85)
ax.set_title("Figure 8. Flood Events by Subtype Over Time (5-yr rolling avg)")
ax.set_xlabel("Year"); ax.set_ylabel("Total Events"); ax.legend(loc="upper left", fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig8.png"); plt.close(fig)

# Fig9: year-over-year growth rate line, with era shading (2 vars)
yoy = yearly.pct_change().rolling(3, min_periods=1).mean() * 100
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(yoy.index, yoy.values, color="purple")
ax.axhline(0, color="black", linewidth=0.8)
ax.axvspan(1900, 1980, color="grey", alpha=0.15)
ax.set_title("Figure 9. Year-over-Year Growth Rate in Total Events (3-yr smoothed)")
ax.set_xlabel("Year"); ax.set_ylabel("YoY Growth (%)")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig9.png"); plt.close(fig)

# Fig10: boxplot distribution of Total Events per record by Disaster Type (2 vars)
fig, ax = plt.subplots(figsize=(9, 5))
data = [df[df["Disaster Type"] == t]["Total Events"] for t in TOP_TYPES]
ax.boxplot(data, labels=TOP_TYPES, showfliers=False)
ax.set_title("Figure 10. Distribution of Per-Record Event Counts by Type")
ax.set_ylabel("Total Events (per record)")
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig10.png"); plt.close(fig)

# Fig11: bubble scatter, Year x Total Events, sized/colored by Disaster Type (3 vars)
sample = df[df["Disaster Type"].isin(TOP_TYPES)].groupby(["Year", "Disaster Type"])["Total Events"].sum().reset_index()
fig, ax = plt.subplots(figsize=(9, 5))
colors = cmap("tab10", len(TOP_TYPES))
for i, t in enumerate(TOP_TYPES):
    sub = sample[sample["Disaster Type"] == t]
    ax.scatter(sub["Year"], sub["Total Events"], s=sub["Total Events"] * 2, alpha=0.5, color=colors(i), label=t)
ax.set_title("Figure 11. Year x Events Bubble Chart (size/color = Disaster Type)")
ax.set_xlabel("Year"); ax.set_ylabel("Total Events"); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig11.png"); plt.close(fig)

# Fig12: decade-dominant-type stacked bar (Decade x dominant share) (3 vars)
decade_pivot = df[df["Disaster Type"].isin(TOP_TYPES)].pivot_table(
    index="Decade", columns="Disaster Type", values="Total Events", aggfunc="sum"
).fillna(0)
decade_share = decade_pivot.div(decade_pivot.sum(axis=1), axis=0)
fig, ax = plt.subplots(figsize=(9, 5))
bottom = np.zeros(len(decade_share))
colors = cmap("tab10", len(decade_share.columns))
for i, col in enumerate(decade_share.columns):
    ax.bar(decade_share.index.astype(str), decade_share[col], bottom=bottom, label=col, color=colors(i), width=8)
    bottom += decade_share[col].values
ax.set_title("Figure 12. Dominant Disaster-Type Composition by Decade")
ax.set_ylabel("Share of Events"); ax.legend(fontsize=8, ncol=2)
plt.setp(ax.get_xticklabels(), rotation=45)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig12.png"); plt.close(fig)

# Fig13: histogram of Total Events per record (distribution overview)
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["Total Events"], bins=30, color="slateblue", edgecolor="white")
ax.set_yscale("log")
ax.set_title("Figure 13. Distribution of Total Events per Record (log y-axis)")
ax.set_xlabel("Total Events (per record)"); ax.set_ylabel("Frequency (log)")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig13.png"); plt.close(fig)

# Fig14: rolling volatility (std dev) of yearly events (2 vars)
rolling_std = yearly.rolling(10, min_periods=3).std()
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(rolling_std.index, rolling_std.values, color="darkgreen")
ax.set_title("Figure 14. 10-Year Rolling Volatility of Annual Event Counts")
ax.set_xlabel("Year"); ax.set_ylabel("Rolling Std. Dev. of Events")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig14.png"); plt.close(fig)

# Fig15: scatter Year vs Total Events with linear trend line + R^2 (2 vars + stat)
yearly_df = yearly.reset_index()
yearly_df.columns = ["Year", "Total Events"]
coeffs = np.polyfit(yearly_df["Year"], yearly_df["Total Events"], 1)
trend = np.poly1d(coeffs)
residuals = yearly_df["Total Events"] - trend(yearly_df["Year"])
ss_res = np.sum(residuals**2); ss_tot = np.sum((yearly_df["Total Events"] - yearly_df["Total Events"].mean())**2)
r2 = 1 - ss_res / ss_tot
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(yearly_df["Year"], yearly_df["Total Events"], alpha=0.6, color="teal")
ax.plot(yearly_df["Year"], trend(yearly_df["Year"]), color="red", label=f"Linear trend (R2={r2:.2f})")
ax.set_title("Figure 15. Year vs Total Events with Linear Trend")
ax.set_xlabel("Year"); ax.set_ylabel("Total Events"); ax.legend()
fig.tight_layout(); fig.savefig(f"{OUT}/Fig15.png"); plt.close(fig)

print("Task Set A (Fig1-15) done.")

# ============================================================
# TASK SET B - GEOGRAPHIC DISTRIBUTION (Fig16-Fig30)
# ============================================================

top_countries = df.groupby("Country")["Total Events"].sum().sort_values(ascending=False).head(15)
top20 = df.groupby("Country")["Total Events"].sum().sort_values(ascending=False).head(20)

# Fig16: heatmap Country x Disaster Type (3 vars)
geo_heat = df[df["Country"].isin(top_countries.index) & df["Disaster Type"].isin(TOP_TYPES)].pivot_table(
    index="Country", columns="Disaster Type", values="Total Events", aggfunc="sum"
).fillna(0).loc[top_countries.index]
fig, ax = plt.subplots(figsize=(9, 7))
im = ax.imshow(geo_heat.values, aspect="auto", cmap="YlGnBu")
ax.set_xticks(range(len(geo_heat.columns))); ax.set_xticklabels(geo_heat.columns, rotation=45, ha="right")
ax.set_yticks(range(len(geo_heat.index))); ax.set_yticklabels(geo_heat.index)
ax.set_title("Figure 16. Country x Disaster Type Exposure Heatmap (Top 15)")
fig.colorbar(im, ax=ax, label="Total Events")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig16.png"); plt.close(fig)

# Fig17: stacked bar composition per country (3 vars)
comp = geo_heat.div(geo_heat.sum(axis=1), axis=0)
fig, ax = plt.subplots(figsize=(10, 6))
bottom = np.zeros(len(comp))
colors = cmap("tab10", len(comp.columns))
for i, col in enumerate(comp.columns):
    ax.barh(comp.index, comp[col], left=bottom, label=col, color=colors(i))
    bottom += comp[col].values
ax.set_title("Figure 17. Disaster-Type Composition by Country (Top 15, share)")
ax.set_xlabel("Share of Total Events")
ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig17.png"); plt.close(fig)

# Fig18: bubble Country rank x Total Events x dominant type (3 vars)
dominant_type = geo_heat.idxmax(axis=1)
fig, ax = plt.subplots(figsize=(10, 5))
type_list = sorted(dominant_type.unique())
color_map = {t: cmap("tab10", 10)(i) for i, t in enumerate(type_list)}
seen = set()
for i, country in enumerate(top_countries.index):
    lbl = dominant_type[country] if dominant_type[country] not in seen else ""
    seen.add(dominant_type[country])
    ax.scatter(i, top_countries[country], s=top_countries[country] / 2, color=color_map[dominant_type[country]], alpha=0.75, label=lbl)
ax.set_xticks(range(len(top_countries))); ax.set_xticklabels(top_countries.index, rotation=45, ha="right")
ax.set_ylabel("Total Events")
ax.set_title("Figure 18. Top-15 Countries, Sized by Events, Colored by Dominant Type")
handles = [plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=color_map[t], markersize=8, label=t) for t in type_list]
ax.legend(handles=handles, bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig18.png"); plt.close(fig)

# Fig19: overview bar top15 (1 var)
fig, ax = plt.subplots(figsize=(9, 6))
ax.barh(top_countries.index[::-1], top_countries.values[::-1], color="teal")
ax.set_title("Figure 19. Total Disaster Events by Country (Top 15, Overview)")
ax.set_xlabel("Total Events")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig19.png"); plt.close(fig)

# Fig20: line trends top5 countries (3 vars)
top5 = top_countries.head(5).index
fig, ax = plt.subplots(figsize=(9, 5))
for country in top5:
    sub = df[df["Country"] == country].groupby("Year")["Total Events"].sum().rolling(5, min_periods=1).mean()
    ax.plot(sub.index, sub.values, label=country)
ax.set_title("Figure 20. Event Trends for Top-5 Countries (5-yr rolling avg)")
ax.set_xlabel("Year"); ax.set_ylabel("Total Events"); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig20.png"); plt.close(fig)

# Fig21: slopegraph, country rank pre-1980 vs post-1980 (3 vars: country, era, rank)
pre_rank = df[df["Reporting Era"] == "Pre-1980 (sparse reporting)"].groupby("Country")["Total Events"].sum().rank(ascending=False)
post_rank = df[df["Reporting Era"] == "1980-present"].groupby("Country")["Total Events"].sum().rank(ascending=False)
common = top_countries.index
fig, ax = plt.subplots(figsize=(7, 8))
for country in common:
    pr = pre_rank.get(country, np.nan); po = post_rank.get(country, np.nan)
    if pd.notna(pr) and pd.notna(po):
        ax.plot([0, 1], [pr, po], marker="o", color="steelblue")
        ax.text(-0.05, pr, country, ha="right", fontsize=8)
        ax.text(1.05, po, country, ha="left", fontsize=8)
ax.invert_yaxis()
ax.set_xticks([0, 1]); ax.set_xticklabels(["Pre-1980 Rank", "Post-1980 Rank"])
ax.set_xlim(-0.6, 1.6)
ax.set_title("Figure 21. Country Rank Shift: Pre-1980 vs Post-1980 (Top 15 today)")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig21.png"); plt.close(fig)

# Fig22: grouped bar top10 countries x Reporting Era x Events (3 vars)
top10 = top_countries.head(10).index
era_country = df[df["Country"].isin(top10)].pivot_table(index="Country", columns="Reporting Era", values="Total Events", aggfunc="sum").fillna(0).loc[top10]
fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(era_country))
ax.bar(x - 0.2, era_country.get("Pre-1980 (sparse reporting)", 0), width=0.4, label="Pre-1980")
ax.bar(x + 0.2, era_country.get("1980-present", 0), width=0.4, label="1980-present")
ax.set_xticks(x); ax.set_xticklabels(era_country.index, rotation=45, ha="right")
ax.set_ylabel("Total Events")
ax.set_title("Figure 22. Top-10 Countries: Event Counts by Reporting Era")
ax.legend()
fig.tight_layout(); fig.savefig(f"{OUT}/Fig22.png"); plt.close(fig)

# Fig23: bubble diversity - country total events x number of distinct types (3 vars)
diversity = df.groupby("Country")["Disaster Type"].nunique()
country_events = df.groupby("Country")["Total Events"].sum()
plot_df = pd.DataFrame({"events": country_events, "diversity": diversity}).loc[top20.index]
top20_heat = df[df["Country"].isin(top20.index) & df["Disaster Type"].isin(TOP_TYPES)].pivot_table(
    index="Country", columns="Disaster Type", values="Total Events", aggfunc="sum"
).reindex(top20.index).fillna(0)
plot_df["dominant"] = top20_heat.idxmax(axis=1)
fig, ax = plt.subplots(figsize=(9, 6))
for i, t in enumerate(type_list):
    sub = plot_df[plot_df["dominant"] == t]
    if len(sub):
        ax.scatter(sub["events"], sub["diversity"], s=sub["events"] / 3, color=color_map.get(t, "grey"), alpha=0.7, label=t)
for country, row in plot_df.iterrows():
    ax.annotate(country, (row["events"], row["diversity"]), fontsize=6, alpha=0.7)
ax.set_xlabel("Total Events"); ax.set_ylabel("Number of Distinct Disaster Types")
ax.set_title("Figure 23. Event Volume vs Disaster-Type Diversity (Top 20 Countries)")
ax.legend(fontsize=7)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig23.png"); plt.close(fig)

# Fig24: scatter persistence - total events x years active, colored dominant type (3 vars)
years_active = df.groupby("Country")["Year"].nunique()
plot_df2 = pd.DataFrame({"events": country_events, "years_active": years_active}).loc[top20.index]
plot_df2["dominant"] = top20_heat.idxmax(axis=1)
fig, ax = plt.subplots(figsize=(9, 6))
for i, t in enumerate(type_list):
    sub = plot_df2[plot_df2["dominant"] == t]
    if len(sub):
        ax.scatter(sub["years_active"], sub["events"], s=60, color=color_map.get(t, "grey"), alpha=0.7, label=t)
for country, row in plot_df2.iterrows():
    ax.annotate(country, (row["years_active"], row["events"]), fontsize=6, alpha=0.7)
ax.set_xlabel("Number of Distinct Years with a Recorded Event"); ax.set_ylabel("Total Events")
ax.set_title("Figure 24. Persistence of Risk: Years Active vs Total Events (Top 20)")
ax.legend(fontsize=7)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig24.png"); plt.close(fig)

# Fig25: histogram of total events across all 225 countries, log x (overview)
fig, ax = plt.subplots(figsize=(8, 5))
all_country_events = df.groupby("Country")["Total Events"].sum()
ax.hist(all_country_events, bins=30, color="darkcyan", edgecolor="white")
ax.set_xscale("log")
ax.set_title("Figure 25. Distribution of Total Events Across All 225 Countries")
ax.set_xlabel("Total Events (log scale)"); ax.set_ylabel("Number of Countries")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig25.png"); plt.close(fig)

# Fig26: diverging bar, growth ratio (post/pre) top and bottom 10 countries with both eras present (2 vars)
pre_events = df[df["Reporting Era"] == "Pre-1980 (sparse reporting)"].groupby("Country")["Total Events"].sum()
post_events = df[df["Reporting Era"] == "1980-present"].groupby("Country")["Total Events"].sum()
both = pd.DataFrame({"pre": pre_events, "post": post_events}).dropna()
both = both[both["pre"] >= 3]
both["ratio"] = both["post"] / both["pre"]
top_growth = both["ratio"].sort_values(ascending=False).head(10)
bottom_growth = both["ratio"].sort_values(ascending=True).head(10)
combined = pd.concat([bottom_growth, top_growth]).sort_values()
fig, ax = plt.subplots(figsize=(8, 7))
colors_div = ["indianred" if v < combined.median() else "seagreen" for v in combined.values]
ax.barh(combined.index, combined.values, color=colors_div)
ax.set_title("Figure 26. Countries with Lowest vs Highest Post/Pre-1980 Growth Ratio")
ax.set_xlabel("Post-1980 / Pre-1980 Event Ratio")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig26.png"); plt.close(fig)

# Fig27: top10 vs rest-of-world share of global events by disaster type (3 vars)
df["is_top10"] = df["Country"].isin(top10)
group_share = df[df["Disaster Type"].isin(TOP_TYPES)].pivot_table(index="Disaster Type", columns="is_top10", values="Total Events", aggfunc="sum").fillna(0)
group_share.columns = ["Rest of World", "Top-10 Countries"]
group_share_pct = group_share.div(group_share.sum(axis=1), axis=0)
fig, ax = plt.subplots(figsize=(8, 5))
group_share_pct.plot(kind="barh", stacked=True, ax=ax, color=["lightgrey", "darkorange"])
ax.set_title("Figure 27. Top-10 Countries' Share of Global Events, by Type")
ax.set_xlabel("Share of Total Events")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig27.png"); plt.close(fig)

# Fig28: heatmap top15 countries x Decade x Events (3 vars)
country_decade = df[df["Country"].isin(top_countries.index)].pivot_table(index="Country", columns="Decade", values="Total Events", aggfunc="sum").fillna(0).loc[top_countries.index]
fig, ax = plt.subplots(figsize=(10, 7))
im = ax.imshow(country_decade.values, aspect="auto", cmap="PuBuGn")
ax.set_xticks(range(len(country_decade.columns))); ax.set_xticklabels(country_decade.columns, rotation=45)
ax.set_yticks(range(len(country_decade.index))); ax.set_yticklabels(country_decade.index)
ax.set_title("Figure 28. Top-15 Countries x Decade Event Heatmap")
fig.colorbar(im, ax=ax, label="Total Events")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig28.png"); plt.close(fig)

# Fig29: bar - number of distinct subtypes experienced per top10 country (diversity depth) (2 vars)
subtype_diversity = df[df["Country"].isin(top10)].groupby("Country")["Disaster Subtype"].nunique().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(subtype_diversity.index, subtype_diversity.values, color="mediumpurple")
ax.set_title("Figure 29. Number of Distinct Disaster Subtypes Experienced (Top-10 Countries)")
ax.set_ylabel("Distinct Subtypes")
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig29.png"); plt.close(fig)

# Fig30: bar - geographic breadth (num countries affected) vs total events, per disaster type (2 vars)
breadth = df.groupby("Disaster Type").agg(countries=("Country", "nunique"), events=("Total Events", "sum")).sort_values("events", ascending=False).head(10)
fig, ax1 = plt.subplots(figsize=(9, 5))
x = np.arange(len(breadth))
ax1.bar(x - 0.2, breadth["events"], width=0.4, color="steelblue", label="Total Events")
ax1.set_ylabel("Total Events", color="steelblue")
ax2 = ax1.twinx()
ax2.bar(x + 0.2, breadth["countries"], width=0.4, color="salmon", label="Countries Affected")
ax2.set_ylabel("Countries Affected", color="salmon")
ax1.set_xticks(x); ax1.set_xticklabels(breadth.index, rotation=45, ha="right")
ax1.set_title("Figure 30. Geographic Breadth vs Event Volume, by Disaster Type")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig30.png"); plt.close(fig)

print("Task Set B (Fig16-30) done.")

# ============================================================
# TASK SET C - IMPACT SEVERITY (Fig31-Fig45)
# ============================================================

agg = df[df["Disaster Type"].isin(TOP_TYPES)].groupby(["Country", "Disaster Type"]).agg(
    events=("Total Events", "sum"), deaths=("Total Deaths", "sum"),
    damage=("Total Damage (USD, adjusted)", "sum"), affected=("Total Affected", "sum")
).reset_index()

# Fig31: scatter events x deaths, size=damage, color=type (4 vars)
sub_agg = agg[(agg["deaths"] > 0) & (agg["events"] > 0)]
fig, ax = plt.subplots(figsize=(9, 6))
for i, dtype in enumerate(TOP_TYPES):
    sub = sub_agg[sub_agg["Disaster Type"] == dtype]
    sizes = 20 + 200 * (sub["damage"].fillna(0) / (agg["damage"].max() or 1))
    ax.scatter(sub["events"], sub["deaths"], s=sizes, alpha=0.6, color=cmap("tab10", 10)(i), label=dtype)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("Total Events (log)"); ax.set_ylabel("Total Deaths (log)")
ax.set_title("Figure 31. Events vs Deaths by Country, Sized by Damage, Colored by Type")
ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig31.png"); plt.close(fig)

# Fig32: top-10 deadliest disaster types (2 vars)
deadliest = df.groupby("Disaster Type")["Total Deaths"].sum().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(deadliest.index[::-1], deadliest.values[::-1], color="firebrick")
ax.set_title("Figure 32. Top-10 Deadliest Disaster Types (Cumulative, 1900-2023)")
ax.set_xlabel("Total Deaths")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig32.png"); plt.close(fig)

# Fig33: dual-axis time series, Year x Damage x Deaths (3 vars)
yearly_impact = df.groupby("Year").agg(damage=("Total Damage (USD, adjusted)", "sum"), deaths=("Total Deaths", "sum"))
fig, ax1 = plt.subplots(figsize=(9, 5))
ax1.plot(yearly_impact.index, yearly_impact["damage"] / 1e9, color="darkorange")
ax1.set_ylabel("Damage (Billion USD, adjusted)", color="darkorange")
ax2 = ax1.twinx()
ax2.plot(yearly_impact.index, yearly_impact["deaths"], color="navy", alpha=0.6)
ax2.set_ylabel("Deaths", color="navy")
ax1.set_title("Figure 33. Economic Damage vs Deaths Over Time")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig33.png"); plt.close(fig)

# Fig34: top-10 costliest countries, color=deaths (3 vars)
cost = df.groupby("Country").agg(damage=("Total Damage (USD, adjusted)", "sum"), deaths=("Total Deaths", "sum")).sort_values("damage", ascending=False).head(10)
norm_deaths = (cost["deaths"] - cost["deaths"].min()) / (cost["deaths"].max() - cost["deaths"].min() + 1)
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(cost.index[::-1], cost["damage"].values[::-1] / 1e9, color=cmap("Reds", 256)(norm_deaths.values[::-1]))
ax.set_title("Figure 34. Top-10 Costliest Countries (color intensity = Total Deaths)")
ax.set_xlabel("Total Damage (Billion USD, adjusted)")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig34.png"); plt.close(fig)

# Fig35: correlation matrix, events/deaths/affected/damage (4 vars)
corr_df = df.groupby(["Country", "Year"]).agg(
    events=("Total Events", "sum"), deaths=("Total Deaths", "sum"),
    affected=("Total Affected", "sum"), damage=("Total Damage (USD, adjusted)", "sum")
).dropna()
corr = corr_df.corr()
fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(corr.values, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_xticks(range(len(corr))); ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticks(range(len(corr))); ax.set_yticklabels(corr.columns)
for i in range(len(corr)):
    for j in range(len(corr)):
        ax.text(j, i, f"{corr.values[i,j]:.2f}", ha="center", va="center", fontsize=8)
ax.set_title("Figure 35. Correlation: Events, Deaths, Affected, Damage")
fig.colorbar(im, ax=ax)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig35.png"); plt.close(fig)

# Fig36: deaths-per-event by type, sorted bar (derived stat, 2 vars)
type_summary = df.groupby("Disaster Type").agg(events=("Total Events", "sum"), deaths=("Total Deaths", "sum"))
type_summary["deaths_per_event"] = type_summary["deaths"] / type_summary["events"]
top_dpe = type_summary["deaths_per_event"].sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(top_dpe.index[::-1], top_dpe.values[::-1], color="crimson")
ax.set_xscale("log")
ax.set_title("Figure 36. Deaths per Event by Disaster Type (log scale)")
ax.set_xlabel("Deaths per Event")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig36.png"); plt.close(fig)

# Fig37: damage-per-event by type, sorted bar (2 vars)
type_summary["damage"] = df.groupby("Disaster Type")["Total Damage (USD, adjusted)"].sum()
type_summary["damage_per_event"] = type_summary["damage"] / type_summary["events"]
top_dape = type_summary["damage_per_event"].sort_values(ascending=False).head(10) / 1e6
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(top_dape.index[::-1], top_dape.values[::-1], color="darkgoldenrod")
ax.set_title("Figure 37. Damage per Event by Disaster Type (Million USD, adjusted)")
ax.set_xlabel("Damage per Event (Million USD)")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig37.png"); plt.close(fig)

# Fig38: top10 countries by Total Affected, colored by dominant type (3 vars)
affected_country = df.groupby("Country")["Total Affected"].sum().sort_values(ascending=False).head(10)
dom_type_country = df[df["Country"].isin(affected_country.index)].groupby(["Country", "Disaster Type"])["Total Events"].sum().unstack().fillna(0).idxmax(axis=1)
fig, ax = plt.subplots(figsize=(8, 5))
colors_aff = [color_map.get(dom_type_country.get(c, ""), "grey") for c in affected_country.index]
ax.barh(affected_country.index[::-1], affected_country.values[::-1] / 1e6, color=colors_aff[::-1])
ax.set_title("Figure 38. Top-10 Countries by People Affected (Million), Colored by Dominant Type")
ax.set_xlabel("Total Affected (Millions)")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig38.png"); plt.close(fig)

# Fig39: time series Total Affected by type, stacked area (3 vars)
affected_pivot = df[df["Disaster Type"].isin(TOP_TYPES)].pivot_table(index="Year", columns="Disaster Type", values="Total Affected", aggfunc="sum").fillna(0)
affected_pivot = affected_pivot.rolling(5, min_periods=1).mean()
fig, ax = plt.subplots(figsize=(9, 5))
ax.stackplot(affected_pivot.index, affected_pivot.T.values / 1e6, labels=affected_pivot.columns, alpha=0.85)
ax.set_title("Figure 39. People Affected by Type Over Time (Millions, 5-yr rolling avg)")
ax.set_xlabel("Year"); ax.set_ylabel("Total Affected (Millions)")
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig39.png"); plt.close(fig)

# Fig40: scatter Total Affected x Total Deaths, size=events, color=type (4 vars)
sub_agg2 = agg[(agg["affected"] > 0) & (agg["deaths"] > 0)]
fig, ax = plt.subplots(figsize=(9, 6))
for i, dtype in enumerate(TOP_TYPES):
    sub = sub_agg2[sub_agg2["Disaster Type"] == dtype]
    sizes = 10 + 100 * (sub["events"] / (agg["events"].max() or 1))
    ax.scatter(sub["affected"], sub["deaths"], s=sizes, alpha=0.6, color=cmap("tab10", 10)(i), label=dtype)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("Total Affected (log)"); ax.set_ylabel("Total Deaths (log)")
ax.set_title("Figure 40. Affected vs Deaths by Country, Sized by Events, Colored by Type")
ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig40.png"); plt.close(fig)

# Fig41: boxplot of Total Deaths distribution by type, log scale (2 vars)
fig, ax = plt.subplots(figsize=(9, 5))
death_data = [df[(df["Disaster Type"] == t) & (df["Total Deaths"] > 0)]["Total Deaths"] for t in TOP_TYPES]
ax.boxplot(death_data, labels=TOP_TYPES, showfliers=False)
ax.set_yscale("log")
ax.set_title("Figure 41. Distribution of Per-Record Deaths by Disaster Type (log scale)")
ax.set_ylabel("Total Deaths (per record, log)")
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig41.png"); plt.close(fig)

# Fig42: CPI over time with total damage overlay, dual-axis (3 vars, uses CPI directly)
yearly_cpi = df.groupby("Year").agg(cpi=("CPI", "mean"), damage=("Total Damage (USD, adjusted)", "sum")).dropna()
fig, ax1 = plt.subplots(figsize=(9, 5))
ax1.plot(yearly_cpi.index, yearly_cpi["cpi"], color="teal")
ax1.set_ylabel("CPI (mean, base year index)", color="teal")
ax2 = ax1.twinx()
ax2.plot(yearly_cpi.index, yearly_cpi["damage"] / 1e9, color="orange", alpha=0.7)
ax2.set_ylabel("Damage (Billion USD, adjusted)", color="orange")
ax1.set_title("Figure 42. CPI Index vs CPI-Adjusted Damage Over Time")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig42.png"); plt.close(fig)

# Fig43: top-10 single deadliest country-type combos (2 vars)
single_deadliest = agg.assign(label=agg["Country"] + " - " + agg["Disaster Type"]).sort_values("deaths", ascending=False).head(10)
fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(single_deadliest["label"][::-1], single_deadliest["deaths"][::-1], color="darkred")
ax.set_title("Figure 43. Top-10 Deadliest Country-Disaster Type Combinations")
ax.set_xlabel("Total Deaths")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig43.png"); plt.close(fig)

# Fig44: original vs CPI-adjusted damage over time (3 vars: year, original, adjusted)
yearly_damage_cmp = df.groupby("Year").agg(original=("Total Damage (USD, original)", "sum"), adjusted=("Total Damage (USD, adjusted)", "sum")).dropna()
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(yearly_damage_cmp.index, yearly_damage_cmp["original"] / 1e9, label="Original USD", color="grey")
ax.plot(yearly_damage_cmp.index, yearly_damage_cmp["adjusted"] / 1e9, label="CPI-Adjusted USD", color="crimson")
ax.set_title("Figure 44. Original vs CPI-Adjusted Damage Over Time")
ax.set_xlabel("Year"); ax.set_ylabel("Damage (Billion USD)"); ax.legend()
fig.tight_layout(); fig.savefig(f"{OUT}/Fig44.png"); plt.close(fig)

# Fig45: heatmap Decade x Disaster Type x Deaths (severity complement to Fig2) (3 vars)
death_heat = df[df["Disaster Type"].isin(TOP_TYPES)].pivot_table(index="Disaster Type", columns="Decade", values="Total Deaths", aggfunc="sum").fillna(0)
fig, ax = plt.subplots(figsize=(10, 4))
im = ax.imshow(np.log1p(death_heat.values), aspect="auto", cmap="Reds")
ax.set_xticks(range(len(death_heat.columns))); ax.set_xticklabels(death_heat.columns, rotation=45)
ax.set_yticks(range(len(death_heat.index))); ax.set_yticklabels(death_heat.index)
ax.set_title("Figure 45. Death-Toll Heatmap: Disaster Type x Decade (log scale)")
fig.colorbar(im, ax=ax, label="log(1+Deaths)")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig45.png"); plt.close(fig)

print("Task Set C (Fig31-45) done.")
print("All 45 figures generated in", OUT)
