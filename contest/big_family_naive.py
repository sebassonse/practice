# input prosessing

def get_database():
    c = int(input())
    cities = dict()
    for i in range(c):
        name, num = input().split()
        cities[name] = []
        for n in range(int(num)):
            cities[name].append(list(input().split()))
    return cities


def get_requests():
    # structure of requests: [[num_of_cities_1, city1, ..., citynum], [num_of_cities_2, city1, ..., citynum2] ...]
    r = int(input())
    requests = []
    for i in range(r):
        requests.append(input().split())
    return requests


def get_citiesBoolAvg(cities):
    # structure of homes: {city1_name:[[room1_inf, room1_name], [room2_inf, room2_name]], city2_name:[...],...}
    # structure of homesBoolAvg: {city1_name:[True, False, ..., False], ...}, len(homesBoolAvg[city1_name]) = 24
    citiesBoolAvg = dict()
    for city in cities:
        citiesBoolAvg[city] = [False for i in range(24)]
        for i in range(24):
            for room in cities[city]:
                if room[0][i] == '.':
                    citiesBoolAvg[city][i] = True
                    break
    return citiesBoolAvg


def request_prosessing(citiesBoolAvg, requests):
    # structure of requests: [[num_of_cities_1, city1, ..., citynum], [num_of_cities_2, city1, ..., citynu2] ...]
    answer = []
    for request in requests:
        need = request[0]
        no = True
        for hour in range(24):
            res = 0
            for city in request[1:]:
                if citiesBoolAvg[city][hour] is True:
                    res += 1
                if int(res) == int(need):
                    answer.append(['YES', hour])
                    no = False
                if no is False:
                    break
        if no is True:
            answer.append(['NO'])
    return answer


def do_output(cities, answer, requests):
    for reqnum in range(len(requests)):
        if answer[reqnum][0] == 'NO':
            print('No')
        else:
            ans = 'Yes '
            for city in requests[reqnum][1:]:
                for room in cities[city]:
                    if room[0][answer[reqnum][1]] == '.':
                        ans += str(room[1] + ' ')
                        break
            print(ans)


# BODY

cities = get_database()
requests = get_requests()

citiesBoolAvg = get_citiesBoolAvg(cities)
answer = request_prosessing(citiesBoolAvg, requests)

do_output(cities, answer, requests)
