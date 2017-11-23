# BabyOnBoard-API

![Build Status](https://travis-ci.org/BabyOnBoard/BabyOnBoard-API.svg?branch=master)

## API to clients comunication

The endpoints will return JSON responses by default, being also capable of rendering web interfaces automatically generated through DJANGORESTFRAMEWORK.

### Heartbeat

- ###### GET

  ##### Returns the last hearbeat info inserted into database (sorted by date, single object)

  ````json
  {
    "pk": 2, 
    "fields": 
    {
      "beats": 60, 
      "date": "2017-09-22", 
      "time": "15:01:42.632"
    }
  }
  ````

- ###### POST - WIP

### Temperature

- ###### GET

  Returns the last temperature info inserted into database (sorted by date, single object)

  ```json
  {
    "pk": 212, 
    "fields": 
    {
      "beats": 94, 
      "date": "2017-09-22", 
      "time": "15:01:42.632"
    }
  }
  ```

- ###### POST - WIP

### Breathing

* ###### GET

  Returns the last breathing info inserted into database (sorted by date, single object)

  ```json
  {
    "pk": 122, 
    "fields": 
    {
      "temperature": 32, 
      "date": "2017-09-22", 
      "time": "15:01:42.632"
    }
  }
  ```

* ###### POST - WIP

### Movement

* ###### GET

  Returns the last movement info inserted into database (sorted by date, single object)

  ```json
  {
    "pk": 2, 
    "fields": 
    {
      "movement": "resting", 
      "date": "2017-09-22",
      "time": "15:01:42.632"
    }
  }
  ```

* ###### POST - WIP

## Sensor to API comunication

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



### Temperature

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

### Breathing

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

### Movement 

Initially the sensor reading will be through TXT files that will be sent by the MSP to the Rasp.

Expected JSON that comes from breathing sensor:

```json
[
    {
      "type":1,
      "timestamp":1234567898
    },
    {
      "type":2,
      "timestamp":1234567898
    },
    {
      "type":3,
      "timestamp":1234567898
    }
]
```

- temperature - Boolean value
- timestamp - Unix timestamp

The APi will parse the file into the local database and forward it to the clients throug a REST API

### Sensor to API Comunication - WIP

----

## Additional Configuration

### Enabling ````motioncontrol.py```` to be executed as sudo without prompting password

* Type ````sudo visudo```` at the terminal to open the sudo permissions (````sudoers````) file
* Around line 25, you'll see this line: ````%sudo   ALL=(ALL:ALL) ALL````
* **Below that line**, insert the following line, where ````username```` is your username:
* ````username  ALL=(ALL) NOPASSWD: /path/to/BabyOnBoard-API/babyonboard/api/scripts/motioncontrol.py````
* Exit the editor (Ctrl+X if nano)

### Starting the Baby on Board application at startup

Add the ````babyonboard.sh```` file to the crontab list:

* Type in terminal:
* ````$crontab -e````
* Then add the following line in it:
* ````@reboot /path/to/BabyOnBoard-API/babyonboard.sh virtualenv portnumber````

````virtualenv```` is the path to your virtualenv /bin/activate

````portnumber```` is the port that you want the application to be run
