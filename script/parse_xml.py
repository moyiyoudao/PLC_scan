from xml.etree import ElementTree as ET
tree = ET.parse('out.xml')
root = tree.getroot()

#print(list(root))
#print(root.tag,':',root.attrib)
all_data = []
for i in list(root):
    if(len(list(i))!=0):
        print(i.tag, ':', i.attrib)
        for iters in list(i):
            if (len(list(iters)) != 0):
                print('\t',iters.tag, ':', iters.attrib)
                for iterss in list(iters):
                    if (len(list(iterss))!=0):
                        print('\t\t', iterss.tag, ':', iterss.attrib)
                        for itersss in list(iterss):
                            print('\t\t\t',itersss.tag,':',itersss.attrib)
                    else:
                        print('\t\t', iterss.tag, ':', iterss.attrib)

            else:
                print('\t', iters.tag, ':', iters.attrib)

    else:
        print(i.tag, ':', i.attrib)