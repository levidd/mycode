#!/usr/bin/env python3

import requests  ## 3rd party URL lookup
import datetime  # for date for use in API call
import wget


def getDate():
    returning = None
    other_date = input("Do you want today or another date? \nyes (y), otherwise assumed no\n")
    if other_date.lower().strip() in ["yes", "y"]:
        while returning is None:
            try:
                print("Date format in YY-MM-DD")
                returning = datetime.datetime.strptime(input(), "%y-%m-%d")
            except ValueError:
                print("Invalide date, try again")

            if returning is not None and returning < datetime.datetime(1995, 6, 16):
                print("Cannot go earlier than Jun 16, 1995")
                returning = None

    return returning


def getHD():
    returning = None
    while returning is None:
        ans = input("Do you want HD (1) or standard picture? (2)\n").lower().strip()
        if ans in ["hd", "1"]:
            returning = True
        elif ans in ["standard", "standard picture", "2"]:
            returning = False
        else:
            print("I need an answer to my question that I understand. I'm a computer so be more specific")
    return returning


def main():
    url = 'https://api.nasa.gov/planetary/apod?'
    date = getDate()
    hd = getHD()
    api_key = 'api_key=tIclf3RKV3YHj71xOlyp1rQr9Hl85TSpJtuoVg9c'

    url += api_key

    if date is not None:
        url += "&date=" + str(date.date())

    r = requests.get(url).json()

    print("Date: " + r.get("date"))
    print("Title: " + r.get("title"))
    print("Explanation" + r.get("explanation"))

    pic_url = ''
    if hd and "hdurl" in r:
        pic_url = r.get('hdurl')
    elif "url" in r:
        pic_url = r.get('url')

    if pic_url != '':
        wget.download(pic_url, "downloads/")


if __name__ == '__main__':
    main()
