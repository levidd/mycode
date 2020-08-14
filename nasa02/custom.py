#!/usr/bin/env python3

import requests  ## 3rd party URL lookup
import datetime # for date for use in API call
import sys
from pprint import pprint
from lazy_streams import stream  # like java8 streams


def getDate():
    returning = None
    while returning == None:
        try:
            print("Date format in dd/mm/yy")
            returning = datetime.datetime.strptime(input(), "%d/%m/%y")
        except:
            print("Invalide date, try again")
    return returning


def get_moon_lengths(missdistance):
    moon_length = 238900.0
    return missdistance / moon_length


def getDistance(neo_obj):
    return neo_obj.get("close_approach_data")[0].get("miss_distance").get("miles")


def findClosestNeo(neos):
    # with lazy-streams
    returning = stream(list(neos.values())) \
        .flatten() \
        .min(key=getDistance)

    # other pythonic way
    # minDistance = sys.maxsize
    # returning = None
    # for date in neos:
    #     closest_neo = min(neos.get(date), key=lambda x: getDistance(x))
    #     if minDistance > float(getDistance(closest_neo)):
    #         returning = closest_neo
    #         minDistance = float(getDistance(returning))

    return returning.get("links").get("self")


def areHazardous(neos):
    returning = []

    # with lazy streams
    returning = stream(list(neos.values())) \
        .flatten() \
        .filter(lambda x: x.get("is_potentially_hazardous_asteroid")) \
        .map(lambda x: x.get("links").get("self")) \
        .to_list()

    # more pythonic way
    # for date in neos:
    #     returning.extend(map(lambda t: t.get("links").get("self"), filter(lambda x: x.get("is_potentially_hazardous_asteroid"), neos.get(date))))

    return returning


## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'  # API URL
    print("Need to get the start date to pull data from NASA")
    start = getDate()
    startdate = 'start_date=' + str(start)  ## start date for data
    end = None
    print("End date..")
    if input("Skip? Type yes or y, otherwise assumed no ").strip().lower() not in ["yes", "y"]:
        end = getDate()
        while abs((start - end).days) > 7:
            print("End date needs to be between 0 to 7 days from start date")
            end = getDate()

    if end == None:
        end = start + datetime.timedelta(days=7)
    enddate = '&end_date=' + str(end)  ## create a mechanism to utilize enddate
    mykey = '&api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c'  ## replace this with our API key

    neourl = neourl + startdate + enddate + mykey

    neojson = (requests.get(neourl)).json()

    print("\n" * 2)
    print("Number of NEOs being tracked during this timeframe:", neojson.get("element_count"))
    closest_NEO = findClosestNeo(neojson.get("near_earth_objects"))
    print("Closest NEO is:", closest_NEO)

    print("All the hazardous neos are:")
    pprint(areHazardous(neojson.get("near_earth_objects")))


## call main
main()
