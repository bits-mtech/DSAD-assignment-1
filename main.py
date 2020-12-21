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
        bucket[i] = [name, phone, memRef, status]
    else:
        bucket.append([name, phone, memRef, status])

    return f"Input Argument are name {name}, phone {phone}, member reference number {memRef}, status {status}"

def updateAppDetails(ApplicationRecords, name, phone, memRef, status):
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
    if (record[2] != status):
        key_changed.append("Application Status")
        bucket[column][2] = status

    return key_changed, bucket[column]


def memRef(ApplicationRecords, memID):
    for record in ApplicationRecords:
        print(record)
    print("")

def appStatus(ApplicationRecords):
    print("")

def destroyHash(ApplicationRecords):
    del ApplicationRecords
    print("Destroys the Hashtable. A cleanup information")

def search(ApplicationRecords, name):
    hash_key = hashing_func(name)
    bucket = ApplicationRecords[hash_key]
    for i, kv in enumerate(bucket):
        if len(kv) > 0:
            if name == (kv[0]) :
                return kv,hash_key,i
        else:
            print("index is blank")

def process_line_record(str):
    return [input.rstrip(" ").lstrip(" ") for input in str.strip("\n").split("/") if
                                       len(input) > 0]

def readFromInputFile(filename):
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
            print("prompts file")
            for line in lines:
                if line.find('Update:') == 0:
                    print("Update Opeartion")
                    processed_array = process_line_record(line.strip("Update:"))
                    msg = updateAppDetails(ApplicationRecords, processed_array[0],
                                           processed_array[1],processed_array[2],
                                           processed_array[3])
                    l = f"{line.strip('Update:')} / {','.join(msg[0])}".strip("\n")
                    writeToOutputFile(l,"update")
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
            processed_array = process_line_record(str)
            if len(processed_array) == 5:
                name = processed_array[0]
                updated_field = processed_array[4]
            else:
                name = ""
                updated_field = ""
            fh.write(f'Updated details of {name}. {updated_field} has been changed. \n')
        elif operation == "reference":
            rest_data = "" #fetch from hash
            fh.write(f'---------- Member reference by {str} ---------- \n {rest_data} \n -------------------------------------')
        elif operation == "status":
            fh.write(f'---------- Application Status ---------- \n {str} \n -------------------------------------')


if __name__ == '__main__':
    ApplicationRecords = initializeHash()
    readFromInputFile('inputPS26.txt')
    readFromInputFile('promptsPS26.txt')
    # print(search(ApplicationRecords,"Vinay Shah"))
    # print(search(ApplicationRecords, "Sandhya Raman"))
    # print(search(ApplicationRecords, "Deepak Prasad"))
    # print(search(ApplicationRecords, "Aravind Shetty"))
    # print(search(ApplicationRecords, "Joginder Singh"))
    print(ApplicationRecords)

