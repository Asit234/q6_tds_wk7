# CAC Quarterly Analysis (2024)

**Author/Contact:** 24f1000537@ds.study.iitm.ac.in

## Summary
This repository analyses Customer Acquisition Cost (CAC) across quarters in 2024 and compares it to the industry benchmark target of **150**.

**Quarterly CAC (2024)**:
- Q1: 226.73
- Q2: 226.27
- Q3: 233.32
- Q4: 230.73

**Average CAC (2024): 229.26**

## Key Findings
1. The company's quarterly CACs are consistently **well above** the industry target of 150.
2. Observed CACs across four quarters are tightly clustered between 226.27 and 233.32 with an overall average of **229.26**, indicating limited seasonality but a persistently elevated acquisition cost.
3. Q3 has the highest CAC (233.32) and Q2 the lowest (226.27), but the spread is small (~7.05 range), hinting that the issue is structural rather than timing-dependent.

## Business implications
- A CAC of ~229 (vs target 150) implies the business is paying ~52.7% more per acquired customer than the benchmark (calculation: (229-150)/150 = 0.5267).
- Persistently high CAC will compress customer lifetime value (LTV) payback period, reduce marketing ROI, and cut margins if prices & retention remain unchanged.
- Because quarter-to-quarter variation is low, short-term promotional fixes are unlikely to bring CAC down to the target — structural changes are required.

## Recommendation (Solution)
**Primary strategy: Optimize digital marketing channels** — a focused, measurable program to reduce CAC by improving channel efficiency and targeting. The program should include:

1. **Channel-level audit & reallocation**
   - Identify top-performing channels by conversion rate and true CAC (include all marketing spend & attribution).
   - Reallocate budget from high-CAC / low-converting channels to efficient channels (e.g., organic search, high-ROI paid search, and email).

2. **Creative & funnel optimization**
   - A/B test landing pages and ad creatives to improve conversion rate (small relative uplift in conversion rate can substantially lower CAC).
   - Improve campaign-to-landing-page relevance to raise quality scores and reduce paid media costs.

3. **Audience & targeting refinement**
   - Improve lookalike modeling, use first-party data segments, and exclude poorly converting audiences.
   - Test lower-funnel bidding strategies and remarketing to reduce wasted spend.

4. **Measurement & attribution**
   - Implement accurate multi-touch attribution or incrementality testing to measure true channel ROI.
   - Set channel-level KPIs (CPA targets, conversion rate targets) and run weekly performance dashboards.

5. **Retention & LTV improvements (parallel track)**
   - Because lowering CAC alone is sometimes slow, increase LTV via retention programs and cross-sell to improve ROI and justify CAC in the near term.

## Concrete / tactical next steps (30/60/90)
- **0–30 days**: Channel audit, implement tracking fixes, choose 2–3 test channels for reallocation.
- **30–60 days**: Launch A/B tests for top funnels, begin reallocated campaigns, set weekly dashboards.
- **60–90 days**: Evaluate test results, scale winning campaigns, run incrementality tests, target a 10–20% CAC reduction in this window.

## Target path
- Aim for incremental improvements: reduce CAC by ~10–20% within 3 months through creative & targeting optimizations, and aim for structural changes (attribution + channel mix) to bring CAC toward the industry target over 9–12 months.
- If the current CAC is 229.26, a 20% reduction would reach ~183.41 — progress, but still above 150; reaching 150 will require multiple levers (conversion lifts, channel mix, retention) over time.

## Files
- `data/quarterly_cac.csv` — raw quarterly data
- `analysis/analysis.py` — reproducible script that computes metrics & saves plots
- `notebooks/cac_analysis.ipynb` — notebook version of the analysis
- `analysis/outputs/` — place where plots and summary CSV will be generated

---

If you want, I can also:
- Provide a ready-made slide (PowerPoint) with the key charts and the story text.
- Generate polished plots (Seaborn/Matplotlib) with branded colors if you provide brand colors.
- Draft a short executive slide deck (3 slides) that you can attach to the PR.

