# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def hashing_func(key):
    return key % len(ApplicationRecords)

def initializeHash():
    '''
    This function is use to initialize the Hash table
    :param self:
    :return: [None]
    '''
    return None

def insertAppDetails(ApplicationRecords, name, phone, memRef, status):
    print(f"Input Argument are name {name}, phone {phone}, member reference number {memRef}, status {status}")

def updateAppDetails(ApplicationRecords, name, phone, memRef, status):
    print("Updated the App details")

def memRef(ApplicationRecords, memID):
    print("")

def appStatus(ApplicationRecords):
    print("")

def destroyHash(ApplicationRecords):
    print("Destroys the Hashtable. A cleanup information")

def readFromInputFile(filename):
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        if filename == "inputPS26.txt":
            writeToOutputFile(len(lines))
        elif filename == "promptsPS26.txt":
            print("prompts file")
            for line in lines:
                if line.find('Update:') == 0:
                    print("Update Opeartion")
                    writeToOutputFile(line.strip("Update:"),"update")
                elif line.find('memberRef:') == 0:
                    print("Member Reference")
                    writeToOutputFile(line.strip("memberRef:"), "reference")
                elif line.find('appStatus') == 0:
                    print("application status")
                    writeToOutputFile('', "status")
        for line in lines:
            print(line.strip("\n").split("/"))

def writeToOutputFile(str,operation="input" ,filename="outputPS26.txt"):
    with open(filename, 'a+') as fh:
        if operation == 'input':
            fh.write(f'Successfully inserted {str} applications into the system. \n')
        elif operation == 'update' :
            name = str.split("/")[0]
            updated_field = ""
            fh.write(f'Updated details of {name}. {updated_field} has been changed. \n')
        elif operation == "reference":
            rest_data = "" #fetch from hash
            fh.write(f'---------- Member reference by {str} ---------- \n {rest_data}')
        elif operation == "status":
            fh.write(f'---------- Application Status ---------- \n')


if __name__ == '__main__':
    ApplicationRecords = initializeHash()
    readFromInputFile('inputPS26.txt')
    readFromInputFile('promptsPS26.txt')
