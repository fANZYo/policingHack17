Policing hackathon 2017

## The problem
The current system by which police officers communicate information to victims is painful and can lead to arguments going back and forth. This can often lead to degrading officer mental wellbeing.

## Our solution
A communication system to share updates on the investigation of a crime, combined with notifications, status and further information regarding the progress of the investigation and optional information explaining some of the reasoning behing the decisions made by the officer.

## Wireframe
![UI](https://i.imgur.com/hwGu6sg.jpg?1)

## Flowchart
![flowchart](https://i.imgur.com/C6IuE51.jpg?1)

JSON file:
```
{
  "crime-id": "000001",
  "name": "Kidnapping of doodle",
  "time": "2017-12-09 17:10",
  "description": "Criminally good hackathon project",
  "status": "Investigating",
  "timeline": [
    {
      "date": "2017-12-09 21:30",
      "title": "Looking for evidence",
      "description": "",
      "state": "pending"
    },
    {
      "date": "2017-12-09 24:15",
      "title": "Handed self administered interview forms",
      "description": "Used because of the large amount of witnesses",
      "state": "pending"
    },
    {
      "date": "2017-12-09 01:25",
      "title": "Found doodle",
      "description": "Found doodle in the cookie jar",
      "state": "done",
      "media": [
        {
          "name": "Picture of doodle in the cookie jar",
          "content-type": "image/jpeg",
          "url": "https://placekitten.com/200/300"
        }
      ]
    }
  ]
}
```

## Scripts
To install the project:
```
$ npm install
```
To run the dev server:
```
$ npm start
```
To run the server:
```
FLASK_APP=server.py flask run
```

## Dependencies
For the backend server, you need the following Python dependencies: `flask`, `flask_cors`, `pymongo`
MongoDB is required for the backend.
