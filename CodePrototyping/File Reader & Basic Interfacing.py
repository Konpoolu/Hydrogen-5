import os

def pathStripper(prompt):
    pathStripped = input(prompt)
    pathStripped = pathStripped.strip()
    pathStripped = pathStripped.strip('"')
    pathStripped = pathStripped.strip("'")
    return pathStripped

def ncChecker(filePath):
    if not os.path.isfile(filePath):
        print(f"Error: File '{filePath}' does not exist.")
        return False
    if not filePath.lower().endswith('.nc'):
        print(f"Error: File '{filePath}' is not an .nc file.")
        return False
    return True

def main():
    print(pathStripper("buffalo"))
