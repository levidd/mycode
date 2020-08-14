#!/usr/bin/env python3

import requests ## 3rd party URL lookup
import datetime

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

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
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
        end = start + datetime.timedelta(days = 7)
    enddate = '&end_date=' + str(end) ## create a mechanism to utilize enddate
    mykey = '&api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c' ## replace this with our API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print("\n"*2)
    print("Number of NEOs being tracked during this timeframe:", neojson.get("element_count"))

    closest_NEO = min(neojson.get("near_earth_objects"), key = x: min(x, key=lambda t: t.get("close_approach_data")[0].get("miss_distance").get("miles")))
    print("Closest NEO is:" closest_NEO)

## call main
main()

