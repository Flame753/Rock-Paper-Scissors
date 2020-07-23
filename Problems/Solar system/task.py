# create the planets.txt
solar_system = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
file = open('planets.txt', 'w', encoding='utf-8')
for planet in solar_system:
    file.write(planet + '\n')
file.close()
