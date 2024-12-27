# Exploratory Data Analysis using Python's AutoViz library

lorem ipsum dolor sit amet

## 📑 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Data Description](#️-data-description)
- [Documentation](#-documentation)

## ✨ Features

- 📊 lorem ipsum dolor sit amet
- 📈 lorem ipsum dolor sit amet
- 📉 lorem ipsum dolor sit amet
- 📑 lorem ipsum dolor sit amet

## 🔧 Prerequisites

- Python 3.11.0
- AutoViz library
- Web browser for viewing HTML reports

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/PreProd-Internship/DIY-Python-AutoViz
```

2. Create and activate a virtual environment (recommended). If using Conda:
```bash
conda create -n env_name python==3.11.0 -y
conda activate env_name
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run source/app.py
```

2. Access the web interface at `http://localhost:8501`

3. Upload your CSV dataset and generate the EDA charts and reports!

## 📁 Project Structure

```
DIY-Python-AutoViz/
    ├── data/
    │   └── urban_public_transporation.csv
    ├── source/
    │   ├── app.py
    │   ├── ???.py
    │   └── eda.py
    ├── .gitignore
    ├── LearnWithPrompts.md
    ├── README.md
    └── requirements.txt
```

## 🗃️ Data Description

### urban_public_transporation.csv

A mock dataset generated using [Mockaroo](https://mockaroo.com/) for learning purposes. The `urban_public_transporation.csv` dataset focuses on analyzing the performance of a city's public transportation system, identifying patterns in ridership, and optimizing routes and schedules to improve efficiency and user satisfaction. Each row represents a single bus trip with columns like

- `trip_id`,
- `time_of_day`,
- `bus_id`,
- `weather`,
- `delay`, and so on.

> *Note: `delay` is the target variable (`target_column`) in this dataset. If you'd like, other fields like `number_of_passengers` or `fuel_consumption` could also be explored as alternative target variables for different perspectives.*

### Use Cases in AutoViz:
- 🚍 Visualizing trip performance based on time of day and traffic conditions.
- ⛽ Analyzing fuel efficiency in relation to traffic and weather.
- 🚌 Identifying underperforming routes based on passenger count and delays.
- 🚦 Comparing bus and driver performance to optimize staffing and assignments.
- ⏱️ Analyzing the correlation between delays and trip duration under different conditions.

This dataset and business case provide a rich, real-world scenario that highlights the capabilities of AutoViz.

## 📚 Documentation

For detailed information about the project, please refer to:
- [AutoViz](https://pypi.org/project/autoviz/) - AutoViz library's documentation
- [LearnWithPrompts.md](LearnWithPrompts.md) - Use your favourite LLM to learn more about AutoViz