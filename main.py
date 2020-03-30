
#Data structure for testing outside zapier and debugging:

input_data = {"first_name": "FirstName",
              "last_name": "LastName",
              "company_id": "00000000", # Company ID that they should be associated with
              "email_address": "example@contoso.com",
              "phone_number": "0000000000"}

#Copy below this to Zapier:

# Zapier contact import script
# used in conjunction with a second zap that brings across the company and main contact
# Copyright 2020 Dorks Delivered

import requests

# Customize this:
domain = "subdomain" # Replace with your syncromsp subdomain (https://mymsp.syncromsp.com.au) would enter mymsp
api_key = "syncro_api_key_here" #Replace with your API key from syncro

# Don't change:
url = "https://" + domain + ".syncromsp.com/api/v1/contacts"
fullname = input_data['first_name'] + " " + input_data['last_name']
phone_number = input_data.get("phone_number")

payload = {'customer_id': input_data['company_id'],
           'name': fullname,
           'email': input_data['email_address']}

if(phone_number != None):
    payload['phone_number'] = phone_number

params = {'api_key': api_key}

#print("URL: " + url + "\n")
#print("Request payload: \n")
#print(payload)
#print("Requesting...")

r = requests.post(url, json=payload, params={'api_key': api_key})

#print("Response: \n" + r.text + "\n")

if(r.status_code == 200):
    status = "pass"
else:
    status = "fail"

