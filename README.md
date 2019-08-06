# Explore US Bikeshare Data
###### 06/08/2019

### Summary
Used Python to explore data related to bike share systems for three major cities in the United States: Chicago, New York City, and Washington.

Wrote code to import the data and answer analytical questions about it by computing descriptive statistics. I also created a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

### Datasets
The data was provided by Motivate, a bike share system provider for many major cities in the United States. The data files contain randomly selected data for the first six months of 2017 for all three cities. All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year

### Statistics Computed
- Popular times of travel
    - most common month
    - most common day of week
    - most common hour of day


- Popular stations and trip
    - most common start station
    - most common end station
    - most common trip from start to end


- Trip duration
    - total travel time
    - average travel time


- User info
    - counts of each user type
    - counts of each gender (only available for NYC and Chicago)
    - earliest, most recent, most common year of birth (only available for NYC and Chicago)


### Software Requirements
- Python 3, NumPy, and pandas installed using Anaconda
- A text editor, like Sublime or Atom
- A terminal application
