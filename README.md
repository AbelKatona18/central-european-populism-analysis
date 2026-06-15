# Quantitative Text-Analysis and Localized Youth Survey on Hungarian Populism (2014-2026)

## Project Overview
This repository contains a quantitative social science data pipeline designed to measure changes in Hungarian political rhetoric between 2014 and 2026. The project uses a custom Python script to calculate the statistical density of two distinct linguistic patterns (absolute/existential framing versus empirical/procedural framing) across six landmark political addresses. 

To evaluate how these rhetorical patterns correlate with public perception on the ground, the pipeline integrates a primary sociological dataset compiled from a localized survey of 64 adolescent participants.

## Directory Structure
*   `data_raw/`: Unabridged, unofficial English transcripts of six foundational political addresses by Viktor Orbán (2014, 2023, 2025) and Péter Magyar (2024, 2026).
*   `data_survey/`: Cleaned, numeric CSV data matrix (N=64) tracking adolescent trust scores regarding institutions such as national governments, local judiciaries, state media, and the European Union.
*   `codebook/`: Methodological framework defining the exact keyword parameters used to isolate absolute/existential markers from empirical/procedural markers.
*   `scripts/`: Automated Python parser (`text_analysis.py`) that filters out transcript metadata, calculates keyword densities, and computes mean trust distributions across the survey sub-samples.

## Project Execution
The analysis script is configured to process the raw text corpus and survey parameters simultaneously to output comparative keyword frequencies alongside regional institutional trust averages.

## Research Affiliation
*   **Lead Researcher:** Ábel Katona, Debrecen, Hungary

  

## Quantitative Research Findings & Output

```text
==================================================================================
File Name                             | Word Count   | Absolute Den | Empirical Den |
==================================================================================

[THESIS: VIKTOR ORBAN CORPUS]

| orban_2014_balvanyos.txt            | 5488         | 0.474       % | 0.237       % |
| orban_2023_state_of_the_nation.txt  | 6048         | 0.397       % | 0.099       % |
| orban_2025_state_of_the_nation.txt  | 5204         | 0.730       % | 0.077       % |

[SYNTHESIS: PETER MAGYAR CORPUS]

| magyar_2024_march_rally.txt         | 2020         | 0.396       % | 0.099       % |
| magyar_2026_march_rally.txt         | 4434         | 0.902       % | 0.180       % |
| magyar_2026_victory_speech.txt      | 2968         | 0.640       % | 0.168       % |

=================================================================
SOCIOLOGICAL LOCALIZED ADOLESCENT SURVEY ANALYSIS (N=64 TOTAL)
=================================================================
--> HUNGARIAN CLUSTER TARGET (N=44 Participants - Eastern Region)
    Mean Trust in National Government (1-5 Scale): 2.95 / 5.0
    Mean Trust in European Union (1-5 Scale):       3.70 / 5.0
    Mean Trust in Regional Judiciary (1-5 Scale):   2.91 / 5.0
    Mean Trust in State-Run News Media (1-5 Scale): 2.41 / 5.0
    Perceived Democratic Reality Score (1-5 Scale): 2.86 / 5.0
    Perceived Fair Election Score (1-5 Scale):      3.18 / 5.0
-----------------------------------------------------------------
--> INTERNATIONAL CONTROL GROUP (N=20 Participants - Global Node)
    Mean Trust in Local Government (1-5 Scale):     2.00 / 5.0
    Mean Trust in European Union (1-5 Scale):       3.20 / 5.0
    Perceived Democratic Reality Score (1-5 Scale): 3.10 / 5.0
=================================================================
```
