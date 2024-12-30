#define weather variable
weather1 = "sunny"
weather2 = "rainy"
weather3 = "cold"

# user input
current_weather = input("What's the weather like today? (sunny/rainy/cold): ")

# clothing recommendation
if current_weather == weather1:
    print("Wear a t-shirt and sunglasses.")
elif current_weather == weather2:
    print("Don't forget your umbrella and a raincoat.")
elif current_weather == weather3:
    print("Make sure to wear a warm coat and a scarf.")
elif current_weather != [weather1, weather2, weather3]:
    print("Sorry, I don't have recommendations for this weather.")