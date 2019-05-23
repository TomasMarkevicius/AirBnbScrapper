# AirBnb scrapper homework by Tomas Markevicius
import sys
import requests
from bs4 import BeautifulSoup

# Turns our html into a soup object which is used to parse and search through html page
def getSoup(htmlContent):
    # Here we give the content to parse and specify which parser to use
    soup = BeautifulSoup(htmlContent,"html.parser")
    return soup

# This method returns a string value of appartment type
def getAppartment(soup):
    # We get appartment type
    appartmentType = soup.find("div", "_1p3joamp")
    if (appartmentType is not None):
        return appartmentType.getText()
    else:
        return "None"

def getRooms(soup):
    # We find appartment div
    appartmentType = soup.find("div", "_1p3joamp")
    # We find room div that follows appartment div
    roomDiv = appartmentType.find_next("div")
    # We use span with value of czm8crp to find all rooms in that div
    listOfRooms = roomDiv.find_all("span", "_czm8crp")
    # If there are no rooms we just return an empty string
    if (listOfRooms is []):
        return ""
    # Final string acts as a string builder
    finalString = ""
    # We iterate through all of the rooms, get their text and concatenate it together
    for room in listOfRooms:
        roomName = room.getText()
        finalString += roomName +  ", "
    # We remove the last unecessary comma
    finalString = finalString[:-2]
    return finalString

def getAmenities(soup):
    # We find amenities div
    amenities = soup.find("div", "_18ilrswp")
    # We find room div that follows amenities div
    amenitiesDiv = amenities.find_next("div")
    # we use div with valuie of czm8crp to find all amenities in that div
    listOfAmenities = amenitiesDiv.find_all("div", "_czm8crp")
    # If there are no amenities we just return an empty string
    if (listOfAmenities is []):
        return ""
    # Acts like string builder
    finalString = ""
    # We iterate through all of the amenities get their values and concatenate them
    for amenity in listOfAmenities:
        amenityName = amenity.getText()
        finalString += amenityName+  ", "
    # We remove the last unecessary comma
    finalString = finalString[:-2]
    return finalString

# Method for fetch page content from a supplied URL
def getPageContent(url):
    # Here we try to get the page from url
    try:
        page = requests.get(url)
    # We throw exception in case our request fails due to timeout, wrong url or some other reasons
    except requests.exceptions.RequestException as e:
        print("Request error! Details below:\n")
        print(e)
        sys.exit(1)
    return page.content

# Prints air bnb scrapped data nicely
def printDetails(url):
    print("---------------------")

    print("Property url:")
    print(url)

    page = getPageContent(url)
    soup = getSoup(page)

    print("Appartment type:")
    print( getAppartment(soup))

    print("Rooms:")
    print( getRooms(soup))

    print("Amenities:")
    print(getAmenities(soup))

def program():
    input1 = 'https://www.airbnb.co.uk/rooms/14531512?s=51'
    printDetails(input1)
    input2 = "https://www.airbnb.co.uk/rooms/19278160?s=51"
    printDetails(input2)
    input3 = "https://www.airbnb.co.uk/rooms/1939240?s=51"
    printDetails(input3)

# We run our program here
program()

