import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
%matplotlib inline
#to fetch images
import urllib.request

#load the data
new_df=pd.read_csv('./listings.csv', usecols=['host_id','host_is_superhost','host_total_listings_count',
       'neighbourhood_cleansed', 'neighbourhood_group_cleansed', 'latitude',
       'longitude','room_type', 'price','minimum_nights','availability_365', 
        'number_of_reviews','review_scores_rating', 'review_scores_location'])

#data prepaing
new_data.info()
#check for NaNs
new_data.isnull().sum()
#replacing all NaN values in review_scores_rating with review_scores_rating median()
new_df.fillna({'review_scores_rating':new_df.review_scores_rating.median()}, inplace=True)
#examing changes
new_df.isnull().sum()
#replacing all NaN values in review_scores_rating with review_scores_rating mean()
new_df.fillna({'review_scores_location':new_df.review_scores_location.median()}, inplace=True)
#examing changes
new_df.isnull().sum()
#To drop any rows that have missing data
new_df=new_df[new_df.host_is_superhost.notna()]
#to trim $ sign from price column
import locale
locale.setlocale(locale.LC_ALL,'')
new_df['price']=new_df.price.map(lambda x: locale.atof(x.strip('$')))

#EDA
# lets figure out the median price for  each borough and plot it 
median_price = new_df.groupby('neighbourhood_group_cleansed')['price'].median().sort_values(ascending=False)
median_price.plot(kind='area', fontsize=14);

#plot prices distribution on map image
sub_price=new_df[new_df.price<150] 
nyc_img=Image.open('nyc.png')
plt.figure(figsize=(12,10))
#scaling the image based on the latitude and longitude max and mins for proper output
plt.imshow(nyc_img,zorder=0,extent=[-74.258, -73.7, 40.49,40.92])
ax=plt.gca()
sub_price.plot(kind='scatter', x='longitude', y='latitude', label='availability_365', c='price', ax=ax, 
           cmap=plt.get_cmap('jet'), colorbar=True, alpha=0.7, zorder=5)

plt.legend()
plt.show()

#plot type of listings distribution 
listings_types=sns.catplot(x='neighbourhood_group_cleansed', hue='room_type', data=new_df, kind='count')
plt.title('Type of listings NYC', fontsize=12)
listings_types.set_xticklabels(rotation=90)
plt.show();

#checking parameters dependence
sns.heatmap(new_df.corr(), cmap="YlGnBu")
sns.pairplot(new_df, hue="host_is_superhost")
plt.show()

#plot classes proportion
new_df.host_is_superhost = new_df.host_is_superhost.replace({"t": 'True', "f": "False"})
feq=new_df['host_is_superhost'].value_counts()
feq.plot.bar(figsize=(10, 8), color=['blue', 'green'], width=1, rot=0)
plt.title("Number of listings with Superhost", fontsize=20)
plt.ylabel('Quantative listings distibution across the city', fontsize=12)
plt.show();

#plot classes distribution across the city
superhost_loc=sns.catplot(x='neighbourhood_group_cleansed', hue='host_is_superhost', data=new_df, palette='Accent',kind='count')
plt.title('is_Superhost')
superhost_loc.set_xticklabels(rotation=90);

#taking small subset of observations to set hypothesis
new_df[:20].groupby('host_is_superhost').agg({'price':'median', 'review_scores_rating': 'median', 'availability_365': 'mean',
                                            'number_of_reviews':'median','review_scores_location':'median'})
#box plot of subset
first_20=new_df[:20]
sns.set(style="ticks", palette="pastel",font_scale=1.2)
viz_2=sns.boxplot(data=first_20, x='host_is_superhost', y='price', whis=3.0, palette=["m", "g"])
viz_2.set_title('Density and distribution of prices between Superhost and not Superhost');
# sns.despine()
plt.show()
plt.savefig('first_20Price', dpi=200);

#prepair data for U-test
SH=df_SH['price'].tolist()
NSH=df_NSH['price'].tolist()

#test
from scipy.stats import mannwhitneyu
stat, p = mannwhitneyu(SH[:500], NSH[:2500], alternative='two-sided')
print('stat=%.3f, p=%.5f' % (stat, p))
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')
 
#let's find out more about how listings price statistically distributed across our group.

#Superhost
sub_1=new_df.loc[new_df['host_is_superhost'] == 'True']
price_sub1=sub_1[['price']]
#Not a Superhost
sub_2=new_df.loc[new_df['host_is_superhost'] == 'False']
price_sub2=sub_2[['price']]
#putting all the prices' dfs in the list
price_list_by_b=[price_sub1, price_sub2]
#creating an empty list that we will append later with price distributions for each group
p_l_b_b_2=[]
#creating list with known values in group column
host_list=['True', 'False']
#creating a for loop to get statistics for price ranges and append it to our empty list
for x in price_list_by_b:
    i=x.describe(percentiles=[.25, .50, .75])
    i=i.iloc[3:]
    i.reset_index(inplace=True)
    i.rename(columns={'index':'Stats'}, inplace=True)
    p_l_b_b_2.append(i)
#changing names of the price column to the area name for easier reading of the table    
p_l_b_b_2[0].rename(columns={'price':host_list[0]}, inplace=True)
p_l_b_b_2[1].rename(columns={'price':host_list[1]}, inplace=True)
stat_df=p_l_b_b_2
stat_df=[df.set_index('Stats') for df in stat_df]
stat_df=stat_df[0].join(stat_df[1:])
stat_df

#using boxplot to showcase density and distribtuion of prices 
df=new_df[new_df.price<500]
sns.set(style="ticks", palette="pastel")
viz_2=sns.boxplot(data=df, x='host_is_superhost', y='price', whis=3.0, palette=["m", "g"])
viz_2.set_title('Density and distribution of prices between Superhost and not Superhost');
# sns.despine()
plt.show();