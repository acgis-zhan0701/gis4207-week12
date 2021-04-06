import Streetlight_analyzer as Sta
import os

Sta.roads_cl_fc = "../../../../data/Ottawa/Road_Centrelines/Road_Centrelines.shp"
Sta.streetlight_fc = "../../../../data/Ottawa/Street_Lights/Street_Lights.shp"
Sta.road_name_field = 'ROAD_NAME_'

def test_get_unique_values():
    expected = 8674
    actual = len(Sta._get_unique_value(Sta.roads_cl_fc, Sta.road_name_field))
    assert expected == actual

def test_get_street_light_count():
    expected = '589'
    actual = str(Sta.get_streetlight_count('RIVERSIDE DR', 0.0002))
    assert expected == actual

def test_save_streetlights():
    actual = os.path.isfile(str(Sta.save_streetlights('RIVERSIDE DR', 0.0002)))
    assert actual == True

