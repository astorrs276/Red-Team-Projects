#SingleInstance Force

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

$q::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 2)
		if (rand2 = 1) {
			Send "qw"
		} else if (rand2 = 2) {
			Send "qa"
		}
	} else {
		Send "q"
	}
	konami("q")
}
$+q::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 2)
		if (rand2 = 1) {
			Send "+q+w"
		} else if (rand2 = 2) {
			Send "+q+a"
		}
	} else {
		Send "+q"
	}
	konami("q")
}
$w::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "wq"
		} else if (rand2 = 2) {
			Send "wa"
		} else if (rand2 = 3) {
			Send "ws"
		} else if (rand2 = 4) {
			Send "we"
		}
	} else {
		Send "w"
	}
	konami("w")
}
$+w::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+w+q"
		} else if (rand2 = 2) {
			Send "+w+a"
		} else if (rand2 = 3) {
			Send "+w+s"
		} else if (rand2 = 4) {
			Send "+w+e"
		}
	} else {
		Send "+w"
	}
	konami("w")
}
$e::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "ew"
		} else if (rand2 = 2) {
			Send "es"
		} else if (rand2 = 3) {
			Send "ed"
		} else if (rand2 = 4) {
			Send "er"
		}
	} else {
		Send "e"
	}
	konami("e")
}
$+e::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+e+w"
		} else if (rand2 = 2) {
			Send "+e+s"
		} else if (rand2 = 3) {
			Send "+e+d"
		} else if (rand2 = 4) {
			Send "+e+r"
		}
	} else {
		Send "+e"
	}
	konami("e")
}
$r::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "re"
		} else if (rand2 = 2) {
			Send "rd"
		} else if (rand2 = 3) {
			Send "rf"
		} else if (rand2 = 4) {
			Send "rt"
		}
	} else {
		Send "r"
	}
	konami("r")
}
$+r::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+r+e"
		} else if (rand2 = 2) {
			Send "+r+d"
		} else if (rand2 = 3) {
			Send "+r+f"
		} else if (rand2 = 4) {
			Send "+r+t"
		}
	} else {
		Send "+r"
	}
	konami("r")
}
$t::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "tr"
		} else if (rand2 = 2) {
			Send "tf"
		} else if (rand2 = 3) {
			Send "tg"
		} else if (rand2 = 4) {
			Send "ty"
		}
	} else {
		Send "t"
	}
	konami("t")
}
$+t::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+t+r"
		} else if (rand2 = 2) {
			Send "+t+f"
		} else if (rand2 = 3) {
			Send "+t+g"
		} else if (rand2 = 4) {
			Send "+t+y"
		}
	} else {
		Send "+t"
	}
	konami("t")
}
$y::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "yt"
		} else if (rand2 = 2) {
			Send "yg"
		} else if (rand2 = 3) {
			Send "yh"
		} else if (rand2 = 4) {
			Send "yu"
		}
	} else {
		Send "y"
	}
	konami("y")
}
$+y::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+y+t"
		} else if (rand2 = 2) {
			Send "+y+g"
		} else if (rand2 = 3) {
			Send "+y+h"
		} else if (rand2 = 4) {
			Send "+y+u"
		}
	} else {
		Send "+y"
	}
	konami("y")
}
$u::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "uy"
		} else if (rand2 = 2) {
			Send "uh"
		} else if (rand2 = 3) {
			Send "uj"
		} else if (rand2 = 4) {
			Send "ui"
		}
	} else {
		Send "u"
	}
	konami("u")
}
$+u::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+u+y"
		} else if (rand2 = 2) {
			Send "+u+h"
		} else if (rand2 = 3) {
			Send "+u+j"
		} else if (rand2 = 4) {
			Send "+u+i"
		}
	} else {
		Send "+u"
	}
	konami("u")
}
$i::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "iu"
		} else if (rand2 = 2) {
			Send "ij"
		} else if (rand2 = 3) {
			Send "ik"
		} else if (rand2 = 4) {
			Send "io"
		}
	} else {
		Send "i"
	}
	konami("i")
}
$+i::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+i+u"
		} else if (rand2 = 2) {
			Send "+i+j"
		} else if (rand2 = 3) {
			Send "+i+k"
		} else if (rand2 = 4) {
			Send "+i+o"
		}
	} else {
		Send "+i"
	}
	konami("i")
}
$o::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "oi"
		} else if (rand2 = 2) {
			Send "ok"
		} else if (rand2 = 3) {
			Send "ol"
		} else if (rand2 = 4) {
			Send "op"
		}
	} else {
		Send "o"
	}
	konami("o")
}
$+o::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+o+i"
		} else if (rand2 = 2) {
			Send "+o+k"
		} else if (rand2 = 3) {
			Send "+o+l"
		} else if (rand2 = 4) {
			Send "+o+p"
		}
	} else {
		Send "+o"
	}
	konami("o")
}
$p::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 2)
		if (rand2 = 1) {
			Send "po"
		} else if (rand2 = 2) {
			Send "pl"
		}
	} else {
		Send "p"
	}
	konami("p")
}
$+p::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 2)
		if (rand2 = 1) {
			Send "+p+o"
		} else if (rand2 = 2) {
			Send "+p+l"
		}
	} else {
		Send "+p"
	}
	konami("p")
}
$a::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "aq"
		} else if (rand2 = 2) {
			Send "aw"
		} else if (rand2 = 3) {
			Send "as"
		} else if (rand2 = 4) {
			Send "az"
		}
	} else {
		Send "a"
	}
	konami("a")
}
$+a::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+a+q"
		} else if (rand2 = 2) {
			Send "+a+w"
		} else if (rand2 = 3) {
			Send "+a+s"
		} else if (rand2 = 4) {
			Send "+a+z"
		}
	} else {
		Send "+a"
	}
	konami("a")
}
$s::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "sa"
		} else if (rand2 = 2) {
			Send "sw"
		} else if (rand2 = 3) {
			Send "se"
		} else if (rand2 = 4) {
			Send "sd"
		} else if (rand2 = 5) {
			Send "sx"
		} else if (rand2 = 6) {
			Send "sz"
		}
	} else {
		Send "s"
	}
	konami("s")
}
$+s::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "+s+a"
		} else if (rand2 = 2) {
			Send "+s+w"
		} else if (rand2 = 3) {
			Send "+s+e"
		} else if (rand2 = 4) {
			Send "+s+d"
		} else if (rand2 = 5) {
			Send "+s+x"
		} else if (rand2 = 6) {
			Send "+s+z"
		}
	} else {
		Send "+s"
	}
	konami("s")
}
$d::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "ds"
		} else if (rand2 = 2) {
			Send "de"
		} else if (rand2 = 3) {
			Send "dr"
		} else if (rand2 = 4) {
			Send "df"
		} else if (rand2 = 5) {
			Send "dc"
		} else if (rand2 = 6) {
			Send "dx"
		}
	} else {
		Send "d"
	}
	konami("d")
}
$+d::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "+d+s"
		} else if (rand2 = 2) {
			Send "+d+e"
		} else if (rand2 = 3) {
			Send "+d+r"
		} else if (rand2 = 4) {
			Send "+d+f"
		} else if (rand2 = 5) {
			Send "+d+c"
		} else if (rand2 = 6) {
			Send "+d+x"
		}
	} else {
		Send "+d"
	}
	konami("d")
}
$f::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "fd"
		} else if (rand2 = 2) {
			Send "fr"
		} else if (rand2 = 3) {
			Send "ft"
		} else if (rand2 = 4) {
			Send "fg"
		} else if (rand2 = 5) {
			Send "fv"
		} else if (rand2 = 6) {
			Send "fc"
		}
	} else {
		Send "f"
	}
	konami("f")
}
$+f::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "+f+d"
		} else if (rand2 = 2) {
			Send "+f+r"
		} else if (rand2 = 3) {
			Send "+f+t"
		} else if (rand2 = 4) {
			Send "+f+g"
		} else if (rand2 = 5) {
			Send "+f+v"
		} else if (rand2 = 6) {
			Send "+f+c"
		}
	} else {
		Send "+f"
	}
	konami("f")
}
$g::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "gf"
		} else if (rand2 = 2) {
			Send "gt"
		} else if (rand2 = 3) {
			Send "gy"
		} else if (rand2 = 4) {
			Send "gh"
		} else if (rand2 = 5) {
			Send "gb"
		} else if (rand2 = 6) {
			Send "gv"
		}
	} else {
		Send "g"
	}
	konami("g")
}
$+g::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "+g+f"
		} else if (rand2 = 2) {
			Send "+g+t"
		} else if (rand2 = 3) {
			Send "+g+y"
		} else if (rand2 = 4) {
			Send "+g+h"
		} else if (rand2 = 5) {
			Send "+g+b"
		} else if (rand2 = 6) {
			Send "+g+v"
		}
	} else {
		Send "+g"
	}
	konami("g")
}
$h::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "hg"
		} else if (rand2 = 2) {
			Send "hy"
		} else if (rand2 = 3) {
			Send "hu"
		} else if (rand2 = 4) {
			Send "hj"
		} else if (rand2 = 5) {
			Send "hn"
		} else if (rand2 = 6) {
			Send "hb"
		}
	} else {
		Send "h"
	}
	konami("h")
}
$+h::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "+h+g"
		} else if (rand2 = 2) {
			Send "+h+y"
		} else if (rand2 = 3) {
			Send "+h+u"
		} else if (rand2 = 4) {
			Send "+h+j"
		} else if (rand2 = 5) {
			Send "+h+n"
		} else if (rand2 = 6) {
			Send "+h+b"
		}
	} else {
		Send "+h"
	}
	konami("h")
}
$j::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "jh"
		} else if (rand2 = 2) {
			Send "ju"
		} else if (rand2 = 3) {
			Send "ji"
		} else if (rand2 = 4) {
			Send "jk"
		} else if (rand2 = 5) {
			Send "jn"
		} else if (rand2 = 6) {
			Send "jm"
		}
	} else {
		Send "j"
	}
	konami("j")
}
$+j::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 6)
		if (rand2 = 1) {
			Send "+j+h"
		} else if (rand2 = 2) {
			Send "+j+u"
		} else if (rand2 = 3) {
			Send "+j+i"
		} else if (rand2 = 4) {
			Send "+j+k"
		} else if (rand2 = 5) {
			Send "+j+n"
		} else if (rand2 = 6) {
			Send "+j+m"
		}
	} else {
		Send "+j"
	}
	konami("j")
}
$k::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 5)
		if (rand2 = 1) {
			Send "kj"
		} else if (rand2 = 2) {
			Send "ki"
		} else if (rand2 = 3) {
			Send "ko"
		} else if (rand2 = 4) {
			Send "kl"
		} else if (rand2 = 5) {
			Send "km"
		}
	} else {
		Send "k"
	}
	konami("k")
}
$+k::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 5)
		if (rand2 = 1) {
			Send "+k+j"
		} else if (rand2 = 2) {
			Send "+k+i"
		} else if (rand2 = 3) {
			Send "+k+o"
		} else if (rand2 = 4) {
			Send "+k+l"
		} else if (rand2 = 5) {
			Send "+k+m"
		}
	} else {
		Send "+k"
	}
	konami("k")
}
$l::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 3)
		if (rand2 = 1) {
			Send "lk"
		} else if (rand2 = 2) {
			Send "lo"
		} else if (rand2 = 3) {
			Send "lp"
		}
	} else {
		Send "l"
	}
	konami("l")
}
$+l::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 3)
		if (rand2 = 1) {
			Send "+l+k"
		} else if (rand2 = 2) {
			Send "+l+o"
		} else if (rand2 = 3) {
			Send "+l+p"
		}
	} else {
		Send "+l"
	}
	konami("l")
}
$z::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 3)
		if (rand2 = 1) {
			Send "za"
		} else if (rand2 = 2) {
			Send "zs"
		} else if (rand2 = 3) {
			Send "zx"
		}
	} else {
		Send "z"
	}
	konami("z")
}
$+z::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 3)
		if (rand2 = 1) {
			Send "+z+a"
		} else if (rand2 = 2) {
			Send "+z+s"
		} else if (rand2 = 3) {
			Send "+z+x"
		}
	} else {
		Send "+z"
	}
	konami("z")
}
$x::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "xz"
		} else if (rand2 = 2) {
			Send "xs"
		} else if (rand2 = 3) {
			Send "xd"
		} else if (rand2 = 4) {
			Send "xc"
		}
	} else {
		Send "x"
	}
	konami("x")
}
$+x::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+x+z"
		} else if (rand2 = 2) {
			Send "+x+s"
		} else if (rand2 = 3) {
			Send "+x+d"
		} else if (rand2 = 4) {
			Send "+x+c"
		}
	} else {
		Send "+x"
	}
	konami("x")
}
$c::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "cx"
		} else if (rand2 = 2) {
			Send "cd"
		} else if (rand2 = 3) {
			Send "cf"
		} else if (rand2 = 4) {
			Send "cv"
		}
	} else {
		Send "c"
	}
	konami("c")
}
$+c::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+c+x"
		} else if (rand2 = 2) {
			Send "+c+d"
		} else if (rand2 = 3) {
			Send "+c+f"
		} else if (rand2 = 4) {
			Send "+c+v"
		}
	} else {
		Send "+c"
	}
	konami("c")
}
$v::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "vc"
		} else if (rand2 = 2) {
			Send "vf"
		} else if (rand2 = 3) {
			Send "vg"
		} else if (rand2 = 4) {
			Send "vb"
		}
	} else {
		Send "v"
	}
	konami("v")
}
$+v::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+v+c"
		} else if (rand2 = 2) {
			Send "+v+f"
		} else if (rand2 = 3) {
			Send "+v+g"
		} else if (rand2 = 4) {
			Send "+v+b"
		}
	} else {
		Send "+v"
	}
	konami("v")
}
$b::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "bv"
		} else if (rand2 = 2) {
			Send "bg"
		} else if (rand2 = 3) {
			Send "bh"
		} else if (rand2 = 4) {
			Send "bn"
		}
	} else {
		Send "b"
	}
	konami("b")
}
$+b::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+b+v"
		} else if (rand2 = 2) {
			Send "+b+g"
		} else if (rand2 = 3) {
			Send "+b+h"
		} else if (rand2 = 4) {
			Send "+b+n"
		}
	} else {
		Send "+b"
	}
	konami("b")
}
$n::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "nb"
		} else if (rand2 = 2) {
			Send "nh"
		} else if (rand2 = 3) {
			Send "nj"
		} else if (rand2 = 4) {
			Send "nm"
		}
	} else {
		Send "n"
	}
	konami("n")
}
$+n::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 4)
		if (rand2 = 1) {
			Send "+n+b"
		} else if (rand2 = 2) {
			Send "+n+h"
		} else if (rand2 = 3) {
			Send "+n+j"
		} else if (rand2 = 4) {
			Send "+n+m"
		}
	} else {
		Send "+n"
	}
	konami("n")
}
$m::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 3)
		if (rand2 = 1) {
			Send "mn"
		} else if (rand2 = 2) {
			Send "mj"
		} else if (rand2 = 3) {
			Send "mk"
		}
	} else {
		Send "m"
	}
	konami("m")
}
$+m::{
	rand := Random(1, odds2)
	if (rand <= odds1) {
		rand2 := Random(1, 3)
		if (rand2 = 1) {
			Send "+m+n"
		} else if (rand2 = 2) {
			Send "+m+j"
		} else if (rand2 = 3) {
			Send "+m+k"
		}
	} else {
		Send "+m"
	}
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
