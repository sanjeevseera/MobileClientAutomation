import sys
import os
import subprocess

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception('Argument is Missing or There are more\nExample: python execute.py Test_cases.cfg')
        elif not os.path.isfile(sys.argv[1]):
            raise Exception('The file Provided as Argument is not exist in the path')
        else:
            command = "python src/Utilities_test/Client_test.py "+sys.argv[1]
            result_out = subprocess.check_output(command).decode().split('\n')
    except Exception as e:
        print("Exception: {}".format(e))
    except IndexError as e:
        print("IndexError: {}".format(e))
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt: {}".format(e))
        os.exit()