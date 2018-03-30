import inspect
import maya.OpenMaya as OpenMaya
import maya.api.OpenMaya as OpenMaya2
import maya.OpenMayaAnim as OpenMayaAnim
import maya.api.OpenMayaAnim as OpenMayaAnim2
import maya.OpenMayaRender as OpenMayaRender
import maya.api.OpenMayaRender as OpenMayaRender2
import maya.OpenMayaUI as OpenMayaUI
import maya.api.OpenMayaUI as OpenMayaUI2
import maya.OpenMayaFX as OpenMayaFX

defunct_classes = set(['MScriptUtil','uCharPtr', 'shortPtr', '_object', 'floatPtr', '_swig_property', 'intPtr', 'charPtr', 'boolPtr', 'doublePtr', 'uIntPtr'])

def get_api_classes(module):
    classes = set()
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            classes.add(name)
    return classes

def get_missing_classes(module1, module2):
    classes1 = get_api_classes(module1)
    classes2 = get_api_classes(module2)
    return classes1 - classes2 - defunct_classes

def print_module_report(module, classes):
    print "These are the {} 1.0 classes missing in 2.0:".format(module.__name__)
    for item in classes:
        print "\t{}".format(item)
    
    print ""
        
def print_full_classes_report():
    missing_openmaya = get_missing_classes(OpenMaya, OpenMaya2)
    missing_anim = get_missing_classes(OpenMayaAnim, OpenMayaAnim2)
    missing_render = get_missing_classes(OpenMayaRender, OpenMayaRender2)
    missing_ui = get_missing_classes(OpenMayaUI, OpenMayaUI2)
    
    print_module_report(OpenMaya, missing_openmaya)
    print_module_report(OpenMayaAnim, missing_anim)
    print_module_report(OpenMayaRender, missing_render)
    print_module_report(OpenMayaUI, missing_ui)
    

if __name__ == "__main__":
    print_full_classes_report()


