# Video Demo Transcript — Arnav Jain's Portion Only

**Target runtime: ~2:20** (1:00 preprocessing intro + ~1:20 Task Set A), fitting within the assignment's overall 5:00 cap for all three presenters combined. Trim further if Kalpit/Lakshya need more time.

---

## [0:00 – 1:00] Introduction & Preprocessing

"Hi, we're Team Pythagoras — I'm Arnav Jain, and with me are Kalpit Phogat and Lakshya Jain. For this assignment we worked with the EM-DAT Natural Disasters Emergency Events Database: just over ten thousand records covering two hundred and twenty-five countries and thirteen disaster types, spanning 1900 to 2023.

Before any analysis, we had to clean this dataset. The source file used semicolons instead of commas, so the first step was converting the delimiter so it would load correctly. We also fixed a couple of typos in the source column names, and corrected the CPI column, which was stored with a comma as the decimal separator — pandas was reading the whole column as text until we fixed that.

The bigger decision was how to handle missing data. About sixty-three percent of records have no damage figure at all, and almost a third are missing death or affected counts — mostly from before 1980. We deliberately left these as missing rather than filling them in as zero, because in this dataset 'zero impact' and 'not reported' are very different things. We also added a field marking each record as Pre-1980 or 1980-to-present, because a big part of our story is figuring out how much of the rise in recorded disasters is real, versus just better record-keeping over time.

With that cleaned dataset, we split into three task sets: I looked at how disasters have changed over time, Kalpit looked at where they happen, and Lakshya looked at how severe they are."

---

## [1:00 – 2:20] Task Set A — Temporal Trends

"Starting with time. Our stacked area chart of events by type [Figure 1] shows recorded events going from single digits a year before 1970 to over three hundred a year by the mid-2000s — more than a thirty-fold increase — driven almost entirely by floods and storms, not earthquakes.

That raises the obvious question: is this real, or just better reporting? We used earthquakes as a control, since a strong earthquake is hard to miss even with 1950s infrastructure. Here's the annualized comparison [Figure 4]: floods rise nearly eighteen-fold after 1980, storms about nine-fold, but earthquakes only rise about four-fold. That gap tells us two things are happening — a general reporting improvement affecting every category by roughly that four-fold earthquake baseline, and then a real, additional rise in flood and storm frequency on top of that.

Two more figures worth flagging: our small-multiples view [Figure 3] shows every single disaster type — even earthquakes and volcanic eruptions — near-zero before 1980, which is direct evidence that gap is a reporting artifact, not a quiet era. And our volatility chart [Figure 14] shows that year-to-year unpredictability in disaster counts has also risen alongside the average — so response planning today needs to budget for that swing, not just a higher average load.

Over to Kalpit for the geographic side."

---

## Notes

- This portion alone runs to roughly 2:20 at a natural ~150 words/minute pace — leaving Kalpit and Lakshya about 2:40 combined for their sections plus a short closing, per the assignment's 5:00 total cap.
- If the team wants each of the three main sections to be closer to equal length, trim the Task Set A section down to Figures 1 and 4 only (drop the Figure 3 / Figure 14 callouts) to bring this portion to about 1:40 total.
- The full 15-figure detailed script for Task Set A (used for the written report, not the video) is in `report.md` Section 5 — pull additional lines from there only if the team decides to extend the video beyond 5 minutes for a non-submission version.
