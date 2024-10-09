from collections import Counter
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics import classification_report, confusion_matrix
from nltk.corpus import wordnet
import category_encoders as ce
import pandas as pd
import numpy as np
import re
import seaborn as sns
import nltk
import matplotlib.pyplot as plt
%matplotlib inline
import warnings

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Suppress all warnings
warnings.simplefilter('ignore')

def categorize_funder(funder):
    """
    Categorizes a funder name into specific groups based on keywords.
    
    Args:
    funder (str): A string representing the name of the funder to categorize.
    
    Returns:
    str: A category name representing the type of organization the funder belongs to.
    
    This function takes a funder name, converts it to lowercase, removes leading/trailing spaces, 
    and categorizes it into predefined groups like 'Government', 'Religious Organizations', 'NGO',
    'International Aid', 'Private Companies', or 'Individual/Other' based on keywords found within the name.
    """
    funder = funder.lower().strip()  # convert to lowercase and strip whitespaces to standardize
    if any(x in funder for x in ['government','ministry','gov','minis']): 
        return 'Government'
    elif any(x in funder for x in ['church', 'muslim','mus', 'islamic','islam','catholic', 'rc']):
        return 'Religious Organizations'
    elif any(x in funder for x in ['ngo', 'foundation', 'fund', 'trust', 'society','socie']):
        return 'NGO'
    elif any(x in funder for x in ['international','internatio', 'un', 'world bank']):
        return 'International Aid'
    elif any(x in funder for x in ['ltd', 'company','compa', 'group', 'enterprise']):
        return 'Private Companies'
    else:
        return 'Individual/Other'

def categorize_installer(installer):
    """
    Categorizes an installer name into specific groups based on keywords.

    Args:
    installer (str): A string representing the name of the installer to categorize.

    Returns:
    str: A category name representing the type of entity the installer belongs to.

    This function processes an installer name by converting it to lowercase and removing
    any leading/trailing whitespace. It categorizes the name into predefined groups such as 
    'DWE', 'Government', 'Community', 'NGO', 'Private Company', 'Institutional', or 'Other' 
    based on specific keywords present in the installer's name. This helps in standardizing 
    installer data for better analysis and insight extraction.
    """
    installer = installer.lower().strip()  # convert to lowercase and strip whitespaces to standardize
    if 'dw' in installer:
        return 'DWE'
    elif any(x in installer for x in ['government', 'govt', 'gove']):
        return 'Government'
    elif any(x in installer for x in ['resource']):
        return 'Other'
    elif any(x in installer for x in ['community', 'villagers', 'village','commu']):
        return 'Community'
    elif any(x in installer for x in ['ngo', 'unicef', 'foundat']):
        return 'NGO'
    elif 'company' in installer or 'contractor' in installer:
        return 'Private Company'
    elif any(x in installer for x in ['school','schoo','church', 'rc']):
        return 'Institutional'
    else:
        return 'Other'
    
def group_scheme_management(value):
    """
    Categorizes scheme management types into broader, more generalized groups.

    Args:
    value (str): A string representing the scheme management type to categorize.

    Returns:
    str: A generalized category name representing the type of scheme management.

    This function takes a specific scheme management type and categorizes it into 
    more generalized groups such as 'Government', 'Community', 'Private Sector', 
    'Water Board', or 'Other'. This categorization aids in simplifying the analysis 
    and understanding of the data by reducing the number of distinct categories, 
    making trends and patterns more discernible.
    """
    if value in ['VWC', 'Water authority', 'Parastatal']:
        return 'Government'
    elif value in ['WUG', 'WUA']:
        return 'Community'
    elif value in ['Company', 'Private operator']:
        return 'Private Sector'
    elif value == 'Water Board':
        return 'Water Board'  # Retain this as a separate category if distinct characteristics are important
    else:
        return 'Other'


def clean_text(text):
    """
    Cleans a text string by converting to lowercase, removing non-alphanumeric characters (excluding numbers),
    and replacing multiple spaces with a single space. If the input is solely numeric, it returns the input as is.

    Args:
    text (str or NaN): The text to be cleaned; can be a string, numeric, or NaN for missing values.

    Returns:
    str or NaN: The cleaned text, with all characters in lowercase, non-alphanumeric characters removed (excluding numbers),
                and multiple spaces collapsed to a single space, or the original text if input was numeric or NaN if input was NaN.

    This function standardizes a text string by making it lowercase, stripping out any characters that are not letters or spaces,
    and then replacing sequences of spaces with a single space, facilitating uniform data processing and analysis. If the input
    is numeric, it is assumed to be standardized already and is returned without modification.
    """
    if pd.isna(text):
        return text
    if isinstance(text, (int, float)):  # Check if the input is numeric
        return text
    text = text.lower()  # Convert to lowercase
    text = ''.join(char for char in text if char.isalpha() or char.isspace())  # Remove special characters and numbers
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text

def analyze_numeric_stats_and_plots(df, columns):
    """
    Calculates and prints descriptive statistics, and generates boxplots and histograms for specified numeric columns in a DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    columns (list): List of numeric column names to analyze.

    The function computes the mean, median, standard deviation, coefficient of variation, skewness,
    kurtosis, and quartiles for the specified columns. It also generates a boxplot and histogram for each column.
    """
    for column in columns:
        if column in df.columns and pd.api.types.is_numeric_dtype(df[column]):
            print(f"Stats for {column}:")
            
            # Calculate statistics
            max_value = df[column].max()
            min_value = df[column].min()
            mean = df[column].mean()
            median = df[column].median()
            std_dev = df[column].std()
            coeff_variation = std_dev / mean if mean != 0 else np.nan
            skewness = df[column].skew()
            kurtosis = df[column].kurtosis()
            quartiles = df[column].quantile([0.25, 0.5, 0.75])
            
            print(f"Max: {max_value}")
            print(f"Min: {min_value}")
            print(f"Mean: {mean}")
            print(f"Median: {median}")
            print(f"Standard Deviation: {std_dev}")
            print(f"Coefficient of Variation: {coeff_variation}")
            print(f"Skewness: {skewness}")
            print(f"Kurtosis: {kurtosis}")
            print(f"25th percentile (Q1): {quartiles[0.25]}")
            print(f"50th percentile (Median): {quartiles[0.5]}")
            print(f"75th percentile (Q3): {quartiles[0.75]}")
            
            # Plotting
            plt.figure(figsize=(12, 6))
            
            # Boxplot
            plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
            sns.boxplot(y=df[column])
            plt.title(f'Boxplot of {column}')
            
            # Histogram
            plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
            sns.histplot(df[column], kde=False, bins=100)
            plt.title(f'Histogram of {column}')
            
            plt.show()
            
def plot_categorical_proportions(df):
    """
    Plots bar charts for each categorical variable in a DataFrame, showing the proportion of each category,
    ordered by proportion in descending order. Each bar is labeled with its percentage value.

    Args:
    df (pd.DataFrame): The DataFrame to analyze.

    This function identifies categorical variables, calculates the proportion of each category, sorts them,
    and plots a bar chart for each categorical variable. Labels on the bars display the percentage proportion of each category.
    """
    # Identifying categorical columns in the DataFrame
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    
    for col in categorical_columns:
        # Calculating proportions
        value_counts = df[col].value_counts(normalize=True).sort_values(ascending=False)
        percentages = value_counts * 100  # Convert proportions to percentages
        
        # Plotting
        plt.figure(figsize=(10, 6))
        ax = percentages.plot(kind='bar')
        ax.set_title(f'Proportion of Categories in {col}')
        ax.set_ylabel('Percentage')
        
        # Adding percentage labels on the bars
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 10), textcoords='offset points')

        plt.show()


def plot_categorical_proportions(df, columns):
    """
    Plots the proportions of categories in specified categorical columns of a DataFrame as bar charts.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        columns (list of str): List of categorical column names to plot.
    """
    for col in columns:
        # Calculating proportions
        value_counts = df[col].value_counts(normalize=True).sort_values(ascending=False)
        percentages = value_counts * 100  # Convert proportions to percentages

        # Plotting
        plt.figure(figsize=(10, 6))
        ax = percentages.plot(kind='bar')
        ax.set_title(f'Proportion of Categories in {col}')
        ax.set_ylabel('Percentage')

        # Adding percentage labels on the bars
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 10), textcoords='offset points')

        plt.show()
        
def plot_grouped_charts(df, status_col, cols):
    """
    Creates combined plots for each column in the DataFrame based on their data type, grouped by a specified status column.
    For numeric columns, histograms for all statuses are combined in one plot, and boxplots for all statuses are combined in another.
    For categorical columns, grouped bar charts are created.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        status_col (str): The name of the column to group data by.
        cols (list of str): List of column names to plot, both categorical and numerical.
    """
    unique_statuses = df[status_col]. unique()
    colors = plt.get_cmap('tab10')  # Fetches a colormap with distinct colors

    for col in cols:
        if df[col].dtype in ['int64', 'float64']:  # Numeric Columns
            plt.figure(figsize=(12, 6))
            
            # Histogram for all statuses
            for i, status in enumerate(unique_statuses):
                sns.histplot(df[df[status_col] == status][col], kde=True, element='step', 
                             stat='density', label=str(status), color=colors(i))
            
            plt.title(f'Combined Histogram of {col} by {status_col}')
            plt.legend(title=status_col)
            plt.show()
            
            # Boxplot for all statuses
            plt.figure(figsize=(12, 6))
            sns.boxplot(x=status_col, y=col, data=df, palette='tab10')
            plt.title(f'Combined Boxplot of {col} by {status_col}')
            plt.show()
        
        elif df[col].dtype == 'object':  # Categorical Columns
            plt.figure(figsize=(10, 6))
            sns.countplot(data=df, x=status_col, hue=col)
            plt.title(f'Grouped Bar Chart of {status_col} by {col}')
            plt.ylabel('Count')
            plt.xlabel(status_col)
            plt.legend(title=col, loc='upper right')
            plt.xticks(rotation=45)
            plt.show()


def generate_proportion_contingency_tables(df, status_col, categorical_cols):
    """
    Generates two-way contingency tables of proportions for the specified status column against a list of provided categorical columns in the DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        status_col (str): The column name to use as one axis of the contingency tables, typically representing different statuses.
        categorical_cols (list of str): List of categorical column names to include in the contingency tables.
    
    Returns:
        dict: A dictionary of pandas DataFrame objects where each key is the column name and the value is the corresponding contingency table as proportions.
    """
    tables = {}
    for col in categorical_cols:
        if col != status_col:  # Ensure the status column is not included in the analysis
            # Compute the contingency table with proportions normalized over all rows
            contingency_table = pd.crosstab(df[status_col], df[col], normalize='index')
            contingency_table_df = pd.DataFrame(contingency_table)
            contingency_table_df = contingency_table_df.round(4) * 100  # Convert proportions to percentages and round off
            tables[col] = contingency_table_df
    
    return tables