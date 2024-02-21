import pandas as pd
import os
import sys
import pyarrow.parquet as pq
import pyarrow as pa
import io
import requests
from datetime import datetime
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

#Function to merge Google Maps Data
def merge_state_dataframes(state_directory, metadata_sites):
    '''
    Function to merge metadata and state dataframes.

    Parameters:
    - state_directory: Path to the directory containing state-specific parquet files.
    - metadata_sites: DataFrame containing metadata from sites.

    Returns:
    - Merged DataFrame combining metadata and state-specific dataframes.
    '''

    # List to store state-specific DataFrames
    state_dataframe_list = []

    # Loop through state-specific parquet files in the given directory
    for state_file in os.listdir(state_directory):
        state_file_path = os.path.join(state_directory, state_file)

        # Read each state-specific parquet file into a DataFrame
        state_dataframe = pd.read_parquet(state_file_path)

        # Extract state name from file path and add it as a new column 'state'
        state_name = state_file_path.split('/')[-1].split('.')[0]
        state_dataframe['state'] = state_name

        # Append the state-specific DataFrame to the list
        state_dataframe_list.append(state_dataframe)

    # Concatenate all state-specific DataFrames along rows
    total_state_dataframe = pd.concat(state_dataframe_list, axis=0, ignore_index=True)

    # Merge metadata_sites DataFrame with the total_state_dataframe on 'gmap_id'
    merged_dataframe = pd.merge(metadata_sites, total_state_dataframe, on='gmap_id', how='inner')

    # Return the merged DataFrame
    return merged_dataframe   


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
    Function to get the city name using reverse geocoding from Bing Maps API.

    Parameters:
    - latitude: Latitude of the location.
    - longitude: Longitude of the location.
    - api_key: API key for Bing Maps API.

    Returns:
    - City name corresponding to the given latitude and longitude.
    """
    # Base URL of Bing Maps reverse geocoding API
    base_url = f'http://dev.virtualearth.net/REST/v1/Locations/{latitude},{longitude}'

    # Parameters for the request
    params = {
        'includeNeighborhood': 1,
        'key': api_key
    }

    # Make request to Bing Maps reverse geocoding API
    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract city name from the response
    if 'resourceSets' in data and len(data['resourceSets']) > 0 and 'resources' in data['resourceSets'][0] and len(data['resourceSets'][0]['resources']) > 0:
        city = data['resourceSets'][0]['resources'][0]['address'].get('locality', '')
        return city
    else:
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

