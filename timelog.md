# Timelog

* Proactive and Reactive Decision Making on Wind Turbine Time Series Data
* Hannah Mehravari
* 2249293M
* Christos Anagnostopoulos

## Week 1

### 28 September 2020

* *4 hours* Read the project guidance notes

### 29 September
* *4 hours* Wrote [project project proposal](https://docs.google.com/document/d/15p8fmXErrMKY59_fgcNVl8EzUGvy0eFHJhcFzhcWBq4/edit#heading=h.hgseaaqcu0kl) based on material sent by industry partner

## Week 2
### 5 Oct 2020
* *0.5 hour* Sent project proposal to surpervisor to be submitted on LTC
### 6 Oct 2020
* *1.5 hours* Read [An overview of time series forecasting models](https://towardsdatascience.com/an-overview-of-time-series-forecasting-models-a2fa7a358fcb) and took notes
* *1.5 hours* Read [Time Series Analysis in Python: An Introduction](https://towardsdatascience.com/time-series-analysis-in-python-an-introduction-70d5a5b1d52a) and took notes
### 7 Oct 2020
* *2 hours* Skimmed time series forecasting tutorial notes by Gesine Reinert


## Week 3
### 12 Oct 2020
* *2 hours* Downloaded data pack from indurstry partner's network and shared with superisor
* *0.5 hour* Created GitHub repository for project

### 13 Oct 2020
* *2 hours* Created starter Jupyter notebook to load in the data to visualise and play around with it and to also have starter code for meeting
* *1 hour* Reading time series forecasting tutorial notes by Gesine Reinert to create the start jupyter notebook

## Week 4
### 22 Oct 2020
* *1 hour* Meeting with supervisor to discuss what statistical properties I should look for in the data
* *4 hours* Created Jupyter notebook to assess stationarity of wind speed and wind direction time series using statistical methods recommended by supervisor
* *0.5 hours* Email conversation with supervisor for next steps to take

### 24 Oct 2020
* *1 hour* Read [How to Identify and Remove Seasonality from Time Series Data with Python](https://machinelearningmastery.com/time-series-seasonality-with-python/)
* *1 hour* Read [Trend, Seasonality, Moving Average, Auto Regressive Model : My Journey to Time Series Data with Interactive Code](https://towardsdatascience.com/trend-seasonality-moving-average-auto-regressive-model-my-journey-to-time-series-data-with-edc4c0c8284b)

### 25 Oct 2020
* *2 hours* Read [Time Series in Python — Exponential Smoothing and ARIMA processes](https://towardsdatascience.com/time-series-in-python-exponential-smoothing-and-arima-processes-2c67f2a52788)
* *2 hours* Read [Time Series in Python — Part 2: Dealing with seasonal data](https://towardsdatascience.com/time-series-in-python-part-2-dealing-with-seasonal-data-397a65b74051)
* *1 hour* Used sample cade from above articles to analyse wind turbine data


## Week 5
### 29 Oct 2020
* *1 hour* Meeting with surpervisor to look at my data analysis Jupyter notebooks and answer some questions about my findings
* *3 hours* Reading about machine learning models for time series forecasting
* *1 hour* Draft meeting agenda for industry partner requirements gathering next week

## Week 6 
### 2 Nov 2020
* *1 hour* Meeting with industry partner for some clarifications on required solution and further requirements gathering
* *1 hour* Make notes on things discussed in industry partner meeting

### 5 Nov 2020
* *1 hour* Meeting with supervisor
* *2 hours* Created UML diagram for system architecture for deploying the solution to an onsite server when developed

## Week 7
## 12 Nov 2020
* *1 hour* Meeting with supervisor
* *2 hours* Read [Continual Learning in Practice](https://assets.amazon.science/8e/63/5bfdb1bb419491ba26ce3b219369/continual-learning-in-practice.pdf)
* *1 hour* Read Machine Learning Architecture and Design Patterns by H Washizaki et al.
* *1 hour* Read [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)

## Week 8
* No work was completed due to personal problems.

## Week 9
### 26 Nov 2020
* *5 hours* Redesigning the systems architecture based on [this paper](https://assets.amazon.science/8e/63/5bfdb1bb419491ba26ce3b219369/continual-learning-in-practice.pdf)
### 27 Nov 2020
* *1 hour* Meeting with supervisor
* *2.5 hours* Write python class for noise campaign wind speed x wind direction histogram

## Week 10
### 1 Dec 2020
* *1 hour* Watching a youtube video explaining the theory of the ARIMA process
* *2 hours* Experimenting with sci-kit learn's ARIMA class and trying to forecast the averaged time series of a turbines

### 2 Dec 2020
* *1 hour* Set an Azure Machine Learning environment for cloud training
* *4 hours* Experimenting with grid searching SARIMA hyperparameters

### 3 Dec 2020
* *4 hours* Working on grid searching using a GPU, still no success

### 4 Dec 2020
* *1 hour* Meeting with supervisor which solves my blocker of not knowing how to configure/grid search ARIMA
* *4 hours* Created notebooks exploring the accuracy of forecasting both wind speed and direction using ARIMA, either using an aggregated time series or single time series
* *2 hours* Installing Zookeeper and Kafka

### 5 Dec 2020
* *2 hours* Create a Kafka message producer, topic and consumer to listen to simulated live turbine data

## Week 11
### 7 Dec 2020
* *2 hours* Create 2D histograms (heatmaps) of both predictions and real data and experiment with create a MSE heatmap

## Week 12
### 14 Dec 2020
* *1 hour* Meeting with supervisor

## Week 11
### 10 Dec 2020
* *2 hour* Preparing progress update for RES contacts

## Week 12
### 14 Dec 2020
* *1 hour* Meeting with supervisor
* *3 hours* Writing progress report to submit to moodle and send to supervisor

### 18 Dec 2020
* *1 hour* Added final touches to progress report and submitted.

## Week 13
* Holidays 
## Week 14
* Holidays
## Week 15
* Holidays

## Week 16
* No work done due to preparing for new semester courses

## Week 17
### 14 Jan 2021
* *1 hour* Meeting with RES contacts to gather new requirements and discuss potential trial run

## Week 18
### 19 Jan 2021
* *1 hour* Meeting with supervisor
## Week 19
### 25 Jan 2021
* *30 mins* Downloaded new 30s Scadinavian data to resample
* *2 hours* Experimented with predicted Scandinavian data with the developed prediction methods
### 26 Jan 2021
* *4 hours* Create a graphic using matplotlib to demonstrate the time taken to predict the wind speed and direction at each time step for the next period and send to RES contact
* *1 hour* Meeting with supervisor
### 27 Jan 2021
* *2 hours* Work on resampling 30s data to 2 minute data
### 28 Jan 2021
* *3 hours* Create new graph on the timeline from 2 minute predictions to turbine commands based on RES contact's corrections and comments.
* *2 hours* Set up a REST API skeleton
* *2 hours* Investigating suitable architecture for the system given the new requirements that about from my exchange with my RES contact when talking through the graphs.

## Week 18
### 7 Feb 2021
* *2 hours* Researching InfluxDB

## Week 19
### 8 Feb 2021
* *1 hour* Meeting with supervisor
* *5 hours* Installing docker, debugging setup, dockerising API, setting up InfluxDB

### 9 Feb 2021
* *3 hours* Writing some tests and setting up a GitHub Actions CI

### 10 Feb 2021
* *7 hours* Connecting the API to the InfluxDB and to set up Chronograf to see whether or not the testing request sent with Postman made it through.

### 11 Feb 2021
* *5 hours* Learning InfluxQL/Flux CLI in order to investigate the best way to initialise the db on build, opted for using the Python interface instead

## Week 19
No work done due to circumstances discussed in Good Cause Submission
## Week 20
No work done due to circumstances discussed in Good Cause Submission
## Week 21
No work done due to circumstances discussed in Good Cause Submission
## Week 22
No work done due to circumstances discussed in Good Cause Submission
## Week 23
No work done due to circumstances discussed in Good Cause Submission
## Week 24
No work done due to circumstances discussed in Good Cause Submission
## Week 25
Project on hold - Exam season (Discussed in good cause submission)

## Week 26
Project on hold - Exam season (Discussed in good cause submission)

## Week 27
Project on hold - Exam season (Discussed in good cause submission)

## Week 28
Project on hold - Exam season (Discussed in good cause submission)

## Week 29
Project on hold - Exam season (Discussed in good cause submission)

## Week 30

### 31 May 2021
* *5 hours* Project resumed, spent some time rounding up outstanding tasks and planning work for the next couple of weeks

### 1 Jun 2021
* *7 hours* Collecting evaluation data for the developed baseline ARIMA model using the RES bins and the predicting the raw values as well as attempting to use an error correction methodology to remedy to errors. Also produced some graphs.

### 2 Jun 2021
* *7 hours* Collecting evaluation data for the 1st modified ARIMA model using the modified bins and the predicting the raw values as well as attempting to use an error correction methodology to remedy to errors. Also produced some graphs.

### 3 Jun 2021
* *7 hours* Collecting evaluation data for the 2nd modified ARIMA model using a wind speed and directio bin time series to predict the bins directly and attempting to use an error correction methodology to remedy to errors. Also produced some graphs.

### 4 Jun 2021
* *7 hours* Wrote the report literature review

### 5 Jun 2021
* *7 hours* Did some planning for developing the decision making algorithm as well as changing the dashboard solution from Chronograf to Grafana since Grafana supported custome plotly graphs which I needed to make the live histogram to work

### 6 Jun 2021
* *7 hours* Wrote a python class to interface with the influxdb instance in order to use when the decision making algorithm was implemented.

## Week 31

### 6 Jun 2021
* *7 hours* Wrote the decision making algorithm and spent time debugging as I was struggling with time alignment.

### 6 Jun 2021
* *7 hours* Wrote the main wind forecasting section of the dissertation report

### 7 Jun 2021
* *7 hours* Spent some time editing the wind forecasting section of the report

### 8 Jun 2021
* *12 hours* Tying all the different system components together and did some manual testing to ensure the componenets were behaving as expected

### 9 Jun 2021
* *12 hours* Time spent on refining the decision making algorithm, debugging and refactoring.

### 10 Jun 2021
* *12 hours* Ran trial of the system by mocking out the turbine control software and imitating it's behaviour. Analysed the data export for the system's decision accuracy and made a demo video showing the live Grafana dashboard update in real-time

## Week 32

### 12 Jun 2021
* *7 hours* Started writing the system implementation section and produced some diagrams for visualising the system architecture and decision making algorithm

### 13 Jun 2021
* *7 hours* Editing the system implementation section.

### 14 Jun 2021
* *7 hours* Writing the conclusion and future work sections

### 15 Jun 2021
* *7 hours* Writing the problem background and proposed solution sections

## Week 33

### 19 Jun 2021
* *7 hours* Writing the abstract, introduction and tying the dissertation together.

### 20 Jun 2021
* *7 hours* Editing the dissertation, producing and refining results tables, figured and the structure of the paper.

### 21 Jun 2021
* *7 hours* Organising the GitHub repository and removing unused files and dependancies.

## Week 34

### 28 Jun 2021
* *7 hours* Editing and proofreading the report

### 29 Jun 2021
* *7 hours* Creating the slides and script for the final presentation and recording it.

### 30 Jun 2021
* *7 hours* Submitting the project, report and presentation