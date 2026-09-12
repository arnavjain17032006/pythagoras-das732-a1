# Video Demo Transcript — Team Pythagoras (DAS732 A1)

**Total runtime target: 5:00.** First minute: preprocessing (Arnav Jain). Remaining ~4:00 split roughly evenly across the three task sets, each presenter covering their curated figures with inferences.

---

## [0:00 - 1:00] Introduction & Preprocessing — Arnav Jain

"Hi, we're Team Pythagoras — I'm Arnav Jain, and with me are Kalpit Phogat and Lakshya Jain. For this assignment we worked with the EM-DAT Natural Disasters Emergency Events Database: just over ten thousand records covering two hundred and twenty-five countries and thirteen disaster types, spanning 1900 to 2023.

Before any analysis, we had to clean this dataset. The source file used semicolons instead of commas, so the first step was converting the delimiter so it would load correctly in both Python and Tableau. We also found a couple of typos in the source column names — 'Disaster Subroup' was missing a 'g', and 'Extreme temperature' had a trailing space — small things, but they'd break any grouping operation if left in. The CPI column was the trickiest fix: it was stored with a comma as the decimal separator, like '2,849...' instead of '2.849...', so pandas was reading the entire column as text until we corrected that.

The more important decision was how to handle missing data. About sixty-three percent of records have no damage figure at all, and almost a third are missing death or affected counts — mostly from before 1980. We deliberately left these as missing rather than filling them in as zero, because in this dataset 'zero impact' and 'not reported' are very different things, and zero-filling would have made early-twentieth-century disasters look artificially harmless. We also added a derived field marking each record as Pre-1980 or 1980-to-present, because — as you'll see in a moment — a huge part of the story here is figuring out how much of the rise in recorded disasters is real, and how much is just better record-keeping over time.

With that cleaned dataset, we split into three task sets: I looked at how disasters have changed over time, Kalpit looked at where they happen, and Lakshya looked at how severe they are. Kalpit, over to you."

---

## [1:00 - 2:15] Task Set A — Temporal Trends — Arnav Jain

*(If time allows, Arnav's own section can be presented here instead of handed off; adjust ordering to match who is speaking on camera.)*

"Starting with time. Here's our stacked area chart of events by type, smoothed over five years [Figure 1]. Recorded events go from single digits a year before 1970 to over three hundred a year by the mid-2000s — more than a thirty-fold increase — and it's floods and storms driving almost all of that growth, not earthquakes or volcanic activity.

That raises the obvious question: is this real, or just better reporting? We used earthquakes as a control, since a magnitude-6 earthquake is hard to miss even with 1950s infrastructure. Here's the annualized comparison [Figure 4]: floods rise nearly eighteen-fold after 1980, storms about nine-fold, but earthquakes only rise about four-fold. That gap tells us two things are happening at once — a general reporting-infrastructure improvement affecting every category equally, roughly that four-fold earthquake baseline, and then a real, additional rise in flood and storm frequency on top of that.

One more figure I'll highlight: this heatmap of decade versus disaster type [Figure 2] shows floods have the steepest decade-over-decade growth of anything in the dataset, which lines up with everything else we found."

---

## [2:15 - 3:30] Task Set B — Geographic Distribution — Kalpit Phogat

"Thanks, Arnav. If disasters are rising, the next question is: where? This heatmap [Figure 16] shows our top fifteen countries by event count, broken down by disaster type. The United States is storm-dominated, China and India are flood-dominated, and the Philippines shows a mix of storms, floods, and earthquakes — no two countries look alike.

But raw event counts can be misleading. This normalized view [Figure 17] shows the *share* of each country's disasters by type, and it tells a different story — countries like Bangladesh and Vietnam are almost entirely flood-and-storm exposed, a narrow but severe risk profile, while the US spreads its risk across several types.

The figure I find most interesting is this slopegraph [Figure 21], comparing each country's rank before and after 1980. Vietnam jumps from rank thirty-nine before 1980 to rank eight after — a nearly twenty-fold increase in events — and Thailand and Malaysia show similarly dramatic jumps. This tells us the 'hotspot' countries for disaster exposure have genuinely shifted over the past forty years, not just grown at the same rate everywhere. Lakshya, over to you for the severity side."

---

## [3:30 - 4:45] Task Set C — Impact Severity — Lakshya Jain

"Thanks, Kalpit. So we know disasters are more frequent, and we know where. The last question is: how much do they actually cost us, in lives and money? This is where the story gets counter-intuitive.

Here's cumulative deaths by disaster type [Figure 32]. Drought is the deadliest category by far — about eleven point seven million deaths — even though it has one of the *lowest* event counts of any major type, just eight hundred and two recorded events. Compare that to floods, which have over five thousand seven hundred events but 'only' about seven million deaths. When we compute deaths per event [Figure 36], drought comes out to roughly fourteen thousand six hundred deaths per event, versus about three hundred for storms — a forty-eight-fold difference.

Our correlation matrix [Figure 35] makes this precise: the correlation between event count and deaths is essentially zero, while damage correlates moderately with event count. So frequency predicts economic cost reasonably well, but it tells you almost nothing about death toll — that's governed by disaster type.

Finally, this dual-axis chart [Figure 33] shows CPI-adjusted damage climbing to over two trillion dollars a decade by the 2010s, while deaths spike in individual bad years rather than climbing steadily — suggesting our early-warning systems have gotten better at saving lives even as our economic exposure keeps growing."

---

## [4:45 - 5:00] Closing — Arnav Jain

"So to summarize: disasters are genuinely becoming more frequent, driven mainly by floods and storms; that risk is concentrated in a shifting set of countries, with Southeast Asia emerging as a new hotspot; and severity doesn't track frequency — drought and earthquakes need a completely different, early-warning-focused response compared to the infrastructure-mitigation approach that makes sense for flood-prone regions. Thanks for watching."

---

**Notes for recording:**
- Swap speaker order/wording as needed to match who is actually presenting each section live.
- Each spoken segment above is roughly 250-300 words, timed at a natural speaking pace (~150 wpm) to fit its allotted window — trim if you're running over 5:00 in a live take.
- Screen-share the corresponding Tableau sheet or the report's figure while narrating each bracketed [Figure N] reference.
