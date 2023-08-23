# Usage: sudo docker build -t recolic/washcrack .

# Usage: sudo docker run -p 443:443 -p 8000:8000 -d --name washcrack --restart=always recolic/washcrack

# Download cert at 8000 port, and then redirect dns to 443
from ubuntu:22.04

arg DEBIAN_FRONTEND=noninteractive
run apt update && apt install -y python3 curl

copy . /src
workdir /src

run curl https://ipinfo.io/ip > /tmp/myip
run echo "<h2>PLease set DNS:</h2>" >> /src/_a_help.html
run echo "<h2>getwashconnect.com $(cat /tmp/myip)</h2>" >> /src/_a_help.html
run echo "<h2>us-central1-washmobilepay.cloudfunctions.net $(cat /tmp/myip)</h2>" >> /src/_a_help.html
run echo "<h2>o424104.ingest.sentry.io $(cat /tmp/myip)</h2>" >> /src/_a_help.html
cmd bash -c "echo -e 'python3 -m http.server & \n python3 httpd-standalone-ssl.py' | bash"

