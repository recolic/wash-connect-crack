# wash crack

Free wash connect. Hardcoded param.

## Recommended Usage Steps

> location code is hardcoded, but it works for any laundry room in my test.

1. Deploy cracked https server with docker: `sudo docker run -p 443:443 -p 8000:8000 -d --name washcrack --restart=always recolic/washcrack`
2. On your phone, access `YOUR_SERVER_IP:8000`, read `_a_help.html` to setup dns, download crt & apk, and install them.
3. Modify DNS record on your phone. [(HOW-TO)](https://recolic.net/blog/post/android-modify-dns-record-hosts-without-root-reliable-way) The following hostname should points to your vps.

```
getwashconnect.com
us-central1-washmobilepay.cloudfunctions.net
o424104.ingest.sentry.io
```

4. **EVERY TIME** Before starting app, please make sure **DNS is modified AND you are in laundry room**. Otherwise, you must clear storage before trying to restart app.
5. Start app. Login with random password, start the washing machine.

## If you want to deploy cracked server manually

1. Run `python -m http.server`. Use your android phone to download `crt` and `apk` from vps. Install the crt and apk.
2. Run `httpd-standalone-ssl.py` in background. 

or, instead, 

## If anything is going wrong

Test if your DNS modification works with your browser or curl. HostsGo is known to be unreliable, do more attempts.

## FAQ / Known issue

- After selecting washing machine, the price button shows "loading" animation, not allowing me to pay.

This is a known issue. It happens on some machine, and you should just try another machine.

It will fix itself after a few days. And I observed, other normal users also avoid this machine even if laundry room is super busy. I believe that machine is somehow broken, and they will send staff to fix it.

- My HTTP server doesn't respond

This is a known issue. If you open such naive HTTPS server to Internet, evil guy will send bad request to break it. 

If you run `docker logs [ContainerName]`, you will see socket-related error msg. My workaround is running such script on server:

```bash
# replace washcrack with your container name
while true; do
	timeout 10s curl https://localhost -k | grep invalid.get || docker restart washcrack
	sleep 300
done
```