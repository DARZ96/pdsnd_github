import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWould you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Sorry, I didn't quite get that. Please input a valid city")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWhich month would you like to filter by? You can filter data by any month from January to June or just type 'all' if you do not have any preference\n").title()
        if month in ['January', 'February', 'March', 'April', 'May', 'June', 'All']:
            break
        else:
            print("Sorry, I didn't quite get that. Please input any month from January to June or type 'all' if you do not have any preference.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWould you like to filter by day as well? You can choose any day from Monday to Sunday or just type 'all' if you have no preference\n").title()
        if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']:
            break
        else:
            print("Sorry, I didn't quite get that. Please input any day from Monday to Sunday or just type 'all' if you have no preference.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month:", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day of the week:", popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print("Most commonly used start station:", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print("Most commonly used end station:", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station', 'End Station']).count()
    print("Most frequent combination of start and end station:", popular_start_station, popular_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time:", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types:", user_types)

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print("Gender types:", genders)
    except KeyError:
        print("No Gender information available for this month")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print("Earliest year of birth:", earliest_birth_year)
    except KeyError:
        print("No Birth Year information available for this month")

    try:
        most_recent_birth_year = df['Birth Year'].max()
        print("Most recent year of birth:", most_recent_birth_year)
    except KeyError:
        print("No Birth Year information available for this month")

    try:
            most_common_birth_year = df['Birth Year'].value_counts()
            print("Most common year of birth:", most_common_birth_year)
    except KeyError:
        print("No Birth Year information available for this month")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    index1 = 0
    index2 = 5
    while True:
        raw_data = input('Would you like to see more raw data?\nPlease type yes or no.\n').lower()
        if raw_data == 'yes':
            print(df.iloc[index1:index2])
            index1 += 5
            index2 += 5
        else:
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
