The goal of this project is the investigate casualty class (Driver or Rider, Pedestrian or Passenger) in accidents in hopes of implementing more safety measures for these classes. The data set has been prepared from manual records of road traffic accident of the year 2017-20 with sensitive information already removed. It has 33 features and 12316 instances of an accident. It also includes weather conditions, type of vehicles, number of casualties and information about them, there are a lot of features in this dataset for analysis. I hope to show casualty traits through visualizations and create an algorithm that can predict the casualty class. 


There are some questions that can be answered using this data such as:
- Does weather affect class of casualty?
- Does gender affect severity?
- What are the age group are most likely to be involved in accidents?
- What are the areas with higher accident severity or lower accident severity?

To Reproducing Findings: 

- Import pandas and copy CSV
- Acquire CSV
- Store that env file in the same repository. 
- Clone my repository along with the acquire.py and prepare.py. You should be able to run Casualty_prediction.

-------------------
|Data Dictionary: |
|----------|----|
|Attribute | Value| Dtype|
|----------|:----:|-----:|
|Age band  | Age band of driver and caualty | Int64|
|Driving_experience | Number band for driving | Int64|
|Area_accident_occured | Where accident happened | Int64|
|Light_conditions | How dark it was | Int64|
|Number_of_vehicles_involved | Number is cars in accident | Int64|
|Number_of_casualties  | Number of casualties | Int64|
|Casualty_class | Class of casualty | Int64|
|Fitness_of_casuality | Impairment of casualty | int64|
|Casualty_severity | How severe the casualty | Float64|
|Accident_severity| Severity of accident	| Int64|
|Sex_of_casualty | Sex | Int64|
|Weather_conditions  | Weather during accident| Int64|
|Educational_level | Education level | Int64|


## Conclusion
We can see that even though Random Forst got close on validate, none of the models beat the baseline. Max depth did not seem to change anything between the two decision tree models. From the feature importance plot, we can conclude age, fitness of casulty, light and weather conditions do have an effect on class. The models made would not provide anything useful, besides possibly features for clustering. 
We can take the common sense logic from this data to help educate those who need a reminder.
## Next Steps
I think in order to make useful models we will need more information. Such as more location information, speedlimit, right of ways. Possibly, getting a "Distraction" column that lists if the casualty/Driver had a distraction at the time of the accident. 
