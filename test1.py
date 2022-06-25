import simplekml
import xml.etree.ElementTree as ET

filename = "C:/Users/Parkash Ladhani/Desktop/pythonProject2/task_2_sensor.kml"


def coordinates(km_file):
    with open(filename, 'r') as myfile:
        doc = myfile.read().encode('UTF-8')
        print(doc)
    tree = ET.parse(filename)
    lineStrings = tree.findall('.//{http://www.opengis.net/kml/2.2}LineString')

    for attributes in lineStrings:
        for subAttribute in attributes:
            if subAttribute.tag == '{http://www.opengis.net/kml/2.2}coordinates':
                print(subAttribute.text)


print(coordinates(filename))
