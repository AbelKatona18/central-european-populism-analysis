# Quantitative Text-Analysis and Localized Youth Survey on Hungarian Populism (2014-2026)

## Project Overview
This repository contains a quantitative social science data pipeline designed to measure changes in Hungarian political rhetoric between 2014 and 2026. The project uses a custom Python script to calculate the statistical density of two distinct linguistic patterns—absolute/existential framing versus empirical/procedural framing—across six landmark political addresses. 

To evaluate how these rhetorical patterns correlate with public perception on the ground, the pipeline integrates a primary sociological dataset compiled from a localized survey of 64 adolescent participants.

## Directory Structure
*   `data_raw/`: Unabridged English transcripts of six foundational political addresses by Viktor Orbán (2014, 2023, 2025) and Péter Magyar (2024, 2026).
*   `data_survey/`: Cleaned, numeric CSV data matrix (N=64) tracking adolescent trust scores regarding national governance, local judiciaries, state media, and European Union frameworks.
*   `codebook/`: Methodological framework defining the exact keyword parameters used to isolate absolute/existential markers from empirical/procedural markers.
*   `scripts/`: Automated Python parser (`text_analysis.py`) that filters out transcript metadata, calculates keyword densities, and computes mean trust distributions across the survey sub-samples.

## Project Execution
The analysis script is configured to process the raw text corpus and survey parameters simultaneously to output comparative keyword frequencies alongside regional institutional trust averages.

## Research Affiliation
*   **Lead Researcher:** Ábel Katona, Debrecen, Hungary

  

### Quantitative Research Findings & Output

### 1. Corpus Text-Mining Performance (Linguistic Density Analysis)

| File Name | Word Count | Absolute/Existential Density | Empirical/Procedural Density |
| :--- | :--- | :--- | :--- |
| `orban_2014_balvanyos.txt` | 5488 | 0.474% | 0.237% |
| `orban_2023_state_of_the_nation.txt` | 6848 | 0.397% | 0.090% |
| `orban_2025_state_of_the_nation.txt` | 5204 | 0.730% | 0.077% |
| `magyar_2025_march_rally.txt` | 2028 | 0.806% | 0.000% |
| `magyar_2026_march_rally.txt` | 4434 | 0.902% | 0.180% |
| `magyar_2026_victory_speech.txt` | 2968 | 0.540% | 0.168% |

### 2. Mixed-Methods Behavioral Survey Results (N=64 Target vs. Control)
*   **Hungarian Cohort (N=44, Sub-Regional Conservative Stronghold Outlier):**
    *   Mean Trust in National Government (1-5 Likert): **2.45 / 5.00**
    *   Mean Trust in European Union Frameworks (1-5 Likert): **3.70 / 5.00**
    *   Mean Trust in Regional Judiciary Systems (1-5 Likert): **2.91 / 5.00**
    *   Mean Trust in State-Run News Media Outlets (1-5 Likert): **2.42 / 5.00**
    *   Perceived Democratic Reality Score (1-5 Likert): **2.86 / 5.00**
    *   Perceived Fair Election Score (1-5 Likert): **3.18 / 5.00**
*   **International Control Group (N=20, Global Node Comparative Baseline):**
    *   Mean Trust in Local Sovereign Government (1-5 Likert): **2.00 / 5.00**
    *   Mean Trust in European Union Frameworks (1-5 Likert): **3.20 / 5.00**
    *   Perceived Democratic Reality Score (1-5 Likert): **3.10 / 5.00**
