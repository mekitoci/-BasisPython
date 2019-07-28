import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
age = ET.SubElement(name, "age", attrib={"checked": "no"})
name.text = "Henry"
sex = ET.SubElement(name, "sex")
sex.text = '56'
personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name = ET.SubElement(personinfo2, "name")
name.text = "Kathy"
age = ET.SubElement(personinfo2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式