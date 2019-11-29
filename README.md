# AIppointment
---------------------------
### What is this project?
This Deep Learning project intents preddict if a patient will miss an medical appointment or not.

### Why is this project needed?
No-show medical appointments are a issue that affects every health public system in the world. One [study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1466756/) found that a hospital reported 62 no-show appointments per day resulting in an estimated cost of $3 million. [Another](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4714455/) study shows that the average cost of no-show per patient was $196 in 2008. 
  
So, altought this theme is [vastly](https://www.kaggle.com/joniarroba/noshowappointments) debated, **our main goal is to build a model that can help clinics and public hospitals to reduce no-shows**. 

Assuming that adding some new features to this dataset can improve its accuracy, we merged a weather timeseries dataset to check what was the weather at appointment day. We had this insight by reading some articles debating this no-show issue (citation needed).

### How this project was built? 
#### Tooling:
* Whe used this amazing tools and libraries:
  * Python 3.7;
  * Jupyter Notebook;
  * Pandas;
  * Keras and Tensorflow. 

## Dataset
We also used a [dataset](https://www.kaggle.com/joniarroba/noshowappointments) found at Kaggle and scraped some weather data of Inmet. 

## Building phases
This work is divided by three main notebooks.

* Dataset Treatment - Here we merge our datasets, fixes some columns and filter some data.
* Exploratory Data Analysis - Here we show our study, check some correlations and do some fancy things like Self Organizing Maps.
* Modeling - Here we develop and train our model

### Future work and caveats

[ building ]

## Installing and using
Before getting some work done, you need to run the following:
* Install requirements: 
``` pip install -r requirements.txt  ```

* To run jupyter notebooks you should open **\nootebook** folder, or it may not run.


## Contributing

[ building ]
