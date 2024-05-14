import json

def updateJSON():
    with open('./Web_UI/data/printers.json', "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()

    #do work here

    with open('./Web_UI/data/printers.json', "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)
        jsonFile.close()

#JOB FUNCTIONS


#FILAMENT FUNCTIONS
def rem_filament(filamentID):
    try:
        with open('./Web_UI/filaments.filaments.json', 'w') as jsonFile:
            filament_data = json.load(jsonFile)
            del (filament_data[filamentID])
            json.dump(filament_data,jsonFile, indent=4)
            jsonFile.close()
        return 1
    except: return 0


# PRINTER FUNCTIONS
def add_printer(printerID, printerPort, filamentType, nozzleSize):
    with open('./Web_UI/data/printers.json', 'r') as jsonFile:
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

    with open('./Web_UI/data/printers.json', 'w') as jsonFile:
        printer_data["printers"].append(added_printer)
        json.dump(printer_data, jsonFile, indent=4)
        jsonFile.close()
    return