from flask import Flask
import json

# Load database configuration from JSON
with open('config/db_config.json', 'r') as f:
    db_config = json.load(f)

# Print database configuration (for debugging purposes)
print(f"Database host: {db_config['host']}")

app = Flask(__name__)

# Set up database configuration in Flask
app.config['DATABASE_HOST'] = db_config['host']
app.config['DATABASE_PORT'] = db_config['port']
app.config['DATABASE_USER'] = db_config['user']
app.config['DATABASE_PASSWORD'] = db_config['password']
app.config['DATABASE_NAME'] = db_config['database']

@app.route('/')
def home():
    return f"App running with database at {app.config['DATABASE_HOST']}"

if __name__ == "__main__":
    app.run(debug=True)
