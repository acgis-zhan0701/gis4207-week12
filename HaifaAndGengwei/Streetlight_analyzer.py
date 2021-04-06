import arcpy
from arcpy import env
import os


streetlight_fc = None
roads_cl_fc = None
road_name_field = None


def _get_unique_value(fc,field_name):
    with arcpy.da.SearchCursor(fc,field_name) as cursor:
        uniList = []
        for row in cursor:
            if not row[0] in uniList:
                uniList.append(row[0])
    return uniList


def get_streetlight_count(road_name, distance):
    ws= os.path.dirname(roads_cl_fc)
    field=arcpy.AddFieldDelimiters(ws,'ROAD_NAME_')
    if road_name not in _get_unique_value(roads_cl_fc, 'ROAD_NAME_'):
        print(f"{road_name} doesn t exist")
    
    wc= f"{field} = '{road_name.upper()}'"
    
    select_road_name = arcpy.management.SelectLayerByAttribute(roads_cl_fc, 'NEW_SELECTION', where_clause=wc)
    select_street_lights = arcpy.management.SelectLayerByLocation(streetlight_fc, 'WITHIN_A_DISTANCE', select_road_name, distance, "SUBSET_SELECTION")
    number_of_selected = arcpy.GetCount_management(select_street_lights)
    return number_of_selected

def save_streetlights(road_name, distance):
    ws= os.path.dirname(roads_cl_fc)
    field=arcpy.AddFieldDelimiters(ws,'ROAD_NAME_')
    if road_name not in _get_unique_value(roads_cl_fc, 'ROAD_NAME_'):
        print(f"{road_name} doesn t exist")
    
    wc= f"{field} = '{road_name.upper()}'"
    
    select_road_name = arcpy.management.SelectLayerByAttribute(roads_cl_fc, 'NEW_SELECTION', where_clause=wc)
    selected_layer = arcpy.management.SelectLayerByLocation(streetlight_fc, 'WITHIN_A_DISTANCE', select_road_name, distance, "SUBSET_SELECTION")
    output = arcpy.SaveToLayerFile_management(selected_layer, r"C:\Users\admin\Desktop\4207\data\Ottawa\selected_street_lights.lyrx")
    return output

def show_road_names(pattern=None):
    if pattern == None:
        return _get_unique_value(roads_cl_fc, 'ROAD_NAME_')
    else:
        wc = f"{'ROAD_NAME_'} LIKE '%" + pattern.upper() + "%'"
        with arcpy.da.SearchCursor(roads_cl_fc,'ROAD_NAME_', wc) as cursor:
            uniList = []
            for row in cursor:
                if not row[0] in uniList:
                    uniList.append(row[0])
        return uniList



