APP_TOKEN="tzksBXvIq9l9Ub985hzK3D5HP"
API_URL="https://data.cityofnewyork.us/resource/pvqr-7yc4.csv?$limit=50000"

curl -v -H "X-App-Token: $APP_TOKEN" "$API_URL" -o data.csv
