Stromer API

This Python package contains the interfaces for interacting with the Stromer web API that is normally used by the Stromer mobile app. Using this API you can retrieve data of your bike. This is the most complete and simple to use package to connect to your Stromer Bike without the need to use the mobile app. On top of that it offers features that the app does not provide (including downloading of data).

Installation:

    pip install -r requirements.txt
    pip install stromer_api

Usage:

    from stromer_api import StromerBike
    mybike = StromerBike(<your username>, <your password>, <stromer client id>)

    # access available data easily
    print(mybike.state.trip_distance)
    print(mybike.position.latitude)

    # modify bike sensors
    mybike.sensors.user_torque_sensitivity = 10

    # Export data to excel
    mybike.week_stats(2022,1,52).excel_dump("exported_data")

The client_id you should intercept using a proxy (eg. mitm proxy) or maybe it can be obtained from decompiling the android apk of the Stromer OMNI app. Many discussions can be found on the internet how to get hold of it.

The following properties can be accessed.

StromerBike class - getters:
* `mybike.bikeid (int)`
* `mybike.nickname (str)`
* `mybike.bikemodel (str)`
* `mybike.biketype (str)`
* `mybike.color (str)`
* `mybike.size (str)`
* `mybike.hardware (str)`
* `mybike.connectivity (str)`
* `mybike.has_crash_detection (bool)`

StromerBike class - setters:
* `mybike.reset_trip_data()`
* `mybike.lock()`
* `mybike.unlock()`
* `mybike.light("on" | "off" | "flash" )`

BikeMaintenance class:
* `mybike.maintenance_feature (BikeMaintenance)`
* `mybike.maintenance_feature.display_maintenance_event`
* `mybike.maintenance_feature.next_maintenance_km`
* `mybike.maintenance_feature.next_maintenance_date`
* `mybike.maintenance_feature.next_maintenance_interval`
* `mybike.maintenance_feature.customer_enabled_maintenance`
* `mybike.maintenance_feature.last_maintenance_reset_km`
* `mybike.maintenance_feature.last_maintenance_reset_date`

BikeState class:
* `mybike.state (BikeState)`
* `mybike.state.trip_distance (float)`
* `mybike.state.suiversion (str)`
* `mybike.state.average_speed_trip (float)`
* `mybike.state.power_on_cycles (int)`
* `mybike.state.tntversion (str)`
* `mybike.state.atmospheric_pressure (int)`
* `mybike.state.battery_SOC (int)`
* `mybike.state.assistance_level (int)`
* `mybike.state.bike_speed (float)`
* `mybike.state.trip_time (int)`
* `mybike.state.trip_time_str (str)`
* `mybike.state.battery_health (int)`
* `mybike.state.theft_flag (bool)`
* `mybike.state.motor_temp (float)`
* `mybike.state.battery_temp (float)`
* `mybike.state.rcvts (int)`
* `mybike.state.rcvts_str (str)`
* `mybike.state.average_energy_consumption (int)`
* `mybike.state.total_time (int)`
* `mybike.state.total_time (str)`
* `mybike.state.total_distance (float)`
* `mybike.state.light_on (int)`
* `mybike.state.total_energy_consumption (int)`
* `mybike.state.lock_flag (bool)`

BikePosition class:
* `mybike.position (BikePosition)`
* `mybike.position.latitude (float)`
* `mybike.position.longitude (float)`
* `mybike.position.altitude (int)`
* `mybike.position.speed (float)`
* `mybike.position.timets (int)`
* `mybike.position.timets_str (str)`
* `mybike.position.rcvts (int)`
* `mybike.position.rcvts_str (str)`

BikeStatistics class:
* `mybike.statistics (BikeStatistics)`
* `mybike.statistics.total_km (float)`
* `mybike.statistics.average_km (float)`
* `mybike.statistics.total_sec (int)`
* `mybike.statistics.total_time_str (str)`
* `mybike.statistics.average_sec (float)`
* `mybike.statistics.average_time_str (str)`
* `mybike.statistics.total_wh (int)`
* `mybike.statistics.average_wh (float)`
* `mybike.statistics.kmh (float)`
* `mybike.statistics.average_kmh (float)`
* `mybike.statistics.active_days (int)`
* `mybike.statistics.average_days (float)`

BikeSensors class - getters:
* `mybike.sensors (BikeSensors)`
* `mybike.sensors.user_torque_sensitivity (int)`
* `mybike.sensors.recup_level_user_offset (int)`

BikeSensors class - setters:
* `mybike.sensors.user_torque_sensitivity = <torque (int)>`
* `mybike.sensors.recup_level_user_offset = <recup (int)>`
* `mybike.sensors.set(<torque (int)>, <recup (int)>)`

BikeMotorTuning class - getters:
* `mybike.motor_tuning (BikeMotroTuning)`
* `mybike.motor_tuning.tuning_speed (int)`
* `mybike.motor_tuning.tuning_torque (int)`
* `mybike.motor_tuning.tuning_agility (int)`
* `mybike.motor_tuning.tuning_speed = <speed (int)>`
* `mybike.motor_tuning.tuning_torque = <torque (int)>`
* `mybike.motor_tuning.tuning_agility = <agility (int)>`
* `mybike.motor_tuning.set(<speed (int)>, <torque (int)>, <agility (int)>)`

BikeSettings class - getters:
* `mybike.settings (BikeSettings)`
* `mybike.settings.auto_lock_mode (bool)`
* `mybike.settings.auto_power_off_time (int)`
* `mybike.settings.clock_format (str)`
* `mybike.settings.date_format (str)`
* `mybike.settings.distance_unit (str)`
* `mybike.settings.language (str)`
* `mybike.settings.speed_unit (str)`
 
BikeSettings class - setters:
* `mybike.settings.auto_lock_mode = <mode (bool)>`
* `mybike.settings.auto_power_off_time = <time (int)>`
* `mybike.settings.clock_format = <format (str)>`
* `mybike.settings.date_format = <format (str)>`
* `mybike.settings.distance_unit = <unit (str)>`
* `mybike.settings.language = <language(str)>`
* `mybike.settings.speed_unit = <unit (str)>`
* `mybike.settings.set(<auto_lock_mode (bool)>, <auto_power_off_time (int)>, <clock_format (str)>, <date_format (str)>, <distance_unit (str)>, <language (str)>, <speed_unit (str)>)`

BikeUser class:
* `mybike.user (BikeUser)`
* `mybike.user.first_name (str)`
* `mybike.user.last_name (str)`
* `mybike.user.street_name (str)`
* `mybike.user.house_number (str)`
* `mybike.user.postal_code (str)`
* `mybike.user.city (str)`
* `mybike.user.country (str)`
* `mybike.user.phone (str)`
* `mybike.user.mobile (str)`
* `mybike.user.email (str)`
* `mybike.user.gender (str)`
* `mybike.user.size (float)`
* `mybike.user.weight (float)`
* `mybike.user.accepted_gdpr_version (str)`
* `mybike.user.may_receive_mails (bool)`

BikeShop class:
* `mybike.user.shop (BikeShop)`
* `mybike.user.shop.name (str)`
* `mybike.user.shop.street (str)`
* `mybike.user.shop.postal_code (str)`
* `mybike.user.shop.city (str)`
* `mybike.user.shop.country_code (str)`
* `mybike.user.shop.country_name (str)`
* `mybike.user.shop.phone (str)`
* `mybike.user.shop.latitude (float)`
* `mybike.user.shop.longitude (float)`
* `mybike.user.shop.debitor (float)`

ServiceInfo class:
* `mybike.service_info (ServiceInfo)`
* `mybike.service_info.shop (BikeShop)`
* `mybike.service_info.vin (str)`
* `mybike.service_info.serial (str)`
* `mybike.service_info.service_logs ([ServiceLog)]`
* `mybike.service_info.bike_parts ([BikePart)]`

ServiceLog class:
* `mybike.service_info.service_logs[] (ServiceLog)`
* `mybike.service_info.service_logs[].note (str)`
* `mybike.service_info.service_logs[].created_on (int)`

BikePart class:
* `mybike.service_info.bike_parts[] (BikePart)`
* `mybike.service_info.bike_parts[].serial (str)`
* `mybike.service_info.bike_parts[].name (str)`
* `mybike.service_info.bike_parts[].category (str)`

BikeShopList class:
* `mybike.shops.lookup(<part of shopname (str)>) (BikeShop)`
* `mybike.shops[i] (BikeShop)`

YearStats class:
* `mybike.year_stats(year (int), num_years (int)) (YearStats)`
* `mybike.year_stats(year (int), num_years (int)).start_date (str)`
* `mybike.year_stats(year (int), num_years (int)).end_date (str)`
* `mybike.year_stats(year (int), num_years (int)).total_years (int)`
* `mybike.year_stats(year (int), num_years (int)).km_avg_years_since_beginning (float)`
* `mybike.year_stats(year (int), num_years (int)).year_record (float)`
* `mybike.year_stats(year (int), num_years (int)).csv_dump()`
* `mybike.year_stats(year (int), num_years (int)).excel_dump()`
* `mybike.year_stats(year (int), num_years (int))[year (str)] (PeriodicInfo)`

MonthStats class:
* `mybike.month_stats(year (int), month (int), num_months (int)) (MonthStats)`
* `mybike.month_stats(year (int), month (int), num_months (int)).start_date (str)`
* `mybike.month_stats(year (int), month (int), num_months (int)).end_date (str)`
* `mybike.month_stats(year (int), month (int), num_months (int)).total_months (int)`
* `mybike.month_stats(year (int), month (int), num_months (int)).km_avg_12_months (float)`
* `mybike.month_stats(year (int), month (int), num_months (int)).month_record (float)`
* `mybike.monthg_stats(year (int), month (int), num_months (int)).csv_dump()`
* `mybike.monthg_stats(year (int), month (int), num_months (int)).excel_dump()`
* `mybike.monthg_stats(year (int), month (int), num_months (int))[month (str)] (PeriodicInfo)`

WeekStats class:
* `mybike.week_stats(year (int), week (int), num_weeks (int)) (WeekStats)`
* `mybike.week_stats(year (int), week (int), num_weeks (int)).start_date (str)`
* `mybike.week_stats(year (int), week (int), num_weeks (int)).end_date (str)`
* `mybike.week_stats(year (int), week (int), num_weeks (int)).total_weeks (int)`
* `mybike.week_stats(year (int), week (int), num_weeks (int)).km_avg_12_weeks (float)`
* `mybike.week_stats(year (int), week (int), num_weeks (int)).week_record (float)`
* `mybike.week_stats(year (int), week (int), num_weeks (int)).csv_dump()`
* `mybike.week_stats(year (int), week (int), num_weeks (int)).excel_dump()`
* `mybike.week_stats(year (int), week (int), num_weeks (int)).[week (str)] (PeriodicInfo)`

DayStats class:
* `mybike.day_stats(year (int), month (int), day (int), num_days (int)) (DayStats)`
* `mybike.day_stats(year (int), month (int), day (int), num_days (int)).start_date (str)`
* `mybike.day_stats(year (int), month (int), day (int), num_days (int)).end_date (str)`
* `mybike.day_stats(year (int), month (int), day (int), num_days (int)).total_days (int)`
* `mybike.day_stats(year (int), month (int), day (int), num_days (int)).km_avg_30_days (float)`
* `mybike.day_stats(year (int), month (int), day (int), num_days (int)).day_record (float)`
* `mybike.day_stats(year (int), month (int), day (int), num_days (int)).csv_dump()`
* `mybike.day_stats(year (int), month (int), day (int), num_days (int)).excel_dump()`
* `mybike.day_stats(year (int), month (int), day (int), num_days (int))[day (str)] (PeriodicInfo)`

Any suggestions for additions are of course also very welcome!
