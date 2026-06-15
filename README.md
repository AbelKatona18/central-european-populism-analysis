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
