import pandas as pd
import os

# CODE FOR CREATING THE SP500 CSV
# the stock that is to be analyzed

sample_df = pd.read_csv("dija/AABA_2006-01-01_to_2018-01-01.csv")
sample_df = sample_df.set_index("Date")
overall_df = pd.DataFrame(index=sample_df.index)
for filename in os.listdir("dija"):
    try:    
        current_df = pd.read_csv("dija/" + filename)
        current_df = current_df.set_index("Date")
        print(filename[:filename.find("_")])
        overall_df[filename[:filename.find("_")]] = (current_df['Close'] - current_df['Open']) / current_df['Open']


    except:
        continue

overall_df.to_csv("dija.csv")
print(overall_df.index)


