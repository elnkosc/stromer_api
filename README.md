Stromer API

This Python package contains the interfaces for interacting with the Stromer web API that is normally used by the Stromer mobile app. Using this API you can retrieve data of your bike.

Create object and access your bike data:

    `mybike = StromerBike(<your username>, <your password>, <stromer client id>)`
    `print(mybike.state.trip_distance)`
    `print(mybike.position.latitude)`

The client_id you should intercept using a proxy (eg. mitm proxy) or maybe it can be obtained from decompiling the android apk of the Stromer OMNI app. Many discussions can be found on the internet how to get hold of it.

This API makes use of the "unofficial" endpoints /bike, /bike/<bike_id>/state, and /bike/<bike_id>/position. If you are aware of new or others that work please leave a message.

Any suggestions for additions are of course also very welcome!
