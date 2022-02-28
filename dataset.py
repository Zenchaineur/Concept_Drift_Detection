import csv

def dataset(dataset_name):
    X = list()
    y = list()
    targets = set()

    first = True
    with open(dataset_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar ='|')
        for row in spamreader:
          
            if first :
                first = False
            else:
                elem = list()
                for i in range (len(row)-1):
                    elem.append(float(row[i].replace(',', '.')))
                X.append(elem)
                y.append(float(row[len(row)-1].replace(',', '.')))
                targets.add(float(row[len(row)-1].replace(',', '.')))
    targets_list = [target for target in targets]
    return X, y, targets_list


