import unittest
from add_tw_to_html import add_tailwind

# initiating test class for unittest
class TestAddTailwind(unittest.TestCase):

    # Test method for invalid directory
    def test_invalid_path(self):
        success, error = add_tailwind('invalid/directory')
        self.assertEqual(success, 'Directory does not exist')
        self.assertIsNone(error)

    # Test method for directory without HTML files
    def test_directory_with_no_html_files(self):
        success, error = add_tailwind('path_to_directory_with_no_html_files')  # replace with actual path
        self.assertEqual(success, 'No HTML files found')
        self.assertIsNone(error)

    # Test method for successful execution
    def test_successful_execution(self):
        success, error = add_tailwind('path_to_directory_with_html_files')  # replace with actual path
        self.assertIsInstance(success, list)
        self.assertIsInstance(error, list)
        self.assertEqual(len(error), 0)  # assuming no errors during processing html files


if __name__ == '__main__':
    unittest.main()