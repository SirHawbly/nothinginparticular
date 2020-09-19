# ---
# Imports

import os
import pathlib


# ---
#
def does_dir_exist(dir_name, ):
    """
    Args
        dir_name: String
            name of the directory we are checking for

    Returns
        Boolean value representing the directory's existence
    """

    return os.path.isdir(dir_name)


# ---
#
def remove_directory(dir_name, ):
    """
    Args
        dir_name: String
            name of the directory we are removing

    Return
        Status of the removal of the provided directory
    """

    # if the directory exists, and is empty, attempt to remove it.
    if does_dir_exist(dir_name):
        if len(os.listdir(dir_name)) == 0:
            return os.remove(dir_name)

        # if it isn't empty, print an error and return false.
        else:
            print("Error in remove_directory:\n    Cannot delete directory, it is not empty.")
            return False

    # if the directory doesnt exist, print an error, and return false.
    print("Error in remove_directory:\n    Cannot delete directory, it does not exist.")
    return False


# ---
#
def create_directory(dir_name, ):
    """
    Args
        dir_name: String
            name of the directory we are creating

    Return
        Status of the creation of the provided directory
    """

    # if there is no directory in the current directory, create one.
    if not does_dir_exist(dir_name):
        return os.mkdir(dir_name)

    # else print an error and return out.
    print("Error in create_directory:\n    Cannot create directory, it already exists.")
    return False


# ---
#
def test():
    """

    """

    print("Starting Test ...")

    print("Done!")

    return True


# ---
# Call to Main
if __name__ == '__main__':
    test()


# ---

