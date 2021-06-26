# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:00:55 2021

@author: luciamarock
"""

import ctypes
from lxml import etree

BLACK_LIST = ["DI","AI","DO","AO","DA","AA_4T","PCO"]
PCO_STRUCTS = []

# finding all the PCOs
def find_all_by_type(root,object_type):
    return root.xpath(f"//Object[@type='{object_type}']")

def get_children(elements):
    children = []
    for element in elements:
        elem_children = element.getchildren()
        for child in elem_children:
            if child.tag == "Objects":
                Objects = child.getchildren()
                for Object in Objects:
                    if Object.attrib.get("type") not in BLACK_LIST:
                        children.append(Object)
    
    return children 

libInfo = ctypes.CDLL("./libinfo.so")   # g++ -o libinfo.so -shared -fPIC info.cpp
libInfo.pinfo() #libInfo = CDLL("./libinfo.so") 
 
tree = etree.parse("model.xml")
root = tree.getroot()
pco_list = find_all_by_type(root,"PCO")

#children = pco_master.getchildren()
for pco in pco_list:
    print("_______________________________________________________ processing PCO:: {} _______________________________________________________".format(pco.attrib.get("tag")))
    levels = []
    children = [pco]
    counter = 0
    while len(children) > 0 and counter < 10:
        counter = counter + 1
        children = get_children(children)
        if len(children) > 0:
            print("\t ------------------------------------------ adding children of level {} ------------------------------------------".format(counter))
            for child in children:
                print("\t {} of type {}".format(child.attrib.get("tag"),child.attrib.get("type")))
                levels.append(child)
    PCO_STRUCTS.append(levels)
    
print(PCO_STRUCTS)

 
'''
 Para cuando implementemos las funciones, Quiero una función que te devuelva todos los hijos de un PCO
todo lo que haya debajo de un PCO que no sea un IO o una alarma o también otro PCO (no queremos coger cosas que estén debajo de otro PCO)

    print(pco.attrib.get("tag"))
    children = pco.getchildren()
    for child in children:
        print("\t{}".format(child.tag))

 '''
 
 
 