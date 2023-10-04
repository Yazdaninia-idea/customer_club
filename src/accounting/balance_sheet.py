import json
from datetime import datetime

# reading the content
balance_sheet_file = open("balance.json", 'r')
data = balance_sheet_file.read()
participant_list = json.loads(data.replace("'", "\""))
a = type(participant_list)
print("a: ", a)
print(participant_list)

balance_sheet_file.close()

# Creating new content
current_date = str(datetime.now())

data_structure = {
        "id": 1001,
        "test": {'id': 'daniel', 'point': 2300},
        "time": current_date
    }

# over writing new content
balance_sheet_file = open("balance.json", 'w')
balance_sheet_file.truncate()
balance_sheet_file.write(f"\n{data_structure}")
balance_sheet_file.close()
