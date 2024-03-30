from xml.etree import ElementTree as ET
import json

class AnswerError(Exception):
    pass

class Transport(object):

    def __init__(self, name, government_number, color):
        self._name = name
        self._government_number = government_number
        self._color = color

    def get_name(self): return self._name
    def get_government_number(self): return self._government_number
    def get_color(self): return self._color

    def set_name(self, name): self._name = name
    def set_government_number(self, government_number): self.government_number = government_number
    def set_color(self, color): self._color = color

    def move(self): print()
    def brake(self): print()
    def passenger_entry(self): print('Passenger entry completed!')

class Bus(Transport):
    def move(self): print('The bus is driving')
    def brake(self): print('The bus is braking')

class Plane(Transport):
    def move(self): print('The plane is flying')
    def brake(self): print('The plane is descending')

def reading_data(data_path):
    print('-----------------------------')

    if (data_path == 'data_json.txt'):
        print()

        if (len(data['Buses']) == 0): print('### Database has no data Buses')
        else:
            for point in data['Buses']:
                print(' Name: ', point['name'], '\n', 'Government number: ', point['government_number'], '\n', 'Color: ', point['color'], '\n')

    else:
        tree = ET.parse('data_1Lab_xml')
        root = tree.getroot()

        if (len(root)==0): print(' ### Database has no data Planes')
        else:
            print()
            for enement in root:
                print('Name: ', enement.text, '\n', 'Government_number: ', enement[0].text, '\n', 'Color: ', enement[1].text, '\n')

    print('-----------------------------', '\n')

def information_about_object(data_path):

    if (data_path == 'data_json.txt'):
        print('The database contains the following government numbers', '\n', 'Enter number for information ', '\n', '---')
        count=0

        for point in data['Buses']:
            print(point['government_number'])
            count+=1

        if (count==0):
            print(' ### The database has no government numbers', '\n', '---', '\n')
            return ()

        print(' ---', '\n', 'Enter government number:', end=" ")
        government_number = str(input())
        print('\n', '-----------------------------', '\n')

        for point in data['Buses']:
            if (point['government_number'] == government_number):
                print(' Name: ', point['name'], '\n', 'Government number: ', point['government_number'], '\n',
                      'Color: ', point['color'], '\n')
    else:
        tree = ET.parse('data_1Lab_xml')
        root = tree.getroot()

        if (len(root) == 0): print(' ### The database has no government numbers')
        else:
            print('The database contains the following government numbers', '\n', 'Enter number for information ', '\n', '---')

            for enement in root: print(enement[1].text)
            print(' ---', '\n', 'Enter government number:', end=" ")
            government_number = str(input())
            print()

            for enement in root:
                if(enement[1].text == government_number):
                    print('-----------------------------', '\n')
                    print(' Name: ', enement.text, '\n', 'Government_number: ', enement[0].text, '\n', 'Color: ', enement[1].text, '\n')

    print(' -----------------------------', '\n')

def add_data_object(data_path, main=None, flag=None, name=None, government_number=None, color=None):

    if (flag!=True): print(' -----------------------------')

    noneDATA_flag = False
    name_another, government_number_another, color_another = '', '', ''

    if (name == None and government_number == None and color == None):
        noneDATA_flag = True
        print('Enter transport name:', end=" ")
        name_another = str(input())
        while(True):
            try:
                print('Enter government number:', end=" ")
                government_number_another = str(input())
                if (len(government_number_another) != 8 and len(government_number_another) != 9):
                    raise AnswerError(government_number_another, ' - number incorrect', '\n')
                break
            except AnswerError:
                print("Please enter correct GosNumber")
        print('Enter color:', end=" ")
        color_another = str(input())

    if (data_path == 'data_json.txt'):
        print()

        if (noneDATA_flag == True):
            data['Buses'].append({'name': name_another, 'government_number': government_number_another, 'color': color_another})
        else:
            data['Buses'].append({'name': name, 'government_number': government_number, 'color': color})

        with open('data_1Lab_json.txt', 'w') as outfile:
            json.dump(data, outfile)

    else:
        name_plane = ET.SubElement(main, 'name')
        government_number_plane = ET.SubElement(name_plane, 'government_number')
        color_plane = ET.SubElement(name_plane, 'color')

        if (noneDATA_flag == True):
            name_plane.text = name_another
            government_number_plane.text = government_number_another
            color_plane.text = color_another
        else:
            name_plane.text = name
            government_number_plane.text = government_number
            color_plane.text = color

        dataXML = ET.tostring(main, encoding='unicode')
        myFile = open('data_1Lab_xml', 'w')
        myFile.write(dataXML)
        myFile.close()

    if (flag!=True): print('\n', '### New transport added to the database', '\n', '-----------------------------', '\n')

def remove_data_object(data_path):

    if (data_path == 'data_json.txt'):
        print(' -----------------------------', '\n', 'The database contains the following government numbers', '\n', '---')
        count = 0

        for point in data['Buses']:
            print(point['government_number'])
            count += 1

        if (count == 0):
            print(' ### The database has no government numbers', '\n', '---', '\n')
            return ()

        print(' ---', '\n', 'Enter government number:', end=" ")
        government_number = str(input())
        print()

        data['Buses'] = list(
            filter(
                lambda x: x.get('government_number') != government_number,
                data.get('Buses', [])
            )
        )
        print('\n', 'Transport removed to the database', '\n', ' -----------------------------', '\n')
        with open('data_1Lab_json.txt', 'w') as outfile:
            json.dump(data, outfile)

    else:
        tree = ET.parse('data_1Lab_xml')
        root = tree.getroot()
        print(' -----------------------------', '\n', 'The database contains the following government numbers', '\n', '---')
        if (len(root) == 0):
            print(' ### The database has no government numbers', '\n', '---', '\n',' -----------------------------', '\n')
            return
        else:
            for element in root: print(element[1].text)
            print(' ---', '\n', 'Enter government number:', end=" ")
            government_number = str(input())
            for element in root:
                if (element[0].text == government_number):
                    root.remove(element)
        tree.write('data_1Lab_xml')
        print('\n', 'Transport removed to the database', '\n', ' -----------------------------', '\n')

def remove_database(data_path):
    print(' -----------------------------')

    if (data_path =='data_json.txt'):
        print()
        open("data_1Lab_json.txt", "w").close()
        data['Buses'] = []
    else:
        tree = ET.parse('data_1Lab_xml')
        root = tree.getroot()
        root.clear()
        tree.write('data_1Lab_xml')

    print(' ### Database was removed', '\n', '-----------------------------', '\n')

def scan(data_path):

    if (data_path== 'data_json.txt'):
        count = 0
        print(' ---')

        for point in data['Buses']:
            print(point['government_number'])
            count += 1

        if (count == 0):
            print(' ### The database has no government numbers', '\n', '---', '\n'
                   '### Database has no data Buses. Enter new object in database')

            add_data_object('data_1Lab_json.txt')
            return Bus(data['Buses'][0]['name'], data['Buses'][0]['government_number'], data['Buses'][0]['color'])

        print(' ---', '\n', 'Enter government number U want to scan:', end=" ")
        government_number = str(input())
        print()

        for point in data['Buses']:
            if (point['government_number'] == government_number):
                print("Scan was completed")
                return Bus(point['name'], point['government_number'], point['color'])
    else:

        tree = ET.parse('data_1Lab_xml')
        root = tree.getroot()

        if (len(root) == 0):
            print(' ### The database has no government numbers', '\n', '---', '\n'
                  '### Database has no data Buses. Enter new object in database')

            add_data_object('data_1Lab_xml', main)
            return Plane(root.text, root[0].text, root[1].text)

        else:
            print('The database contains the following government numbers', '\n', 'Enter number for information ', '\n',  '---')

            for enement in root: print(enement[1].text)
            print(' ---', '\n', 'Enter government number:', end=" ")
            government_number = str(input())

            for enement in root:
                if (enement[1].text == government_number):
                    print("Scan was completed")
                    return Plane(enement.text, enement[0].text, enement[1].text)



with open('data_1Lab_json.txt') as file:
    data = json.load(file)
if (len(data) == 0):
    data['Buses'] = []

main = ET.Element('Planes')
tree = ET.parse('data_1Lab_xml')
root = tree.getroot()
if (len(root)==0):
    dataXML = ET.tostring(main, encoding='unicode')
    myFile = open('data_1Lab_xml', 'w')
    myFile.write(dataXML)
    myFile.close()
else:
    for element in root: add_data_object('data_1Lab_xml', main, True, element.text, element[0].text, element[1].text)

answer = -1
while (answer!=0):
    print('Enter what do U want to do?', '\n', '1 - read database', '\n', '2 - read information about object database')
    print(' 3 - add database object', '\n', '4 - remove database object', '\n', '5 - delete database')
    print(' 0 - Exit', '\n', 'Enter:', end=" ")

    try:
        answer = int(input())
    except ValueError:
        print('\n', '### You must enter integer numbers', '\n')

    else:
        if (answer == 1):
            print('Enter database U want to read: JSON or XML', end = " ")
            if (str(input()) == 'JSON'): reading_data('data_1Lab_json.txt')
            else: reading_data('data_1Lab_xml')

        if (answer == 2):
            print('Enter database U want to read: JSON or XML', end = " ")
            if (str(input()) == 'JSON'): information_about_object('data_1Lab_json.txt')
            else: information_about_object('data_1Lab_xml')

        if (answer == 3):
            print('Enter database U want to read: JSON or XML', end = " ")
            if (str(input()) == 'JSON'): add_data_object('data_1Lab_json.txt')
            else: add_data_object('data_1Lab_xml', main)

        if (answer == 4):
            print('Enter database U want to read: JSON or XML', end=" ")
            if (str(input()) == 'JSON'):
                remove_data_object('data_1Lab_json.txt')
            else:
                remove_data_object('data_1Lab_xml')

        if (answer == 5):
            print('Enter database U want to read: JSON or XML', end=" ")
            if (str(input()) == 'JSON'): remove_database('data_1Lab_json.txt')
            else: remove_database('data_1Lab_xml')


# add_data_object('data_1Lab_xml', main)
# plane = scan('data_1Lab_xml')
# print(plane.get_name())
# plane.move()
# remove_database('data_1Lab_xml')

# name = ET.SubElement(main, 'name')
# government_number = ET.SubElement(name, 'government_number')
# color = ET.SubElement(name, 'color')
# name.text = 'XYI'
# government_number.text = '1H.7Q'
# color.text = 'black'

# dataXML = ET.tostring(model_plane, encoding = 'unicode')
# myFile = open('data_1Lab_xml', 'w')
# myFile.write(dataXML)
# myFile.close()
#
# first_bus = scan('data_1Lab_json.txt')
# information_about_object('data_1Lab_json.txt')
#
# not_dataJSON_bus = Bus('Mark_1', 'g913tr.777', 'black')
# print(not_dataJSON_bus.get_name())
# reading_data('data_1Lab_json.txt')
#
# add_data_object('data_1Lab_json.txt', None, False, not_dataJSON_bus.get_name(), not_dataJSON_bus.get_government_number(), not_dataJSON_bus.get_color())
# reading_data('data_1Lab_json.txt')

# <Planes><name>iii<government_number>222</government_number><color>black</color></name></Planes>
# {"Buses": [{"name": "1", "government_number": "1", "color": "1"}]}