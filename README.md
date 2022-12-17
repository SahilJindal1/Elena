# Elena
Elevation-based navigation system (EleNA) 

EleNA is a navigation system that provides a path based on the user’s preference of minimizing or maximizing elevation gain along with limiting the extra total distance the user wants to travel.


## Requirements

python3 

node == v14.16.0 

npm == 6.14.11 


## How to Run

### To run the backend server

Install all the dependencies using python

```
pip install -r requirements.txt
```

```
python backend/app.py
```

### To run the User Interface

Switch to the frontend directory

Install all dependencies
```
npm i
```

Start the npm server

```
npm start
```

![User Interface of Elena](/images/UI.png)


Currently our application shows routes only in the region of Amherst, MA but can be extended to other locations.

Users can enter the start and end destination of their route.

User can choose between minimum or maximum elevation gain.

User can set the maximum extra distance they want to travel.

This application displays the route with required elevation gain on map for the users.

Providing details of their final route like distance of complete route and elevation gain.
