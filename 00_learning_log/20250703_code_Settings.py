# Setting things up  
# [Overview](https://edgartools.readthedocs.io/en/latest/)
# https://github.com/dgunning/edgartools/blob/main/notebooks/Beginners-Guide.ipynb

# 0. Venv and install edgar library
# python3 -m venv .venv
# source .venv/bin/activate
# pip install -U edgartools # latest version -U
# pip install packaging

# 1. Import the edgar library and set up the local storage
# https://edgartools.readthedocs.io/en/latest/getting-started/
from edgar import *

# 2. Tell the SEC who you are (required by SEC regulations)
set_identity("email@address.com")  # Replace with your email

# 3. Set the local storage directory
# This is where the downloaded data will be stored
# download_edgar_data() - this will download the latest data from the SEC (to update the local database)
use_local_storage()

