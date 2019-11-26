import pandas as pd
import os

# CODE FOR CREATING THE SP500 CSV
# the stock that is to be analyzed
"""
sample_df = pd.read_csv("sp500/FB_data.csv")
sample_df = sample_df.set_index("date")
overall_df = pd.DataFrame(index=sample_df.index)

overall_df['percentageChange'] = 100 * (sample_df['close'] - sample_df['open']) / sample_df['open']

overall_df['result'] = [ 0 if -1 < i and i < 1 else 1 for i in overall_df['percentageChange']]
for filename in os.listdir("sp500"):

    try:    
        current_df = pd.read_csv("sp500/" + filename)
        current_df = current_df.set_index("date")
        overall_df[filename] = (current_df['close'] - current_df['open']) / current_df['open']


    except:
        continue

overall_df.to_csv("sp500.csv")
print(overall_df.index)
"""

