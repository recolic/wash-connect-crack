openssl req -x509 -newkey rsa:4096 -sha256 -days 3650 \
  -nodes -keyout example.com.key -out example.com.crt -subj "/CN=getwashconnect.com" \
  -addext "subjectAltName=DNS:o424104.ingest.sentry.io,DNS:us-central1-washmobilepay.cloudfunctions.net"

#      getwashconnect.com
#      o424104.ingest.sentry.io
#      us-central1-washmobilepay.cloudfunctions.net



