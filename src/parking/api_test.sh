APP_TOKEN="tzksBXvIq9l9Ub985hzK3D5HP"
curl -v -H "X-App-Token: $APP_TOKEN" "https://data.cityofnewyork.us/resource/pvqr-7yc4.csv?\$limit=100" -o data.csv
