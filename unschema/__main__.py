import sys
import xml.etree.ElementTree as ET

def convert_kml(input_path, output_path):
    ns = {"kml": "http://www.opengis.net/kml/2.2"}

    tree = ET.parse(input_path)
    root = tree.getroot()

    # Remove <Schema> blocks
    for schema in root.findall(".//kml:Schema", ns):
        parent = root.find(".//kml:Document", ns) or root
        parent.remove(schema)

    # Replace <SchemaData> with <Data>
    for schema_data in root.findall(".//kml:SchemaData", ns):
        # Find the parent ExtendedData element
        for ext_data in root.findall(".//kml:ExtendedData", ns):
            if schema_data in ext_data:
                # Create Data elements from SimpleData
                for simple in schema_data.findall("kml:SimpleData", ns):
                    data_el = ET.Element("Data", name=simple.attrib["name"])
                    value_el = ET.SubElement(data_el, "value")
                    value_el.text = simple.text or ""
                    ext_data.append(data_el)
                # Remove the SchemaData element
                ext_data.remove(schema_data)
                break

    ET.register_namespace('', "http://www.opengis.net/kml/2.2")
    tree.write(output_path, encoding="utf-8", xml_declaration=True)

def main():
    if len(sys.argv) != 3:
        print("Usage: unschema <input.kml> <output.kml>")
        sys.exit(1)
    convert_kml(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()