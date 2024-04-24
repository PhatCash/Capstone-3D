import json

def updateJSON():
    with open('./data/printers.json', "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()

    #do work here

    with open('./data/printers.json', "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)
        jsonFile.close()

def add_printer(printerID, printerPort, filamentType, nozzleSize):
    
    with open('./data/printers.json', 'r') as jsonFile:
        printer_data = json.load(jsonFile)
        jsonFile.close()

    added_printer = {
        "id": printerID, 
        "port": printerPort,
        "filamentColor": "na",
        "filamentTpe": filamentType,
        "nozzleDiameter": nozzleSize,
        "jobStatus": "Ready"
        }

    with open('./data/printers.json', 'w') as jsonFile:
        printer_data["printers"].append(added_printer)
        json.dump(printer_data, jsonFile, indent=4)
        jsonFile.close()
    return

    '''
    added_printer = {
        "id": '"'+ printerID +'"',
        "port": '"'+ printerPort +'"',
        "filamentColor": '"''"',
        "filamentType": '"'+ filamentType +'"',
        "nozzleDiameter": '"'+ nozzleSize +'"',
        "jobStatus": "Ready"
    }

    added_printer = {
        "id": printerID, 
        "port": printerPort,
        "filamentColor": "na",
        "filamentTpe": filamentType,
        "nozzleDiameter": nozzleSize,
        "jobStatus": "Ready"
        }
    '''