import pandas as pd
from tabulate import tabulate
import numpy as np

def show_stats():
    try:
        df = pd.read_csv("storage.csv", header=0)
        if df.empty:
            print("No data found.")
            return
        # Replace NaN with empty string for display
        df = df.replace({np.nan: ""})
        print("Blood Sugar and Insulin Log:")
        print(tabulate(df, headers="keys", tablefmt="github", showindex=False))
    except FileNotFoundError:
        print("No data found.")
    except Exception as e:
        print(f"Error: {e}")