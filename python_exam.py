import json

with open('source_file_2.json', 'r') as myfile, open('watchers.json', 'w') as watchers, open('managers.json', 'w') as managers:
    data = myfile.read()
    objs = json.loads(data)
    
    manager_json = {}
    watcher_json = {}
    scores = []
    for obj in objs:                    
        for man in obj['managers']:
            if manager_json.get(man) is None:
                manager_json[man] = []
            if len(manager_json[man]) == 0:
                manager_json[man].append((obj['name'],(obj['priority'])))
            else:
                added = False
                i = 0
                for l in manager_json[man]:
                    if((obj['priority']) < l[1]):
                        manager_json[man].insert(i,(obj['name'],(obj['priority'])))
                        added = True
                        break
                    i+=1
                if not added:
                    manager_json[man].append((obj['name'],(obj['priority'])))
            
        for wa in obj['watchers']:
            if watcher_json.get(wa) is None:
                watcher_json[wa] = []
            if len(watcher_json[wa]) == 0:
                watcher_json[wa].append((obj['name'],(obj['priority'])))
            else:
                added = False
                i = 0
                for l in watcher_json[wa]:
                    if((obj['priority']) < l[1]):
                        watcher_json[wa].insert(i,(obj['name'],(obj['priority'])))
                        added = True
                        break
                    i+=1
                if not added:
                    watcher_json[wa].append((obj['name'],(obj['priority'])))

    final_man = {}
    for a in manager_json:
        final_man[a] = [res[0] for res in manager_json[a]]
        print(final_man[a])

    final_watcher = {}
    for a in watcher_json:
        final_watcher[a] = [res[0] for res in watcher_json[a]]

    json.dump(final_watcher, watchers)
    json.dump(final_man, managers)