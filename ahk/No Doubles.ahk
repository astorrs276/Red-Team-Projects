#SingleInstance Force

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

$q::{
    if (previous != "q") {
        Send "q"
    }
    global previous := "q"
    konami("q")
}
$w::{
    if (previous != "w") {
        Send "w"
    }
    global previous := "w"
    konami("w")
}
$e::{
    if (previous != "e") {
        Send "e"
    }
    global previous := "e"
    konami("e")
}
$r::{
    if (previous != "r") {
        Send "r"
    }
    global previous := "r"
    konami("r")
}
$t::{
    if (previous != "t") {
        Send "t"
    }
    global previous := "t"
    konami("t")
}
$y::{
    if (previous != "y") {
        Send "y"
    }
    global previous := "y"
    konami("y")
}
$u::{
    if (previous != "u") {
        Send "u"
    }
    global previous := "u"
    konami("u")
}
$i::{
    if (previous != "i") {
        Send "i"
    }
    global previous := "i"
    konami("i")
}
$o::{
    if (previous != "o") {
        Send "o"
    }
    global previous := "o"
    konami("o")
}
$p::{
    if (previous != "p") {
        Send "p"
    }
    global previous := "p"
    konami("p")
}
$a::{
    if (previous != "a") {
        Send "a"
    }
    global previous := "a"
    konami("a")
}
$s::{
    if (previous != "s") {
        Send "s"
    }
    global previous := "s"
    konami("s")
}
$d::{
    if (previous != "d") {
        Send "d"
    }
    global previous := "d"
    konami("d")
}
$f::{
    if (previous != "f") {
        Send "f"
    }
    global previous := "f"
    konami("f")
}
$g::{
    if (previous != "g") {
        Send "g"
    }
    global previous := "g"
    konami("g")
}
$h::{
    if (previous != "h") {
        Send "h"
    }
    global previous := "h"
    konami("h")
}
$j::{
    if (previous != "j") {
        Send "j"
    }
    global previous := "j"
    konami("j")
}
$k::{
    if (previous != "k") {
        Send "k"
    }
    global previous := "k"
    konami("k")
}
$l::{
    if (previous != "l") {
        Send "l"
    }
    global previous := "l"
    konami("l")
}
$z::{
    if (previous != "z") {
        Send "z"
    }
    global previous := "z"
    konami("z")
}
$x::{
    if (previous != "x") {
        Send "x"
    }
    global previous := "x"
    konami("x")
}
$c::{
    if (previous != "c") {
        Send "c"
    }
    global previous := "c"
    konami("c")
}
$v::{
    if (previous != "v") {
        Send "v"
    }
    global previous := "v"
    konami("v")
}
$b::{
    if (previous != "b") {
        Send "b"
    }
    global previous := "b"
    konami("b")
}
$n::{
    if (previous != "n") {
        Send "n"
    }
    global previous := "n"
    konami("n")
}
$m::{
    if (previous != "m") {
        Send "m"
    }
    global previous := "m"
    konami("m")
}
$Space::{
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
^Esc::ExitApp
