def average_temperature(name):
    with open(name, 'r', encoding='utf8') as file:
        lines = file.readlines()
        count = 0
        result = 0
        for line in lines:
            line = line.replace(' ', '').replace('°C', '').split(':')
            count += 1
            result += int(line[1])

    return round(result/count, 2)

print(average_temperature('weather.txt'))

