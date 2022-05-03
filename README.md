Stromer API

This Python package contains the interfaces for interacting with the Stromer web API that is normally used by the Stromer mobile app. Using this API you can retrieve data of your bike.

Installation:

    `pip install stromer_api`

Usage:

    `from stromer_api import StromerBike`
    `mybike = StromerBike(<your username>, <your password>, <stromer client id>)`

    `print(mybike.state.trip_distance)`
    `print(mybike.position.latitude)`

The client_id you should intercept using a proxy (eg. mitm proxy) or maybe it can be obtained from decompiling the android apk of the Stromer OMNI app. Many discussions can be found on the internet how to get hold of it.

The following properties can be accessed:
* `.state`
* `.state.trip_distance`
* `.state.suiversion`
* `.state.average_speed_trip`
* `.state.power_on_cycles`
* `.state.tntversion`
* `.state.atmospheric_pressure`
* `.state.battery_SOC`
* `.state.assistance_level`
* `.state.bike_speed`
* `.state.trip_time`
* `.state.trip_time_str`
* `.state.battery_health`
* `.state.theft_flag`
* `.state.motor_temp`
* `.state.battery_temp`
* `.state.rcvts`
* `.state.rcvts_str`
* `.state.average_energy_consumption`
* `.state.total_time`
* `.state.total_time`
* `.state.total_distance`
* `.state.light_on`
* `.state.total_energy_consumption`
* `.state.lock_flag`
* `.position`
* `.position.latitude`
* `.position.longitude`
* `.position.altitude`
* `.position.speed`
* `.position.timets`
* `.position.timets_str`
* `.position.rcvts`
* `.position.rcvts_str`

This API makes use of the "unofficial" endpoints /bike, /bike/<bike_id>/state, and /bike/<bike_id>/position. If you are aware of new or others that work please leave a message.

Any suggestions for additions are of course also very welcome!
