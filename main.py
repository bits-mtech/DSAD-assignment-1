class ClubApplicant(object):
    def __init__(self):
        self.clubapplicant = [[] for _ in range(4)]

def hashing_func(name):
    #return hash(key)
    return hash(name) % len(ApplicationRecords)

def initializeHash():
    '''
    This function is use to initialize the Hash table
    :param self:
    :return: [None]
    '''
    return [[] for _ in range(4)]

def insertAppDetails(ApplicationRecords, name, phone, memRef, status):
    hash_key = hashing_func(name)
    key_exists = False
    bucket = ApplicationRecords[hash_key]
    for i, kv in enumerate(bucket):
        if name == kv[0]:
            key_exists = True
            break
    if key_exists:
        print(len(bucket[i]))
        bucket[i] = (name, phone, memRef, status)
    else:
        bucket.append((name, phone, memRef, status))

    return f"Input Argument are name {name}, phone {phone}, member reference number {memRef}, status {status}"

def updateAppDetails(ApplicationRecords, name, phone, memRef, status):
    hash_key = hashing_func(name)
    bucket = ApplicationRecords[hash_key]
    key_exists = False
    for i, kv in enumerate(bucket):
        if name == kv[0]:
            key_exists = True
            break
    if key_exists:
        if len(bucket[i])>0:
            for j,kv in enumerate(bucket[i]):
                if name == kv[0]:
                    print(j)
        else:
            bucket[i] = (name, phone, memRef, status)

    print("Updated the App details")


def memRef(ApplicationRecords, memID):
    print("")

def appStatus(ApplicationRecords):
    print("")

def destroyHash(ApplicationRecords):
    print("Destroys the Hashtable. A cleanup information")

def search(ApplicationRecords, name):
    hash_key = hashing_func(name)
    bucket = ApplicationRecords[hash_key]
    print(bucket)
    for i, kv in enumerate(bucket):
        if name == kv[0] and len(bucket[i]) == 1:
            return kv,i,0
        elif name == kv[0] and len(bucket[i]) > 1:
            for j,kv in enumerate(bucket[i]):
                print(kv)
                print(i,j)
                if name == kv[0]:
                    return bucket[i][j],i,j

def readFromInputFile(filename):
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        if filename == "inputPS26.txt":
            for line in lines:
                processed_array = [input.rstrip(" ").lstrip(" ") for input in line.strip("\n").split("/") if len(input) >0]
                if len(processed_array) == 4:
                    msg = insertAppDetails(ApplicationRecords, processed_array[0],processed_array[1],processed_array[2],processed_array[3])
                    print(msg)
                else:
                    print(f"Some record is missing in {line}")
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
    #readFromInputFile('promptsPS26.txt')
    print(search(ApplicationRecords,"Vinay Shah"))
    print(search(ApplicationRecords, "Sandhya Raman"))
    print(search(ApplicationRecords, "Deepak Prasad"))
    print(search(ApplicationRecords, "Aravind Shetty"))
    print(search(ApplicationRecords, "Joginder Singh"))
    print(ApplicationRecords)

