
  curl -X 'POST' \
  'http://127.0.0.1:8000/files_iris/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@Test_data.csv;type=text/csv'