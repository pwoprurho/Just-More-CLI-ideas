import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    return pd.read_csv(path)
    
def data_cleaning(data):
    data = data.drop_duplicates()
    data = data.dropna()
    data = data.reset_index(drop=True)
    return data
    
def convert_datatypes(data, types_dict=None):
    if types_dict:
        data = data.astype(dtype=types_dict)
    data["Date"] = pd.to_datetime(data["Date"])
    return data
    
def data_analysis(data):
    data["Month"] = data["Date"].dt.month
    ndf = data.groupby("Month")["Units Sold"].mean()
    return ndf # Return the grouped data, not the original dataframe
    
def visualize_data(ndf, vis_type="line"): # changed default to line
    ndf.plot(kind = vis_type, figsize=(10, 5), title="Average Units Sold per Month")
    plt.xlabel("Month")
    plt.ylabel("Units Sold") 
    plt.show()
    return ndf
    
path = "OnlineSalesData.csv"
try:
    df = (pd.DataFrame()
                                       .pipe(lambda x: load_data(path))
                                       .pipe(data_cleaning)
                                       .pipe(convert_datatypes)
                                       .pipe(data_analysis)
                                       .pipe(visualize_data, "line")
                                       )
except FileNotFoundError:
    print(f"Error: File '{path}' not found.")
except KeyError as e:
    print(f"Error: Column '{e.args[0]}' not found in the CSV file. Please check the column names.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
