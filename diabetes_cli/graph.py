import pandas as pd
import plotext as plt

def plot_graph(data_type):
    try:
        df = pd.read_csv("storage.csv", header=0)
        data = df[df["Type"] == data_type]
        data = data.dropna(subset=["Value", "Date", "Time"])
        if data.empty:
            print(f"No {data_type} data to plot.")
            return
        # Combine date and time, then format as required by plotext
        timestamps = pd.to_datetime(data["Date"].astype(str) + " " + data["Time"].astype(str), errors="coerce")
        x = [t.strftime("%d/%m/%Y %H:%M") for t in timestamps]
        y = data["Value"].astype(float).tolist()
        plt.clear_figure()
        plt.theme("clear") # Use a clear theme for better visibility
        plt.date_form('d/m/Y H:M')
        plt.plot(x, y, marker='dot', color='blue')
        plt.title(f"{data_type.replace('_', ' ').title()} Over Time")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.grid(False)  # Remove grid for a cleaner look
        plt.show()
    except FileNotFoundError:
        print("No data to plot.")
    except Exception as e:
        print(f"Error plotting graph: {e}")