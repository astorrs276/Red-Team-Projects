# compile the ahk scripts more efficiently
# chars = [
#     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
#     'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
#     'z', 'x', 'c', 'v', 'b', 'n', 'm',
# ]
neighbors = {
    'q': ['w', 'a'],
    'w': ['q', 'a', 's', 'e'],
    'e': ['w', 's', 'd', 'r'],
    'r': ['e', 'd', 'f', 't'],
    't': ['r', 'f', 'g', 'y'],
    'y': ['t', 'g', 'h', 'u'],
    'u': ['y', 'h', 'j', 'i'],
    'i': ['u', 'j', 'k', 'o'],
    'o': ['i', 'k', 'l', 'p'],
    'p': ['o', 'l'],

    'a': ['q', 'w', 's', 'z'],
    's': ['a', 'w', 'e', 'd', 'x', 'z'],
    'd': ['s', 'e', 'r', 'f', 'c', 'x'],
    'f': ['d', 'r', 't', 'g', 'v', 'c'],
    'g': ['f', 't', 'y', 'h', 'b', 'v'],
    'h': ['g', 'y', 'u', 'j', 'n', 'b'],
    'j': ['h', 'u', 'i', 'k', 'n', 'm'],
    'k': ['j', 'i', 'o', 'l', 'm'],
    'l': ['k', 'o', 'p'],

    'z': ['a', 's', 'x'],
    'x': ['z', 's', 'd', 'c'],
    'c': ['x', 'd', 'f', 'v'],
    'v': ['c', 'f', 'g', 'b'],
    'b': ['v', 'g', 'h', 'n'],
    'n': ['b', 'h', 'j', 'm'],
    'm': ['n', 'j', 'k']
}

result = "#SingleInstance Force\n\nodds := 10\n\n"

for key in neighbors:
    adjacent = neighbors[key]
    result += "$" + key + '::{\n\trand := Random(1, odds)\n\tif (rand = 1) {\n\t\t'
    result += 'rand2 := Random(1, ' + str(len(adjacent)) + ")\n\t\t"
    first = True
    for i in range(len(adjacent)):
        if not first:
            result += ' else '
        else:
            first = False
        result += 'if (rand2 = ' + str(i + 1) + ') {\n\t\t\tSend "' + key + adjacent[i] + '"\n\t\t}'
    result += '\n\t} else {\n\t\tSend "' + key + '"\n\t}'
    result += '\n}\n'

    result += "$+" + key + '::{\n\trand := Random(1, odds)\n\tif (rand = 1) {\n\t\t'
    result += 'rand2 := Random(1, ' + str(len(adjacent)) + ")\n\t\t"
    first = True
    for i in range(len(adjacent)):
        if not first:
            result += ' else '
        else:
            first = False
        result += 'if (rand2 = ' + str(i + 1) + ') {\n\t\t\tSend "+' + key + "+" + adjacent[i] + '"\n\t\t}'
    result += '\n\t} else {\n\t\tSend "+' + key + '"\n\t}'
    result += '\n}\n'

with open("output.txt", "w") as file:
    file.write(result + "^Esc::ExitApp")
