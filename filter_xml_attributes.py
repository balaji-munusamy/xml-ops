import xml.etree.ElementTree as ET
from tqdm import tqdm

in_file_path = r"input.xml"
out_file_path = r"output.xml"

# print("parsing started...")
# tree = ET.parse(file_path) # element tree
# print("parsing finished...")
# root = tree.getroot()
# print("processing...")
# for child in tqdm(root[:]):
#     if child.attrib["attr2"] == "1" : #NOTE: condition to filter xml elements
#         pop_keys = [key for key in child.attrib.keys() if key not in ["attr1", "attr2", "attr3"] ] #Remove attributes other than specified
#         for key in pop_keys:
#             child.attrib.pop(key)
#     else:
#         root.remove(child)
# print("processed!")
# tree.write("output.xml")

file_out = open(out_file_path, 'w', encoding='utf-8')
root = ET.Element('root')
file_out.write("<root>\n")
count = 0
progress = tqdm(desc="Records", total=56264790 #optional total number of records
for event, element in ET.iterparse(in_file_path, events=["start"]):
    if element.tag == "row":
        if element.attrib["attr2"]=="1": #NOTE: condition to filter xml elements
            pop_keys = [key for key in element.attrib.keys() if key not in ["attr1", "attr2", "attr3"]] #Remove attributes other than specified
            for key in pop_keys:
                element.attrib.pop(key)
            post = ET.SubElement(posts, element.tag, element.attrib)
            file_out.write(ET.tostring(post).decode('utf-8'))
            file_out.write("\n")
    progress.update(count+1)
progress.close()
file_out.write("</root>")
file_out.flush()
file_out.close()

