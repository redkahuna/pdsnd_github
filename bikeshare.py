import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_city():
    while True:
        city = input("Please enter the name of a city (Chicago, New York City, Washington): ").title().lower()
        if city in CITY_DATA:
            return city
        else:
            print("Invalid input. Please try again.")

def get_month():
    while True:
        month = input("Please enter the name of a month (all, January, February, ..., June): ").title().lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            return month
        else:
            print("Invalid input. Please try again.")

def get_day():
    while True:
        day = input("Please enter the name of a day (all, Monday, Tuesday, ..., Sunday): ").title().lower()
        if day in [ x.lower() for x in ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]:
            return day
        else:
            print("Invalid input. Please try again.")

def get_filters():
    print('\nHello! Let\'s explore some US bikeshare data!')
    city = get_city()
    print("You selected:", city)
    month = get_month()
    print("You selected:", month)
    day = get_day()
    print("You selected:", day)
    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == [ x.lower() for x in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']].index(day)]
    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', popular_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', popular_start_station)
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', popular_end_station)
    # display most frequent combination of start station and end station trip
    df['Start-End Stations'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Start-End Stations'].mode()[0]
    print('Most Frequent Trip:', popular_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)
    # Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)
    else:
        print('\nGender Types:\nNo data available for this city.')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest Year of Birth:', earliest_year)
        print('Most Recent Year of Birth:', most_recent_year)
        print('Most Common Year of Birth:', most_common_year)
    else:
        print('\nYear of Birth:\nNo data available for this city.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
    # print(load_data('chicago', 'june', 'monday'))