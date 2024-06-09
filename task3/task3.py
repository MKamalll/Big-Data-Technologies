from pyspark import SparkContext
from operator import add

"""
    Initialize SparkContext
"""

sc = SparkContext('local', 'pyspark')

"""
    Define age_group Function
"""
def age_group(age):
    """
          Assigns an age group label based on the age.
    """
    if age < 10:
        return '0-10'
    elif age < 20:
        return '10-20'
    elif age < 30:
        return '20-30'
    elif age < 40:
        return '30-40'
    elif age < 50:
        return '40-50'
    elif age < 60:
        return '50-60'
    elif age < 70:
        return '60-70'
    elif age < 80:
        return '70-80'
    else:
        return '80+'
    
def parse_with_age_group(data):
    """
        Parse each line of the input data and categorizes it into the correct age group.
        The expected format for the input line is:

                        userid|age|gender|occupation|zipcode
    """
    userid, age, gender, occupation, zipcode = data.split('|')

    """
        The return array will be as following:
                        
                        userid|age_group|gender|occupation|zipcode
    """
    return userid, age_group(int(age)), gender, occupation, zipcode, int(age)

# Load data from u.user file
fs = sc.textFile("file:///Users/kamal/Kamal-Drive/MSc/Modules/Big Data Technologies/Coursework/Coursework-OSK/big_data_mrjob/assigment/task3/u.user")

"""
    Apply the parse_with_age_group function to each record
    a new RDD fs2 is now created with the mapped age-group
"""
fs2 = fs.map(parse_with_age_group)

# Filter the records to include only those in the "40-50" age group
fs4050 = fs2.filter(lambda x: x[1] == "40-50")

# Filter the records to include only those in the 50-60 age group
fs5060 = fs2.filter(lambda x: x[1] == "50-60")

# Extract the distinct occupations list for the 40-50 age group
distOccupation_4050 = fs4050.map(lambda x: x[1]).distinct()

# Extract the distinct occupations list for the 50-60 age group
distOccupation_5060 = fs5060.map(lambda x: x[1]).distinct()

# Create key-value pairs with (occupation, 1)
occupation_4050 = fs4050.map(lambda x: (x[3], 1))
occupation_5060 = fs5060.map(lambda x: (x[3], 1))

# Reduce by key to count the occurrences of each occupation
occupation_count_4050 = occupation_4050.reduceByKey(add)
occupation_count_5060 = occupation_5060.reduceByKey(add)

# Collect the results and sort by frequency in descending order
result_4050 = occupation_count_4050.sortBy(lambda x: -x[1]).collect()
result_5060 = occupation_count_5060.sortBy(lambda x: -x[1]).collect()

# Print the Top 10 results for occupation counts in the 40-50 age group
print("Top 10 occupations in age group 40-50:")
for item in result_4050[:10]:
    print(item)

# Print the Top 10 results for occupation in the 50-60 age group
print("Occupations in age group 50-60:")
for item in result_5060[:10]:
    print(item)

"""
    Stop SparkContext
"""
sc.stop()
