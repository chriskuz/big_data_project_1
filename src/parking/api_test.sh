APP_TOKEN="tzksBXvIq9l9Ub985hzK3D5HP"
#API_URL="https://data.cityofnewyork.us/resource/pvqr-7yc4.csv?limit=0&$$app_token=${APP_TOKEN}"

curl -v -H "X-App-Token: $APP_TOKEN" "https://data.cityofnewyork.us/resource/pvqr-7yc4.csv?limit=50000" -o data.csv
