import json
for i in range(1, 8):
    path = 'C://Users/GEM/Desktop/SITRTS/data segments/DataSegment%s.json' % i
    with open(path, 'r') as f:
        data = json.load(f)


    def is_open(a):
        if a['motion1'] == True or a['motion2'] == True or a['motion3'] == True:
            if a['existed1'] == False and a['existed2'] == False and a['existed3'] == False:
                return True
        return False


    def is_close(a):
        if a['motion1'] == False and a['motion2'] == False and a['motion3'] == False:
            if a['existed1'] == True or a['existed2'] == True or a['existed3'] == True:
                return True
        return False


    def is_working(a):
        if a['existed1'] == True and a['motion1'] == True and a['noise'] < .3 and a['light1'] > .5:
            return True
        return False


    def is_edu(a):
        if a['existed1'] == True and a['motion1'] == True and a['monotone'] == True:
            return True
        return False


    for a in data:
        if is_open(a):
            if a['class'] != "open":
                print(a)
            a['class'] = "open"
        if is_close(a):
            if a['class'] != "close":
                print(a)
            a['class'] = "close"
        if is_working(a):
            if a['class'] != "working":
                print(a)
            a['class'] = "working"
        if is_edu(a):
            if a['class'] != "edu":
                print(a)
            a['class'] = "edu"

    f.close()

    with open(path, 'w+') as f:
        json.dump(data, f, indent=2)

