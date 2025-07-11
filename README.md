# 🚲 Toronto Bike Share Ridership Analysis

This project explores ridership patterns of Toronto's public bike sharing system using open data from the City of Toronto. 

> This project is still being worked on.

---

## 📊 Key Objectives
- Identify usage trends across time and location
- Understand differences between member and casual users
- Highlight busiest stations and trip durations

## 📚 Table of Contents
1. [Dataset Description]
2. [Challenges & Learnings]
3. [How to Install and Run the Project]
4. [How to Use the Project]
5. [Sample Output]
6. [Key Insights & Analysis]
7. [Tech Stack]
8. [Project Structure]
9. [Author]
10. [License]

---

## 📦 Dataset Description

This project uses open data from the City of Toronto Open Data Portal, focusing on Bike Share Toronto ridership data for the year 2023.

The dataset includes over 800,000 anonymized trip records, each representing a single ride within the city’s bike share system.

### ✅ Key Features Collected:

| **Feature**                   | **Description**                                             |
| ----------------------------- | ----------------------------------------------------------- |
| Trip ID                       | Unique identifier for each ride                             |
| Trip Duration                 | Duration in seconds                                         |
| Trip Start Station ID         | Unique ID for the station where the trip began              |
| Trip Start time               | Timestamps for trip start                                   |
| Trip Start Station Location   | Coordinates of the start station (not present in all files) |
| Trip End Station ID           | Unique ID for the station where the trip ended              |
| Trip End Time                 | Timestamps for trip end                                     |
| Trip End Station Location     | Coordinates of the end station (not present in all files)   |
| Bike ID                       | Unique ID of the bike used                                  |
| User type                     | Either Casual Member or Annual Member                       |

---

## 🧠 Challenges & Learnings

### 🔍 1. Working with Real-World Open Data

One of the primary challenges was handling inconsistencies in the raw dataset:
	
    •	Files were provided in mixed formats (ZIP, CSV, XLSX) with varying character encodings.
	•	Some CSVs contained malformed headers (e.g., ï»¿trip_id) due to encoding artifacts.
	•	Several months lacked complete data — notably, Annual Member records were missing from August to December 2023.

These issues underscored the importance of robust data cleaning and careful data validation before analysis.

### 🗂 2. Managing Large Volumes of Data

With over 800,000 trip records, handling memory and processing time became a key consideration:
	
    •	Only relevant columns were retained throughout processing
	•	Outlier durations (e.g., trips longer than 2 hours) were excluded to reduce skew
	•	Efficient pandas operations and modular scripts helped maintain performance

### 📊 3. Data Visualization and Storytelling

Beyond plotting, this project focused on deriving insights and understanding user behavior:
	
    •	Investigating why 8am rides are higher than 5pm, despite both being rush hours
	•	Identifying key traffic hubs like Bay St / College St (East Side) and Union Station
	•	Comparing Casual vs Annual Member behavior by trip duration, weekday, and month

This process sharpened both visualization techniques and interpretive thinking.

### ⚠️ 4. Data Limitations

While analyzing the 2023 Bike Share Toronto ridership data, a significant gap was identified:

Annual Member data is missing from August to December 2023.
During this period, all recorded trips are labeled as “Casual Members”, with no entries for annual users. This appears to be a dataset omission rather than a behavioral trend.

As a result:
	
	• All user behavior analysis comparing Casual vs. Annual Members is limited to January through July 2023.
	• Insights beyond July reflect only Casual Member usage and should be interpreted accordingly.

This gap was retained intentionally to preserve dataset integrity and highlight real-world challenges analysts face when working with open data.

---
## 📁 Project Structure
- `data/` — Raw and cleaned datasets
- `scripts/` — Automation for data fetching and cleaning
- `visuals/` — Saved figures and charts

---

## 🔧 Tech Stack

- **Python** (Pandas, Seaborn, Matplotlib, NumPy)

---

## 👨‍💻 Author

Ashutosh Dubal  
🔗 [GitHub Profile](https://github.com/Ashutosh-Dubal)

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
