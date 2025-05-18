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
    Send "q{Left}"
    konami("q")
}
$+q::{
    Send "+q{Left}"
    konami("q")
}
$w::{
    Send "w{Left}"
    konami("w")
}
$+w::{
    Send "+w{Left}"
    konami("w")
}
$e::{
    Send "e{Left}"
    konami("e")
}
$+e::{
    Send "+e{Left}"
    konami("e")
}
$r::{
    Send "r{Left}"
    konami("r")
}
$+r::{
    Send "+r{Left}"
    konami("r")
}
$t::{
    Send "t{Left}"
    konami("t")
}
$+t::{
    Send "+t{Left}"
    konami("t")
}
$y::{
    Send "y{Left}"
    konami("y")
}
$+y::{
    Send "+y{Left}"
    konami("y")
}
$u::{
    Send "u{Left}"
    konami("u")
}
$+u::{
    Send "+u{Left}"
    konami("u")
}
$i::{
    Send "i{Left}"
    konami("i")
}
$+i::{
    Send "+i{Left}"
    konami("i")
}
$o::{
    Send "o{Left}"
    konami("o")
}
$+o::{
    Send "+o{Left}"
    konami("o")
}
$p::{
    Send "p{Left}"
    konami("p")
}
$+p::{
    Send "+p{Left}"
    konami("p")
}
$a::{
    Send "a{Left}"
    konami("a")
}
$+a::{
    Send "+a{Left}"
    konami("a")
}
$s::{
    Send "s{Left}"
    konami("s")
}
$+s::{
    Send "+s{Left}"
    konami("s")
}
$d::{
    Send "d{Left}"
    konami("d")
}
$+d::{
    Send "+d{Left}"
    konami("d")
}
$f::{
    Send "f{Left}"
    konami("f")
}
$+f::{
    Send "+f{Left}"
    konami("f")
}
$g::{
    Send "g{Left}"
    konami("g")
}
$+g::{
    Send "+g{Left}"
    konami("g")
}
$h::{
    Send "h{Left}"
    konami("h")
}
$+h::{
    Send "+h{Left}"
    konami("h")
}
$j::{
    Send "j{Left}"
    konami("j")
}
$+j::{
    Send "+j{Left}"
    konami("j")
}
$k::{
    Send "k{Left}"
    konami("k")
}
$+k::{
    Send "+k{Left}"
    konami("k")
}
$l::{
    Send "l{Left}"
    konami("l")
}
$+l::{
    Send "+l{Left}"
    konami("l")
}
$z::{
    Send "z{Left}"
    konami("z")
}
$+z::{
    Send "+z{Left}"
    konami("z")
}
$x::{
    Send "x{Left}"
    konami("x")
}
$+x::{
    Send "+x{Left}"
    konami("x")
}
$c::{
    Send "c{Left}"
    konami("c")
}
$+c::{
    Send "+c{Left}"
    konami("c")
}
$v::{
    Send "v{Left}"
    konami("v")
}
$+v::{
    Send "+v{Left}"
    konami("v")
}
$b::{
    Send "b{Left}"
    konami("b")
}
$+b::{
    Send "+b{Left}"
    konami("b")
}
$n::{
    Send "n{Left}"
    konami("n")
}
$+n::{
    Send "+n{Left}"
    konami("n")
}
$m::{
    Send "m{Left}"
    konami("m")
}
$+m::{
    Send "+m{Left}"
    konami("m")
}
$1::{
    Send "1{Left}"
    konami("1")
}
$+1::{
    Send "+1{Left}"
    konami("1")
}
$2::{
    Send "2{Left}"
    konami("2")
}
$+2::{
    Send "+2{Left}"
    konami("2")
}
$3::{
    Send "3{Left}"
    konami("3")
}
$+3::{
    Send "+3{Left}"
    konami("3")
}
$4::{
    Send "4{Left}"
    konami("4")
}
$+4::{
    Send "+4{Left}"
    konami("4")
}
$5::{
    Send "5{Left}"
    konami("5")
}
$+5::{
    Send "+5{Left}"
    konami("5")
}
$6::{
    Send "6{Left}"
    konami("6")
}
$+6::{
    Send "+6{Left}"
    konami("6")
}
$7::{
    Send "7{Left}"
    konami("7")
}
$+7::{
    Send "+7{Left}"
    konami("7")
}
$8::{
    Send "8{Left}"
    konami("8")
}
$+8::{
    Send "+8{Left}"
    konami("8")
}
$9::{
    Send "9{Left}"
    konami("9")
}
$+9::{
    Send "+9{Left}"
    konami("9")
}
$0::{
    Send "0{Left}"
    konami("0")
}
$+0::{
    Send "+0{Left}"
    konami("0")
}
$-::{
    Send "-{Left}"
    konami("-")
}
$+-::{
    Send "+-{Left}"
    konami("-")
}
$=::{
    Send "={Left}"
    konami("=")
}
$+=::{
    Send "+={Left}"
    konami("=")
}
$[::{
    Send "[{Left}"
    konami("[")
}
$+[::{
    Send "+[{Left}"
    konami("[")
}
$]::{
    Send "]{Left}"
    konami("]")
}
$+]::{
    Send "+]{Left}"
    konami("]")
}
$\::{
    Send "\{Left}"
    konami("\")
}
$+\::{
    Send "+\{Left}"
    konami("\")
}
$;::{
    Send ";{Left}"
    konami(";")
}
$+;::{
    Send "+;{Left}"
    konami(";")
}
$'::{
    Send "'{Left}"
    konami("'")
}
$+'::{
    Send "+'{Left}"
    konami("'")
}
$,::{
    Send ",{Left}"
    konami(",")
}
$+,::{
    Send "+,{Left}"
    konami(",")
}
$.::{
    Send ".{Left}"
    konami(".")
}
$+.::{
    Send "+.{Left}"
    konami(".")
}
$/::{
    Send "/{Left}"
    konami("/")
}
$+/::{
    Send "+/{Left}"
    konami("/")
}
$Space::{
    Send "{Space}{Left}"
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
