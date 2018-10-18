import json

data = {}

with open('trello.json') as json_file:  
    data = json.load(json_file)
    
import csv

with open('trello.csv', mode='w', newline='') as trello_file:
    trello_writer = csv.writer(trello_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    trello_writer.writerow(['backlogID', 'name', 'desc', 'size'])

    for c in data['cards']:
        backlogID = 0
        size = ""
        board = ""
        user = ""
        for k in c:
            if k == "customFieldItems" and isinstance(c[k],(list,)):  
                for i in c[k]:
                    if 'value' in i:
                        backlogID = i["value"]["number"]
                    if 'idValue' in i:
                        for o in data['customFields'][1]['options']:
                            if o['id'] == i["idValue"]:
                                size = o['value']['text']
            for l in data['lists']:
                if c['idList'] == l['id']:
                    board = l['name']
            for m in data['members']:
                for mId in c['idMembers']:
                    if mId == m['id']:
                        user = m['fullName']

        trello_writer.writerow([backlogID, c['name'], c['desc'], size, user, board])