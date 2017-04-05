Cities = {
    "Katowice" : [["Krakow" , 81.18], ["Lodz" , 261.0], ["Olsztyn" , 482.6], ["Poznan" , 375.9], ["Torun" , 365.5], ["Warszawa" , 289.5], ["Wroclaw" , 194.3]],
    "Krakow" : [["Katowice" , 81.18], ["Lodz" , 238.4], ["Olsztyn" , 503.7], ["Poznan" , 430.2], ["Torun" , 405.7], ["Warszawa" , 310.6], ["Wroclaw" , 269.3]],
    "Lodz" : [["Katowice" , 261.0], ["Krakow" , 238.4], ["Olsztyn" , 284.8], ["Poznan" , 204.7], ["Torun" , 174.4], ["Warszawa" , 130.0], ["Wroclaw" , 222.3]],
    "Olsztyn" : [["Katowice" , 482.6], ["Krakow" , 503.7], ["Lodz" , 284.8], ["Poznan" , 339.1], ["Torun" , 172.7], ["Warszawa" , 214.8], ["Wroclaw" , 486.3]],
    "Poznan" : [["Katowice" , 375.9], ["Krakow" , 430.2], ["Lodz" , 204.7], ["Olsztyn" , 237.8], ["Torun" , 161.3], ["Warszawa" , 310.4], ["Wroclaw" , 173.3]],
    "Torun" : [["Katowice" , 365.5], ["Krakow" , 405.7], ["Lodz" , 174.4], ["Olsztyn" , 172.7], ["Poznan" , 161.3], ["Warszawa" , 210.3], ["Wroclaw" , 289.0]],
    "Warszawa" : [["Katowice" , 289.5], ["Krakow" , 269.3], ["Lodz" , 130.0], ["Olsztyn" , 214.8], ["Poznan" , 310.4], ["Torun" , 210.3], ["Wroclaw" , 351.8]],
    "Wroclaw" : [["Katowice" , 194.3], ["Krakow" , 310.6], ["Lodz" , 222.3], ["Olsztyn" , 486.3], ["Poznan" , 173.3], ["Torun" , 289.0], ["Warszawa" , 351.8]]
}

print("Program which allow us to find a shortest path between eight voivodeship cities\n")
print("Cities: Katowice, Krakow, Lodz, Olsztyn, Poznan, Torun, Warszawa, Wroclaw\n")
start = input("Please enter a city: ")

distance = 0
list_of_cities = []
city_name = ""


if start in Cities:

    for number_of_repetitions in range(len(Cities)):

        counter = list(range(len(Cities[start])-1))

        for position in counter:
            if Cities[start][position][0] not in list_of_cities:
                city_name = Cities[start][position][0]
                distance = Cities[start][position][1]


        for city in Cities[start]:
            for item in city:
                if distance > city[1] and city[0] not in list_of_cities:
                   city_name = city[0]
                   distance = city[1]


        list_of_cities.append(start)
        start = city_name

print("\nThe shortest path is:\n\n", list_of_cities, "\n")