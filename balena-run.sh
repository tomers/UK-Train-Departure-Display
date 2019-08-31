#!/usr/bin/env bash

# Show 'Not Connected' message
python ./src/process.py
sleep 60

export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

# Optional step - it takes couple of seconds (or longer) to establish a WiFi connection
# sometimes. In this case, following checks will fail and wifi-connect
# will be launched even if the device will be able to connect to a WiFi network.
# If this is your case, you can wait for a while and then check for the connection.
sleep 15

# Choose a condition for running WiFi Connect according to your use case:

# 1. Is there a default gateway?
# ip route | grep default

# 2. Is there Internet connectivity?
# nmcli -t g | grep full

# 3. Is there Internet connectivity via a google ping?
# wget --spider http://google.com 2>&1

# 4. Is there an active WiFi connection?
iwgetid -r

if [ $? -eq 0 ]; then
    printf 'Skipping WiFi Connect\n'
else
    printf 'Starting WiFi Connect\n'
    ./wifi-connect
fi


if [ ! -f config.json ]; then
  cp config.sample.json config.json
  jq .journey.departureStation=\""${departureStation}"\" config.json | sponge config.json
  jq .journey.destinationStation=\""${destinationStation}"\" config.json | sponge config.json
  jq .journey.outOfHoursName=\""${outOfHoursName}"\" config.json | sponge config.json
  jq .refreshTime="${refreshTime}" config.json | sponge config.json
  jq .transportApi.appId=\""${transportApi_appId}"\" config.json | sponge config.json
  jq .transportApi.apiKey=\""${transportApi_apiKey}"\" config.json | sponge config.json
  jq .transportApi.operatingHours=\""${transportApi_operatingHours}"\" config.json | sponge config.json
fi

# python ./src/main.py

# Start your application here.
sleep infinity
