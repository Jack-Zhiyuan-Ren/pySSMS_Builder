import xml.etree.ElementTree as ET
import os
import re

def xml2struct(file):
    tree = ET.parse(file)
    root = tree.getroot()
    return _element_to_dict(root)

def _element_to_dict(element):
    result = {}
    if len(element) == 0:
        return element.text

    for child in element:
        child_data = _element_to_dict(child)
        if child.tag not in result:
            result[child.tag] = child_data
        elif type(result[child.tag]) is list:
            result[child.tag].append(child_data)
        else:
            result[child.tag] = [result[child.tag], child_data]

    return result
    
# def xml2struct(file):
    # if file is None:
        # print("xml2struct usage:")
        # print("xml2struct(file)")
        # return
    
    # if isinstance(file, (org.apache.xerces.dom.DeferredDocumentImpl, org.apache.xerces.dom.DeferredElementImpl)):
        # input is a Java XML object
        # xDoc = file
    # else:
        # check for existence
        # if not os.path.isfile(file):
            # Perhaps the XML extension was omitted from the file name. Add the
            # extension and try again.
            # if not file.endswith('.xml'):
                # file = file + '.xml'
            
            # if not os.path.isfile(file):
                # raise FileNotFoundError(f"The file {file} could not be found")
        
        # read the XML file
        # xDoc = ET.parse(file)
    
    # parse xDoc into a Python structure
    # s = parseChildNodes(xDoc.getroot())
    
    # return s


# def parseChildNodes(node):
    # Recursively parse XML nodes into a Python structure
    # children = {}
    # ptext = {}
    # textflag = 'Text'

    # for child in node:
        # text, name, attr, childs, textflag = getNodeData(child)

        # if name not in ['#text', '#comment', '#cdata_dash_section']:
            # if name in children:
                # if not isinstance(children[name], list):
                    # children[name] = [children[name]]

                # children[name].append(childs)

                # if text:
                    # children[name][-1] = text

                # if attr:
                    # children[name][-1]['Attributes'] = attr
            # else:
                # children[name] = childs

                # if text:
                    # children[name] = text

                # if attr:
                    # children[name]['Attributes'] = attr
        # else:
            # ptextflag = 'Text'

            # if name == '#cdata_dash_section':
                # ptextflag = 'CDATA'
            # elif name == '#comment':
                # ptextflag = 'Comment'
            
            # if text and text[textflag].strip():
                # if ptextflag not in ptext or not ptext[ptextflag].strip():
                    # ptext[ptextflag] = text[textflag]
                # else:
                    # ptext[ptextflag] += text[textflag]
    
    # if ptext:
        # if len(ptext) == 1:
            # textflag = next(iter(ptext))
            # ptext = ptext[textflag]
        # else:
            # textflag = 'Text'
            # ptext = ptext.get('Text', '')

    # if children:
        # return children, ptext, textflag
    # else:
        # return ptext, None, textflag


# def getNodeData(node):
    # Create structure of node info
    # name = re.sub(r'[-:.]', lambda m: f"_{m.group(0)}", node.tag)
    # attr = parseAttributes(node)

    # if node.text and node.text.strip() and not any(child.tag != '#text' for child in node):
        # text = { 'Text': node.text.strip() }
    # else:
        # text, _, textflag = parseChildNodes(node)

    # return text, name, attr, text, textflag


# def parseAttributes(node):
    # Create attributes structure
    # attributes = {}

    # for key, value in node.attrib.items():
        # attr_name = re.sub(r'[-:.]', lambda m: f"_{m.group(0)}", key)
        # attributes[attr_name] = value

    # return attributes