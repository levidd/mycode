#!/usr/bin/env python3

import custom
import pytest

# from nasa02 import custom

@pytest.mark.parametrize("test_input, expected", [(0, 0), (455, 0.0019045625784847), (1234.5342, 0.0051675772289661)])
def test_get_moon_lengths(test_input, expected):
    assert abs(custom.get_moon_lengths(test_input) - expected) < 1e10

def test_getDistance(api_data):
    objs = api_data.get("near_earth_objects").get("2020-08-27")
    assert "28392401.166752195" == custom.getDistance(objs[0])
    assert "27598426.6606323198" == custom.getDistance(objs[1])

def test_findClosestNeo(api_data):
    objs = api_data.get("near_earth_objects")
    assert "http://www.neowsapp.com/rest/v1/neo/2085275?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c" == custom.findClosestNeo(objs)


def test_areHazardous(api_data):
    objs = api_data.get("near_earth_objects")
    hazards = ['http://www.neowsapp.com/rest/v1/neo/2505657?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                'http://www.neowsapp.com/rest/v1/neo/3692867?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/2477519?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/3508168?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/3588013?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/3390647?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/2065690?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/2411165?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/2221980?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/3381448?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/2452302?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/2455148?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c',
                 'http://www.neowsapp.com/rest/v1/neo/54049354?api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c']

    assert hazards == custom.areHazardous(objs)


