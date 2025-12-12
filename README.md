# Westminster Child Population Projections 2025

Interactive visualisation comparing Mid-Year Estimates with GLA 2024-based population projections for Children's Services.

## About This Project

This Streamlit app was created to resolve confusion among Westminster Children's Services teams about 2025 child population estimates. Different teams were citing conflicting figures, which arose from referencing different age bands (0-15 vs 0-19), different projection variants, and potentially outdated documents.

## What This Tool Shows

- **Interactive charts** comparing actual Mid-Year Estimates (2023-2024) with GLA 2024-based projections (2025)
- **Three migration variants** showing range of plausible outcomes:
  - 5-year migration trend (2019-2024 average)
  - **10-year migration trend (2014-2024 average) ⭐ RECOMMENDED**
  - 15-year migration trend (2009-2024 average)
- **Gender breakdowns** (optional toggle)
- **Full methodology** with strengths and limitations

## Key Findings

### Recommended Figures for 2025 (10-year migration variant):
- **Ages 0-19:** 34,705 persons
- **Ages 0-15:** 25,516 persons

### Range Across All Variants:
- **Ages 0-19:** 34,705 to 34,897 (192 persons range)
- **Ages 0-15:** 25,516 to 25,668 (152 persons range)

### Projected Changes from 2024:
- **Ages 0-19:** Decrease of 720 to 912 persons (depending on variant)
- **Ages 0-15:** Decrease of 552 to 704 persons (depending on variant)

## Methodology

**Data Source:** GLA 2024-based trend-based population projections (research outputs)

**Base Year:** 2024 Mid-Year Estimates (ONS, published July 2024)

**Assumptions:**
- **Fertility:** Principal (central) assumption - held constant
- **Life expectancy:** Principal (central) assumption - held constant
- **Migration:** VARIED across three scenarios (5yr, 10yr, 15yr historical averages)

**Why only migration variants?**  
This analysis focuses exclusively on migration variants because Westminster is a highly mobile borough where migration is the most volatile demographic component and the primary driver of uncertainty in child population projections.

**Other GLA variants not examined:**  
The GLA produces seven projection variants in total, combining different fertility, life expectancy, and migration assumptions. This analysis examines only the three variants that hold fertility and life expectancy constant whilst varying migration assumptions.

## Why GLA Projections?

**Strengths:**
- ✅ Most recent data available (based on 2024 MYEs)
- ✅ Incorporates latest migration trends
- ✅ Transparent methodology
- ✅ Widely used for planning across London boroughs

**Limitations:**
- ⚠️ Labelled as "research outputs" - not yet quality assured
- ⚠️ Projections are inherently uncertain - actual 2025 MYE may differ
- ⚠️ The 2025 MYE won't be published until mid-2026
- ⚠️ This analysis only examines migration variants

## Files in This Repository

- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Sample Email Templates

### Template 1: Detailed Response

**Subject:** Clarification on 2025 Child Population Estimates

Hi [Team],

Following the query about conflicting child population figures for 2025, I've analysed the most recent data and created an interactive tool to clarify the numbers.

**Quick Answer:**
- **Ages 0-19 (2025):** Approximately 34,700 persons (recommended figure: 34,705)
- **Ages 0-15 (2025):** Approximately 25,500 persons (recommended figure: 25,516)

**Why the confusion?**  
Different teams were referencing different age bands (0-15 vs 0-19), different projection variants, and potentially older projection rounds.

**Source & Methodology:**  
These figures come from the GLA's 2024-based population projections (research outputs), which are:
- Based on the latest 2024 Mid-Year Estimates (published July 2024)
- Using principal fertility and life expectancy assumptions
- With three migration variants (5yr, 10yr, 15yr historical trends)
- The 10-year variant is the recommended "core" projection

Since the 2025 Mid-Year Estimates won't be published until mid-2026, these projections are currently our best available evidence.

**Interactive Visualisation:**  
[INSERT YOUR STREAMLIT URL HERE]

This tool allows you to:
- See the actual vs projected figures
- Compare different projection scenarios
- View gender breakdowns
- Understand the methodology and limitations

**Recommendation:**  
For planning purposes, I recommend using the 10-year migration variant figures:
- Ages 0-19: 34,705 persons
- Ages 0-15: 25,516 persons

Note that all projections show a continuing decline in child population from 2024 to 2025.

Please let me know if you need any clarification or have questions about the methodology.

Best regards,  
[Your name]

---

### Template 2: Quick Response

**Subject:** 2025 Child Population Figures - Clarification

Hi [Team],

Quick clarification on the 2025 child population query:

**Recommended figures (GLA 2024-based projections):**
- Ages 0-19: 34,705 persons
- Ages 0-15: 25,516 persons

These are from the most recent GLA projections based on 2024 Mid-Year Estimates. The 2025 MYEs won't be available until mid-2026, so these projections are our best current evidence.

**Interactive visualisation with full methodology:**  
[INSERT YOUR STREAMLIT URL HERE]

The confusion arose from teams referencing different age bands and projection variants. The tool clarifies all of this.

Best,  
[Your name]

---

### Template 3: Executive Summary for Senior Leadership

**Subject:** Westminster Child Population 2025: Best Available Estimates

**Summary:**  
Based on the latest GLA 2024-based projections, Westminster's 2025 child population is estimated at:
- **0-19 years:** ~34,705 persons (declining by ~912 from 2024)
- **0-15 years:** ~25,516 persons (declining by ~704 from 2024)

**Context:**  
Recent queries revealed confusion among teams about 2025 figures. Different sources were being referenced:
- Different age bands (0-15 vs 0-19)
- Different projection variants
- Potentially outdated documents

**Data Source:**  
GLA 2024-based trend-based population projections (research outputs), published November 2024, using 2024 Mid-Year Estimates as the base year. These are currently the most reliable estimates available, as the 2025 MYE won't be published until mid-2026.

**Confidence Level:**  
The range across different migration scenarios is relatively narrow (152-192 persons depending on age band), suggesting high confidence in these projections for 2025.

**Interactive tool:** [INSERT YOUR STREAMLIT URL HERE]

---

## Updating the Data

When new data becomes available (e.g., 2025 MYEs in mid-2026):

1. Edit `app.py` on GitHub
2. Update the `default_data` dictionary (around line 155)
3. Commit changes
4. Streamlit will automatically redeploy within ~1 minute

## Technical Details

**Built with:**
- Python 3.9+
- Streamlit 1.29.0
- Pandas 2.1.3
- Plotly 5.18.0

**Data embedded in code** - no external files or databases required.

## Contact & Support

This tool was created for Westminster City Council Children's Services.  
For questions about the data or methodology, please contact [your contact details].

For technical issues with the Streamlit app, check the [Streamlit documentation](https://docs.streamlit.io/).

---

**Last updated:** December 2024  
**Data source:** GLA 2024-based Population Projections (Research Outputs) | ONS Mid-Year Estimates  
**GLA Documentation:** https://data.london.gov.uk/blog/gla-2024-based-population-projections-research-outputs/
