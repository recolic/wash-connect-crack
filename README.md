# How to use this crack on vps

> Make sure there is not existing HTTPS server running on your machine.

1. Run `python -m http.server`. Use your android phone to download `crt` and `apk` from vps. Install the crt and apk.
2. Run `httpd-standalone-ssl.py` in background.
3. Modify DNS record on your phone. The following hostname should points to your vps.

```
getwashconnect.com
us-central1-washmobilepay.cloudfunctions.net
o424104.ingest.sentry.io
```

4. (maybe u need to update the location code?)
5. clear storage for wash connect app, **enter laundry room before open the app**, login with random password, start the washing machine
6. when the washing machine is started, close the app and clear storage.

## docker image

Read dockerfile, start the docker container on your vps.

On your phone, access `YOUR_SERVER_IP:8000`, read `_a_help.html` to setup dns, download crt & apk, and complete the setup.

go with step 5.

## WARNING

You might have to update the location code, to make it working for your laundry room.

Refer to `httpd*.py` to learn how to update them.

