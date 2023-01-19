# To run this open new bash from the terminal below
# Then type sh curl_fastapi.sh   --- To see the results

curl -X 'POST' \
  'http://127.0.0.1:8000/files/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@test_data.csv;type=text/csv'
