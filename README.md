The goal of this project is the investigate casualty class (Driver or Rider, Pedestrian or Passenger) in accidents in hopes of implementing more safety measures for these classes. The data set has been prepared from manual records of road traffic accident of the year 2017-20 with sensitive information already removed. It has 33 features and 12316 instances of an accident. It also includes weather conditions, type of vehicles, number of casualties and information about them, there are a lot of features in this dataset for analysis. I hope to show casualty traits through visualizations and create an algorithm that can predict the severity of accidents. 



There are some questions that can be answered using this data such as:
- Does weather affect class of casualty?
- Does gender affect severity?
- What are the age group are most likely to be involved in accidents?
- What are the areas with higher accident severity or lower accident severity?


|Data Dictionary:|
|----------|-----|
|Attribute | Value| Dtype|
|----------|:----:|-----:|
|Age band  | Age band of driver and caualty | Int64|
|Driving_experience | Number of bathrooms in home | Float|
|Bedrooms  | Number of bedrooms | Float|
|Sqft      | Calculated total finished living area of the home | Float|
|Cola      | Where properties are located | Int|
|Fips      | Federal Information Processing Standard Code | Float|
|$ per sqft| How many dollars per sqft | Float|
|Latitude  | Latitude of property | Float|
|Longitude | Longitude of property | Float|
|Home_value| Value of home	| Float|
|Land_tax  | The 2017 total tax assessed value of the land | Float|
|Age       | Number of years from original construction until the home sold in 2017.| Float|
|Acres     | Square footage of lot converted to acres | Category|
|Has_pool  | If the property has a pool |Float|
|County	   | What county it is in | Float|
|Logerror  | the log(Zestimate) - log(SalePrice) | Float|