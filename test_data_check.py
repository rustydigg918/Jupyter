import pandas as pd
import numpy as np

def check_data_quality(df):
    """
    Perform data quality checks on a pandas DataFrame.
    Returns a dictionary containing the results of each check.
    """
    
    # Initialize an empty dictionary to store the results of each check
    results = {}
    
    # Check 1: Missing values
    missing_values = df.isnull().sum()
    results['missing_values'] = missing_values
    
    # Check 2: Duplicate rows
    duplicate_rows = df.duplicated().sum()
    results['duplicate_rows'] = duplicate_rows
    
    # Check 3: Outliers
    outlier_columns = df.select_dtypes(include=np.number).columns
    outliers = {}
    for col in outlier_columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers[col] = df[(df[col] < lower_bound) | (df[col] > upper_bound)].shape[0]
    results['outliers'] = outliers
    
    # Check 4: Data types
    data_types = df.dtypes
    results['data_types'] = data_types
    
    # Check 5: Invalid values
    invalid_values = {}
    for col in df.columns:
        unique_values = df[col].unique()
        if len(unique_values) == 1:
            invalid_values[col] = unique_values[0]
    results['invalid_values'] = invalid_values
    
    # Check 6: Date ranges
    date_columns = df.select_dtypes(include=np.datetime64).columns
    date_ranges = {}
    for col in date_columns:
        min_date = df[col].min()
        max_date = df[col].max()
        date_ranges[col] = {'min_date': str(min_date), 'max_date': str(max_date)}
    results['date_ranges'] = date_ranges
    
    # Check 7: Cardinality
    cardinality = {}
    for col in df.columns:
        num_unique = df[col].nunique()
        cardinality[col] = num_unique
    results['cardinality'] = cardinality
    
    # Check 8: Categorical values
    categorical_columns = df.select_dtypes(include='object').columns
    categorical_values = {}
    for col in categorical_columns:
        unique_values = df[col].unique()
        categorical_values[col] = unique_values
    results['categorical_values'] = categorical_values
    
    # Check 9: Numeric values
    numeric_columns = df.select_dtypes(include=np.number).columns
    numeric_values = {}
    for col in numeric_columns:
        numeric_values[col] = df[col].describe().to_dict()
    results['numeric_values'] = numeric_values
    
    # Check 10: Text length
    text_columns = df.select_dtypes(include='object').columns
    text_lengths = {}
    for col in text_columns:
        text_lengths[col] = df[col].str.len().describe().to_dict()
    results['text_lengths'] = text_lengths
    
    # Check 11: Correlations
    correlations = df.corr()
    results['correlations'] = correlations
    
    # Check 12: Skewness
    skewness = df.skew()
    results['skewness'] = skewness
    
    # Check 13: Kurtosis
    kurtosis = df.kurtosis()
    results['kurtosis']
