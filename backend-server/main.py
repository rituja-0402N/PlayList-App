import pathlib
from datetime import datetime
from fastapi import FastAPI,HTTPException,status
from contextlib import asynccontextmanager
import models
from models import Track
import json
from typing import List
from fastapi.middleware.cors import CORSMiddleware
# Make 'data' accessible globally
data = []


# Utility function to load existing data
def load_data(filepath: pathlib.Path) -> List[dict]:
    """Load and return existing data from the JSON file."""
    try:
        if filepath.exists() and filepath.stat().st_size > 0:
            with open(filepath, 'r') as f:
                existing_data = json.load(f)
                return existing_data
        else:
                existing_data = []
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to decode JSON file.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

# Utility function to save data to the file
def save_data(filepath: pathlib.Path, data: List[dict]):
    """Save the provided data list to the JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save data: {str(e)}")

@asynccontextmanager
async def lifespan(app: FastAPI):
    global data  # Ensure the global 'data' list is updated
    datapath = pathlib.Path() / 'data' / 'tracks.json'

    # Load data at startup
    data.extend(load_data(datapath))

    # Initialize empty JSON file if missing
    if not datapath.exists() or not datapath.stat().st_size:
        save_data(datapath, [])

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
        if str(track['id']) == str(track_id):
            print(track)
            return track
    raise HTTPException(status_code=404, detail="Track not found")

@app.post("/tracks/")
async def add_tracks(request:models.Track):
    global data  # Ensure global access to 'data'
    datapath = pathlib.Path() / 'data' / 'tracks.json'

    # Convert the Track object to a dictionary
    new_track = request.dict()
    #converted to string
    new_track['id'] = str(new_track['id'])

    for track in data:
        print(new_track['id'], "newid",track['id'])
        if str(track['id'])== str(new_track['id']):
            return f"{track['id']} already exists"
    new_track["last_play"] = datetime.now().isoformat()
    print("new_track",new_track)

    data.append(new_track)
    # Save updated data to JSON
    save_data(datapath, data)

    return new_track

@app.put("/tracks/{track_id}")
async def update_track(request:models.Track,track_id:int):
    global data  # Ensure global access to 'data'
    datapath = pathlib.Path() / 'data' / 'tracks.json'

    for track in data:
        if track['id'] == str(track_id):
            # Update the track details
            track["title"] = request.title
            track["duration"] = request.duration
            track["artist"] = request.artist
            track["last_play"] = datetime.now().isoformat()
            print("where",track)
            # Save updated data to JSON
            save_data(datapath, data)
            return track



origins = [
    "http://localhost:3000"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow credentials like cookies
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

