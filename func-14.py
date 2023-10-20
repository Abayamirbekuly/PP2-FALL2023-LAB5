from func_2 import farenheit_to_celsium
print("-Hello, I am from Kazakhstan! What's the weather today in Los Angeles?")

farenheits_1 = float(input())

print(f"-{farenheits_1} farenheits")
print("-Sorry, I don't understand Farenheits. Can you tell me in Celsiums?")

celsiums = int(farenheit_to_celsium(farenheits_1))

print(f"-{celsiums} degree Celsium")

if celsiums >= 25:
    print("Pretty Hot!")
elif celsiums <= 0:
    print("Pretty Cold!")
elif celsiums > 0 and celsiums < 25:
    print("Nice Weather!")