import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

        """
        Asks user to enter a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to explore
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter

        """
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ["chicago", "washington", "new york city"]
    valid_city = []
    for item in range(len(cities)):
        cities[item] = cities[item].lower()
        valid_city.append(cities[item])

    city = input("Which city would you like to explore: chicago, new york city or washington? (NOTE: You can explore only the cities mentioned earlier): \n").lower()

    while True:
        if city in valid_city:
            print("Looks like you want to explore {}\n".format(city))
            break
        else:
            print("Oops, looks like you entered a wrong input, remember, you can explore only chicago, new york city or washington: \n")
            city = input(" \n").lower()
            

    # TO DO: get user input for month (none, january, february, ... , june)
   
    months = ["none", "january", "february", "march", "april", "may", "june"]
    valid_month = []

    for item in range(len(months)):
        months[item] = months[item].lower()
        valid_month.append(months[item])

    month = input("Fiter by the Month you want to explore (NOTE: Enter 'none' if you don't want to filter by month.Your input should look like 'january'): ").lower()

    while True:
        if month in valid_month:
            print("\nFiltering....\n")
            break
        else:
            print("Oops, looks like you entered a wrong input, remember, Your input should be any value from [none, january, february,...,june]: ")
            month = input(" ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["none", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    valid_days = []

    for item in range(len(days)):
        days[item] = days[item].lower()
        valid_days.append(days[item])

    day = input("Filter by the Day you want to explore(NOTE:Enter 'none' if you don't want to filter by day. Your input should look like 'sunday'.): ").lower()

    while True:
        if day in valid_days:
            print("\nFiltering....\n")
            break
        else:
            print("Oops, looks like you entered a wrong input, remember,Your input should be any value from [none, sunday, monday,...,saturday]: ")
            day = input(" ").lower()

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
    print("\nJust a moment.....loading the data.....\n")
#     load the data file of the cities into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
#     convert the start time column to datetime format
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
#     create a column for month by extracting data from the Start Time column
    df["month"] = df["Start Time"].dt.month
#     df["month"] = df["Start Time"].dt.strftime('%B')
    
#     create a column for day by extracting data from the Start Time column
    df["day"] = df["Start Time"].dt.weekday_name
    
#    create a column for hour by extracting data from the Start Time column
    df['hour'] = df['Start Time'].dt.hour
    
    print("Data loaded, Now applying filters....\n")
    
#     filter by month if user demands
    if month != "none":
#         
        months = ["january", "february", "march", "april", "may", "june"]
        if item in months:
            df = df[df["month"] == item]

#     using the index of the months list to get the corresonding integer of the month the user wants,
#     1 is added to the month index because the index of a list starts from 0
        # month = months.index(month) + 1
    
#     create the dataframe of the month chosen by the user
        # df = df[df["month"] == month]
        
        

#     filter by day if user demands
    if day != "none":
#         create the dataframe of the month chosen by the user
        df = df[df["day"] == day.title() ]
    
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating Statistics Of The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month   
    
    common_month = df["month"].value_counts().idxmax()
    mode_month = calendar.month_name[common_month]
    print("What is the most popular month for traveling? \n {}".format(mode_month))
    
    # TO DO: display the most common day of week
    
    common_day_of_week = df["day"].mode()
    print('\nCalculating Statistics...\n')
    print("What is the most popular day for traveling? \n {}".format(common_day_of_week))
    
    # TO DO: display the most common start hour
    
    #  create a column for hour by extracting data from the Start Time column
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df["hour"].mode()
    print('\nCalculating Statistics...\n')
    print("What is the most popular hour of the day to start your travel? \n {}".format(common_start_hour))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    common_start_station = df["Start Station"].mode()  
    print('\nCalculating Statistics...\n')
    print("What is the most popular start station? \n {}".format(common_start_station))


    # TO DO: display most commonly used end station
    
    common_end_station = df["End Station"].mode()   
    print('\nCalculating Statistics...\n')
    print("What is the most popular end station? \n {}".format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    
#     create a panda series to store both start station and end station columns 
    station_series = pd.Series(list(zip(df["Start Station"], df["End Station"])))
#     extracting the most frequent combination of start station and end station from the resulting series
    start = station_series.mode()[0][0]
    end = station_series.mode()[0][1]
    print('\nCalculating Statistics...\n')
    print("What is the most frequent combination of start station and end station trip? \nStart Station: {}\nEnd Station: {}".format(start, end))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_travel_time = np.sum(df["Trip Duration"])
    total_unit_time = pd.to_timedelta(total_travel_time, unit="s")
    print('\nCalculating Statistics...\n')
    print("What is the total travel time? \n {}".format(total_unit_time))


    # TO DO: display mean travel time
    
    mean_travel_time = np.mean(df["Trip Duration"])
    mean_unit_time = pd.to_timedelta(mean_travel_time, unit="s")
    print('\nCalculating Statistics...\n')
    print("What is the average travel time? \n {}".format(mean_unit_time))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
#     convert the dataframe to pandas series
    user_type_series = df["User Type"].squeeze()
    count_user_type = user_type_series.value_counts()
    print('\nCalculating Statistics...\n')
    print("What is the breakdown of the users? \n{}".format(count_user_type))


    # TO DO: Display counts of gender
    try: 
        gender_series = df["Gender"].squeeze()
        gender_count = gender_series.value_counts()
        print('\nCalculating Statistics...\n')
        print("What is the breakdown of the gender? \n{}".format(gender_count))
    except KeyError as e:
        print("What is the count of the gender?")
        print("No gender data to share")
        print("None")
        


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\nCalculating Statistics...\n')
        earliest_year_of_birth = df["Birth Year"].min()
        print("What is the earliest year of birth? \n{}".format(earliest_year_of_birth))
        recent_year_of_birth = df["Birth Year"].max()
        print("What is the most recent year of birth? \n{}".format(recent_year_of_birth))
        common_year_of_birth = df["Birth Year"].mode()
        print("What is the most common year of birth? \n{}".format(common_year_of_birth))
    except KeyError as e:
        print("What is the earliest, most recent, and most common year of birth?")
        print("No birth year data to share")
        print("None")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        view_data = input("Would you like to view individual trip data (Type Yes or No): ")
#         while True:
        if view_data.lower() == "yes":
            display_data = df.sample(5)
            print(display_data)
            view_data = input("Would you like to view individual trip data (Type Yes or No): ")
        else:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
            
            
    


if __name__ == "__main__":
    main()
