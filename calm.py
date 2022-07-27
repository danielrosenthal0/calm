#creating an algorithm to find which variables from instagram scrape correlate
#with finding a good influencer for the Calm app and a good influencer in general

# installing packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#importing data
calm = pd.read_excel("calm3.xlsx")
#print(calm.head())


#selecting smaller set of data that aren't strings to create correlation map
calm_small = calm.loc[0:37,["username", "is_verified", "media_count","follower_count","following_count","has_external_url","total_igtv_videos","total_clips_count","usertags_count","has_highlight_reels","is_business","account_type","engagement_rate","is_person_category","influencer_score","calm_influencer_score"]]
plt.figure(figsize=(16, 6))

heatmap = sns.heatmap(calm_small.corr()[["calm_influencer_score"]].sort_values(by="calm_influencer_score", ascending = False), vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Features correlating with how good a user may be for Calm', fontdict={'fontsize':12}, pad=12);
plt.show()