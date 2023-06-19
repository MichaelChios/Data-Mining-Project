import importlib

def install_library(package_name):
    try:
        importlib.import_module(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        import pip
        pip.main(['install', package_name])
        print(f"{package_name} has been installed.")

# List of libraries to install
libraries = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "tensorflow",
    "keras",
]

for library in libraries:
    install_library(library)

# Additional installation for specific modules
install_library("scipy")  # Required by seaborn

print("All libraries have been installed.")