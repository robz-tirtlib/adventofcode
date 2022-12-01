with open("input.txt", 'r') as f:
    mas = list(map(lambda x: sum(map(int, x.split())), f.read().split('\n\n')))
    print(sum(sorted(mas)[-3:]))
