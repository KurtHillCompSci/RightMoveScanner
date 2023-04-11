from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import webbrowser


def get_latest_property_id(rightmove_url):
    html = urlopen(rightmove_url).read()
    soup = BeautifulSoup(html, features="html.parser")
    return soup.find_all("a", {"class": "propertyCard-priceLink"})[1]['href'][12:-18]

def main():
    counter = 0
    sleep_timer = 300
    search_url = "https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E1483&minBedrooms=3&maxPrice=280000&sortType=6&propertyTypes=detached%2Csemi-detached%2Cterraced&includeSSTC=false&mustHave=&dontShow=retirement%2CsharedOwnership&furnishTypes=&keywords="

    current_property = get_latest_property_id(search_url)
    print("\nInitialising with Property",current_property,"\n")
    time.sleep(sleep_timer/10)

    while True:
        counter += 1
        print("==============================================")
        
        temp_property = get_latest_property_id(search_url)
        if temp_property != current_property:
            current_property = temp_property
            webbrowser.get().open("www.rightmove.co.uk/properties/"+current_property)
            print("  New Property Found! Opening Property",current_property)
            
        else:
            print("  No New Properties found...")
            
        print("  Counter:",counter)
        print("  Trying again in", sleep_timer, "seconds")
        print("==============================================\n")
            

        time.sleep(sleep_timer)

if __name__=="__main__":
    main()
    
