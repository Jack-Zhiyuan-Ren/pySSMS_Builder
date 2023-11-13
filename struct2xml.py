import xml.etree.ElementTree as ET


def struct2xml(data):
    root = ET.Element('data')
    _dict_to_xml(root, data)
    return ET.tostring(root, encoding='unicode', method='xml')

def _dict_to_xml(parent, data):
    for key, value in data.items():
        if isinstance(value, dict):
            elem = ET.Element(key)
            parent.append(elem)
            _dict_to_xml(elem, value)
        else:
            elem = ET.Element(key)
            elem.text = str(value)
            parent.append(elem)