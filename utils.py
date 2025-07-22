import pandas as pd
import numpy as np

def load_excel_data(file):
    try:
        xls = pd.ExcelFile(file)

        # Extract year from the 'Information' sheet
        info_df = xls.parse(sheet_name="Information")
        year = info_df['Unnamed: 1'][6]

        # Extract city from the first row (header=0) of 'Data' sheet
        header_df = xls.parse(sheet_name="Data", header=0)
        city = header_df.columns[1]

        # Extract main data with proper headers (header=2)
        df = xls.parse(sheet_name="Data", header=2)

        return year, city, df
    except Exception as e:
        raise ValueError(f"Error reading Excel: {e}")

