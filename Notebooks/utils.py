import pandas as pd
import os
import sys
import pyarrow.parquet as pq
import pyarrow as pa
import io
import requests
from datetime import datetime
from geopy.distance import geodesic
from textblob import TextBlob
# Warnings ignore
import warnings
warnings.filterwarnings("ignore")



def read_parquet_file(file_path):
    """
    Read a Parquet file from the specified path.

    Parameters:
    file_path (str): The path to the Parquet file to be read.

    Returns:
    pyarrow.Table: The data table contained in the Parquet file.
    """
    try:
        parquet_table = pq.read_table(file_path)
        return parquet_table
    except Exception as e:
        print("Error reading Parquet file:", e)
        return None
    

    
def json_to_dataframe(main_folder_path):
    '''
    Function to read JSON files from a directory, process them,
    and return a dictionary of Pandas DataFrames.

    Parameters:
    - main_folder_path (str): The path to the main folder containing subfolders with JSON files.

    Returns:
    - dicc (dict): A dictionary where keys are folder names and values are Pandas DataFrames
                  containing processed data from corresponding JSON files.
    '''
    # Dictionary to store DataFrames, where keys are folder names
    dicc = {}

    # Loop through items in the main folder
    for sub_folder in os.listdir(main_folder_path):
        sub_folder_path = os.path.join(main_folder_path, sub_folder)

        # Check if the item is a subfolder
        if os.path.isdir(sub_folder_path):
            # Extract folder name from subfolder and initialize an empty list for DataFrames
            folder_name = sub_folder.split('-')[1]

            # List to store DataFrames, where keys are the .json files
            dataframe_list = []

            # Loop through json files in the subfolder
            for json_file in os.listdir(sub_folder_path):
                json_file_path = os.path.join(sub_folder_path, json_file)

                # Read each json file into a DataFrame and append to the list
                dataframe_aux = pd.read_json(json_file_path, lines=True)
                dataframe_list.append(dataframe_aux)

            # Concatenate all DataFrames in the list along rows.
            dataframe_object = pd.concat(dataframe_list, axis=0, ignore_index=True)
            dataframe_object['date'] = dataframe_object['time'].apply(mili_to_datetime)

            # Store the resulting DataFrame in the dictionary with the folder name as the key
            dicc[folder_name] = dataframe_object
            print(f'Data from {sub_folder} successfully loaded')

        # Check if the item is a single json file
        elif sub_folder_path.endswith('.json'):

            # Read the json file into a DataFrame and store it in the dictionary
            dataframe_aux = pd.read_json(sub_folder_path, lines=True)
            dataframe_object = pd.concat([dataframe_aux], axis=0, ignore_index=True)
            # Extract json file name and use it as the key for the dictionary
            json_name = sub_folder_path.split('/')[-1]
            print(f'Loading File JSON = {json_name}')
            folder_name = main_folder_path.split('/')[-1]  # name for dataset
            dicc[folder_name] = dataframe_object

    # Return the dictionary containing DataFrames
    return dicc



def others_to_dataframe(main_folder_path):
    '''Function that focuses on making a list of
    folder's items and looks for those json files
    to transform them into DataFrames '''

    # Dictionary to store DataFrames, where keys are folder names
    dicc = {}

    # Loop through items in the main folder
    for sub_folder in os.listdir(main_folder_path):
        sub_folder_path = os.path.join(main_folder_path, sub_folder)

        # Check if the item is a subfolder
        if os.path.isdir(sub_folder_path):
            # Extract folder name from subfolder and initialize an empty list for DataFrames
            folder_name = sub_folder.split('-')[1]

            # List to store DataFrames, where keys are the .json files
            dataframe_list = []

            # Loop through json files in the subfolder
            for json_file in os.listdir(sub_folder_path):
                json_file_path = os.path.join(sub_folder_path, json_file)

                # Read each json file into a DataFrame and append to the list
                dataframe_aux = pd.read_json(json_file_path, lines=True)
                dataframe_list.append(dataframe_aux)

            # Concatenate all DataFrames in the list along rows, drop specified columns, and duplicates
            dataframe_object = pd.concat(dataframe_list, axis=0, ignore_index=True)
            dataframe_object['date'] = dataframe_object['time'].apply(mili_to_datetime)
           

            # Store the resulting DataFrame in the dictionary with the folder name as the key
            dicc[folder_name] = dataframe_object
            print(f'Data from {sub_folder} successfully loaded')

        # Check if the item is a single json file
        elif sub_folder_path.endswith('.json'):

            # Read the json file into a DataFrame and store it in the dictionary
            dataframe_aux = pd.read_json(sub_folder_path, lines=True)
            dataframe_object = pd.concat([dataframe_aux], axis=0, ignore_index=True)

            # Extract json file name and use it as the key for the dictionary
            json_name = sub_folder_path.split('/')[-1]
            print(f'Loading File JSON = {json_name}')
            folder_name = sub_folder_path.split('/')[-1]  # name for dataset
            dicc[folder_name] = dataframe_object

        elif sub_folder_path.endswith('.pkl'):
            dataframe_aux = pd.read_pickle(sub_folder_path)
            dataframe_object = pd.concat([dataframe_aux], axis=0, ignore_index=True)
            dataframe_object = dataframe_object.loc[:, ~dataframe_object.columns.duplicated()]

            # Extract pickle file name and use it as the key for the dictionary
            pickle_name = sub_folder_path.split('/')[-1]
            print(f'Loading File Pickle = {pickle_name}')
            dicc[pickle_name] = dataframe_object

        elif sub_folder_path.endswith('.parquet'):
            parquet_name = sub_folder_path.split('/')[-1].split('.')[0]
            dataframe_object = pd.read_parquet(sub_folder_path)
            print(f'loading File Parquet = {parquet_name}')
            dicc[parquet_name] = dataframe_aux

    # Return the dictionary containing DataFrames
    return dicc
                                                                      



def dataframe_to_parquet(dicc, subfolder_name):
    '''
    Function to save Pandas DataFrames as Parquet files.

    Parameters:
    - dicc (dict): A dictionary where keys are folder names and values are Pandas DataFrames.
    - subfolder_name (str): The desired subfolder name to be used in the file path.

    Returns:
    - None
    '''
    for key, dataframe_aux in dicc.items():
        # Construct the dynamic file path with the specified subfolder name
        file_path = f'/lakehouse/default/Files/df_database/{subfolder_name}/{key}.parquet'

        # Convert Pandas DataFrame to PyArrow Table and write to Parquet file
        #dataframe_aux.drop_duplicates(inplace=True)
        table = pa.Table.from_pandas(dataframe_aux)
        pq.write_table(table, file_path)

        print(f'Dataframes saved successfully in df_database/{subfolder_name}')




def calculate_original_memory_usage(main_folder_path):
    '''
    Function to calculate the total amount of memory usage
    by original dataframes files.

    Parameters:
    - main_folder_path: Path to the main folder containing original dataframe files.

    Returns:
    - Total memory usage in megabytes.
    '''

    # Initialize size variable to store total memory usage
    size = 0 

    # Loop through each DataFrame in the list
    for sub_folder in os.listdir(main_folder_path):
        sub_folder_path = os.path.join(main_folder_path, sub_folder)

        if os.path.isdir(sub_folder_path):
            for file_name in os.listdir(sub_folder_path):
                current_file_path = os.path.join(sub_folder_path, file_name)

                # Get the size of the file in megabytes and add to the total size
                amount = os.path.getsize(current_file_path) / (1024 * 1024)
                size += amount

        elif sub_folder_path.endswith('.json') or sub_folder_path.endswith('.pkl') or sub_folder_path.endswith('.parquet'):
            # Get the size of the file in megabytes and add to the total size
            amount = os.path.getsize(sub_folder_path) / (1024 * 1024)
            size += amount

    # Return the total memory usage
    return size


def calculate_parquet_memory_usage(main_folder_path):
    '''
    Function to calculate the total amount of memory usage
    by parquet files.

    Parameters:
    - main_folder_path: Path to the main folder containing parquet files.

    Returns:
    - Total memory usage in megabytes.
    '''

    # Initialize size variable to store total memory usage
    size = 0

    # Loop through each Parquet file in the specified folder
    for sub_folder in os.listdir(main_folder_path):
        sub_folder_path = os.path.join(main_folder_path, sub_folder)

        if os.path.isdir(sub_folder_path):
            for parquet_file in os.listdir(sub_folder_path):
                parquet_path = os.path.join(sub_folder_path, parquet_file) 

                # Get the size of the Parquet file in megabytes and add to the total size
                amount = os.path.getsize(parquet_path) / (1024 * 1024)
                size += amount 

    # Return the total memory usage
    return size



def data_summ(df, title=None):
    '''
    Function to provide detailed information about the dtype, null values,
    and outliers for each column in a DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame for which information is to be generated.
    - title (str, optional): Title to be used in the summary. If None, the title will be omitted.

    Returns:
    - df_info (pd.DataFrame): A DataFrame containing information about each column,
                              including data type, non-missing quantity, percentage of
                              missing values, missing quantity, and information about outliers.
    '''
    info_dict = {"Column": [], "Data_type": [], "No_miss_Qty": [], "%Missing": [], "Missing_Qty": []}

    for column in df.columns:
        info_dict["Column"].append(column)
        info_dict["Data_type"].append(df[column].apply(type).unique())
        info_dict["No_miss_Qty"].append(df[column].count())
        info_dict["%Missing"].append(round(df[column].isnull().sum() * 100 / len(df), 2))
        info_dict['Missing_Qty'].append(df[column].isnull().sum())

  
    df_info = pd.DataFrame(info_dict)

    if title:
        print(f"{title} Summary")
        print("\nTotal rows: ", len(df))
        print("\nTotal full null rows: ", df.isna().all(axis=1).sum())

    print(df_info.to_string(index=False))
    print("=====================================")

    return df_info



def data_summ_on_parquet(folder_path):
    '''
    Function to apply data_summ function to each Parquet file in a folder.

    Parameters:
    - folder_path (str): The path to the folder containing Parquet files.

    Returns:
    - summaries (list): A list of DataFrames containing the summary information for each Parquet file.
    '''
    summaries = []

    # Loop through each file in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Check if the file is a Parquet file
        if file_name.endswith('.parquet'):
            # Read the Parquet file into a DataFrame
            df = pq.read_table(file_path).to_pandas()

            # Get the title for the DataFrame based on the file name
            title = file_name.replace('.parquet', '')

            # Apply data_summ function to the DataFrame
            summary = data_summ(df, title=title)

            # Append the summary DataFrame to the list
            summaries.append(summary)

    return summaries



# Function to convert milliseconds to datetime format
def mili_to_datetime(dato):

    '''This function is useful for converting time values from milliseconds to a human-readable datetime format,
 handling missing values appropriately. 
Note that the code assumes the presence of the pandas library (pd) and the datetime module, 
so make sure to import these libraries before using this function.'''

    # Check if the input is a missing value (NaN)
    if pd.isna(dato):
        return None

    try:
        # Convert milliseconds to seconds
        time = dato / 1000

        # Convert the time in seconds to a UTC datetime string format ('YYYY-MM-DD HH:MM:SS')
        date_time = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

        # Return the formatted datetime string
        return date_time
    except ValueError:
        # If there's an error during the conversion, return None
        return None
    

#Function to manage duplicates values
def duplicates(df, column):
    '''
    Checks and displays duplicate rows in a DataFrame based on a specific column.

    This function takes as input a DataFrame and the name of a specific column.
    Then, identify duplicate rows based on the content of the specified column,
    filters and sorts them for easier comparison.

    Parameters:
        df (pandas.DataFrame): The DataFrame to search for duplicate rows.
        column (str): The name of the column based on which to check for duplicates.

    Returns:
        pandas.DataFrame or str: A DataFrame containing the filtered and sorted duplicate rows,
        lists for inspection and comparison, or the message "No Duplicates" if no duplicates are found.
    '''
    # Duplicate rows are filtered out
    duplicated_rows = df[df.duplicated(subset=column, keep=False)]
    if duplicated_rows.empty:
        return "There are no duplicates"
    
    # sort duplicate rows to compare with each other
    duplicated_rows_sorted = duplicated_rows.sort_values(by=column)
    return duplicated_rows_sorted



#Function tu manage null values
def replace_all_nulls(df):
    '''
    Receives a df as parameter and fill all the null values per column depending on their dType
    '''

    for column in df.columns:
        dtype = df[column].apply(type).unique()

        if None in dtype:  # Manejar valores None
            df[column] = df[column].fillna('ND')
        elif dtype[0] == str: 
            df[column] = df[column].fillna('ND')
        elif dtype[0] == float:
            mean = df[column].mean()
            df[column] = df[column].fillna(mean)
        elif dtype[0] == list:
            df[column] = df[column].fillna('ND')
            
    return df

#Function to conctact Google Maps States Data
def clean_states_and_concat(folder_path):

    """
This function takes a folder_path as input, which represents the directory containing multiple parquet files, each corresponding to a state's data.

For each parquet file in the specified folder, the function reads the data into a DataFrame, extracts the state name from the file name, and adds it as a new column named 'state' to the DataFrame.

After processing all the parquet files, it concatenates all the DataFrames along the rows axis (axis=0) to create a single DataFrame containing data from all states. Finally, it returns this concatenated DataFrame.
"""
   
    concat_list = []

    for parquet in os.listdir(folder_path):
        aux_path = os.path.join(folder_path, parquet)
        df = pd.read_parquet(aux_path)
       # Agregar el nombre del estado como nueva columna
        state_name = parquet.split('.')[0]
        df['state'] = state_name

        concat_list.append(df)
    
    dataframe_object = pd.concat(concat_list, axis=0, ignore_index=True)
    return dataframe_object  


def clean_sites(file_path, keywords):

    """
This function filters rows from a DataFrame based on the presence of certain keywords in the 'category' column.

Parameters:
- file_path: Path to the parquet file containing the DataFrame to be cleaned.
- keywords: List of keywords to filter rows based on their presence in the 'category' column.

Returns:
- DataFrame: A new DataFrame containing rows where the 'category' column contains any of the specified keywords.
"""
    # Read the DataFrame from the parquet file
    df_sitios = pd.read_parquet(file_path)

    # List to store indices of rows to be filtered
    filas_a_filtrar = []

    # Iterate over each row in the DataFrame
    for row in df_sitios.itertuples():
        category = row.category
        index = row.Index
    
        # Check if 'category' is not None
        if category is not None:
            # Iterate over each keyword
            for key in keywords:
                # Check if any keyword is in the 'category' list
                if any(key in item for item in category):
                    filas_a_filtrar.append(index)

    # Create a new DataFrame with the filtered rows
    df_filtrado = df_sitios.loc[df_sitios.index.isin(filas_a_filtrar)]
    df_filtrado.reset_index(drop=True, inplace=True)

    return df_filtrado



def drop_columns(dataframe, columns_to_drop):
    """
    Drop the specified columns from a DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame from which columns will be dropped.
    columns_to_drop (list): List of column names to be dropped.

    Returns:
    pd.DataFrame: The resulting DataFrame after dropping the columns.
    """
    try:
        dataframe = dataframe.drop(columns=columns_to_drop)
        return dataframe
    except Exception as e:
        print("Error dropping columns:", e)
        return None
    


def explode_column(dataframe, column_name):
    """
    Explode a column in a DataFrame containing lists into multiple rows.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the column to be exploded.
    column_name (str): The name of the column to be exploded.

    Returns:
    pd.DataFrame: The DataFrame with the specified column exploded into multiple rows.
    """
    try:
        exploded_df = dataframe.explode(column_name)
        return exploded_df
    except Exception as e:
        print("Error exploding column:", e)
        return None
    

def group_column(dataframe, column_name):
    """
    Group a DataFrame by a specified column and aggregate values into a list.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the exploded column.
    column_name (str): The name of the column to be grouped.

    Returns:
    pd.DataFrame: The DataFrame with the specified column grouped back into a list.
    """
    try:
        # Agrupar la columna
        grouped_column = dataframe.groupby(dataframe.index)[column_name].agg(list)

        # Combinar el DataFrame original con la columna agrupada
        grouped_df = pd.merge(dataframe.drop(columns=[column_name]).drop_duplicates(), grouped_column, left_index=True, right_index=True)
        return grouped_df
    except Exception as e:
        print("Error grouping column:", e)
        return None



def get_city(latitude, longitude, api_key):
    """
    Function to get the city name using reverse geocoding from Google Maps API.

    Parameters:
    - latitude: Latitude of the location.
    - longitude: Longitude of the location.
    - api_key: API key for Google Maps API.

    Returns:
    - City name corresponding to the given latitude and longitude.
    """
    # Base URL of Google Maps reverse geocoding API
    base_url = f'https://maps.googleapis.com/maps/api/geocode/json'

    # Parameters for the request
    params = {
        'latlng': f'{latitude},{longitude}',
        'key': api_key
    }

    # Make request to Google Maps reverse geocoding API
    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract city name from the response
    if 'results' in data and len(data['results']) > 0:
        for component in data['results'][0]['address_components']:
            if 'locality' in component['types']:
                return component['long_name']
    return None

def city_dataframe(df1, file_location, api_key):
    """
    Function to load or create the city DataFrame.

    If the specified file exists, load the DataFrame from the file.
    Otherwise, execute the get_city function to obtain the DataFrame and save it to the specified file.

    Parameters:
    - df1: DataFrame containing the data.
    - file_location: Location of the file to load or save.
    - api_key: API key for Bing Maps API.

    Returns:
    - DataFrame containing city information.
    """
    # Check if the specified file exists
    if os.path.exists(file_location):
        # If exists, load the DataFrame from the Parquet file
        df_city = pd.read_parquet(file_location)
    else:
        # If not exists, execute get_city function to obtain the DataFrame
        df_city = df1.copy()  # Copy the original DataFrame
        df_city['City'] = df_city.apply(lambda row: get_city(row['latitude'], row['longitude'], api_key), axis=1)
        
        # Save the DataFrame to the specified file
        df_city.to_parquet(file_location)
    
    return df_city


def get_state(latitude, longitude, api_key):
    """
    Function to get the state name using reverse geocoding from Google Maps API.

    Parameters:
    - latitude: Latitude of the location.
    - longitude: Longitude of the location.
    - api_key: API key for Google Maps API.

    Returns:
    - State name corresponding to the given latitude and longitude.
    """
    # Base URL of Google Maps reverse geocoding API
    base_url = f'https://maps.googleapis.com/maps/api/geocode/json'

    # Parameters for the request
    params = {
        'latlng': f'{latitude},{longitude}',
        'key': api_key
    }

    # Make request to Google Maps reverse geocoding API
    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract state name from the response
    state_name = None
    if 'results' in data and len(data['results']) > 0:
        for component in data['results'][0]['address_components']:
            if 'administrative_area_level_1' in component['types']:
                state_name = component['long_name']
                break
    return state_name

def state_dataframe(df1, file_location, api_key):
    """
    Function to load or create the state DataFrame.

    If the specified file exists, load the DataFrame from the file.
    Otherwise, execute the get_state function to obtain the DataFrame and save it to the specified file.

    Parameters:
    - df1: DataFrame containing the data.
    - file_location: Location of the file to load or save.
    - api_key: API key for Google Maps API.

    Returns:
    - DataFrame containing state information.
    """
    # Check if the specified file exists
    if os.path.exists(file_location):
        # If exists, load the DataFrame from the Parquet file
        df_state = pd.read_parquet(file_location)
    else:
        # If not exists, execute get_state function to obtain the DataFrame
        df_state = df1.copy()  # Copy the original DataFrame
        df_state['State'] = df_state.apply(lambda row: get_state(row['latitude'], row['longitude'], api_key), axis=1)
        
        # Save the DataFrame to the specified file
        df_state.to_parquet(file_location)
    
    return df_state   



def sentiment_analysis(file_path, df):
    """
    Perform sentiment analysis on the text data in the given DataFrame.
    If the file specified by file_path exists, read it and return a DataFrame called 'total_sa'.
    If the file does not exist, apply sentiment analysis to the provided DataFrame and save the result as a parquet file.

    Args:
    file_path (str): Path to the file.
    df (pd.DataFrame): DataFrame containing the text data.

    Returns:
    pd.DataFrame: DataFrame containing the sentiment analysis results.
    """

    # Check if file exists
    if os.path.exists(file_path):
        # Read the file
        total_sa = pd.read_parquet(file_path)
    else:
        # Apply sentiment analysis
        df['Sentiment_Analysis'] = df['Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity if pd.notna(x) and x != 'No data' else None)

        # Define a function to map sentiment scores
        def map_sentiment(score):
            if score is None:
                return 1  # If the review is absent or 'No data', take the value of 1
            elif score < 0:
                return 0  # bad
            elif score == 0:
                return 1  # neutral
            else:
                return 2  # positive

        # Apply mapping function to 'Sentiment_Analysis' column
        df['Sentiment_Analysis'] = df['Sentiment_Analysis'].apply(map_sentiment)

        # Save DataFrame as parquet file
        df.to_parquet(file_path)
        total_sa = df

    return total_sa

def divide_by_state(df, state_column='State'):
    """
    This function divides a DataFrame into multiple DataFrames based on the unique values
    in the specified state column.

    Parameters:
        df (DataFrame): The DataFrame to be divided.
        state_column (str): The name of the column containing state information.

    Returns:
        dict: A dictionary where keys are unique states and values are DataFrames corresponding
        to each state.
    """
    # Get the unique values of the state column
    states = df[state_column].unique()
    
    # Create a dictionary to store DataFrames divided by state
    dataframes_by_state = {}
    
    # Iterate over each unique state
    for state in states:
        # Filter the DataFrame by the current state
        df_state = df[df[state_column] == state].copy()
        
        # Select the required columns
        required_columns = ['Business_Name', 'Latitude', 'Longitude', 'Category']
        df_state = df_state[required_columns]
        
        # Add the DataFrame to the dictionary, with the name corresponding to the state
        dataframes_by_state[state] = df_state
        
        # Print a message indicating that the DataFrame for the current state was generated successfully
        print(f"{state} DataFrame was generated successfully.")
    
    return dataframes_by_state


    

def calculate_distances(df):
    """
    This function calculates the minimum distances from each non-touristic business to the nearest
    touristic business and stores the result in a DataFrame.

    Parameters:
        df (DataFrame): The DataFrame containing business data.

    Returns:
        DataFrame: The original DataFrame with additional columns for minimum distance,
        closest touristic business, and its category.
    """
    # Touristic categories
    tourist_categories = ['Museum', "Shopping mall", 'Roller coaster', 'Park', 'National forest', 'Art gallery', 'Zoo']
    
    # Create new columns to store minimum distance and the name of the closest touristic business
    df['Distance'] = None  # Initialize with None
    df['Closest_Touristic_Business'] = ''
    df['Tourism_Cat'] = ''
    
    # Filter businesses by touristic categories
    tourist_businesses = df[df['Category'].isin(tourist_categories)]
    other_businesses = df[~df['Category'].isin(tourist_categories)]
    
    # Iterate over each non-touristic business
    for index_other, other_business in other_businesses.iterrows():
        # Initialize minimum distance as infinity
        min_distance = float('inf')
        closest_business_name = ''
        tourism_category = ''
        
        # Iterate over each touristic business
        for index_tourist, tourist_business in tourist_businesses.iterrows():
            # Calculate geodesic distance between businesses
            distance = geodesic((other_business['Latitude'], other_business['Longitude']), 
                                 (tourist_business['Latitude'], tourist_business['Longitude'])).kilometers
            
            # If the distance is less than the minimum found so far for this non-touristic business,
            # update the minimum distance, the name of the closest touristic business, and its category
            if distance < min_distance:
                min_distance = distance
                closest_business_name = tourist_business['Business_Name']
                tourism_category = tourist_business['Category']
        
        # Assign the minimum distance, the name of the closest touristic business, and its category to the current non-touristic business
        df.at[index_other, 'Distance'] = min_distance
        df.at[index_other, 'Closest_Touristic_Business'] = closest_business_name if min_distance != float('inf') else 'itself'
        df.at[index_other, 'Tourism_Cat'] = tourism_category
    
    return df


def distances(file_location, df):
    """
    This function loads a DataFrame from a file if the file exists at the specified location,
    otherwise, it applies the calculate_distances function to the DataFrame and saves the result
    to the file location.

    Parameters:
        file_location (str): The location of the file to load or save.
        df (DataFrame): The DataFrame to process.

    Returns:
        DataFrame: The DataFrame loaded from the file or the result of calculate_distances function.
    """
    # Check if the file exists at the specified location
    if os.path.exists(file_location):
        # Load the DataFrame from the file
        df_state = pd.read_parquet(file_location)
        print(f"Dataframe {df} was successfully loaded from {file_location}")
    else:
        # Apply the calculate_distances function if the file does not exist
        df_state = calculate_distances(df)
        # Save the resulting DataFrame to the specified location
        df_state.to_parquet(file_location)
        print(f"Dataframe {df} was successfully generated and saved to {file_location}")
    
    return df_state

