# Video Demo Transcript — Arnav Jain's Portion Only

**Target runtime: ~2:20** (1:00 preprocessing intro + ~1:20 Task Set A), fitting within the assignment's overall 5:00 cap for all three presenters combined. Trim further if the other presenters need more time.

**Camera:** the assignment does not require a face-cam — it only requires "each member explains their task, visualization solutions, and inferences." A screen recording with voiceover is sufficient; showing your face is optional.

---

## 0:00 – 1:00 Introduction & Preprocessing

**On screen:** the raw CSV vs. the cleaned CSV side by side, or `code/preprocess.py`, or the cleaned dataset (`data/emdat_cleaned.csv`) loaded in Tableau/Excel.

"Hi, I'm Arnav Jain from Team Pythagoras, and for this assignment we worked with the EM-DAT Natural Disasters Emergency Events Database, which is just over ten thousand records covering two hundred and twenty-five countries and thirteen disaster types, spanning 1900 to 2023.

Before any analysis we had to clean this dataset, and the source file used semicolons instead of commas, so the first step was converting the delimiter so it would load correctly, and then we also fixed a couple of typos in the source column names, and corrected the CPI column, which was stored with a comma as the decimal separator, because pandas was reading the whole column as text until we fixed that.

The bigger decision was how to handle missing data, and about sixty-three percent of records have no damage figure at all, and almost a third are missing death or affected counts, mostly from before 1980, so we deliberately left these as missing rather than filling them in as zero, because in this dataset 'zero impact' and 'not reported' are very different things, and we also added a field marking each record as Pre-1980 or 1980-to-present, because a big part of our story is figuring out how much of the rise in recorded disasters is real, versus just better record-keeping over time.

So with that cleaned dataset, we split into three task sets covering when disasters happen, where they happen, and how severe they are, and my task set covers temporal trends."

---

## 1:00 – 1:30 Task Set A, Part 1 — The Overall Rise

**On screen:** Figure 1 (`images/Fig1.png`), or the equivalent live sheet in Tableau if connected.

"So starting with time, our stacked area chart of events by type (Figure 1) shows recorded events going from single digits a year before 1970 to over three hundred a year by the mid-2000s, so that's more than a thirty-fold increase, and it's driven almost entirely by floods and storms, not earthquakes."

## 1:30 – 1:50 Task Set A, Part 2 — Real Rise or Just Better Reporting?

**On screen:** Figure 4 (`images/Fig4.png`) — the pre/post-1980 annualized-rate bar chart.

"And that raises the obvious question: is this real, or just better reporting? So we used earthquakes as a control, since a strong earthquake is hard to miss even with 1950s infrastructure, and here's the annualized comparison (Figure 4): floods rise nearly eighteen-fold after 1980, and storms rise about nine-fold, but earthquakes only rise about four-fold, so that gap tells us two things are happening — a general reporting improvement affecting every category by roughly that four-fold earthquake baseline, and then on top of that, a real, additional rise in flood and storm frequency."

## 1:50 – 2:20 Task Set A, Part 3 — Two Supporting Figures

**On screen:** Figure 3 (`images/Fig3.png`), then Figure 14 (`images/Fig14.png`).

"And two more figures worth flagging — our small-multiples view (Figure 3) shows every single disaster type, even earthquakes and volcanic eruptions, near-zero before 1980, which is direct evidence that gap is a reporting artifact and not a quiet era, and then our volatility chart (Figure 14) shows that year-to-year unpredictability in disaster counts has also risen alongside the average, so response planning today needs to budget for that swing, and not just a higher average load."

---

## Notes

- This portion alone runs to roughly 2:20 at a natural ~150 words/minute pace — leaving about 2:40 combined for the other two task sets plus a short closing, per the assignment's 5:00 total cap.
- If the team wants each of the three main sections to be closer to equal length, trim the Task Set A section down to the 1:00-1:50 block only (Figures 1 and 4, drop Figure 3/14) to bring this portion to about 1:40 total.
- The full 15-figure detailed script for Task Set A (used for the written report, not the video) is in `report.md` Section 5 — pull additional lines from there only if the team decides to extend the video beyond 5 minutes for a non-submission version.
