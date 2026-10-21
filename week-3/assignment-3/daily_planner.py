day = input("What day of the week is it? ").lower()
time = input("What time of day is it? ").lower()

if (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday") and time == "morning":
    print("Have a good day at work!")
elif (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday") and time == "afternoon":
    print("Off work, it's a great time to study!")
elif (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday") and time == "evening":
    print("It's time to get ready for bed!")
elif (day == "saturday" or day == "sunday") and time == "morning":
    print("Let's start studying!")
elif day == "saturday" or day == "sunday":
    print("Find something fun to do!")

if day != "monday" and day != "tuesday" and day != "wednesday" and day != "thursday" and day != "friday" and day != "saturday" and day != "sunday":
    print("Sorry, I don't recognize that day. Try picking another day.")
if time != "morning" and time != "afternoon" and time != "evening":
     print("Sorry, I don't recognize that time of day. Try picking morning, afternoon, or evening!")