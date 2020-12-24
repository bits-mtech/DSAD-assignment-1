def hashing_func(name):
    '''
    This function calculates the insertion address of array based on input as name.
    :param name: Key name
    :return: <Integer>
    '''
    return hash(name) % len(ApplicationRecords)

def initializeHash():
    '''
    This function is use to initialize the Hash table. By default initializes with 4 elements
    :param self:
    :return: [None]
    '''
    return [[] for _ in range(4)]

def insertAppDetails(ApplicationRecords, name, phone, memRef, status):
    '''
    This function inserts the applicant’s name and corresponding details into the hash table.
    :param ApplicationRecords:
    :param name: Applicant Name
    :param phone: Phone Number
    :param memRef: Member reference
    :param status: Application status
    :return: <String>
    '''
    hash_key = hashing_func(name)
    key_exists = False
    bucket = ApplicationRecords[hash_key]
    for i, kv in enumerate(bucket):
        if name == kv[0]:
            key_exists = True
            break
    if key_exists:
        bucket[i] = [name, phone, memRef, status]
    else:
        bucket.append([name, phone, memRef, status])

    return f"Input Argument are name {name}, phone {phone}, member reference number {memRef}, status {status}"

def updateAppDetails(ApplicationRecords, name, phone, memRef, status):
    '''
    This function finds the applicant’s details based on the name and updates the corresponding details into the hash table.
    :param ApplicationRecords:
    :param name: Applicant Name
    :param phone: Phone Number
    :param memRef: Member reference
    :param status: Application status
    :return: <String>
    '''
    hash_key = hashing_func(name)
    bucket = ApplicationRecords[hash_key]
    key_changed = []
    record, row,column = search(ApplicationRecords,name)
    if(record[1] != phone):
        key_changed.append("Phone Number")
        bucket[column][1] = phone
    if(record[2] != memRef):
        key_changed.append("Member reference")
        bucket[column][2] = memRef
    if (record[3] != status):
        key_changed.append("Application Status")
        bucket[column][3] = status

    return key_changed, bucket[column]


def memRef(ApplicationRecords, memID):
    '''
    This function prints the list of all applicants who have been referred by a particular member
    :param ApplicationRecords:
    :param memID:
    :return:<string>
    '''
    result = []
    for i, record in enumerate(ApplicationRecords):
        if len(record) > 0:
            for j, value in enumerate(record):
                if value[2]  == memID:
                    result.append(f'{value[0]} / {value[1]} / {value[3]}')
    return '\n'.join(result)

def appStatus(ApplicationRecords):
    '''
    This function prints the list of number of applications in each stage of the application process including Applied, Verified and Approved.
    :param ApplicationRecords:
    :return: <String>
    '''
    count = []
    name = []
    for i, record in enumerate(ApplicationRecords):
        if len(record) > 0:
            for j, value in enumerate(record):
                if value[3] not in name:
                    name.append(value[3])
                    count.append(1)
                else:
                    count[name.index(value[3])] += 1
    result = ""
    for i,kv in enumerate(count):
        result += f'{name[i]}: {count[i]} \n'
    return result

def destroyHash(ApplicationRecords):
    '''
    This function destroys all the entries inside hash table. This is a clean-up code.
    :param ApplicationRecords:
    :return:
    '''
    del ApplicationRecords
    print("Destroys the Hashtable. A cleanup information")

def search(ApplicationRecords, name):
    '''
    This function finds the applicant’s details based on the name.
    :param ApplicationRecords:
    :param name:
    :return:
    '''
    hash_key = hashing_func(name)
    bucket = ApplicationRecords[hash_key]
    for i, kv in enumerate(bucket):
        if len(kv) > 0:
            if name == (kv[0]) :
                return kv,hash_key,i
        else:
            print("index is blank")

def process_line_record(str):
    '''
    This is helper function to process line information from input and prompts file.
    :param str: Line content
    :return: <Array>
    '''
    return [input.rstrip(" ").lstrip(" ") for input in str.strip("\n").split("/") if
                                       len(input) > 0]

def readFromInputFile(filename):
    '''
    Read the content of file.
    :param filename:
    :return: <None>
    '''
    with open(filename, 'r') as fh:
        lines = fh.readlines()
        if filename == "inputPS26.txt":
            for line in lines:
                processed_array = process_line_record(line)
                if len(processed_array) == 4:
                    insertAppDetails(ApplicationRecords, processed_array[0],
                                           processed_array[1],processed_array[2],
                                           processed_array[3])
                else:
                    print(f"Some record is missing in {line}")
            writeToOutputFile(len(lines))
        elif filename == "promptsPS26.txt":
            for line in lines:
                if line.find('Update:') == 0:
                    processed_array = process_line_record(line.strip("Update:"))
                    msg = updateAppDetails(ApplicationRecords, processed_array[0],
                                           processed_array[1],processed_array[2],
                                           processed_array[3])
                    l = f"{line.strip('Update:')} / {','.join(msg[0])}".strip("\n")
                    writeToOutputFile(l,"update")
                elif line.find('memberRef:') == 0:
                    processed_array = process_line_record(line.strip("memberRef:"))
                    l = f"{line.strip('memberRef:')}|{memRef(ApplicationRecords,processed_array[0])}"
                    writeToOutputFile(l, "reference")
                elif line.find('appStatus') == 0:
                    result = appStatus(ApplicationRecords)
                    writeToOutputFile(result, "status")

def writeToOutputFile(str,operation="input" ,filename="outputPS26.txt"):
    '''
    This function write output of the program into supplied filename parameter.
    :param str: Content needs to be written in output file
    :param operation: Mode of operations like insert,update,status check, member refernce check.
    :param filename: Output filename default value is outputPS26.txt
    :return: <None>
    '''
    with open(filename, 'a+') as fh:
        if operation == 'input':
            fh.write(f'Successfully inserted {str} applications into the system. \n')
        elif operation == 'update' :
            processed_array = process_line_record(str)
            if len(processed_array) == 5:
                name = processed_array[0]
                updated_field = processed_array[4]
            else:
                name = ""
                updated_field = ""
            fh.write(f'Updated details of {name}. {updated_field} has been changed. \n')
        elif operation == "reference":
            ref_id = str.split('|')[0].strip('\n')
            rest_data = str.split('|')[1].strip('|') #fetch from hash
            fh.write(f'---------- Member reference by {ref_id} ---------- \n{rest_data}\n------------------------------------- \n')
        elif operation == "status":
            fh.write(f'---------- Application Status ---------- \n{str}------------------------------------- \n')


if __name__ == '__main__':
    ApplicationRecords = initializeHash()
    readFromInputFile('inputPS26.txt')
    readFromInputFile('promptsPS26.txt')
    # print(appStatus(ApplicationRecords))
    #print(memRef(ApplicationRecords,'11129'))
    # print(search(ApplicationRecords,"Vinay Shah"))
    # print(search(ApplicationRecords, "Sandhya Raman"))
    # print(search(ApplicationRecords, "Deepak Prasad"))
    # print(search(ApplicationRecords, "Aravind Shetty"))
    # print(search(ApplicationRecords, "Joginder Singh"))
    # print(ApplicationRecords)

