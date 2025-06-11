import csv
import pandas as pd

def read_csv_from_local(LOCAL_CSV_FILE_PATH_HEADER,LOCAL_CSV_FILE_PATH_LINE):
    try:
        input_file=LOCAL_CSV_FILE_PATH_HEADER
        df_input=pd.read_csv(input_file)
        input_file_line= LOCAL_CSV_FILE_PATH_LINE
        df_input_line=pd.read_csv(input_file_line)
        return df_input, df_input_line
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None
    

