Import json 
Import viotp.sdk.device
Import time 
myConfig = { 
     "identity":{ 
          "orgId":  "3cghy5", 
          "typeId": "Childsafty",
          "deviceId": "2631"
     },
     "auth":{ 
          "token": "87654321"
     } 
}
client wiotp.sdk.device. DeviceClient (config-myConfig, logHandlers=None)
client.connect()
while True:
    name="Smartbridge"
    #in area location
    latitude= 17.4225176
    longitude 78.5458842 
    #out area location
    #latitude= 17.4219272
    #longitude= 78.5488783
    myData={'name': name, 'lat': latitude, 'lon': longitude)
    client.publishEvent (eventId="status", msgFormat="json", data-myData, qos=0, onPublish=None)
    print("Data published to IBM IoT platform: ",myData)
    time.sleep(5)

Client.disconnect()
