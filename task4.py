from xml.dom.minidom import *

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
cnt = 0
summa = 0

# Count sum Value and count of Values to know average
for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Value':
                if child.firstChild.nodeType == 3:
                    price = child.firstChild.data
                    price = price.replace(',', '.')
                    price = float(price)
                    summa += price
                    cnt += 1

print(summa / cnt)

xml_file.close()
