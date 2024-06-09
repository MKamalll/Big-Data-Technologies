import unittest
from io import StringIO
from mrjob.job import MRJob
from mrjob.inline import InlineMRJobRunner
from task1_c1 import StudentAVGGradeCalculator 

class TestStudentAVGGradeCalculator(unittest.TestCase):

    def test_mapper(self):
        # Test with valid input data
        job = StudentAVGGradeCalculator()
        input_data = ("John,Math,85")

        # Set up the job with the input data
        job.sandbox(stdin=StringIO(input_data))

        # Call the mapper function and collect the output
        output = []
        for key, value in job.mapper(None, input_data):
            output.append((key, value))
        

        expected_output = [('John', '85')]

        # Assert that the output matches the expected output
        self.assertEqual(expected_output,output)

if __name__ == '__main__':
    unittest.main()
