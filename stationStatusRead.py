import requests
import json
import os
import time

s = requests.session()


def informationRead():

    r = s.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
    text = json.loads(r.text)

    lastUpdated = text['last_updated']
    savPath = os.path.join(path,'station_status_' + str(lastUpdated) + '.txt')
    print(savPath)
    f = open(savPath,'w')

    
    ks = ["station_id","num_bikes_available","num_bikes_disabled","num_docks_available","num_docks_disabled","is_installed","is_renting","is_returning","last_reported","eightd_has_available_keys"]


    f.write('"station_id":,"num_bikes_available":,"num_bikes_disabled":,"num_docks_available":,"num_docks_disabled":,"is_installed":,"is_renting":,"is_returning":,"last_reported":,"eightd_has_available_keys":,"last_updated":\n')

    data = text['data']
    stations = data['stations']

    for st in stations:
        rec = ""
        for k in ks:
            rec += str(st[k]) + ' '
        f.write(rec + str(lastUpdated) + '\n')

    f.write(str(text))

    f.close()

print('beginning')
path = os.path.join(os.path.abspath('.'),'StationStatus')
if not os.path.exists(path):
    os.mkdir(path)
print(path)
while True:
    informationRead()
    time.sleep(300)


