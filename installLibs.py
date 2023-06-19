import importlib

def install_package(package):
    try:
        importlib.import_module(package)
        print(f"{package} is already installed.")
    except ImportError:
        print(f"{package} is not installed. Installing...")
        try:
            import pip
            pip.main(['install', package])
        except AttributeError:
            import subprocess
            subprocess.check_call(['pip', 'install', package])
        print(f"{package} has been installed successfully.")

# List of required packages
required_packages = [
    'pandas',
    'matplotlib',
    'seaborn',
    'scikit-learn',
    'tensorflow',
]

# Install required packages if not already installed
for package in required_packages:
    install_package(package)
