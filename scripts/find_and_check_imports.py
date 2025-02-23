import glob
import sys
import traceback
from importlib.machinery import SourceFileLoader


def run_check_imports(files):
    has_failure = False
    for file in files:
        try:
            SourceFileLoader("x", file).load_module()
        except Exception:
            has_failure = True
            print(file)  # noqa: T201
            traceback.print_exc()
            print()  # noqa: T201

    sys.exit(1 if has_failure else 0)


python_files = glob.glob(f"{sys.argv[1]}/**/*.py", recursive=True)
if python_files:
    sys.exit(run_check_imports(python_files))
else:
    print("No Python files found to check") # noqa: T201
    sys.exit(0)
