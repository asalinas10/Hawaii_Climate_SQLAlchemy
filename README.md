# Hawaii SQLAlchemy Vacation

You decide to do a climate analysis about Hawaii. The following sections outline the steps that you need to take to accomplish this task.

Summary

1. Analyze and Explore the Climate Data

- In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

  - Note that you’ll use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete your climate analysis and data exploration.

  - Use the SQLAlchemy create_engine() function to connect to your SQLite database.

  - Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

  - Link Python to the database by creating a SQLAlchemy session.

  - Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

- Precipitation Analysis

  - Find the most recent date in the dataset.

  - Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

  - Select only the "date" and "prcp" values.

  - Load the query results into a Pandas DataFrame. Explicitly set the column names.

  - Sort the DataFrame values by "date".

  - Plot the results by using the DataFrame plot method

  - Use Pandas to print the summary statistics for the precipitation data.

![Alt text](<Screen Shot 2024-01-10 at 10.47.54 AM.png>)

- Station Analysis

  - Design a query to calculate the total number of stations in the dataset.

  - Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

    - List the stations and observation counts in descending order.

    - Answer the following question: which station id has the greatest number of observations?

  - Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

  - Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

    - Filter by the station that has the greatest number of observations.

    - Query the previous 12 months of TOBS data for that station.

    - Plot the results as a histogram with bins=12

    - Close your session.

  ![Alt text](<Screen Shot 2024-01-10 at 10.48.35 AM.png>)









