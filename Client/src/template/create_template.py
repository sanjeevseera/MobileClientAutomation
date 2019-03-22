import sys
import os
import inspect
libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])
from Utilities.Test_flow import TestFlow


path = "src/template/cases_template.py"
dtst_str = ""
with open(path, 'w') as file_path:
    file_path.write("""\"\"\"\nthis the template to create the test_cases.py file\nthis file used by Convert_csvToPy.py file\n\"\"\"\ntest_case_dict = {""")
    fun_data = inspect.getsource(TestFlow)
    for s in fun_data.split('\n'):
        if "def" in s:
            key_str = s.lstrip().split(' ', 1)[-1].split('(')[0]
            val_list = s.lstrip().split(' ', 1)[-1].split('(')[1].split(')', 1)[0].split(',')[1:]
            if dtst_str == "":
                dtst_str += "\n{0}'{1}': [".format(" "*4, key_str)
            else:
                dtst_str += ",\n{0}'{1}': [".format(" " * 4, key_str)
            val_str = ""
            for c in val_list:
                if '=' in c.rstrip():
                    if val_str == "":
                        val_str += "('{0}', '{1}')".format(c.lstrip().split('=')[0], 'OPTIONAL')
                    else:
                        val_str += ", ('{0}', '{1}')".format(c.lstrip().split('=')[0], 'OPTIONAL')
                else:
                    if val_str == "":
                        val_str += "('{0}', '{1}')".format(c.lstrip().split('=')[0], 'MANDATE')
                    else:
                        val_str += ", ('{0}', '{1}')".format(c.lstrip().split('=')[0], 'MANDATE')
            val_str += ']'
            dtst_str += val_str

    file_path.write(dtst_str+"\n}\n")
print("Done --- you are now ready to share framework")
