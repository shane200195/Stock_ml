import pandas as pd
import os

# CODE FOR CREATING THE SP500 CSV
# the stock that is to be analyzed

sample_df = pd.read_csv("djia_long/AAPL.csv")
sample_df = sample_df.set_index("Date")
overall_df = pd.DataFrame(index=sample_df.index)
for filename in os.listdir("djia_long"):
    try:    
        current_df = pd.read_csv("djia_long/" + filename)
        current_df = current_df.set_index("Date")
        overall_df[filename[:filename.find(".")]] = (current_df['Close'] - current_df['Open']) / current_df['Open']


    except:
        continue

overall_df.to_csv("djia_long.csv")
print(overall_df.index)


