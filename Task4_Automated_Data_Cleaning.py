import pandas as pd

def clean_data(file_path, output_file="cleaned_data.csv"):
    # Load dataset
    df = pd.read_csv(file_path)

    print("\n📊 Initial Data Preview (Before Cleaning):")
    print(df.head(), "\n")

    # Standardize column names (lowercase & remove spaces)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Handle missing values
    df.fillna(method='ffill', inplace=True)  # Forward fill missing values
    df.dropna(inplace=True)  # Drop remaining NaN rows if any

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert 'date' column to datetime (handle errors)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Convert 'salary' to numeric (handle non-numeric values)
    if 'salary' in df.columns:
        df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
        df['salary'].fillna(df['salary'].median(), inplace=True)  # Fill missing salary with median

    # Convert dates back to proper string format for output
    if 'date' in df.columns:
        df['date'] = df['date'].dt.strftime('%Y-%m-%d')

    # **Fix: Reset index after cleaning**
    df.reset_index(drop=True, inplace=True)

    print("\n✅ Data Cleaning Completed!")
    print("\n📊 Afterward Data Preview (After Cleaning):")
    print(df.head(), "\n")

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print("💾 Cleaned file saved as:", output_file)

# Run the function (Replace 'uncleaned_data.csv' with your actual file)
clean_data("uncleaned_data.csv")
