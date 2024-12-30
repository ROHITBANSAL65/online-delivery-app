#!/bin/bash

# Load environment variables from dev.env (PowerShell compatible)
. config/dev.env

# Run the Flask application
flask run
