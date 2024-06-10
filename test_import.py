import sys
import os

# Add the 'app' directory to the Python path
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))
print(f"Adding to PYTHONPATH: {app_path}")
sys.path.append(app_path)

try:
    from app.application import Application
    print("Import successful!")
except ModuleNotFoundError as e:
    print(f"Error importing Application: {e}")
    print("Current PYTHONPATH:", sys.path)
    raise e


def before_all(context):
    context.app = Application()
