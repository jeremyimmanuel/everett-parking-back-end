# Everett Parking App
## Coughacks 2020 Project

## Team
Jeremy Tandjung : https://github.com/jeremyimmanuel <br>
Jun Zhen : https://github.com/jpzhen <br>
Krish Kalai : https://github.com/krishkalai07

Also, check out our fourth member's repositories, who unfortunately couldn't come to the hackathon due to ilness.
Nathan Phan : https://github.com/irredentist

## Problem
Residents and visitors find it difficult to find on street parking within the downtown area of Everett. Past parking utilization studies have shown there may be enough parking stalls in the downtown, but public perception is parking availability is a challenge.

## Solution
A mobile app that lets users see parking lots in Everett's downtown area based on Everett's 2015 Central Business District Parking map (https://coughacks.io/datasets/CBD%20PARKING%202015-Map.pdf).

We have separates repoes for the Front-end side (a mobile application) and the Back-end side (a sql-backed python flask server). You can visit the repoes through the link below: <br> Front-end: https://github.com/jeremyimmanuel/everett-parking-front-end <br> Back-end: https://github.com/jeremyimmanuel/everett-parking-back-end

# Backend

## Flask server

We decided to use Flask to build a webserver because deploying it is very quick. Since it is written in Python, any changes are reflected almost instantationsly. Also Flask has a bridge to SQL, so database access is simple.

### Usage
- Get your local ipaddress with `ifconfig | grep inet`
- Change the ipaddress in the source code of the app in the front-end side in `polygonList.dart`
- python3 app.py

Once the server is up, you can make a call to:
- /data/parkinglot
  - returns a list of all parking spaces.
- /data/add
  - params: id, type, coords, num\_spots, restriction, time\_restriction
  - returns the id of the new object, or an error if adding failed.

More information is provided in code.

## SQL database

We use SQL database to manage our data. Data are collected manual by hand and put into a JSON file. This JSON file will be processed through a script and insert/update the database.

### Future work

- Add validation to add\_lot()
  - right now, only coords are validated
- Add call to delete all elements on the table
  - currently, if the table has an error (i.e. new field), the table needs to be deleted manually and rebuilt.
- Add call to get lots by id or range of ids
  - the only retrieval method sends the entire database, in which when scaled to include all the lots, it's not accessible
- Add call to get the number of elements
  - useful for the above future goal
- Add probability of space being available

# Technology Used
## Front-end
1. Flutter
2. Dart
3. Google Cloud console
4. Google Maps SDK

## Back-end
1. Python
2. Flask
3. SQL
4. JSON

# Conclusion
Overall we had an awesome time at the hackathon. Shout out to WSU Everett ACM and their sponsors for organizing this event!
