import requests, random, os.path
from decouple import config


def calculate_bmi(weight, height):
    bmi=round(weight/(height*height)*10000,2)
    return bmi

def check_bmi(bmi, api_key):
    url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/weight-category"
    querystring = {"bmi":bmi}

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "body-mass-index-bmi-calculator.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = response.json()
    category=res["weightCategory"]
    return category

def make_training_plan(category, max_time):
    if category == "Obese":
        time_for_exercise = random.randint(max_time*4/5,max_time)
    elif category == "Overweight":
        time_for_exercise = random.randint(max_time*3/4,max_time)
    else:
        time_for_exercise = random.randint(max_time/2,max_time)
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    list_of_exercises=["running", "swimming", "tennis", "bicycling", "jogging", "football", "badminton", "basketball", "walking"]

    #write to file

    if os.path.isfile("your_training.txt"):
        training = open("your_training.txt", "w")
    else:
        training = open("your_training.txt", "a")

    training.write("Each exercise should last at least {} minutes\n".format(time_for_exercise))

    for day in days:
        training.write("{}: {}\n".format(day, random.choice(list_of_exercises)))

    training.close()



def main():
    mass = int(input("Your weight: "))
    height = int(input("Your height (in centimeters!): "))
    max_time = int(input("How much time do you have for exercising (in minutes!): "))

    if max_time<30:
        max_time = 30

    API_KEY = config('KEY')
    bmi=calculate_bmi(mass,height)
    category=check_bmi(bmi,API_KEY)

    print("Your bmi : ", bmi)
    print("Category : ", category)

    make_training_plan(category, max_time)
    print("Your training plan is ready")



if __name__ == "__main__":
    main()