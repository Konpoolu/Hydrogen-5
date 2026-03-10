import os

def pathStripper(prompt):
    #Intake prompt and output stripped text
    pathStripped = prompt
    pathStripped = pathStripped.strip()
    pathStripped = pathStripped.strip('"')
    pathStripped = pathStripped.strip("'")
    return pathStripped

def ncChecker(filePath):
    # Check if file exists and if it is a .nc or .gcode file
    if not os.path.isfile(filePath):
        print(f"Error: File '{filePath}' does not exist.")
        return False
    if not filePath.lower().endswith(('.nc', '.gcode')):
        print(f"Error: File '{filePath}' is not an .nc or .gcode file.")
        return False
    return True

def fileGrabber():
    path = input("Enter the path to your .nc or .gcode file: ")
    path = pathStripper(path)
    if ncChecker(path):
        print(f"File '{path}' works.")
        # add stuff i guess
    else:
        print("We don't ball")
        os.system.exit(1)

def main():
    fileGrabber()

if __name__ == "__main__":
    main()
