import os, sys
import nose
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
import config as cfg


def _classify_test_paths(path, items):
    dirs = []
    tests = []
    for item in items:
        if os.path.isdir(os.path.join(path, item)):
            dirs.append(item)
        else:
            tests.append(item)
    return (dirs, tests)

def main():
    exclude = [x.replace(":", ".") for x in cfg.EXCLUDE]
    argv = ["runner.py", "-s"]
    argv += cfg.INCLUDE
    exclude_dirs, exclude_tests = _classify_test_paths(cfg.PATH, exclude)
    if exclude_dirs:
        argv += ["--exclude-dir=%s" % d for d in exclude_dirs]
    if exclude_tests:
        argv += ["--exclude-test=%s" % t for t in exclude_tests]

    test_runner = None
    if is_running_under_teamcity():
        test_runner = TeamcityTestRunner()
    nose.run(argv=argv, testRunner=test_runner)

if __name__ == "__main__":
    main()

