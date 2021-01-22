import requests
import json


APIURL = "https://api.udentify.co"
APIUSER = "delandcaglar@hotmail.com"
APIPASS = "caglar2020"
APITOKEN = ""


#https://api.udentify.co/Store/240/AreaCount?sdate=15/10/2020&edate=30/10/2020&stime=10:00&etime=22:00&tzoffset=0

def get_token():
    url = "{}/token".format ( APIURL )
    payload = (("grant_type", "password"), ("username", APIUSER), ("password", APIPASS))
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    return requests.post ( url, data=payload, headers=headers ).json ()["access_token"]


def get_performancetable(storeId, start, end):
    global APITOKEN
    if APITOKEN == "":
        APITOKEN = get_token ()
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + APITOKEN,
    }

    #url = "{}/Store/{}/AreaTable?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset=0&layer=1".format ( APIURL,storeId,start,end )
    url = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset=0".format ( APIURL,
                                                                                                             storeId,
                                                                                                             start,
                                                                                                             end )
    r = requests.get ( url, headers=headers )
    return r.json ()


def main():
    data = get_performancetable ( 240, '15/10/2020', '30/10/2020' ) ##240 akasyaya baktigimiz icin
    #print ( data )

    #list_data = json.loads ( data )

    headersiz_data = ((data["Data"]))
    print(headersiz_data)
    print("________________________________")
    print(headersiz_data[0]["Name"]) # Labels tarih
    print ( headersiz_data[0]["Serial"] )
    print ( headersiz_data[1]["Name"] ) #Customer
    print ( headersiz_data[1]["Serial"] )
    print ( headersiz_data[3]["Name"] ) ##eime
    print ( headersiz_data[3]["Serial"] )


    #list_data = json.loads ( headersiz_data )

    #print(list_data['fruits'])


if __name__ == "__main__":
    main ()

