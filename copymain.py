import pathlib
from datetime import datetime
from logging import raiseExceptions

from fastapi import FastAPI,HTTPException,status
from contextlib import asynccontextmanager

import models
from models import Track
import json
from typing import List

# Make 'data' accessible globally
data = []

@asynccontextmanager
async def lifespan(app: FastAPI):
    global data  # Ensure the global 'data' list is updated
    datapath = pathlib.Path() / 'data' / 'tracks.json'
    print(datapath)
    try:
        # Load data during startup
        with open(datapath, 'r') as f:
            tracks = json.load(f)
            for track in tracks:
                data.append(Track(**track).dict())  # Populate 'data' list
        print("Loaded data:")  # Print data for debugging
    except FileNotFoundError:
        print(f"Error: File not found at {datapath}")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {datapath}")

    yield  # Pass control to the application

    # Shutdown logic (if any)
    print("Shutting down application")


app = FastAPI(lifespan=lifespan)

@app.get("/tracks/")
async def get_tracks():
    return data

@app.get("/tracks/{track_id}")
async def get_track(track_id:int):
    for track in data:
        if track['id'] == track_id:
            print(track)
            return track

@app.get("/tracks/duration/{duration}")
async def get_by_duration(duration:int):
    for track in data:
        if track['duration'] > duration:
            return track

@app.post("/tracks/")
async def add_tracks(request:models.Track):
    global data  # Ensure global access to 'data'
    datapath = pathlib.Path() / 'data' / 'tracks.json'

    # Load the existing records from the file to ensure consistency
    try:
        if datapath.exists() and datapath.stat().st_size > 0:
            with open(datapath, 'r') as f:
                existing_data = json.load(f)
        else:
            existing_data = []
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to read existing data from JSON file.")

    # Convert the Track object to a dictionary
    new_track = request.dict()
    #converted to string
    new_track['id'] = str(new_track['id'])

    for track in data:
        print(new_track['id'], "newid")
        if str(track['id'] )== str(new_track['id']):
            return f"{track['id']} already exists"
    new_track["last_play"] = datetime.now().isoformat()
    print("new_track",new_track)
    # Append the new track to the existing data
    existing_data.append(new_track)

    # Update the in-memory 'data' list
    data.clear()
    data.extend(existing_data)
    try:
        # Save the updated data back to the JSON file
        with open(datapath, 'w') as f:
            json.dump(existing_data, f, indent=4)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save data: {str(e)}")

    return new_track

@app.put("/tracks/{track_id}")
async def update_track(request:models.Track,track_id:int):
    global data  # Ensure global access to 'data'
    datapath = pathlib.Path() / 'data' / 'tracks.json'
    #Load the existing records
    try:
        if datapath.exists() and datapath.stat().st_size > 0:
            with open(datapath,'r') as f:
                existing_data = json.load(f)
        else:
            existing_data = []
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to read existing data from JSON file.")
        # Check for duplicate IDs in the loaded data


    for track in data:
        if track['id'] == str(track_id):
            # Update the track details
            track["title"] = request.title
            track["duration"] = request.duration
            track["artist"] = request.artist
            track["last_play"] = datetime.now().isoformat()
            print("where",track)



    #Update the in-memory 'data' list
        data.clear()
        data.extend(existing_data)
        try:
            with open(datapath,'w') as f:
                json.dump(existing_data,f,indent=4)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to save data: {str(e)}")
            return track