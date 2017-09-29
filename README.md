 # BabyOnBoard-API

### Heartbeat Sensor to Api comunication

Initially the sensor reading will be through TXT files that will be sent by the MSP to the Rasp.

Expected JSON that comes from heartbeat sensor:

````json
[
    {
      "heartbeat":97,
      "timestamp":1234567898
    },
    {
      "heartbeat":97,
      "timestamp":1234567898
    },
    {
      "heartbeat":97,
      "timestamp":1234567898
    }
]
````

* heartbeat - BPM
* timestamp - unixtimestamp

The APi will parse the file into the local database and forward it to the clients throug a REST API



### Temperature Sensor to Api comunication

Initially the sensor reading will be through TXT files that will be sent by the MSP to the Rasp.

Expected JSON that comes from temperature sensor:

```json
[
    {
      "temperature":37,
      "timestamp":1234567898
    },
    {
      "temperature":37,
      "timestamp":1234567898
    },
    {
      "temperature":37,
      "timestamp":1234567898
    }
]
```

* temperature - Celcius
* timestamp - Unix timestamp

The APi will parse the file into the local database and forward it to the clients throug a REST API

### Breathing Sensor to Api comunication

Initially the sensor reading will be through TXT files that will be sent by the MSP to the Rasp.

Expected JSON that comes from breathing sensor:

```json
[
    {
      "breathing":true,
      "timestamp":1234567898
    },
    {
      "breathing":true,
      "timestamp":1234567898
    },
    {
      "breathing":true,
      "timestamp":1234567898
    }
]
```

- temperature - Boolean value
- timestamp - Unix timestamp

The APi will parse the file into the local database and forward it to the clients throug a REST API