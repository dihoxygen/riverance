
import config
from dataretrieval import waterdata

'''
From the USGS Github Demo Notebook:

Data endpoints:
- get_daily() - Daily values for monitoring locations, parameters, stat codes, and more.
- get_continuous() - Instantaneous values for monitoring locations, parameters, statistical codes, and more.
- get_monitoring_locations()- Monitoring location information such as name, monitoring location ID, latitude, longitude, huc code, site types, and more.
- get_time_series_metadata() - Timeseries metadata across monitoring locations, parameter codes, statistical codes, and more.
    --Can be used to answer the question: what types of data are collected at my site(s) of interest and over what time period are/were they collected?
- get_latest_continuous() - Latest instantaneous values for requested monitoring locations, parameter codes, statistical codes, and more.
- get_latest_daily() - Latest daily values for requested monitoring locations, parameter codes, statistical codes, and more.
- get_field_measurements() - Physically measured values (a.k.a discrete) of gage height, discharge, groundwater levels, and more for requested monitoring locations.
- get_samples() - Discrete water quality sample results for monitoring locations, observed properties, and more.
'''

pcodes, metadata = waterdata.get_reference_table('parameter-codes')
display(pcodes.head())
