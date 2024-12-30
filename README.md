# Analyzing the Relationship Between Socioeconomic Factors, Exercise Routines, and Obesity Rates (2010-2024)

## Project Overview

This project aims to analyze the correlation between socioeconomic factors, exercise routines, and obesity rates across different age groups and genders over the period from 2018 to 2023. The obesity epidemic is a significant public health concern, and understanding the underlying factors can inform effective interventions and policy decisions. This analysis investigates the following research questions:

### Primary Research Question
- **How do socioeconomic factors and exercise routines correlate with obesity rates across different age groups and genders, and how have these relationships changed over time?**

### Secondary Research Questions
- **What is the relationship between exercise routines and obesity rates over the years?**
- **Have socioeconomic disparities in obesity rates widened or narrowed over time?**

## Initial Dataset 
-The raw dataset, consisting of 104,273 rows, was downloaded from the CDC website and saved on my desktop. It contains various metrics related to obesity and associated socioeconomic factors. 
-To prepare the data for analysis, I undertook a comprehensive preprocessing phase. First, I removed rows containing null values to ensure the integrity and reliability of our analysis. Next, I retained only the relevant columns that would assist in our analysis, specifically focusing on YearStart, LocationDesc, Class, Data_Value, Sample_Size, StratificationCategory1, and Stratification1, while discarding unnecessary columns.
 -Additionally, I filtered the dataset to include only the years from 2018 to 2023, aligning the data with our research objectives. 
 -To manage the dataset's size effectively, I performed "random sampling", selecting 4,082 rows, which represents approximately 10% of the cleaned dataset. -This preprocessing was meticulously documented in a separate Python script to maintain clarity and reproducibility in our analysis workflow. The modified dataset is available in CSV format for further analysis.

## Final Dataset

The dataset used in this analysis contains approximately 4,000 rows, encompassing various aspects related to obesity and physical activity. The key columns include:

- **`YearStart`**: The year during which the data was collected. This is essential for analyzing trends over time.
- **`LocationDesc`**: The geographic location where the data was collected, which can influence socioeconomic factors and health outcomes.
- **`Class`**: The classification of the data point, such as "Obesity / Weight Status" or "Physical Activity." This categorization helps to differentiate between various health metrics.
- **`Data_Value`**: The value associated with the classification, representing metrics like obesity rates (in percentage).
- **`Sample_Size`**: The number of individuals surveyed or data points collected, providing context for the reliability of the data.
- **`StratificationCategory1`**: A category used for stratifying data (e.g., Age, Income, Race/Ethnicity), allowing for a deeper understanding of demographic impacts.
- **`Stratification1`**: The specific stratification value that provides further detail (e.g., income brackets, age groups).

### Data Source
THE DATA IS EXTRACTED FROM " https://data.cdc.gov/" website 

## Analysis Process

### 1. Data Preprocessing
The initial step involved cleaning and preparing the dataset for analysis. This included:
- **Filtering Data**: The dataset was filtered to include only records from the years 2018 to 2023 to focus on recent trends and changes.
- **Handling Missing Values**: Rows with null values were removed to ensure the integrity of the analysis.
- **Data Type Conversion**: Relevant columns were converted to appropriate data types (e.g., categorical variables) to facilitate analysis.
- **Random Sampling**: A random sampling approach was applied to manage the dataset's size to 10% of the total dataset, making it easier to analyze while retaining representativeness.

### 2. Exploratory Data Analysis (EDA)
During EDA, various visualizations were created to gain insights into the dataset's structure and distributions:
- ** Jupyter notebook was created and used foe=r the analysis and and the visualizations.
as step1 , I imported required libraries and then, 
- **Descriptive Statistics**: Summary statistics (mean, median, standard deviation) were calculated for numerical columns to understand overall trends.
- **Visualizations**: Initial plots such as line plots and bar charts were created to identify patterns and outliers in the data.
- **Visual Representations**:  were utilized to visually represent significant correlations, making it easier to identify patterns.

### 4. Time-Series Analysis of Obesity Trends
The analysis included a time-series approach to evaluate trends in obesity rates over the years:
- **Trend Analysis**: Line charts were created to illustrate changes in obesity rates across different demographic groups, highlighting any seasonal patterns or long-term trends.

### 5. Visualization of Key Findings
Comprehensive visualizations were generated to effectively communicate the analysis results:
- **Bar Charts**: Displayed comparisons of obesity rates across various socioeconomic groups.
- **Line Charts**: Illustrated trends over time, emphasizing any significant changes or patterns.
- Highlighted correlation strength among variables, allowing for quick visual insights into the data.

## Key Findings

In this section, summarize the main findings from your analysis. Discuss how socioeconomic factors, exercise routines, and obesity rates are interconnected. Highlight any surprising trends or significant changes over time, particularly in relation to your research questions.

- **Finding 1**:We can see that the average obesity rates have been increasing progressively from 2018- 2023.
- **Finding 2**: Obesity Rates Over Time by Gender: although both genders revealed increase in obesity rates over years, we can observe a significant higher rates of obesity in men than in women which might lead to further research about factors influencing the obesity rates.
- **Finding 3**: When we observe the obesity rates across different sociol-economies,surprisingly, middle economy people has the highest obesity rates over all the years peaking in 2021.
-- **Finding 4**:We also established a relationship between physical activity and obesity rates over time. when we try to correlate these two factors, we can observe that the obesity rates are always higher than the exercising rates. Although, by the year 2023, exercising and physical activity rates have improved and crossed the obesity rate, which indicates a betterment toward health.

## Conclusion

The analysis underscores the complexity of obesity as a public health issue, influenced by a myriad of socioeconomic factors and exercise routines across different genders.Understanding these dynamics is crucial for developing targeted interventions to combat obesity and improve health outcomes across different demographic groups. 

## Future Directions

Based on the findings, suggest potential areas for further research. This could include:
- Analyzing specific demographics or geographic areas that show notable trends.
- Investigating the impact of policy changes on exercise and obesity rates.
- Exploring qualitative factors that may influence exercise habits and health outcomes.

## Acknowledgments

Thanking ALEX HARDING,our professor for helping us to use the skills we learnt from the lectures, and applying with the real time data.  


