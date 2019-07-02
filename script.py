import csv
from itertools import combinations

basic_items = ["bf", "rod", "bow", "tear", "vest", "cloak", "belt", "spat"]
combined_items = {}
current_items = []

class CombItem:
    def __init__(self, name, children, value):
        self.name = name
        self.children = children
        self.value = value

    def get_other_item(self, basic_item):
        copy = list(self.children)
        copy.remove(basic_item)
        return copy[0]

def get_all_items():
    current_set = set()
    for pair in combinations(current_items, 2):
        current_set.add(combined_items[frozenset(pair)])

    return sorted(list(current_set), reverse=True, key=lambda item: item.value)

def get_next_items(current_set):
    next_set = set()
    for basic_item in current_items:
        for other_item in basic_items:
            pair = (basic_item, other_item)
            comb_item = combined_items[frozenset(pair)]
            if comb_item not in current_set:
                next_set.add((comb_item, comb_item.get_other_item(basic_item)))

    return sorted(list(next_set), reverse=True, key=lambda item: item[0].value)


with open('combined.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        name, children, values = row[0], (row[1], row[2]), row[3]
        item = CombItem(row[0], [row[1], row[2]], row[3])
        combined_items[frozenset(children)] = item

while(True):
    value = input("Input: ").split(" ")

    item = value[0]
    action = ""

    if len(value) > 1:
        action = value[1]

    if item in basic_items:

        if action == "--":
            try:
                current_items.remove(item)
            except:
                pass

        else:
            current_items.append(item)

        print("==============")
        print("Current items: ")
        print(current_items)

        if len(current_items) > 1:
            current_set = get_all_items()
            print("==============")
            print("You can build: ")
            print([item.name + " [" + item.value + "]" for item in current_set])

            print("==============")
            n = 10
            print("Best " + str(n) + " next items: ")
            print([item[0].name + " [" + item[0].value + ", " + item[1] + "]" for item in get_next_items(current_set)][:n])

    else:
        print("Input not recognized.")
        
    print("******************")

if __name__ == "__main__":
    main()
