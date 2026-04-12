# Section D: Logging

# Create a logger, set logging levels and custom texts,
# log messages, write log to disks.

# Logging is important because it can provide output to a system,
# or for visualizations. 

# We're going to just log to disk.

# Import the necessary modules.
import logging
import pandas as pd
import os

# Here is a brief debugging pattern for CWD, since filepaths are tricky sometimes.
# Check if the file exists where the filepath points, THEN try to read it.
print("CWD:", os.getcwd())
print("Exists?", os.path.exists("dummy_data/brevened_dataset.csv"))
# df = pd.read_csv("1.4-PythonForDataEngineers/dummy_data/dummy_data.csv")

# Let's load a CSV file.
e_commerce_data_path_csv = "dummy_data/brevened_dataset.csv"
e_commerce_csv_df = pd.read_csv(
    e_commerce_data_path_csv,  encoding='unicode_escape', nrows=1000)

# Now we configure our logger.
logging.basicConfig(
    filename="./logging_data/reading_csvs.log", # Logging output destination file. 
    level=logging.DEBUG,    # Set minimum severity to DEBUG. Lowest level available. 
    format="%(asctime)s - %(levelname)s - %(message)s",  # time level message
)

# Write a lil function. 
def is_positive(number):
    logging.debug(f"Checking if {number} is greater than 4.")
    if number > 4:
        logging.info(f"{number} is greater than 4.")
    else:
        logging.error(f"Error! Number {number} is not greater than 4!")

# Make a list from the Quantity column in the CSV. 
quantities = e_commerce_csv_df["Quantity"].to_list()

# Iterate over item in the list and log the output of the function to the logfile.
for quantity in quantities:
    is_positive(quantity)