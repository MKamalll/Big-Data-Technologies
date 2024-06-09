"""
This program users MRJob to calculate the mathematical average of students' scores.
The input data file (student_grades.txt) is provided as a command-line argument to this program.
The data is in text format with the following structure: <student name>, <subject>, <score> 
The output of this program is <student name> <average score> for each student in the input file
In this program, we will use the mapper, combiner and reducer functions.
The result of this program is incorrect calculation of average score for each student 
"""
# Import the MRJob class from the mrjob.job module. MRJob is used to create MapReduce jobs 
from mrjob.job import MRJob
# Import statistics, which is used to calculate mathematical average (mean).  
import statistics
# Import the MRStep to define the steps in which mapper, combiner and reducer are executed 
from mrjob.step import MRStep

# Define a class for calculating the average grade of students, inherit this class from MRJob
class StudentAVGGradeCalculator(MRJob):
  
    # Define mapper method. This function is called for each input record 
    # It takes one text line as input in "value"
    def mapper(self, _, value):
        # "value" is split using the delimiter ',' and stored in "data"
        data=value.split(',')   
        # As per the structure of text file, first word is student name, and third is grade.
        student=data[0].strip()
        grade=data[2].strip()
        # if there are 3 or more words in the text line 
        if len(data)>=3:
            # key value pair returned are <student name> <grade>
            # int() function converts grade value to integer
            yield student, int(grade)

    # Define combiner method. this function take student name as key and all scores for that student as values
    def combiner(self, key, values):
        yield key, statistics.mean(values)

    # Define reducer method. this function take student name as key and all scores for that student as values
    def reducer(self, key, values):
        # Calculate and return the mean of the grades for each student
        yield key, statistics.mean(values)

    # The steps method defines the sequence of operations (map, combine, reduce) to be performed by the MRJob.
    def steps(self):
            return[
            MRStep(mapper=self.mapper, 
            combiner=self.combiner,
            reducer=self.reducer),
            ]

#main program 
if __name__ == '__main__':
    StudentAVGGradeCalculator.run()
