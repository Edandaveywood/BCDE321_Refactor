import unittest
from unittest.mock import patch
from main import CommandLineInterface


class TestCases(unittest.TestCase):
    @patch('builtins.print')
    def test_default(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.default("wrong")
        expected = mock_print.assert_called_with('wrong', 'is an incorrect command,'
                                                          ' type help to see the command list')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_load_data(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_load_data()
        expected = mock_print.assert_called_with('Loads data from '
                                                 'a provided Javascript file '
                                                 '\nSyntax: load_data '
                                                 '[file path]')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_load_data(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.do_load_data("JSTest1.js")
        expected = mock_print.assert_called_with("The current directory is:"
                                                 " \nYour selected js file is: JSTest1.js")
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_load_data_wrong(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.do_load_data("JSTest1")
        expected = mock_print.assert_called_with('You did not input any path'
                                                 ' or your input file is not existed')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_load_data_wrong_filetype(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.do_load_data("JSTest1.fake")
        expected = mock_print.assert_called_with('JSTest1.fake is not a js file,'
                                                 ' please re-select')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_create_pickle(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_create_pickle()
        expected = mock_print.assert_called_with("Creates a pickle of the "
                                                 "provided JavaScript file's classes,"
                                                 " attributes and methods "
                                                 "\nSyntax: create_pickle")
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_create_pickle(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest1.js")
        cmd.do_extract_data(None)
        actual = cmd.do_create_pickle(None)
        expected = mock_print.assert_called_with("Pickle has been created")
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_create_pickle_no_data(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.do_create_pickle(None)
        expected = mock_print.assert_called_with('Dictionary is empty, '
                                                 'try loading then extracting '
                                                 'data first')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_load_pickle(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_load_pickle()
        expected = mock_print.assert_called_with('Loads the previously saved '
                                                 'pickle and displays in terminal'
                                                 ' \nSyntax: load_pickle')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_load_pickle(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest1.js")
        cmd.do_extract_data(None)
        actual = cmd.do_load_pickle(None)
        expected = mock_print.assert_called_with("Pickle shown above")
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_remove_pickle(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_remove_pickle()
        expected = mock_print.assert_called_with('Removes the saved pickle '
                                                 'from your HDD '
                                                 '\nSyntax: remove_pickle')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_remove_pickle(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest1.js")
        cmd.do_extract_data(None)
        actual = cmd.do_remove_pickle(None)
        expected = mock_print.assert_called_with("pickle has been deleted")
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_extract_data(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_extract_data()
        expected = mock_print.assert_called_with('Extracts data from loaded'
                                                 ' JavaScript file '
                                                 '\nSyntax: extract_data')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_extract_data(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest1.js")
        actual = cmd.do_extract_data(None)
        expected = mock_print.assert_called_with("Data has been extracted")
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_extract_data_wrong(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest2.js")
        actual = cmd.do_extract_data(None)
        expected = mock_print.assert_called_with('There was an error in '
                                                 'the JavaScript file: Line 7: '
                                                 'Unexpected token this')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_convert_to_uml(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_convert_to_uml()
        expected = mock_print.assert_called_with('Converts extracted data '
                                                 'and displays image '
                                                 '\nSyntax: convert_to_uml')
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_convert_to_uml(self, mock_print):
        cmd = CommandLineInterface()
        cmd.do_load_data("JSTest1.js")
        cmd.do_extract_data(None)
        actual = cmd.do_convert_to_uml(None)
        expected = mock_print.assert_called_with("Conversion complete, "
                                                 "opening now")
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_help_exit(self, mock_print):
        cmd = CommandLineInterface()
        actual = cmd.help_exit()
        expected = mock_print.assert_called_with('Exits the program '
                                                 '\nSyntax: exit')
        self.assertEqual(expected, actual)

    def test_exit(self):
        cmd = CommandLineInterface()
        actual = cmd.do_exit(None)
        expected = True
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
