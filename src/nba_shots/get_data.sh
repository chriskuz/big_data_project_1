#!/bin/sh

# === Config ===
PROJECT_DIR="/mapreduce-test/mapreduce-project1/big_data_computing_project1"
DATA_DIR="$PROJECT_DIR/data"
ZIP_NAME="nba-shot-logs.zip"
KAGGLE_USER=$(jq -r .username ~/.kaggle/kaggle.json)
KAGGLE_KEY=$(jq -r .key ~/.kaggle/kaggle.json)

# === Prep directory ===
echo "Creating data dictionary if not already present.."
mkdir -p "$DATA_DIR"
cd "$DATA_DIR" || { echo: "Failed data directory access"; exit 1;}

# === Download ZIP using curl and API token ===
echo "Downloading NBA shot logs ZIP from Kaggle"
curl -L -u "${KAGGLE_USER}:${KAGGLE_KEY}" \
  -o "$ZIP_NAME" \
  "https://www.kaggle.com/api/v1/datasets/download/dansbecker/nba-shot-logs"

# === Extract & clean up ===
echo "Extracting contents"
unzip -o "$ZIP_NAME" #== might need brackets (also above)
rm -f "$ZIP_NAME" #== might need brackets

echo "Done"

