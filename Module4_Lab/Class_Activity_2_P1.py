import pandas as pd
import numpy as np

def clean_mushroom_dataset(file_path, method='rows', threshold=0.5):
    """
    Clean mushroom dataset by removing rows or columns with missing values.

    Parameters:
    file_path (str): Path to the mushroom dataset CSV file
    method (str): 'rows' to remove rows with missing values,
                  'columns' to remove columns with missing values,
                  'both' to remove both rows and columns
    threshold (float): For method='both', fraction of missing values to trigger column removal

    Returns:
    pandas.DataFrame: Cleaned dataset
    """

    # Load the dataset
    print("Loading mushroom dataset...")

    # Define column names for the mushroom dataset (UCI standard)
    column_names = [
        'class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
        'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
        'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
        'stalk-surface-below-ring', 'stalk-color-above-ring',
        'stalk-color-below-ring', 'veil-type', 'veil-color',
        'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat'
    ]

    try:
        # Read the CSV file
        df = pd.read_csv(file_path, header=None, names=column_names)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

    # Replace '?' with NaN for proper missing value handling
    df = df.replace('?', np.nan)

    print(f"Original dataset shape: {df.shape}")
    print(f"Total missing values: {df.isnull().sum().sum()}")

    # Show missing values per column
    missing_per_column = df.isnull().sum()
    if missing_per_column.sum() > 0:
        print("\nMissing values per column:")
        for col, count in missing_per_column.items():
            if count > 0:
                percentage = (count / len(df)) * 100
                print(f"  {col}: {count} ({percentage:.2f}%)")
    else:
        print("\nNo missing values found in the dataset!")

    # Create a copy for cleaning
    df_cleaned = df.copy()

    if method == 'rows':
        # Remove rows with any missing values
        df_cleaned = df_cleaned.dropna()
        print(f"\nCleaning method: Removing rows with missing values")

    elif method == 'columns':
        # Remove columns with any missing values
        df_cleaned = df_cleaned.dropna(axis=1)
        print(f"\nCleaning method: Removing columns with missing values")

    elif method == 'both':
        # First remove columns with high percentage of missing values
        missing_percentages = df_cleaned.isnull().sum() / len(df_cleaned)
        columns_to_drop = missing_percentages[missing_percentages > threshold].index

        if len(columns_to_drop) > 0:
            print(f"\nRemoving columns with >{threshold*100}% missing values:")
            for col in columns_to_drop:
                percentage = missing_percentages[col] * 100
                print(f"  {col}: {percentage:.2f}% missing")
            df_cleaned = df_cleaned.drop(columns=columns_to_drop)

        # Then remove remaining rows with missing values
        df_cleaned = df_cleaned.dropna()
        print(f"\nCleaning method: Removing high-missing columns (>{threshold*100}%) then rows with missing values")

    else:
        print(f"Error: Invalid method '{method}'. Use 'rows', 'columns', or 'both'.")
        return df

    print(f"Cleaned dataset shape: {df_cleaned.shape}")
    print(f"Rows removed: {len(df) - len(df_cleaned)}")
    print(f"Columns removed: {len(df.columns) - len(df_cleaned.columns)}")
    print(f"Data retention: {(len(df_cleaned) * len(df_cleaned.columns)) / (len(df) * len(df.columns)) * 100:.2f}%")

    return df_cleaned

def save_cleaned_dataset(df, output_path):
    """Save the cleaned dataset to a CSV file."""
    try:
        df.to_csv(output_path, index=False)
        print(f"\nCleaned dataset saved to: {output_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def analyze_dataset(df):
    """Provide basic analysis of the cleaned dataset."""
    print("\n" + "="*50)
    print("DATASET ANALYSIS")
    print("="*50)

    print(f"Dataset shape: {df.shape}")
    print(f"Number of features: {len(df.columns) - 1}")  # Excluding class column
    print(f"Number of samples: {len(df)}")

    # Check class distribution
    if 'class' in df.columns:
        print(f"\nClass distribution:")
        class_counts = df['class'].value_counts()
        for class_val, count in class_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {class_val}: {count} ({percentage:.2f}%)")

    # Check for any remaining missing values
    remaining_missing = df.isnull().sum().sum()
    print(f"\nRemaining missing values: {remaining_missing}")

    # Show data types
    print(f"\nData types:")
    print(df.dtypes.value_counts())

# Main execution
if __name__ == "__main__":
    # Configuration
    input_file = "agaricus-lepiota.data"  # Update this with your file path
    output_file = "mushroom_dataset_cleaned.csv"

    print("Mushroom Dataset Cleaner")
    print("="*30)

    # Method options
    print("\nCleaning methods available:")
    print("1. 'rows' - Remove rows with missing values")
    print("2. 'columns' - Remove columns with missing values")
    print("3. 'both' - Remove high-missing columns, then rows with missing values")

    # Clean the dataset using different methods
    methods = ['rows', 'columns', 'both']

    for method in methods:
        print(f"\n{'='*60}")
        print(f"CLEANING WITH METHOD: {method.upper()}")
        print(f"{'='*60}")

        cleaned_df = clean_mushroom_dataset(input_file, method=method, threshold=0.1)

        if cleaned_df is not None:
            # Analyze the cleaned dataset
            analyze_dataset(cleaned_df)

            # Save the cleaned dataset
            output_filename = f"mushroom_cleaned_{method}.csv"
            save_cleaned_dataset(cleaned_df, output_filename)

    print(f"\n{'='*60}")
    print("CLEANING COMPLETE!")
    print(f"{'='*60}")

    # Additional utility function for custom cleaning
    print("\nFor custom cleaning, use:")
    print("cleaned_df = clean_mushroom_dataset('your_file.csv', method='rows')")