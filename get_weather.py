import os
from wwo_hist import retrieve_hist_data

os.chdir("C:/Users/stapl/Downloads/gpx_to_csv")

frequency=1
start_date = '22-AUG-2021'
end_date = '22-AUG-2021'
api_key = os.environ["API_KEY"]
location_list = ['22801']


print("Retrieving data using key " + api_key + '...')
hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)
