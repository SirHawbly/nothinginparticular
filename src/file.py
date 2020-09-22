# ---
# Imports

import os
import pathlib


# ---
#
def does_file_exist(file_name, ):
    """
    Args
        file_name: String
            name of the file we are checking for
  
    Returns
        Boolean value representing the file's existence
    """
    
    return os.path.isfile(file_name)


# ---
#
def remove_file(file_name, ):
    """
    Args
        file_name: String
            name of the file we are removing
  
    Returns
        Status of the removal of the provided file
    """
    
    # check to see if the file exists, and if so, attempt to remove it.
    if does_file_exist(file_name):
        try:
            os.remove(file_name)
            return True

        except OSError as e:
            print('Error in remove_file:\n',
                  '\tCannot delete file, it does not exist:\n\t',
                  e.strerror)
        
    # if the file does not exist, print an error message and return false.
    print('Error in remove_file:\n\tCannot delete file, it does not exist.')
    return False


# ---
#
def create_file(file_name, ):
    """
    Args
        file_name: String
            name of the file we are creating
  
    Returns
        Status of the creation of the provided file
    """
    
    # check for the file and attempt to open it, returning out if that works.
    if not does_file_exist(file_name):
        pathlib.Path(file_name).touch()
        return True
    
    # if the file was un-openable, we print an error message and return false.
    print("Error in create_file:\n\tCannot create file, it already exists.")
    return False


# ---
#
def write_to_file(file_name, out_string, ):
    """
    Args
        file_name: String
            name of the file we are writing to, if not existent, create it
        out_string: String
            Contents you would like added to file_name
  
    Returns
        Whether the provided string was written to the given file.
    """
    
    # check for the file, if nothing, create it.
    if not does_file_exist(file_name):
        create_file(file_name)
    
    # open up the file, and write the given string.
    with open(file_name, 'w') as output_file:
        return output_file.write(out_string)
    
    # return false, if opening the file failed.
    return False


# ---
#
def read_from_file(file_name, ):
    """
    Args
        file_name: String
            name of the file we are reading from

    Returns
        contents of the provided file, if it exists.
    """
    
    contents = []
    
    if does_file_exist(file_name):
        with open(file_name, 'r') as outfile:
            for line in outfile:
                contents += [line, ]
    
    return contents
    

# ---
#
def test(continues=True, ):
    """
    Args
        N/A

    Returns
        Status of the tests, asserts false if needed.
    """
    
    def print_current_dir_contents(string):
        print(string, end='')
        print('\t{}'.format([e for e in pathlib.Path('.').iterdir() if e.is_file()]))
        print()
        
    print('Starting Tests ...\n')
    
    test_file = 'TEST_FILE.txt'
    test_string = 'HERE\n\tARE\n\t\tSOME\n\t\t\tLINES'

    print_current_dir_contents('Current directory contents ...\n\t')
    
    print('Checking if test file exists ...', end=' ')
    if does_file_exist(test_file):
        
        print('File found, removing now ...', end=' ')
        assert remove_file(test_file)
        print_current_dir_contents('File removed.\n\t')

    else:
        print('File not found, no action taken.\n')

    print('Creating test file ...', end=' ')
    assert create_file(test_file)
    print_current_dir_contents('File created.\n\t')

    if continues:
        input('Continue? ')
        print('')
    
    print('Writing to test file ...', end=' ')
    assert write_to_file(test_file, test_string)
    print('Writing complete.\n')
    
    print('Checking file\'s contents ...')
    file_contents = ''
    
    with open(test_file) as o:
        print('"""')
        for line in o:
            file_contents += line
            print(line, end='')
        print('\n"""')
    
    assert file_contents == test_string
    print('Content matches!\n')
    
    if continues:
        input('Continue? ')
        print('')
    
    print('Printing the contents of the file in list form ...')
    print('\t{}'.format(read_from_file(test_file)))
    print('Printing complete.\n')
    
    print('Removing File ...', end=' ')
    assert remove_file(test_file)
    print_current_dir_contents('File removed.\n\t')
    
    print('Tests Complete!')
    
    return True


# ---
# Call to Main
if __name__ == '__main__':
    test(continues=False)

# ---

