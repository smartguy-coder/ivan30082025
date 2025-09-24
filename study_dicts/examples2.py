from pprint import pprint

car = {
    "price": 2_500_000,
    'weight_kg': 1564.5,
    'options': ['music', "leather seats"],
    'plate_number': None,
    'engine': {
        'hp': 125,
        'pistols': 6,
        'fuel': "gasoline"
    }
}

pprint(car, indent=4, width=60)

car_engine_hp = car["engine"]["hp"]
# print(car_engine_hp)

# parameters = []
# for key in car:
#     print(key)
#     parameters.append(key)
#
# print(parameters)


# for p in car.keys():
# for p in car.values():
#     print(p)


for key, value in car.items():
    print(key, "-------", value)