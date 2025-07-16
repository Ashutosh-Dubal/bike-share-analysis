#!/bin/bash

# Run the full Toronto Bike Share analysis pipeline

echo "🔄 Step 1: Cleaning raw data..."
python3 src/clean_data.py || { echo "❌ Failed at clean_data.py"; exit 1; }

echo "📊 Step 2: Running Exploratory Data Analysis..."
python3 src/EDA.py || { echo "❌ Failed at EDA.py"; exit 1; }

echo "⏱️ Step 3: Running Trip Duration Analysis..."
python3 src/trip_duration_analysis.py || { echo "❌ Failed at trip_duration_analysis.py"; exit 1; }

echo "📍 Step 4: Analyzing Station Imbalance..."
python3 src/station_imbalance.py || { echo "❌ Failed at station_imbalance.py"; exit 1; }

echo "🔗 Step 5: Performing Cluster Analysis..."
python3 src/cluster_analysis.py || { echo "❌ Failed at cluster_analysis.py"; exit 1; }

echo "🗺️ Step 6: Generating Spatial Maps..."
python3 src/spatial_analysis.py || { echo "❌ Failed at spatial_analysis.py"; exit 1; }

echo "✅ All steps completed successfully!"