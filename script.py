import json
import datetime
import os, os.path
import time


start = time.time()
csvFile = open('output2.csv', 'a')

# for filename in os.listdir('C:/Users/dulaj/OneDrive/Desktop/Excel to CSV/jsons'):
for filename in os.listdir('jsons'):
    jsonFile = open('jsons/'+filename, encoding='utf8')
    # jsonFile = open('C:/Users/dulaj/OneDrive/Desktop/Excel to CSV/jsons/'+filename, encoding='utf8')
    data = json.load(jsonFile)
    elements = data['elements']
    print("-------- Starting "+filename+" --------")
    for i in elements:
        orderNumber = i['order_number']
        inspections = i['inspections']
        for j in inspections:

            if j['scheduled_inspection_date'] is not None:
                inspectionDate = j['scheduled_inspection_date']
            else:
                inspectionDate = ""

            bookingDate = j['booking_date']
            if bookingDate is not None:
                dateObj = datetime.datetime.strptime(bookingDate, '%Y-%m-%d')
                year = dateObj.date().year
                if year > 2001:
                    brandPriority = "TRUE"
                else:
                    brandPriority = ""
            else:
                brandPriority = ""

            assigendUser = j['assigned_user']
            if assigendUser is not None:
                email = assigendUser['email']
            else:
                email = ""

            try:
                # if "inspection_type" in j:
                #     if j["inspection_type"]["name"] is not None:
                inspectionType = j["inspection_type"]["name"]
            except:
                inspectionType = ""
        
            print(inspectionType)
            outputStr = orderNumber+";"+inspectionDate+";"+brandPriority+";"+email+";"+inspectionType
            csvFile.write("\n"+outputStr)
            # print(outputStr)
    jsonFile.close()
    print("-------- Ending "+filename+" --------")
print("\nTime taken to execute program: "+str(time.time()-start)+" Seconds")