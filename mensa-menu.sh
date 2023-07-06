#!/bin/bash

OUTPUT_DIR="MENUs"

# Array of IDs
Mensas=("mensa-arcisstr" "mensa-garching" "mensa-leopoldstr" "mensa-lothstr")

week_number=$(date +%V)
current_year=$(date +%Y)

echo "Current year: $current_year"
echo "Current week number: $week_number"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Iterate over the array of IDs
for id in "${Mensas[@]}"; do
  API_URL="https://tum-dev.github.io/eat-api/$id/$current_year/$week_number.json"
  # Output file path for the current ID
  OUTPUT_FILE="$OUTPUT_DIR/response_$id.json"

  # Make the API call and store the response in the output file
  curl -X 'GET' "$API_URL" -H 'accept: application/json' -o "$OUTPUT_FILE"

  echo "API call for ID $id completed. Response saved in $OUTPUT_FILE"
done