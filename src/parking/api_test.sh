APP_TOKEN="tzksBXvIq9l9Ub985hzK3D5HP"
API_URL="https://data.cityofnewyork.us/resource/pvqr-7yc4.csv?limit=100000&$$app_token=${APP_TOKEN}"

curl -v "$API_URL" -o data.csv