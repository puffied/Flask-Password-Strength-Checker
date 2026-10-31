# PASSWORD STRENGTH CHECKER

A self-hosted password strength checker built with (Html-CSS-JS | Python) Flask.

## Features

  * Real-time strength checking as you type (no page reloads)
  * Python backend API with regex validation
  * Dynamic scoring system (Weak, Medium, Strong)
  * Visual feedback with color-changing UI
  * Auto-adds checks for length, numbers, uppercase, and special characters
  * Modern style UI with custom css styling and favicon
  * Live reload during development (`debug=True`)

## How It Works

  1. You type a password into the input field
  2. JavaScript immediately sends the password to the Python backend via AJAX (Fetch API)
  3. The Python script analyzes the password using Regex and calculates a score
  4. The browser receives the JSON response and updates the UI (color and text) in real-time

NOTE!!

This project uses Flask's standard folder structure. Make sure you have a folder named "static" for your css, js, and favicon files, and a folder named "templates" for your index.html file.

## Usage

terminal:

    pip install flask
    python pwStrengthCheck.py

Then open your browser at: http://localhost:5000/ and start typing!
