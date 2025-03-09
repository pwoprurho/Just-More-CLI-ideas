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
    data = data.astype(dtype=types_dict)
    # Convert date column to datetime format
    data["Date"] = pd.to_datetime(data["Date"])
    return data
    
def data_analysis(data):
    data["Month"] = data["Date"].dt.month
    ndf = data.groupby("Month")["Units Sold"].mean()
    return data
    
def visualize_data(ndf, vis_type="bar"):
    ndf.plot(kind = vis_type, fig_size=(10, 5), title="Average Units Sold per Month")
    plt.xlabel("Month")
    plt.ylabel("Units Sold") 
    plt.show()
    return ndf
    
path = "OnlineSalesData.csv"
df = (pd.DataFrame()
                                   .pipe(lambda x: load_data(path))
                                   .pipe(data_cleaning)
                                   .pipe(convert_datatypes)
                                   .pipe(visualize_data, "line")
                                   )
