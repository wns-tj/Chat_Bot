

def Random(List1):
    import random

    return random.choice(List1)





def Weather1(location):

 
    # Have a pro subscription? Then use:
    # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
    

    # Search for current weather in London (Great Britain)
    try:
        list1 = []


        import pyowm
    
        owm = pyowm.OWM('f839a7a2ab29ab784f3348e5b96a467e')  # You MUST provide a valid API key
    
        observation = owm.weather_at_place(location)
        # status=Clouds>

        w = observation.get_weather()

        # Weather details
        w.get_wind()                  # {'speed': 4.6, 'deg': 330}
        w.get_humidity()
    
    
        from datetime import datetime
        date_tomorrow = datetime(2019, 10, 19, 12, 0)
        from pyowm import timeutils
        t = datetime(2013, 1, 27, 8, 12, 0)
    
        fc = owm.three_hours_forecast(location)
        f = fc.get_forecast()
        print("Giving 5 day forecast :")
        for weather in f:
           b = weather.get_reference_time('iso'),weather.get_temperature('celsius')
         
           #print(b)
           b=str(b)
           b = b.replace("'","")


           if '21:00:00+00' in b:
               list = ["(",")","{","}"]
              
               index = b.index("temp_kf")
               index1 = b.index("temp_max")
               a = b[index:index1]
               b = b.replace(a,"")
               b = b.replace("temp_max","Max Temperature",1)
               b = b.replace("temp_min","Minimum Temperature",1)
               b = b.replace("temp","Temperature",1)
               b = b.replace(b,b+",")
               b = b.replace(",","°C\n")
           
               for listentry in list:
                   b = b.replace(listentry,"")
               b = b.replace("21:00:00+00°C","" + "\n")

               list1.append(b)

             #  print("\n" + b)
        return(list1)
    
    except:
        print("Couldn't find that location")
        return ("Couldn't find that location")
  
                   # <Weather - reference time=2013-12-18 09:20,
    


        
    
    # 87
    
    
    
   # temperature = w.get_temperature('celsius')
 ###   
 #   temperature = str(temperature)
    
    
 #   index = temperature.index("temp_kf")
    
    
 #   temperature = temperature[0:index]
  ##  temperature = temperature.replace("temp_max","Max Temperature",1)
  #  temperature = temperature.replace("temp_min","Minimum Temperature",1)
   ## temperature = temperature.replace("temp","Temperature",1)
  #  temperature = temperature.replace(",","°C\n")
    
    
    
   # print(temperature)
   # 
def main(input):


    print("lol")
  



    import random
    #testinf some greetings with user input
    greet = ["hello", "hello", "hi", "hi", "hey","hey"]
    
    #testing some questions with user input
    moodqa = ["how are you","how are you doing"]
    response = ["okay","i'm fine"]

#for the weather which needs an api
    Weather = ["what is the weather in"]
    wea_response = []

#travel section dont really know since we need an api
    Travelqa = ["information about"]
    travelres = []

    userInput = input
    userInput = userInput.lower()
    word_list = userInput.split()

    try:
        for information1 in Travelqa:
            if information1 in userInput:
               word = word_list[-1]
               return(information(word))


        for greeting in greet:
           if greeting in userInput:
               return(Random(greet))
        for weather1 in Weather:
           if weather1 in userInput:
               word = word_list[-1]
               list1 = Weather1(word)
               return(list1)
           print(word)
        for questions in moodqa:
            if questions in userInput:
               return(Random(response))
    except:
        return("Please check your sentence!")
        


    

       
def information(Location):
    import wikipedia


    try:
        Summary = wikipedia.summary(Location)
        FirstSentence = Summary.index(".")
        Summary = Summary[0:FirstSentence]
        return Summary
    except:
        return("Couldn't find information about that")










# {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}