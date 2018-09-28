# -*- coding: UTF-8 -*-
import SimpleHttpClient


def main(vendor_id):
    req = SimpleHttpClient.SimpleHttpClient("9e2402ba-6703-11e7-a5fa-9801a79f70e5_cee20b86-cc4b-4c25-ab32-0d727ce08554")
    r = req.get("http://st.mwoperation.meiweishenghuo.com/2b/consumer/resetPayPassword", {"consumerId":vendor_id})
    print r.text


main("ea46608a-1d43-4012-a6c8-f42a31e44c53")