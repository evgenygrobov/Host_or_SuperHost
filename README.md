# Host or SuperHost?
![](https://github.com/evgenygrobov/AIRBNB_NYC/blob/main/pictures/ny_baby.jpeg)
# PROJECT DESCRIPTION: 
## What makes someone a superhost?
* Airbnb awards the title of “Superhost” to some fraction of its dependable hosts. 
* Completed at least 10 trips OR completed 3 reservations that total at least 100 nights 
* Maintained a 90% response rate or higher Maintained 
* A 1% percent cancellation rate (1 cancellation per 100 reservations) or lower
* Maintained a 4.8 overall rating

## Data
* The data is sourced from the Inside Airbnb website http://insideairbnb.com/get-the-data.html which hosts publicly available data from the Airbnb site.

 * Detailed listings data showing 96 atttributes for each of the listings. Some of the attributes used in the analysis are price (continuous), longitude (continuous), latitude (continuous), listing_type (categorical), is_superhost (categorical), neighbourhood (categorical), ratings (continuous) among others.

* A quick glance at the data shows that there are: 45756 unique listing in NYC in total.
* How likely the SuperHost's listings prices are higher than not a SuperHost.

## Exploratory Data Analysis

### Lets see median price distribution across the city. No wonder the Manhattan is the winner.
---

![](https://github.com/evgenygrobov/Host_or_SuperHost/blob/main/images/price%20nyc.png)
---


### Almost 25% of hosts are Super Host. Lets see the presence of them across the city.
![](https://github.com/evgenygrobov/Host_or_SuperHost/blob/main/images/hostsPortion.png)
---

Almost equal proprtion of host we can see only in Staten Island. Man and Brooklyn has most listings but less the 25% Super Host between them.

### Here I show result of simple price request. First 20 samples. SuperHost listings price is higher. 

![](https://github.com/evgenygrobov/Host_or_SuperHost/blob/main/images/first_20.png)
---

![](https://github.com/evgenygrobov/Host_or_SuperHost/blob/main/images/first_20numbers.png)
---

## Hypothesis test. U-test.

Since we observed listing price difference I wanted to know if we have more observations will it affect the difference.
I presumed that trend will hold, therefore no matter how many new observations we get the Super Host listings will be higher. 
I need to test the Hypothesis. To do that, I need set null and alternative hypothesises.

* Ho= Listings price the same. No diference
* Ha= Listings price not the same. There is a difference.

I need to compute p-value, and also compare value to alpha(cut off level) equal to 0.05. 
Since we know that data not normally distributed and sample size are not the same I applied U-test.


![](https://github.com/evgenygrobov/Host_or_SuperHost/blob/main/images/U_test.png)
---

Now we have p-value greater than our cut of level. Having that, we fail to reject Ho.Thus having higher samples size there probably will be no diffence in listing price. 
We can check this right now. I compute five numbers summary for all 46K samples we have available.

![]()
