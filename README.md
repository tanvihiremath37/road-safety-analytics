Road Safety Analytics System

1. Introduction

This project presents an end-to-end data analytics pipeline designed to analyze road accident data and extract actionable insights. It integrates data generation, processing, storage, querying, and visualization to support data-driven decision-making in road safety analysis.

The system leverages Python for data generation and ETL, MySQL for structured storage and querying, and Power BI for interactive visualization.

2. Objectives

The primary objectives of this project are:

* To design a structured pipeline for handling accident-related data
* To analyze accident patterns across cities, conditions, and severity levels
* To identify high-risk scenarios and geographic hotspots
* To present insights through an interactive dashboard for non-technical stakeholders



3. Technology Stack

| Component       | Technology Used           |
| --------------- | ------------------------- |
| Data Generation | Python (Pandas, Random)   |
| ETL Pipeline    | Python                    |
| Database        | MySQL                     |
| Data Modeling   | SQL (Views, Aggregations) |
| Visualization   | Power BI                  |

4. System Architecture

Raw Data (Synthetic Generation)
* Python ETL Pipeline
* MySQL Database
* SQL Queries & Views
* Power BI Dashboard

5. Dataset Description

The dataset is synthetically generated to simulate realistic road accident scenarios. It incorporates domain-informed logic to reflect real-world patterns such as increased severity during nighttime and adverse road conditions.

Key Features:

* accident_id
* date, time
* city
* area_type (Urban / Rural / Highway)
* vehicle_type
* road_condition (Dry / Wet / Damaged)
* light_condition (Day / Night)
* vehicles_involved
* severity (Minor / Serious / Fatal)
* latitude, longitude

6. Data Processing (ETL)

The ETL pipeline performs:

* Data generation with realistic constraints and distributions
* Feature engineering (e.g., severity classification based on multiple factors)
* Data cleaning and structuring
* Loading into MySQL using SQLAlchemy

7. Database Design

The processed data is stored in a MySQL database (`road_safety_db`) with the primary table:

*accidents

Contains all accident records with structured attributes.

*risk_analysis (SQL View)

A derived view used for analytical purposes:

* Encapsulates business logic for risk classification
* Enables simplified querying for high-risk scenarios
* Improves modularity and reusability of queries


8. Key Analytics Performed

* Total accident count across dataset
* Severity distribution (Minor, Serious, Fatal)
* Identification of high-risk cases (Serious + Fatal)
* City-wise accident comparison
* Geospatial hotspot detection using latitude and longitude
* Condition-based analysis (road, lighting, vehicle type)


9. Dashboard Overview (Power BI)

The Power BI dashboard provides:

Key Performance Indicators

* Total Accidents
* Fatal Accidents
* High-Risk Cases

 Visualizations

* Severity distribution (pie chart)
* Accidents by city (bar chart)
* Accident hotspots (map visualization)

Interactivity

* Filters (slicers) for city and severity
* Tooltips for contextual data exploration



10. Key Insights

* Accidents are concentrated in major urban centers
* Serious and fatal cases constitute a significant portion of total incidents
* High-risk conditions are associated with adverse environments and peak activity periods
* Geospatial visualization highlights clear accident clusters (hotspots)


11. Setup Instructions

Prerequisites

* Python 3.x
* MySQL Server
* Power BI Desktop

Steps

1. Install dependencies:
   pip install -r requirements.txt

2. Generate dataset: 
   python scripts/generate_data.py
  

3. Run ETL pipeline:
   python scripts/db_pipeline.py
  

4. Open Power BI dashboard:

   * Load `.pbix` file
   * Connect to MySQL database if required

13. Future Enhancements

* Integration with real-time traffic and accident data sources
* Incorporation of weather and environmental datasets
* Predictive modeling for accident risk using machine learning
* Deployment of dashboard as a web-based application

14. Conclusion

This project demonstrates the design and implementation of a complete data analytics workflow, combining data engineering, database management, and business intelligence. It highlights the ability to transform raw data into meaningful insights and deliver them through interactive visualizations.