#SingleInstance Force

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
    Send "w"
    konami("q")
}
$w::{
    Send "e"
    konami("w")
}
$e::{
    Send "r"
    konami("e")
}
$r::{
    Send "t"
    konami("r")
}
$t::{
    Send "y"
    konami("t")
}
$y::{
    Send "u"
    konami("y")
}
$u::{
    Send "i"
    konami("u")
}
$i::{
    Send "o"
    konami("i")
}
$o::{
    Send "p"
    konami("o")
}
$p::{
    Send "q"
    konami("p")
}
$a::{
    Send "s"
    konami("a")
}
$s::{
    Send "d"
    konami("s")
}
$d::{
    Send "f"
    konami("d")
}
$f::{
    Send "g"
    konami("f")
}
$g::{
    Send "h"
    konami("g")
}
$h::{
    Send "j"
    konami("h")
}
$j::{
    Send "k"
    konami("j")
}
$k::{
    Send "l"
    konami("k")
}
$l::{
    Send "a"
    konami("l")
}
$z::{
    Send "x"
    konami("z")
}
$x::{
    Send "c"
    konami("x")
}
$c::{
    Send "v"
    konami("c")
}
$v::{
    Send "b"
    konami("v")
}
$b::{
    Send "n"
    konami("b")
}
$n::{
    Send "m"
    konami("n")
}
$m::{
    Send "z"
    konami("m")
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
^Esc::ExitApp
