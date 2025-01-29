# Playlist App 🎵

The **Playlist App** is a FastAPI-based backend application designed to manage and display playlists. It provides functionality to retrieve playlists, fetch individual tracks, and integrate with third-party frontend applications via API endpoints.

---

## 🚀 Features

- **Retrieve All Playlists**: Fetch a list of all playlists with metadata.
- **Track Details**: Fetch detailed information about specific tracks.
- **Pagination**: Support for paginated data display in frontend integrations.
- **CORS Support**: Seamlessly integrate with frontend applications hosted on different domains.
- **JSON-Based Storage**: Reads and validates playlist data from a `jobs.json` file.

---

## 📋 Prerequisites

Ensure you have the following installed:
- Python 3.8 or later
- `pip` (Python package manager)

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rituja-0402N/PlayList-App.git
   cd PlayList-App

2. python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Ensure jobs.json is present: Place a jobs.json file with playlist data in the project root directory. Example structure:
[
  {
    "id": 1,
    "title": "Song Title",
    "artist": "Artist Name",
    "duration": 240,
    "last_play": "2023-01-01T00:00:00Z"
  }
]
▶️ Usage

Run the FastAPI server:
uvicorn main:app --reload
Access API documentation: Open your browser and go to:
Interactive API docs: http://127.0.0.1:8000/docs
ReDoc documentation: http://127.0.0.1:8000/redoc
Available Endpoints:
GET /jobs: Fetch all playlists.
GET /jobs/{job_id}: Fetch a specific playlist by ID.
🌟 Features in Detail

API Endpoints
Endpoint	Method	Description
/jobs	GET	Retrieves all playlists from the jobs.json file.
/jobs/{job_id}	GET	Fetches details of a specific track by ID.
📂 Project Structure

PlayList-App/
│
├── main.py                 # Main FastAPI application
├── schema.py               # Data models and validation using Pydantic
├── jobs.json               # Sample JSON file with playlist data
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
⚙️ Environment Variables (Optional)

To configure custom settings, create a .env file in the root directory. Example:

PORT=8000
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000
🤝 Contributing

Fork the repository.
Create your feature branch:
git checkout -b feature/my-feature
Commit your changes:
git commit -m "Add some feature"
Push to the branch:
git push origin feature/my-feature
Open a pull request.
📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgments

FastAPI Documentation
Pydantic Documentation
Uvicorn
📞 Contact

For questions or support, please contact:

Author: Rituja
Email: rituja@example.com
GitHub: rituja-0402N



### Key Sections Explained:
1. **Features**: Highlights core functionality.
2. **Installation**: Detailed steps to set up the project.
3. **Usage**: Provides API endpoints and instructions to run the app.
4. **Project Structure**: Outlines the directory layout.
5. **Contributing**: Guidelines for adding to the project.
6. **License**: Placeholder for the licensing terms.


![Screenshot 2025-01-28 at 3 55 24 PM](https://github.com/user-attachments/assets/1f978426-fd9e-4634-b45c-3c6629fefa66)
![Screenshot 2025-01-28 at 3 55 14 PM](https://github.com/user-attachments/assets/f355035a-34a7-4be3-aa48-08863197af63)
![Screenshot 2025-01-28 at 3 54 51 PM](https://github.com/user-attachments/assets/ceacbee1-6db1-49e9-991f-450c007ae824)
