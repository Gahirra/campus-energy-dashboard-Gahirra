# campus-energy-dashboard-Gahirra

This project reads electricity usage data from buildings and creates a simple dashboard and summary report.
# Features
- Reads all CSV files from the /data/ folder
- Cleans and merges them into one dataset
- Calculates daily and weekly electricity usage
- Creates building-wise summaries
- Generates three matplotlib charts in one image
- Saves cleaned data and report

## Tools Used
- Python
- Pandas
- Matplotlib

## Files Generated
- cleaned_energy_data.csv
- building_summary.csv
- dashboard.png
- summary.txt

## How to Run
1. Place your data CSV files inside the /data/ folder
2. Run: `python main.py`
