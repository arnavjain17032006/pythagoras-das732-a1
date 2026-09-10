"""Generate the 15 report figures (5 per task set) for EM-DAT Natural Disasters.

Task Set A (Arnav Jain)    - Temporal trends       -> Fig1-Fig5
Task Set B (Kalpit Phogat) - Geographic distribution -> Fig6-Fig10
Task Set C (Lakshya Jain)  - Impact severity        -> Fig11-Fig15
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

# ---------- Task Set A: Temporal Trends ----------

# Fig1: stacked area, Year x Disaster Type x Total Events (3 vars)
pivot = df[df["Disaster Type"].isin(TOP_TYPES)].pivot_table(
    index="Year", columns="Disaster Type", values="Total Events", aggfunc="sum"
).fillna(0)
pivot = pivot.rolling(5, min_periods=1).mean()  # 5-yr smoothing for readability
fig, ax = plt.subplots(figsize=(9, 5))
ax.stackplot(pivot.index, pivot.T.values, labels=pivot.columns, alpha=0.85)
ax.set_title("Figure 1. Disaster Events by Type Over Time (5-yr rolling avg)")
ax.set_xlabel("Year"); ax.set_ylabel("Total Events")
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig1.png"); plt.close(fig)

# Fig2: heatmap, Decade x Disaster Type, color = Total Events (3 vars)
df["Decade"] = (df["Year"] // 10) * 10
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

# Fig3: small multiples, Year x Total Events trellised by Disaster Type (2 vars x facets)
fig, axes = plt.subplots(2, 3, figsize=(12, 6), sharex=True)
for ax, dtype in zip(axes.flat, TOP_TYPES):
    sub = df[df["Disaster Type"] == dtype].groupby("Year")["Total Events"].sum()
    ax.plot(sub.index, sub.values, color="steelblue")
    ax.axvspan(1900, 1980, color="grey", alpha=0.15)
    ax.set_title(dtype, fontsize=9)
fig.suptitle("Figure 3. Per-Type Trends (grey = pre-1980 sparse-reporting era)")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig3.png"); plt.close(fig)

# Fig4: pre/post-1980 comparison bar (Reporting Era x Disaster Type x events)
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

# Fig5: overview single line, total events per year with reporting-era shading
yearly = df.groupby("Year")["Total Events"].sum()
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(yearly.index, yearly.values, color="darkred")
ax.axvspan(1900, 1980, color="grey", alpha=0.15, label="Sparse reporting era")
ax.set_title("Figure 5. Total Disaster Events per Year, 1900-2023 (Overview)")
ax.set_xlabel("Year"); ax.set_ylabel("Total Events"); ax.legend()
fig.tight_layout(); fig.savefig(f"{OUT}/Fig5.png"); plt.close(fig)

# ---------- Task Set B: Geographic Distribution ----------

top_countries = df.groupby("Country")["Total Events"].sum().sort_values(ascending=False).head(15)

# Fig6: heatmap Country x Disaster Type, color = Total Events (3 vars)
geo_heat = df[df["Country"].isin(top_countries.index) & df["Disaster Type"].isin(TOP_TYPES)].pivot_table(
    index="Country", columns="Disaster Type", values="Total Events", aggfunc="sum"
).fillna(0).loc[top_countries.index]
fig, ax = plt.subplots(figsize=(9, 7))
im = ax.imshow(geo_heat.values, aspect="auto", cmap="YlGnBu")
ax.set_xticks(range(len(geo_heat.columns))); ax.set_xticklabels(geo_heat.columns, rotation=45, ha="right")
ax.set_yticks(range(len(geo_heat.index))); ax.set_yticklabels(geo_heat.index)
ax.set_title("Figure 6. Country x Disaster Type Exposure Heatmap (Top 15 Countries)")
fig.colorbar(im, ax=ax, label="Total Events")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig6.png"); plt.close(fig)

# Fig7: stacked bar, Country x Disaster Type composition (3 vars)
comp = geo_heat.div(geo_heat.sum(axis=1), axis=0)
fig, ax = plt.subplots(figsize=(10, 6))
bottom = np.zeros(len(comp))
colors = cm.get_cmap("tab10", len(comp.columns))
for i, col in enumerate(comp.columns):
    ax.barh(comp.index, comp[col], left=bottom, label=col, color=colors(i))
    bottom += comp[col].values
ax.set_title("Figure 7. Disaster-Type Composition by Country (Top 15, share of events)")
ax.set_xlabel("Share of Total Events")
ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig7.png"); plt.close(fig)

# Fig8: bubble chart, Country (rank) x Total Events x dominant type (3 vars)
dominant_type = geo_heat.idxmax(axis=1)
fig, ax = plt.subplots(figsize=(10, 5))
type_list = sorted(dominant_type.unique())
color_map = {t: cm.get_cmap("tab10")(i) for i, t in enumerate(type_list)}
for i, country in enumerate(top_countries.index):
    ax.scatter(i, top_countries[country], s=top_countries[country] / 2,
               color=color_map[dominant_type[country]], alpha=0.75,
               label=dominant_type[country] if dominant_type[country] not in ax.get_legend_handles_labels()[1] else "")
ax.set_xticks(range(len(top_countries))); ax.set_xticklabels(top_countries.index, rotation=45, ha="right")
ax.set_ylabel("Total Events")
ax.set_title("Figure 8. Top-15 Countries by Events, Sized by Volume, Colored by Dominant Type")
handles = [plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=color_map[t], markersize=8, label=t) for t in type_list]
ax.legend(handles=handles, bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig8.png"); plt.close(fig)

# Fig9: overview bar, Total Events by Country (1 var, simple - overview)
fig, ax = plt.subplots(figsize=(9, 6))
ax.barh(top_countries.index[::-1], top_countries.values[::-1], color="teal")
ax.set_title("Figure 9. Total Disaster Events by Country (Top 15, Overview)")
ax.set_xlabel("Total Events")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig9.png"); plt.close(fig)

# Fig10: trend, Country x Year x Total Events for top 5 countries (3 vars)
top5 = top_countries.head(5).index
fig, ax = plt.subplots(figsize=(9, 5))
for country in top5:
    sub = df[df["Country"] == country].groupby("Year")["Total Events"].sum().rolling(5, min_periods=1).mean()
    ax.plot(sub.index, sub.values, label=country)
ax.set_title("Figure 10. Event Trends for Top-5 Countries (5-yr rolling avg)")
ax.set_xlabel("Year"); ax.set_ylabel("Total Events"); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig10.png"); plt.close(fig)

# ---------- Task Set C: Impact Severity ----------

# Fig11: scatter, Total Events x Total Deaths, size=Damage, color=Type (4 vars)
agg = df[df["Disaster Type"].isin(TOP_TYPES)].groupby(["Country", "Disaster Type"]).agg(
    events=("Total Events", "sum"), deaths=("Total Deaths", "sum"),
    damage=("Total Damage (USD, adjusted)", "sum")
).reset_index()
agg = agg[(agg["deaths"] > 0) & (agg["events"] > 0)]
fig, ax = plt.subplots(figsize=(9, 6))
for i, dtype in enumerate(TOP_TYPES):
    sub = agg[agg["Disaster Type"] == dtype]
    sizes = 20 + 200 * (sub["damage"].fillna(0) / (agg["damage"].max() or 1))
    ax.scatter(sub["events"], sub["deaths"], s=sizes, alpha=0.6, color=cm.get_cmap("tab10")(i), label=dtype)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("Total Events (log)"); ax.set_ylabel("Total Deaths (log)")
ax.set_title("Figure 11. Events vs Deaths by Country, Sized by Damage, Colored by Type")
ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig11.png"); plt.close(fig)

# Fig12: top-10 deadliest disaster types, bar (2 vars - overview)
deadliest = df.groupby("Disaster Type")["Total Deaths"].sum().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(deadliest.index[::-1], deadliest.values[::-1], color="firebrick")
ax.set_title("Figure 12. Top-10 Deadliest Disaster Types (Cumulative, 1900-2023)")
ax.set_xlabel("Total Deaths")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig12.png"); plt.close(fig)

# Fig13: dual-axis time series, Year x Damage x Deaths (3 vars)
yearly_impact = df.groupby("Year").agg(
    damage=("Total Damage (USD, adjusted)", "sum"), deaths=("Total Deaths", "sum")
)
fig, ax1 = plt.subplots(figsize=(9, 5))
ax1.plot(yearly_impact.index, yearly_impact["damage"] / 1e9, color="darkorange")
ax1.set_ylabel("Damage (Billion USD, adjusted)", color="darkorange")
ax2 = ax1.twinx()
ax2.plot(yearly_impact.index, yearly_impact["deaths"], color="navy", alpha=0.6)
ax2.set_ylabel("Deaths", color="navy")
ax1.set_title("Figure 13. Economic Damage vs Deaths Over Time")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig13.png"); plt.close(fig)

# Fig14: top-10 costliest countries, bar with Deaths as color-intensity (3 vars)
cost = df.groupby("Country").agg(
    damage=("Total Damage (USD, adjusted)", "sum"), deaths=("Total Deaths", "sum")
).sort_values("damage", ascending=False).head(10)
fig, ax = plt.subplots(figsize=(8, 5))
norm_deaths = (cost["deaths"] - cost["deaths"].min()) / (cost["deaths"].max() - cost["deaths"].min() + 1)
bars = ax.barh(cost.index[::-1], cost["damage"].values[::-1] / 1e9, color=cm.get_cmap("Reds")(norm_deaths.values[::-1]))
ax.set_title("Figure 14. Top-10 Costliest Countries (color intensity = Total Deaths)")
ax.set_xlabel("Total Damage (Billion USD, adjusted)")
fig.tight_layout(); fig.savefig(f"{OUT}/Fig14.png"); plt.close(fig)

# Fig15: correlation matrix-style scatter grid (events, deaths, affected, damage) (4 vars)
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
ax.set_title("Figure 15. Correlation: Events, Deaths, Affected, Damage")
fig.colorbar(im, ax=ax)
fig.tight_layout(); fig.savefig(f"{OUT}/Fig15.png"); plt.close(fig)

print("All 15 figures generated in", OUT)
