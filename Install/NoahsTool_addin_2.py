import arcpy
import pythonaddins

class ButtonClass1(object):
    """Implementation for NoahsTool_addin.button1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.MessageBox("woot","this worked",0)