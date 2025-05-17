# Collaborative Journal

A real-time collaborative journal application where users can write and draw together.

## Features

- Create and edit journal entries
- Real-time updates across all connected clients
- Rich text formatting support
- Drawing canvas with color and brush size options
- Responsive design that works on desktop and mobile
- Auto-save functionality

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd MMOJournal
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

- Click "New Entry" to create a new journal entry
- Type in the editor to add text
- Click "Draw" to switch to drawing mode
- Use the color picker and brush size slider to customize your drawing
- Click "Save" to save your changes (auto-save also occurs every 30 seconds)
- Click on any entry in the sidebar to view or edit it

## Project Structure

- `app.py` - Main application file with Flask routes and Socket.IO events
- `templates/` - Contains HTML templates
  - `index.html` - Main application interface
- `static/` - Static files (CSS, JavaScript, images)
- `instance/` - Database file will be created here

## Technologies Used

- Backend: Python, Flask, Flask-SocketIO, SQLAlchemy
- Frontend: HTML5, CSS3, JavaScript, Canvas API
- Database: SQLite

## License

This project is open source and available under the [MIT License](LICENSE).
