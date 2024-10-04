import unittest
from unittest.mock import patch
import io
import studentgrade

class TestMainFunction(unittest.TestCase):
    
    # Test with valid inputs
    @patch('builtins.input', side_effect=['3', '85', '90', '75'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_input(self, mock_stdout, mock_input):
        """
        Test for valid input: 3 students with grades 85, 90, 75.
        Expected class average: 83.33
        """
        # Call the function 'main()' from studentgrade.py
        studentgrade.main()

        # Retrieve the captured output
        output = mock_stdout.getvalue()

        # Check if the printed output is as expected
        self.assertIn("The class average is 83.33\n", output)

    # Test for invalid input followed by valid input
    @patch('builtins.input', side_effect=['-1', '3', '85', '90', '75'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_and_valid_input(self, mock_stdout, mock_input):
        """
        Test for invalid input followed by valid input.
        -1 is an invalid number of students, followed by valid input.
        """
        # Call the function 'main()' from studentgrade.py
        studentgrade.main()

        # Retrieve the captured output
        output = mock_stdout.getvalue()

        # Check if the printed output is as expected
        self.assertIn("Invalid input.\n", output)  # Include the period
        self.assertIn("The class average is 83.33\n", output)

    # Test for invalid grades (e.g., grade > 100 or < 0)
    @patch('builtins.input', side_effect=['2', '105', '82', '-10', '70'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_grade(self, mock_stdout, mock_input):
        """
        Test for invalid grade input.
        Grades 105 and -10 should trigger an error, followed by valid grades.
        """
        # Call the function 'main()' from studentgrade.py
        studentgrade.main()

        # Retrieve the captured output
        output = mock_stdout.getvalue()

        # Check if the printed output is as expected
        self.assertIn("Grade must be between 0 to 100.", output)
        self.assertIn("The class average is 76.00", output)

if __name__ == "__main__":
    unittest.main()
