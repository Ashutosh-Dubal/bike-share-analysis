# 🚲 Toronto Bike Share Ridership Analysis

This project explores ridership patterns of Toronto's public bike sharing system using open data from the City of Toronto. 

> This project is still being worked on.

## 📊 Key Objectives
- Identify usage trends across time and location
- Understand differences between member and casual users
- Highlight busiest stations and trip durations

## 📁 Project Structure
- `data/` — Raw and cleaned datasets
- `scripts/` — Automation for data fetching and cleaning
- `visuals/` — Saved figures and charts

## ⚠️ Data Limitations

While analyzing the 2023 Bike Share Toronto ridership data, a significant gap was identified:

Annual Member data is missing from August to December 2023.
During this period, all recorded trips are labeled as “Casual Members”, with no entries for annual users. This appears to be a dataset omission rather than a behavioral trend.

As a result:
	•	All user behavior analysis comparing Casual vs. Annual Members is limited to January through July 2023.
	•	Insights beyond July reflect only Casual Member usage and should be interpreted accordingly.

This gap was retained intentionally to preserve dataset integrity and highlight real-world challenges analysts face when working with open data.
