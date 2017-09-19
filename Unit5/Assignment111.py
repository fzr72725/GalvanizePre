import pandas as pd

df = pd.read_csv('data/beds.csv', encoding='utf-8-sig')

def max_facility_id(df):
    '''
    INPUT: DataFrame
    OUTPUT: int

    Write a query on the input data frame that returns the maximum facility id.
    '''
    return df['Facility ID'].max()

def number_of_censuses(df, facility_id):
    '''
    INPUT: DataFrame, int
    OUTPUT: date
    Write a pandas query that returns count of how many censuses were reported
    for the specified facility id
    '''
    return len(df[(df['Facility ID']==facility_id)])

def earliest_census_date(df, facility_id):
    '''
    INPUT: DataFrame, int
    OUTPUT: date
    Write a pandas query that returns the earliest census date for the
    specified facility id
    Note: The dates are currently stored as strings, not date objects
    Hint: pd.to_datetime is very useful
    '''
    return pd.to_datetime(df[(df['Facility ID']==facility_id)]['Bed Census Date']).min()

def beds_top_ten(df, facility_id):
    '''
    INPUT: DataFrame, int
    OUTPUT: date
    Write a pandas query that returns the ten census dates with the highest
    number of available beds for the nursing home with the specified facility id
    REQUIREMENTS:
    Do a filter followed by a sort rather than a sort followed by a merge.
    '''
    return df[(df['Facility ID']==facility_id)].sort_values('Available Residential Beds',ascending=False)[:10]['Bed Census Date']    

if __name__ == '__main__':
    print beds_top_ten(df, facility_id)
