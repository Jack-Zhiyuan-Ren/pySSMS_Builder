import xml.etree.ElementTree as ET

def struct2xml(data):
    root = ET.Element('root')  # Create the root element of the XML tree

    def dict_to_xml(element, data):
        for key, value in data.items():
            if isinstance(value, dict):
                child = ET.Element(key)
                element.append(child)
                dict_to_xml(child, value)
            elif isinstance(value, list):
                for item in value:
                    child = ET.Element(key)
                    element.append(child)
                    dict_to_xml(child, item)
            else:
                child = ET.Element(key)
                child.text = str(value)
                element.append(child)

    dict_to_xml(root, data)
    xml_string = ET.tostring(root, encoding='utf-8', method='xml')
    return xml_string.decode('utf-8')