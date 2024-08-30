#!/bin/bash

# Start the Flask API in the background
echo "Starting Flask API..."
cd ./API/  # Change this to your API directory
nohup python index.py &  # Run the API in the background

# Wait for a few seconds to ensure the API starts
sleep 5

# Execute the main.py script
echo "Running main.py..."
cd ../
python main.py

sleep 5

# #start UI
# echo "Starting UI ..."
# cd ./pdcp_logger/
# npm start &

