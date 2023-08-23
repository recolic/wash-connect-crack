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
5. clear storage for wash connect app, enter laundry room, open the app, login with random password, start the washing machine
6. when the washing machine is started, close the app and clear storage.

