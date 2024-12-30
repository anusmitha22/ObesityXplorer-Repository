# 🥗 Analyzing the Relationship Between Socioeconomic Factors, Exercise Routines, and Obesity Rates (2018–2023)

## 🚀 Project Overview

This project investigates the correlation between **socioeconomic factors**, **exercise routines**, and **obesity rates** across different age groups and genders from **2018 to 2023**. The goal is to provide insights into obesity trends and inform policy interventions to combat this growing public health challenge.

---

## 🔍 Research Questions

### 📌 Primary Research Question
- How do socioeconomic factors and exercise routines correlate with obesity rates across **age groups** and **genders**, and how have these relationships evolved over time?

### 📌 Secondary Research Questions
- What is the relationship between exercise routines and obesity rates over the years?
- Have socioeconomic disparities in obesity rates widened or narrowed over time?

---

## 📊 Dataset Overview

### 🗂 Initial Dataset
- **Source**: [CDC website](https://data.cdc.gov/)
- **Size**: 104,273 rows
- **Preprocessing**:
  - Removed rows with null values.
  - Retained relevant columns: `YearStart`, `LocationDesc`, `Class`, `Data_Value`, `Sample_Size`, `StratificationCategory1`, `Stratification1`.
  - Filtered data for **2018–2023**.
  - Applied random sampling to create a smaller dataset of **4,082 rows** for ease of analysis.

### 🗂 Final Dataset
- The dataset includes:
  - **YearStart**: Data collection year.
  - **LocationDesc**: Geographic location.
  - **Class**: Data classification (e.g., "Obesity/Weight Status").
  - **Data_Value**: Metric values like obesity rates (percentage).
  - **StratificationCategory1**: Stratifying category (e.g., Age, Income, Gender).
  - **Stratification1**: Detailed stratification value (e.g., specific income brackets).

---

## 🛠 Analysis Process

### 1️⃣ Data Preprocessing
- Filtered records to include years **2018–2023**.
- Removed null values.
- Converted relevant columns to appropriate data types.
- Randomly sampled **4,082 rows** (~10% of the original dataset).

### 2️⃣ Exploratory Data Analysis (EDA)
- **Descriptive Statistics**:
  - Mean obesity rate: **33.72%** across all years.
  - Standard deviation: **±2.43%**.
- **Visualizations**:
  - Line plots for trends over time.
  - Bar charts for obesity rates by income groups.

---

## 📈 Key Findings

### 1️⃣ Obesity Rates Over Time (2018–2023)
- **Overall Trend**: Obesity rates increased from **32.8%** in **2018** to **34.5%** in **2023**.
- **By Gender**:
  - Males: Higher average obesity rate (**34.1%**) compared to females (**33.3%**).
  - Significant variations in females' obesity rates over time.

### 2️⃣ Socioeconomic Factors
- Obesity rates by income group:
  - **Low Income**: Average rate of **35.2%**, peaking at **36.8%** in **2021**.
  - **Middle Class**: Average rate of **34.5%**, the highest among groups, peaking at **37.1%** in **2021**.
  - **Upper Class**: Average rate of **30.4%**, consistently lower across all years.

### 3️⃣ Physical Activity and Obesity
- Exercise rates remained consistently below obesity rates until **2023**, when exercise participation improved and surpassed obesity rates:
  - **2023 Exercise Rate**: **34.8%** (higher than the obesity rate of **34.5%**).

---

## 📂 Tools & Skills
- **Libraries**: `pandas`, `matplotlib`, `seaborn`.
- **Data Manipulation**: Filtering, grouping, and descriptive statistics.
- **Visualization**: Line plots, bar charts.

---

## 🔮 Future Directions
- Investigate qualitative factors influencing exercise habits and obesity.
- Examine regional disparities in obesity trends.
- Extend analysis to include policy impacts and other health indicators.

---

## 🙏 Acknowledgments
Special thanks to **Professor Alex Harding** for guiding me in applying real-world data skills to uncover meaningful insights.

---

