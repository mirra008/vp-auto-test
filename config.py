import os


PATH = os.path.dirname(os.path.abspath(__file__))

"""
Don't capture stdout; same as command line option -s.
"""
NOCAPTURE = True

"""
Include dirs, modules, test cases or test methods.
If you want to include single test method you should use form module.path:ClassNameInFile.method_name, with a colon separating the module/file path and the objects within the file.
Run all tests if empty.
"""
INCLUDE = [
    "module1/submodule1",
    "module2.test_module21:Module21TestCase.test_method21_1",
]

"""
Exclude dirs, modules, test cases or test methods.
"""
EXCLUDE = [
    #"module1.submodule1.test_submodule1.Submodule1TestCase.test_method_sub1_2",
]

