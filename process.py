import csv

# Constants for each column used in this module
COLUMN_SURVIVED = 1
COLUMN_CLASS = 2
COLUMN_NAME = 3
COLUMN_SEX = 4
COLUMN_AGE = 5


def load_data(file_path):
    """
    Load the records from the data file whose path is provided by the file_path parameter.

    :param file_path:
    :return:
    """
    # TODO: Your code here (remove pass below)
    pass


def extract_passengers(records):
    """
    Task: Extract the name of each passenger from the records.

    The records parameter contains a list of passenger records.
    Each record is a list of values for an individual passenger.
    The passenger name is the fourth value (index 3) in the record.
    For example:
        records[0] is the first passenger, records[1] is the second passenger, and so on
        If passenger = records[0] then passenger[3] is the passenger's name

    Use an appropriate loop to iterate through each record in records and extract the name of the passenger.
    Return a list containing the passenger names.

    :param records: A list of passenger records
    :return: A list of passenger names
    """
    # TODO: Your code here (remove pass below)
    pass


def count_survivors(records):
    """
    Task: Count the number of passengers that survived. Return the count.

    The records parameter contains a list of passenger records.
    Each record is a list of values for an individual passenger.
    The passenger's survival status is the second value (index 1) in the record.
    For example:
        records[0] is the first passenger, records[1] is the second passenger, and so on
        If passenger = records[0] then passenger[1] is the passenger's survival status
    A passenger survived if the passenger's survival status is 1

    Use an appropriate loop to iterate through each record in records and count the number of passengers that
    survived. Return the count.

    :param records: A list of passenger records
    :return: An integer corresponding to the number of passengers that survived.
    """
    # TODO: Your code here (remove pass below)
    pass


def count_per_sex(records):
    """
    Task: Count the number of passengers per sex. Return the counts.

    The records parameter contains a list of passenger records.
    Each record is a list of values for an individual passenger.
    The passenger's sex is the fifth value (index 4) in the record.
    For example:
        records[0] is the first passenger, records[1] is the second passenger, and so on
        If passenger = records[0] then passenger[4] is the passenger's sex

    Use an appropriate loop to iterate through each record in records and count the number of passengers that
    are male and female. Return the male and female counts.

    :param records: A list of passenger records
    :return: The male and female counts
    """
    # TODO: Your code here (remove pass below)
    pass


# Add additional functions below.
# For example, a function to count the number of passengers of each class.
