# 🚲 Toronto Bike Share Ridership Analysis

This project analyzes ridership patterns of Toronto’s public bike-sharing system using open data provided by the City of Toronto.

Through exploratory data analysis (EDA), trip duration breakdowns, clustering, and spatial usage analysis, we aim to uncover user behavior trends, system usage hotspots, and potential operational challenges.

The analysis leverages:

- Pandas for data cleaning and transformation

- Seaborn and Matplotlib for visualizing patterns and trends.

- Folium for interactive, map-based visualizations

Our findings highlight key usage patterns across neighborhoods, reveal imbalances in bike flows between stations, and offer insights into how Toronto’s bike share system can improve efficiency and meet rider demand.

---

## 📚 Table of Contents
1. [Dataset Description](https://github.com/Ashutosh-Dubal/bike-share-analysis/tree/main?tab=readme-ov-file#-dataset-description)
2. [Challenges & Learnings](https://github.com/Ashutosh-Dubal/bike-share-analysis/tree/main?tab=readme-ov-file#-challenges--learnings)
3. [How to Install and Run the Project](https://github.com/Ashutosh-Dubal/bike-share-analysis?tab=readme-ov-file#%EF%B8%8F-how-to-install-and-run-the-project)
4. [How to Use the Project](https://github.com/Ashutosh-Dubal/bike-share-analysis?tab=readme-ov-file#-how-to-use-this-project)
5. [Sample Output](https://github.com/Ashutosh-Dubal/bike-share-analysis?tab=readme-ov-file#-sample-output)
6. [Key Insights & Analysis](https://github.com/Ashutosh-Dubal/bike-share-analysis/tree/main?tab=readme-ov-file#-key-insights--analysis)
7. [Tech Stack](https://github.com/Ashutosh-Dubal/bike-share-analysis/tree/main?tab=readme-ov-file#-tech-stack)
8. [Project Structure](https://github.com/Ashutosh-Dubal/bike-share-analysis/tree/main?tab=readme-ov-file#-project-structure)
9. [Author](https://github.com/Ashutosh-Dubal/bike-share-analysis?tab=readme-ov-file#-author)
10. [License](https://github.com/Ashutosh-Dubal/bike-share-analysis?tab=readme-ov-file#-license)

---

## 📦 Dataset Description

This project uses open data from the City of Toronto Open Data Portal, focusing on Bike Share Toronto ridership data for the year 2023.

The dataset includes over ~5,000,000 anonymized trip records, each representing a single ride within the city’s bike share system.

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

One of the primary challenges was handling inconsistencies and unexpected issues in the raw dataset:
- Files were provided in mixed formats (ZIP, CSV, XLSX) with varying character encodings.
- Some CSVs contained malformed headers (e.g., ï»¿trip_id) due to encoding artifacts.
- Several months lacked complete data — notably, Annual Member records were missing from August to December 2023.
- Opening the full dataset in a spreadsheet tool like Excel was not feasible, as it exceeded Excel’s row limit (1,048,576 rows), forcing all validation and inspection to be done in Python. This was a shift in workflow and required new habits for spotting issues like NaN values or formatting errors programmatically.

These challenges underscored the importance of robust data validation, fallback plans, and adaptability when working with real-world open data.

### 🧱 2. Handling Missing and Incomplete Data

This project involved more than just removing NaN values:
- Over 1.1 million records were missing critical fields like start_station_name, end_station_id, or end_station_name. Instead of discarding them, I attempted to reconstruct the data using a station ID-to-name mapping dictionary. This experiment didn’t work as expected, but it taught me the value of data recovery attempts before dropping rows. I’ll be trying alternative strategies in future projects.
- Station coordinate data was retrieved using an API, but this presented problems too — about 25% of the stations had missing coordinates, and some had inaccurate results. I manually corrected these errors and filled in the missing locations.

If you’re planning to reuse this project, I recommend keeping the cleaned station coordinate sheet as-is — it’s been manually verified for accuracy.
- The absence of Annual Member data after July 2023 is not a behavioral pattern but likely a reporting omission. This greatly limits any analysis split by user type, especially for the second half of the year.

All user-type-based insights are based on data from January to July and should be interpreted with caution.
- I initially planned to do the project for 2024, but data for the second half of that year was not available, which led me to focus on 2023.

### 🗂 3. Managing Large Volumes of Data

The dataset contains over 5 million rows, making performance and memory management key concerns:
- Only relevant columns were retained throughout processing.
- Outlier trips over 2 hours were excluded to reduce skew.
- Efficient use of Pandas, modular script design, and batch processing helped ensure that data transformations remained performant on a local machine.

### 📊 4. Data Visualization and Storytelling

Visualization in this project wasn’t just about pretty charts — it was about making the data speak:
- I compared trip timing patterns and asked why 8 AM rides were lower than 5 PM, despite both being rush hours.
- Identified hotspots like Bay St & College St and Union Station using frequency analysis and heatmaps.
- Analyzed Casual vs. Annual Member behavior across multiple dimensions — trip duration, daily patterns, and monthly trends.

### 🗺️ 5. First-Time Use of Folium & Spatial Tools

This was my first deep dive into Folium, and it ended up being one of the most exciting parts of the project:
- Learning how to generate interactive maps, heatmaps, and colored marker clusters took time and trial/error.
- I experimented with color gradients to better highlight importer vs. exporter stations, and added the Spatial Analysis section to explore these further.
- Visualizing net flow and usage intensity via Folium gave the project a whole new dimension — making the findings more accessible and engaging.

### ⚠️ 6. Data Limitations & Integrity

Real-world datasets aren’t perfect, and this one was no exception:
- The missing Annual Member data after July 2023 skews the member vs. casual user distribution and may underrepresent commuting behavior.
- Rather than dropping those months, I retained them to keep the full context of the system’s usage and used explicit caveats throughout the analysis.

This project reflects a key lesson in balancing data integrity with storytelling — sometimes it’s more valuable to highlight limitations than to force completeness.

---

## 🛠️ How to Install and Run the Project


Follow these steps to set up and run the Toronto Bike Share project:

### 1. Clone the Repository

```bash
git clone https://github.com/Ashutosh-Dubal/bike-share-analysis.git
cd bike-share-analysis
```

### 2. (Optional) Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Project Pipline

Use the provided shell script to execute the full project pipeline — from data cleaning to analysis and visualizations — in a single step:

```bash
bash run_pipeline.sh
```

This script will sequentially run the following components:
- fetch_data.py: Downloads the raw dataset from the City of Toronto
- clean_data.py: Cleans and processes the data
- EDA.py: Performs exploratory data analysis
- trip_duration.py: Analyzes trip durations by user type
- station_imbalance.py: Examines net flows at each station
- cluster_analysis.py: Clusters stations using KMeans
- spatial_usage.py: Generates heatmaps and usage maps

### 5. View Visualizations

- Generated plots are saved in the visuals/ directory.
- Folium-based interactive maps are saved as .html files and can be opened in any web browser.

---

## 📦 How to Use This Project

Once you’ve run the full pipeline (fetch_data.py → clean_data.py → EDA.py → trip_duration.py → station_imbalance.py → cluster_analysis.py → spatial_usage.py), the project will:

- Generate a cleaned dataset at data/processed/bikeshare_2023_combined.csv

- Create multiple visualizations in the visuals/ folder, including:
  - User type distribution and daily ride activity
  - Ride duration trends
  - Station cluster maps (using Folium)
  - Heatmaps and net flow diagrams of bike usage
  
- Help you analyze bike-sharing patterns in Toronto by examining:
  - Downtown vs. Suburban usage
  - Station-level imbalances (import vs. export hotspots)
  - Clusters of station locations and demand zones

You can explore or extend the analysis by modifying any of the scripts under scripts/ — for example:
	
- Add new clustering methods (e.g. DBSCAN)
- Refine net flow thresholds or colormap styling
- Add support for additional years of data

---

## 📊 Sample Output

Below are examples of the key outputs generated by this project:

✅ Cleaned Dataset
- data/processed/bikeshare_2023_combined.csv: Contains cleaned and merged trip data with normalized station names and resolved missing values.
- data/processed/stations_with_coords_clean.csv: Cleaned list of station names with corresponding latitude and longitude coordinates.
- data/processed/station_clusters_all_k.csv: Cluster assignments for all stations across different values of k (used in KMeans analysis).

📈 Visualizations

All visual outputs are saved in the visuals/ folder:
- **EDA**:
  - top_10_routes.png: Breakdown of casual vs. annual members. 
  - top_start_stations.png: Daily ridership patterns throughout the year.
  - trip_duration_dist.png: Histogram showing the distribution of trip durations, revealing how long most bike trips typically last.
  - trips_by_day_user_type.png: Bar chart showing daily ridership split by user type (Casual vs. Annual), highlighting user behavior patterns.
  - trips_by_day.png: Bar chart of total daily bike trips throughout the year, showing overall demand and seasonal trends.
  - trips_by_hour_user_type.png: Bar chart showing peak riding hours broken down by user type, useful for identifying commuting vs. recreational usage.
  - trips_by_hour.png: Bar chart showing the volume of trips for each hour of the day, identifying general peak usage times.
  - trips_by_month_user_type.png: Bar chart comparing monthly ridership trends across user types to reveal seasonal engagement differences.
  - trips_by_month.png: Bar chart showing how total trips change across months, indicating seasonal trends in ridership.
  - user_type_breakdown.png: Bar chart showing the proportion of Casual vs. Annual members, providing insight into user demographics.

- **Trip Duration**:
  - trip_duration_histogram.png: Distribution of ride durations with filtering for outliers.
  - avg_trip_duration_by_day_user.png: Bar chart showing the average trip duration per day for each user type, highlighting how usage behavior differs over time.
  - trip_duration_boxplot_usertype.png: Boxplot comparing trip duration distributions across user types, useful for spotting differences in variability and outliers.
  - trip_duration_kde_usertype.png: KDE (kernel density estimate) plot visualizing the distribution of trip durations by user type, giving a smooth comparison of usage patterns.
   
- **Station Imbalance**:
  - top_station_importers.png:  
  - top_station_exporters.png: 

- **Cluster Analysis**:
   - clusters_k5_styled.html, clusters_k7_styled.html: Interactive Folium maps showing station clusters for different values of k.
   - elbow_method_using_inertias.png: Plot of inertia values across different cluster counts to identify the optimal number of clusters using the Elbow Method.
   - silhouette_score.png: Plot of silhouette scores for various cluster counts, helping evaluate how well-separated and cohesive the clusters are.

- **Spatial Analysis**:
  - net_flow_distribution.png: Histogram showing the distribution of net bike flow (starts − ends) across stations to highlight imbalances.
  - net_flow_map.html: nteractive Folium map with color-coded stations based on net flow — red for exporters, blue for importers, and purple for balanced.
  - station_usage_heatmap.html: Heatmap displaying station activity intensity based on the total number of trips (starts + ends), giving a visual sense of demand hotspots.

These outputs give a rich understanding of how Toronto’s bike share system is used — both spatially and behaviorally.

---

## 👁 Key Insights & Analysis

### 📊 Exploratory Data Analysis (EDA)

#### 🔝 Top Stations: Where People Ride Most

The most frequently used station was Bay St & College St (East Side). Its popularity stems from its location near the University of Toronto, Eaton Centre, and numerous office towers and medical buildings. Well-integrated with bike lanes and transit (College subway station), it serves both students and professionals with high foot traffic throughout the day.

Other high-traffic locations include:

- York St & Queens Quay W — a scenic waterfront station near Union Station, popular among both commuters and tourists.
- Union Station — although it’s the city’s busiest transit hub, it ranked third. This may be because many riders walk from Union to nearby destinations or avoid biking in the heavily congested Front Street area.

#### 📅 Ridership by Day: The Hybrid Work Effect

Ridership peaks on Tuesdays, Wednesdays, and Thursdays, reflecting a midweek commuting trend consistent with hybrid work schedules. Mondays and Fridays show lower usage, possibly due to flexible remote work and extended weekends.

#### ⏰ Peak Usage Window Analysis

Hourly trip data reveals a clear bimodal distribution, with significant spikes at:
- 8 AM — Morning commutes
- 5 PM — Evening commutes

Interestingly, the 5 PM peak is significantly higher. This suggests that:
- In the morning, riders are more time-sensitive and may prefer predictable transit options (e.g., TTC, GO).
- Evening trips are more flexible, often used for leisure, errands, or social activities.
- Casual riders and tourists contribute heavily to the afternoon traffic.

This has practical implications for operations:

> 📌 Bike redistribution efforts should focus on ensuring availability in the late afternoon and freeing up docks before the evening rush.

#### 👥 Who Uses the System?

In 2023:
- Casual users took nearly ~4,000,000 trips
- Annual members accounted for only ~500,000 trips

This points to Bike Share Toronto being used more for occasional or leisure purposes than daily commuting. It suggests:
- High usage by tourists, infrequent riders, and weekend explorers
- Opportunity to increase adoption by annual users through improved coverage and membership incentives

#### 🔁 Trip Patterns: Loops and Leisure

Many of the most common trips were looped routes, starting and ending at the same station — especially in scenic areas like Queens Quay, Tommy Thompson Park, and Martin Goodman Trail.

This emphasizes the recreational nature of many trips, particularly among casual riders and tourists.

### ⏱️ Trip Duration Analysis

Trip duration offers insight into how users interact with the system — whether for quick errands or leisurely rides. Breaking this down by user type reveals distinct usage behaviors.

> Note: All trip durations are capped at 120 minutes to remove outliers.

Most trips are under 20 minutes, suggesting that quick commutes and short errands are the primary use cases for Bike Share Toronto.

When we break down trip durations by user type, a clearer pattern emerges (see trip_duration_boxplot_usertype.png and trip_duration_kde_usertype.png):
- Annual members show a tight distribution of shorter trips, reflecting regular, utilitarian use — likely for commuting or quick errands.
- Casual users, on the other hand, have a broader spread of durations. Their rides tend to be longer and more varied, which points to recreational or scenic usage, such as rides around Tommy Thompson Park or Centre Island.

The median trip duration for casual users is slightly higher than that of annual members, reinforcing the idea that casual riders are less time-constrained and use the system more for leisure or tourism. In contrast, annual members rely on the bikes for routine, time-efficient travel.

We also observe a weekend spike in casual ridership, aligning with leisure activity patterns. Annual member usage remains steady throughout the week, consistent with regular commuting habits.

### 🔄 Station Imbalance Insights: Comparing Exporters vs. Importers

In analyzing station-level imbalances—where significantly more trips either start or end at a location—we found that **importer stations** (where more trips end than begin) often reveal deeper insights into rider behavior and system stress points than exporters.

#### 📥 Importer Stations: Where Trips End

- **Key examples**: King St W / Bay St, Union Station, and York St / Queens Quay W.
- These highlight **commute destinations**, especially in the **Financial District** and at major **transit hubs**.
- Their usage patterns suggest strong **multi-modal travel**, where users bike to these hubs and continue by foot, subway, or GO Transit.
- Operationally, these stations often face **dock saturation**, especially during the **morning rush**, frustrating users trying to end trips.

#### 📤 Exporter Stations: Where Trips Begin

- **Key examples**: Bay St / Wellesley St W, Sherbourne St / Wellesley St E, and Spadina Ave / Sussex Ave.
- Typically located in **residential areas**, these stations see **early morning demand** as people begin their commutes.
- They signal where **bike availability must be ensured**, calling for overnight or early-morning **rebalancing efforts**.

#### 🧠 Why Importers May Offer Deeper Insights

While both exporter and importer stations are valuable for understanding flow patterns:

- **Importers** better identify **workplaces**, **transit intersections**, and **high-demand destinations**.
- They expose stations under stress due to **limited dock capacity**.
- Trends such as **short-distance travel to Billy Bishop Airport** become clearer through import-heavy locations.

Taken together, exporters and importers offer a **complementary view** of how Toronto moves — supporting smarter **fleet management**, **dock planning**, and **urban mobility improvements**.

### 🧠 Cluster Analysis: Segmenting Toronto’s Bike Share Network

To better understand spatial patterns in station usage, we used K-Means clustering to group stations into geographic segments.

We applied K-Means clustering to group stations based on their geographic coordinates, running the algorithm for k = 4 through k = 12. Each run uses KMeans++ initialization, repeated 12 times to select the solution with the lowest inertia (distortion score).

To identify the optimal number of clusters, we generated:
- Elbow Plot: Shows the rate of inertia decline as k increases. While helpful, the plot did not yield a clearly defined “elbow.”
- Silhouette Score Plot: Revealed peaks at k = 5 and k = 7, suggesting that those values may best capture naturally forming groups.

We focused our analysis on k = 5, which produced distinct clusters aligned with key geographic and functional areas in Toronto.

#### 📍 Cluster Interpretation: Understanding Toronto’s Station Segments

While most clusters are concentrated in downtown Toronto, a number of distinct groups emerged in North York and Scarborough. At first glance, these may appear as outliers, but their presence reflects intentional planning and localized demand.

1. Transit Hubs & Connectivity

Many stations in outlying areas are near GO Train stations, TTC subway terminals, or major bus corridors. These act as first-mile/last-mile connections, enabling commuters to reach the core network efficiently.

2. Equity & Expansion Zones

Bike Share Toronto has prioritized expansion into underserved neighborhoods through equity-focused initiatives. These stations may be newer, have lower density, or be part of pilot programs, but they fill critical gaps in the city’s active transportation grid.

3. Recreational Corridors

Some clusters align with scenic or parkland areas — like Tommy Thompson Park, Downsview Park, or Rouge National Urban Park. These attract seasonal and weekend users, explaining their unique demand patterns.

4. Campus-Driven Clusters

Institutions such as York University and UTSC show enough localized, recurring ridership to form standalone clusters. Their internal demand loops make them operationally distinct from commuter-heavy downtown stations.

#### 🔍 Key Takeaway

While downtown clusters reflect dense, interconnected commuter flows, peripheral clusters in North York and Scarborough highlight self-contained ecosystems shaped by:
- Geographic isolation
- Unique land use (parks, campuses)
- Policy-driven expansion

Understanding these clusters allows Bike Share Toronto to tailor station design, rebalancing strategies, and marketing efforts based on how riders use the system in different parts of the city.

### 🌍 Spatial Analysis

To visualize how station usage varies across the city, we mapped activity hotspots, net flows, and regional patterns.

#### 🗺️ Station Usage Patterns

As expected, downtown Toronto dominates the map in terms of bike share activity. The central business district, the University of Toronto’s St. George campus, and dense transit access all contribute to this high volume.

An interesting observation is the cluster of active stations near the waterfront, especially around Queens Quay and Tommy Thompson Park. These are likely driven by recreational riding, particularly in warmer months when biking along the lake becomes a popular leisure activity.

#### ⚖️ Import/Export Balance Map

In our net flow visualization, we observed:
	•	A deep red core at Union Station and Bay/College — importer stations, where more trips end than begin.
	•	A few blue outer stations, indicating exporter locations, typically in residential zones or campuses.
	•	However, most stations are purple, suggesting a well-balanced system, with similar numbers of starts and ends.

This balance supports the idea that a significant portion of trips are circular in nature — where the rider begins and ends at the same or nearby location — especially in recreational zones.

#### 📊 Net Flow Distribution

The net_flow_distribution.png chart shows a relatively tight, centered distribution around zero, meaning:
	•	Most stations have balanced inflow and outflow.
	•	There are few extreme outliers, such as Union Station (importer) or residential feeder stations (exporters).
	•	This indicates that Bike Share Toronto is already doing well with natural self-balancing, reducing the operational strain of constant manual bike rebalancing.

#### 📍 Location-Based Usage Patterns: Downtown vs. Suburban Analysis

The bike share system in Toronto exhibits a strong downtown-centric usage pattern. As shown in the summary below, over 99% of all ride activity occurs within stations classified as “Downtown.” Suburban stations, while present in areas like North York, Scarborough, and Etobicoke, account for less than 0.3% of total activity.

| **Location Type** | **Starts**  | **Ends**  | **Total Activity**|
| ----------------- | ----------- | --------- | ----------------- |
| Downtown          | 5,099,883   | 5,098,005 | 10,197,888        |
| Suburban          | 15,752      | 14,169    | 29,921            |

This pattern suggests that the bike share system is heavily optimized for short-distance, urban commutes and errands. The balance of starts and ends downtown indicates strong local circulation. In contrast, suburban stations may serve longer, more directional commutes and might benefit from better integration with transit or more station density.

### 🔍 Final Takeaway

Bike Share Toronto is a downtown-driven system, primarily used for short, flexible trips by Casual Users. However, the growing reach into suburban neighborhoods, combined with diverse usage patterns—like commuting, recreation, and transit connectivity—highlights both its versatility and potential for targeted expansion.

### 📊 Summary Table

|**Metric**                 | **Insight**                                                  |
|-------------------------- |------------------------------------------------------------- | 
|Most Active Station        | Bay St & College St - high accessibility & mixed land use    |
|Peak Usage Time            | 5 PM (more flexible/leisure-based trips)                     |
|Casual vs. Member Split    | ~4M casual vs. ~0.5M annual - mostly tourist/recreational use|
|Avg Trip Duration (Casual) | Longer, more varied                                          |
|Avg Trip Duration (Member) | Shorter, tight distribution - commuting/errands              |
|Importer Station Example   | Union Station, York/Queens Quay W                            |
|Exporter Station Example   | Sherbourne/Wellesley                                         |
|Downtown Usage Share       | Over 99% of all trips                                        |
|Suburban Activity          | <0.3% of trips - potential growth area                       |

---

## 🔧 Tech Stack

- **Python** (Pandas, Seaborn, Matplotlib, NumPy, Folium)
- **HTML** (For Folium maps)

---

## 📁 Project Structure

```
toronto-bike-share-analysis/
├── data/
│   ├── raw/                      # Original raw CSVs from Open Toronto
│   └── processed/                # Cleaned & engineered datasets
│      ├── cleaned_trip_data.csv
│      ├── stations_with_coords_clean.csv
│      └── station_clusters_all_k.csv
│
├── visuals/                      # Generated plots and charts
│   ├── EDA/
│   ├── trip_duration/
│   ├── station_imbalance/
│   ├── cluster/
│   └── spatial/
│
├── src/                          # Main Python scripts
│   ├── fetch_data.py
│   ├── clean_data.py
│   ├── EDA.py
│   ├── trip_duration_analysis.py
│   ├── station_imbalance.py
│   └── cluster_analysis.py
│
├── requirements.txt              # Required Python packages
├── run_pipeline.sh               # Optional shell script to run the full analysis
├── README.md                     # Project documentation (you are here!)
└── .gitignore                    # Files and folders to ignore in version control
```
---

## 👨‍💻 Author

Ashutosh Dubal  
🔗 [GitHub Profile](https://github.com/Ashutosh-Dubal)

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
