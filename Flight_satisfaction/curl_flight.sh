curl -X 'POST' \
  'http://127.0.0.1:8000/files_flight/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@test_data.csv;type=text/csv'