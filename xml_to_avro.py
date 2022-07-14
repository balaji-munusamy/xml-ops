# this file converts xml file to avro format with some conditions on xml elements
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import xml.etree.ElementTree as ET
from tqdm import tqdm

in_file_path=r"input.xml"
out_file_path=r"output.avro"

dict_schema = '''{ 
                    "namespace": "example.avro",
                    "name": "root", 
                    "type": "record", 
                    "fields": [
                                {"name": "attr1", "type": "string"},
                                {"name": "attr2", "type": "string"},
                                {"name": "attr3", "type": "string"}
                              ]
                    }'''

schema = avro.schema.parse(dict_schema)
writer = DataFileWriter(open(out_file_path, "wb"), DatumWriter(), schema)
count = 0
progress = tqdm(desc="Records", total=56264790)
for event, element in ET.iterparse(in_file_path, events=["start"]):
    if element.tag == "row":
        if element.attrib["attr2"]=="1": #condition to select xml elements
            writer.append({"attr1": element.attrib.get("attr1"), "attr2": "1", "attr3": element.attrib.get("attr3")}) #select xml attributes
    progress.update(count+1)
writer.close()
progress.close()

