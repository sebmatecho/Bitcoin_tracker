# Capturing and testing data ingestion using public API 
#### By [Sébastien Lozano Forero](https://www.linkedin.com/in/sebastienlozanoforero/)

This respository contains a Data Engineering project based on the API proposed by [The Covid Tracking Project](https://covidtracking.com/), intended to report daily cases of covid-19 at the beginning of the covid-19 pandemic (early 2020). This project served realiable data to the US federal governement in the first phase of the pandemics, until March 7, 2021. 

## Project Structure

The following is the main idea behind the chunks composing this project
#### API
The API is proposed. It would contain the endpoint's construction and the request to get data for a determined state on a certain date. As data is being consumed directly from a public API, certain conditions were put in place to not get blocked by over using it.
#### ingestor
The ingestor create and keep track of the last date used as endpoint. This way, we are able to keep the data flowing without worrying to much about the having to manually modified the checkpoint or overwriting data. 

#### writer
As the project would ingest data into the final output based on daily information, the writer hand the appending of a new data point into the compiled file. 
#### main
Finally, the *main* file will initialize the whole process of gathering the data. Here, the API would be initialized and the job would be dscheduled. 

## Test 

Unit and integration tests are proposed in order to assess the data ingestion process and to guarantee quality data being inserted to the final dataset. 