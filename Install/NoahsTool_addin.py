import arcpy
import pythonaddins
import urllib, urllib2, json




class ButtonClass1(object):
    """Implementation for NoahsTool_addin.button1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class GoogleSearchComboBox(object):
    """Implementation for NoahsTool_addin.combobox1 (ComboBox)"""
    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = ''
        self.width = '1234567890123456789012345678901234567890123456789012345678901234567890'
    def onSelChange(self, selection):
        pass
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        pass
    def onEnter(self):
        print "Current Value:",self.value
        address = self.value
        def decode_address_to_coordinates(address):
                params = {
                        'address' : address,
                        'sensor' : 'false',
                }  
                url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
                response = urllib2.urlopen(url)
                result = json.load(response)
                try:
                        return result['results'][0]['geometry']['location']
                except:
                        print "The given address did not work."
                        return
        lat = decode_address_to_coordinates(address)['lat']
        lng = decode_address_to_coordinates(address)['lng']
        print lat
        print lng
        def panToExtent(lat,lng):
                mxd = arcpy.mapping.MapDocument('CURRENT')
                dataFrame = arcpy.mapping.ListDataFrames(mxd)[0]
                extent = arcpy.Extent(lng, lat, lng, lat)
                dataFrame.panToExtent(extent)
                dataFrame.scale = 12000 # 1:1,000
                arcpy.RefreshActiveView()
        panToExtent(lat,lng)
    def refresh(self):
        pass
