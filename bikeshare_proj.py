import pandas as pd
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    CITY_DATA = {'chicago': 'chicago.csv',
                 'new york': 'new_york_city.csv',
                 'washington': 'washington.csv'}
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['trip']=df['Start Station'] + '--' + df['End Station']
    df['travel_time'] = df['End Time'] - df['Start Time']
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]

    return df


def main():
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower()
        if city not in ('chicago', 'new york', 'washington'):
            continue
        else:
            break
    while True:
        ask_filter = input('Would you like to filter the data by month, day, or both or all (for no filter at all?\n').lower()
        if ask_filter not in ('month', 'day', 'all','both'):
            continue
        else:
            if ask_filter == 'month':
                while True:
                    month = input('Which month - January, February, March, April, May, or June?\n').lower()
                    if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                        break
                    else:
                        continue
                day = 'all'
            elif ask_filter == 'day':
                while True:
                    day = input('Which day - Monday  , Tuesday ...  Sunday ?\n').capitalize()
                    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                        break
                    else:
                        continue
                month = 'all'
            elif ask_filter == 'both':
                while True:
                    month = input('Which month - January, February, March, April, May, or June?\n').lower()
                    if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                        break
                    else:
                        continue
                while True:
                    day = input('Which day - Monday  , Tuesday ...  Sunday ?\n').capitalize()
                    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                        break
                    else:
                        continue
            elif ask_filter == 'all':
                day = 'all'
                month = 'all'
            break
    print(city, month, day)
    Filtered_data = load_data(city, month, day)


    print('Printing Statistics : ......')
    print('=============================')
    print('Popular times of travel: ')
    print('-------------------------')
    common_month = Filtered_data['month'].mode()[0]
    print('Most common month is : ', common_month)
    print('Count of most common month is : ', Filtered_data['month'].value_counts()[common_month])
    common_day = Filtered_data['day_of_week'].mode()[0]
    print('most common day of week is : ', common_day)
    print('Count of most common day of week is : ', Filtered_data['day_of_week'].value_counts()[common_day])
    common_hour = Filtered_data['hour'].mode()[0]
    print('Most common hour of day is : ', common_hour)
    print('Count of most common hour of day is : ', Filtered_data['hour'].value_counts()[common_hour])
    print('============================================================')

    print('Popular trips: ')
    print('---------------')
    common_start = Filtered_data['Start Station'].mode()[0]
    print('Most common start station is  : ', common_start)
    print('Count of most common start station is : ', Filtered_data['Start Station'].value_counts()[common_start])
    common_end = Filtered_data['End Station'].mode()[0]
    print('Most common end station is : ', common_end)
    print('Count of most common end station is : ', Filtered_data['End Station'].value_counts()[common_end])
    common_trip = Filtered_data['trip'].mode()[0]
    print('Most common trip from start to end  is : ', common_trip)
    print('Count of Most common trip from start to end  is : ', Filtered_data['trip'].value_counts()[common_trip])
    print('============================================================')
    print('Stats travel times: ')
    print('-------------------------')
    print('total travel time is : ', Filtered_data['travel_time'].sum())
    print('average travel time is : ', Filtered_data['travel_time'].mean())
    print('============================================================')
    print('User Stats Info: ')
    print('-----------------')
    print('Count of each user type : ')
    user_count = Filtered_data['User Type'].value_counts()
    for i in range(0, len(user_count)):
        print('     ', user_count.index[i], user_count[i])

    if city in ['Chicago', 'New York']:
        gender_count = Filtered_data['Gender'].value_counts()
        print('Most common Gender is : ', gender_count)
        print('Count of Most common Gender is : ', Filtered_data['Gender'].value_counts()[gender_count])
        common_year = Filtered_data['Birth Year'].mod()[0]
        earliest_year = Filtered_data['Birth Year'].min()
        recent_year = Filtered_data['Birth Year'].min()
        print('Most common Year of birth is : ', common_year)
        print('Most early Year of birth is : ', earliest_year)
        print('Most recent Year of birth is : ', recent_year)

if __name__ == '__main__':
    while True:
        main()
        while True:
            print('=======================================================')
            print('=======================================================')
            print('=======================================================')
            answer = str(input('Do you want to Run again? (y/n): '))
            if answer not in ('y', 'n'):
                continue
            else:
                break
        if answer == 'y':
            continue
        else:
            print("Goodbye")
            break
