import os
from dotenv import load_dotenv

# load enviornment variables
load_dotenv()

#  Store USGS Water Data API Key    
water_key = os.getenv('USGS_WATER_DATA_API')
