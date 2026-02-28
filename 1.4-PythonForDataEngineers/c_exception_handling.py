# Section C: Exception Handling

# We are going to raise our own Exceptions, catch a thrown Exception,
# and create our own custom Exception Class.

# Import pandas.
import pandas

# We're going to try to read two CSV files. One exists, one doesn't! 
# These Strings are filepaths to our CSV's.
e_commerce_data_path_csv = "./dummy_data/dummy_data.csv"    # File exists.
e_commerce_data_fake_path_csv = "./dummy_data/fake_data.csv"  # File doesn't exist.

# Try-Except example, raise BaseException. We try and fail to read a nonexistent file.
try:
    e_commerce_csv_df = pandas.read_csv(
        e_commerce_data_fake_path_csv,  encoding='unicode_escape', nrows=1000)
except: # Catch the exception, print something.
    print(
        "Please provide a correct path to the file!"
    )
# > Please provide a correct path to the file!

# Now raise an Exception that also provides information about the error. 
try:
    e_commerce_csv_df = pandas.read_csv(
        e_commerce_data_fake_path_csv,  encoding='unicode_escape', nrows=1000)
# Catch the error.
except FileNotFoundError as error:
    print(
        # f string for better formatting.
        f"{error}, please provide a correct path to the file!"
    )
# > [Errno 2] No such file or directory: 'fake_data.csv', please provide a correct path to the file!

# We are catching errors without quitting the program. We have controlled exits, controlled failures.

# Now create a custom Exception. It has as a base class the standard Exception class.
class FileHasToManyRows(Exception):
    """Exception raised if file has too many rows.

    Attributes:
        salary -- input csv file
        message -- error description
    """

    def __init__(self, number_of_rows):
        self.number_of_rows = number_of_rows
        self.message = f"Csv file has too many rows, max rows is 1000 and the file has {self.number_of_rows}"

        super().__init__(self.message)


try:
    print("Now trying the excessive number of rows exception.")
    e_commerce_csv_df = pandas.read_csv(
        e_commerce_data_path_csv,  encoding='unicode_escape', nrows=1100)

    number_of_rows = len(e_commerce_csv_df)

    if number_of_rows > 1000:
        raise FileHasToManyRows(number_of_rows)
# Catch the error.
except FileNotFoundError as error:
    print(
        f"{error}, please provide a corect path to the file!"
    )
# > Traceback (most recent call last):
# >   File "<string>", line 6, in <module>
# > FileHasToManyRows: Csv file has too many rows, max rows is 1000 and the file has 1100