from subprocess import check_output


# Function to get the latest version of a package
def get_latest_version(package_name):
    output = check_output(["pip", "index", "versions", package_name]).decode("utf-8")
    output.replace("Available versions: ", "")
    start = output.find("(")
    end = output.find(")")
    return output[start + 1 : end]


# List of packages with their current versions (example here)
packages = {
    "gunicorn": "21.2.0",
}


for package in packages.keys():
    lts = get_latest_version(package)
    if packages[package] != lts:
        print(f"💥{package}💥 Version : {packages[package]}, LTS : {lts}")
