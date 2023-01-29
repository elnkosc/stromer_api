Stromer API

This Python package contains the interfaces for interacting with the Stromer web API that is normally used by the Stromer mobile app. Using this API you can retrieve data of your bike.

Installation:

    pip install stromer_api

Usage:

    from stromer_api import StromerBike
    mybike = StromerBike(<your username>, <your password>, <stromer client id>)

    print(mybike.state.trip_distance)
    print(mybike.position.latitude)

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
* `.bike.sensors`
* `.bike.sensors.user_torque_sensitivity`
* `.bike.sensors.recup_level_user_offset`
* `.bike.motor_tuning`
* `.bike.motor_tuning.tuning_speed`
* `.bike.motor_tuning.tuning_torque`
* `.bike.motor_tuning.tuning_agility`
* `.bike.settings`
* `.bike.settings.auto_lock_mode`
* `.bike.settings.auto_power_off_time`
* `.bike.settings.clock_format`
* `.bike.settings.date_format`
* `.bike.settings.distance_unit`
* `.bike.settings.language`
* `.bike.settings.speed_unit`
* `.bike.user`
* `.bike.user.first_name`
* `.bike.user.last_name`
* `.bike.user.street_name`
* `.bike.user.house_number`
* `.bike.user.postal_code`
* `.bike.user.city`
* `.bike.user.country`
* `.bike.user.phone`
* `.bike.user.mobile`
* `.bike.user.email`
* `.bike.user.gender`
* `.bike.user.size`
* `.bike.user.weight`
* `.bike.user.accepted_gdpr_version`
* `.bike.user.may_receive_mails`
* `.bike.user.shop `
* `.bike.user.shop.name`
* `.bike.user.shop.street`
* `.bike.user.shop.postal_code`
* `.bike.user.shop.city`
* `.bike.user.shop.country_code`
* `.bike.user.shop.country_name`
* `.bike.user.shop.phone`
* `.bike.user.shop.latitude`
* `.bike.user.shop.longitude`
* `.bike.user.shop.debitor`
* `.bike.year_stats(year, num_years)`
* `.bike.year_stats(year, num_years).info`
* `.bike.year_stats(year, num_years).start_date`
* `.bike.year_stats(year, num_years).end_date`
* `.bike.year_stats(year, num_years).total_years`
* `.bike.year_stats(year, num_years).km_avg_years_since_beginning`
* `.bike.year_stats(year, num_years).year_record`
* `.bike.year_stats(year, num_years).csv_dump()`
* `.bike.year_stats(year, num_years)[year]`
* `.bike.month_stats(year, month, num_months)`
* `.bike.month_stats(year, month, num_months).info`
* `.bike.month_stats(year, month, num_months).start_date`
* `.bike.month_stats(year, month, num_months).end_date`
* `.bike.month_stats(year, month, num_months).total_months`
* `.bike.month_stats(year, month, num_months).km_avg_12_months`
* `.bike.month_stats(year, month, num_months).month_record`
* `.bike.monthg_stats(year, month, num_months).csv_dump()`
* `.bike.monthg_stats(year, month, num_months)[month]`
* `.bike.week_stats(year, week, num_weeks)`
* `.bike.week_stats(year, week, num_weeks).info`
* `.bike.week_stats(year, week, num_weeks).start_date`
* `.bike.week_stats(year, week, num_weeks).end_date`
* `.bike.week_stats(year, week, num_weeks).total_weeks`
* `.bike.week_stats(year, week, num_weeks).km_avg_12_weeks`
* `.bike.week_stats(year, week, num_weeks).week_record`
* `.bike.week_stats(year, week, num_weeks).csv_dump()`
* `.bike.week_stats(year, week, num_weeks).[week]`
* `.bike.day_stats(year, month, day, num_days)`
* `.bike.day_stats(year, month, day, num_days).info`
* `.bike.day_stats(year, month, day, num_days).start_date`
* `.bike.day_stats(year, month, day, num_days).end_date`
* `.bike.day_stats(year, month, day, num_days).total_days`
* `.bike.day_stats(year, month, day, num_days).km_avg_30_days`
* `.bike.day_stats(year, month, day, num_days).day_record`
* `.bike.day_stats(year, month, day, num_days).csv_dump()`
* `.bike.day_stats(year, month, day, num_days)[day]`

This API makes use of the "unofficial" endpoints /bike, /bike/<bike_id>/state, and /bike/<bike_id>/position. If you are aware of new or others that work please leave a message.

Any suggestions for additions are of course also very welcome!
