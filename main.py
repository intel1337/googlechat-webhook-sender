from datetime import datetime
import sys
from json import dumps
from httplib2 import Http
import os

def main():
    myobj = datetime.now()
    os.system('clear')
    print("Current hour ", myobj.hour)
    print("Current minute ", myobj.minute)
    url = input("Enter WebHook URL : ")
    exos = input("Enter Exos Content : ")
    while True:
        if myobj.hour == 9 and myobj.minute == 0: # Change to == instead of != for the code to work as a service and not a test version
            app_message = {"text": "Salut c'est le bot des exos du matin ! Voici un exo au hasard : " + exos}
            message_headers = {"Content-Type": "application/json; charset=UTF-8"}
            http_obj = Http()
            response = http_obj.request(
                uri=url,
                method="POST",
                headers=message_headers,
                body=dumps(app_message),
            )
            print(response)

if __name__ == "__main__":
    main()

