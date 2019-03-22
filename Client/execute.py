import sys
import os
import subprocess
import platform

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception('Argument is Missing or There are more\nExample: python execute.py Test_cases.cfg')
        elif not os.path.isfile(sys.argv[1]):
            raise Exception('The file Provided as Argument is not exist in the path')
        else:
            if sys.argv[1].lower().endswith('.cfg'):
                command = "python src/Utilities_test/Convert_cfgToPy.py " + sys.argv[1]
            elif sys.argv[1].lower().endswith('.csv'):
                command = "python src/Utilities_test/Convert_csvToPy.py " + sys.argv[1]
            else:
                raise Exception("Use file either *.csv or *.cfg, other file formats are not supported\n")
            try:
                if platform.system().lower() == "windows":
                    result_out = subprocess.check_output(command).decode().split('\n')
                elif platform.system().lower() == "darwin":
                    subprocess.call(command, shell=True)
                else:
                    subprocess.call(command, shell=True)

            except subprocess.CalledProcessError as e:
                print("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    except Exception as e:
        print("Exception: {}".format(e))
    except IndexError as e:
        print("IndexError: {}".format(e))
    except KeyboardInterrupt as e:
        print("KeyboardInterrupt: {}".format(e))
        sys.exit()
