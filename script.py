import requests
from datetime import datetime,timedelta

age = 52
num_days = 2
district_id = 164 #navsari


flag = 'Y'




print("Starting search for covid vaccine")

actual = datetime.today() #for date today
list_format = [actual + timedelta(days=i) for i in range(num_days)]
actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]  # two days 

#we get the date


counter = 0

for given_date in actual_dates:

    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district_id,given_date)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} 
    
    #obttaining the json results

    result = requests.get(URL, headers=header)

    #print(result)  # --> 200

    if result.ok:
        response_json = result.json()

        # print(response_json) #--> json data

        #checking that json has the center dictionary or not

        if response_json["centers"]:

            if flag.lower() == 'y':
                # printing the json data:
                for center in response_json['centers']:
                    for session in center['sessions']:
                        if (session['min_age_limit'] <= age and (session['available_capacity_dose1'] > 0 or session['available_capacity_dose2'] > 0 )) :
                            print ("Available on: {}".format(given_date))
                            print("\t", center["name"])
                            print("\t", center["block_name"])
                            print("\t", center["pincode"])
                            print("\t Price: ", center["fee_type"])
                            print("\t Availablity : ", session["available_capacity_dose1"])
                            print("\t Availablity : ", session["available_capacity_dose2"])

                            if(session["vaccine"] != ''):
                                        print("\t Vaccine type: ", session["vaccine"])
                                    
                            print("\n")
                            counter = counter + 1

    else:
        print("NO RESPONSE! 404")

if counter == 0:
    print("No Vaccination slot available!")
else:
    print("Search Completed!")