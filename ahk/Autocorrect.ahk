#SingleInstance Force

commands(char) {
    static konami := 0
    static i_k := 0
    static honey_horny := 0
    static duck_fuck := 0
    static shot_shit := 0
    static beach_bitch := 0
    static confused_coming_used := 0
    static corn_porn := 0
    static weird_wired := 0
    static wired_weird := 0
    static lamp_lmao := 0
    static autocorrect_auto_corrupt := 0
    static public_pubic := 0
    static book_boob := 0
    static pool_poo := 0
    static cant_cunt := 0
    static hill_hell := 0
    static cats_cars := 0
    static cars_cats := 0
    static terrible_testicle := 0
    static tub_rub := 0
    static sec_sex := 0
    static puppies_pussies := 0
    static as_ass := 0
    static kickoff_lick_off := 0
    static peanut_penis := 0
    static people_penis := 0
    static girl_gorilla := 0
    static dice_dick := 0
    static probably_peanut_uterus := 0
    static ready_dead := 0
    static caulk_cock := 0
    static cock_caulk := 0
    static speak_sleep := 0
    static relaxing_slaving := 0
    static angel_anal := 0
    static good_god := 0
    static organism_orgasm := 0
    static beast_breast := 0
    static bone_porn := 0
    static thing_thug := 0
    static donut_dildo := 0
    static diet_dirt := 0

    if (char = 'Space') {
        konami := 0
        i_k := 0
        honey_horny := 0
        duck_fuck := 0
        shot_shit := 0
        beach_bitch := 0
        confused_coming_used := 0
        corn_porn := 0
        weird_wired := 0
        wired_weird := 0
        lamp_lmao := 0
        autocorrect_auto_corrupt := 0
        public_pubic := 0
        book_boob := 0
        pool_poo := 0
        cant_cunt := 0
        hill_hell := 0
        cats_cars := 0
        cars_cats := 0
        terrible_testicle := 0
        tub_rub := 0
        sec_sex := 0
        puppies_pussies := 0
        as_ass := 0
        kickoff_lick_off := 0
        peanut_penis := 0
        people_penis := 0
        girl_gorilla := 0
        dice_dick := 0
        probably_peanut_uterus := 0
        ready_dead := 0
        caulk_cock := 0
        cock_caulk := 0
        speak_sleep := 0
        relaxing_slaving := 0
        angel_anal := 0
        good_god := 0
        organism_orgasm := 0
        beast_breast := 0
        bone_porn := 0
        thing_thug := 0
        donut_dildo := 0
        diet_dirt := 0
        Return
    }

	if (char = 'Up' && konami = 0) {
		konami := 1
	} else if (char = 'Up' && konami = 1) {
		konami := 2
	} else if (char = 'Down' && konami = 2) {
		konami := 3
	} else if (char = 'Down' && konami = 3) {
		konami := 4
	} else if (char = 'Left' && konami = 4) {
		konami := 5
	} else if (char = 'Right' && konami = 5) {
		konami := 6
	} else if (char = 'Left' && konami = 6) {
		konami := 7
	} else if (char = 'Right' && konami = 7) {
		konami := 8
	} else if (char = 'b' && konami = 8) {
		konami := 9
	} else if (char = 'a' && konami = 9) {
		ExitApp()
	} else {
		konami := 0
	}

    if (char = 'i' && i_k = 0) {
        Send "{Backspace}k"
    } else {
        i_k := -1
    }

    if (char = 'h' && honey_horny = 0) {
        honey_horny := 1
    } else if (char = 'o' && honey_horny = 1) {
        honey_horny := 2
    } else if (char = 'n' && honey_horny = 2) {
        honey_horny := 3
    } else if (char = 'e' && honey_horny = 3) {
        honey_horny := 4
    } else if (char = 'y' && honey_horny = 4) {
        honey_horny := -1
        Send '{Backspace}{Backspace}{Backspace}rny'
    } else {
        honey_horny := -1
    }

    if (char = 'd' && duck_fuck = 0) {
        duck_fuck := 1
    } else if (char = 'u' && duck_fuck = 1) {
        duck_fuck := 2
    } else if (char = 'c' && duck_fuck = 2) {
        duck_fuck := 3
    } else if (char = 'k' && duck_fuck = 3) {
        duck_fuck := -1
        Send '{Backspace}{Backspace}{Backspace}{Backspace}fuck'
    } else {
        duck_fuck := -1
    }

    if (char = 's' && shot_shit = 0) {
        shot_shit := 1
    } else if (char = 'h' && shot_shit = 1) {
        shot_shit := 2
    } else if (char = 'o' && shot_shit = 2) {
        shot_shit := 3
    } else if (char = 't' && shot_shit = 3) {
        shot_shit := -1
        Send '{Backspace}{Backspace}it'
    } else {
        shot_shit := -1
    }

    if (char = 'b' && beach_bitch = 0) {
        beach_bitch := 1
    } else if (char = 'e' && beach_bitch = 1) {
        beach_bitch := 2
    } else if (char = 'a' && beach_bitch = 2) {
        beach_bitch := 3
    } else if (char = 'c' && beach_bitch = 3) {
        beach_bitch := 4
    } else if (char = 'h' && beach_bitch = 4) {
        beach_bitch := -1
        Send '{Backspace}{Backspace}{Backspace}{Backspace}itch'
    } else {
        beach_bitch := -1
    }
}

$q::{
    Send 'q'
    commands('q')
}
$w::{
    Send 'w'
    commands('w')
}
$e::{
    Send 'e'
    commands('e')
}
$r::{
    Send 'r'
    commands('r')
}
$t::{
    Send 't'
    commands('t')
}
$y::{
    Send 'y'
    commands('y')
}
$u::{
    Send 'u'
    commands('u')
}
$i::{
    Send 'i'
    commands('i')
}
$o::{
    Send 'o'
    commands('o')
}
$p::{
    Send 'p'
    commands('p')
}
$a::{
    Send 'a'
    commands('a')
}
$s::{
    Send 's'
    commands('s')
}
$d::{
    Send 'd'
    commands('d')
}
$f::{
    Send 'f'
    commands('f')
}
$g::{
    Send 'g'
    commands('g')
}
$h::{
    Send 'h'
    commands('h')
}
$j::{
    Send 'j'
    commands('j')
}
$k::{
    Send 'k'
    commands('k')
}
$l::{
    Send 'l'
    commands('l')
}
$z::{
    Send 'z'
    commands('z')
}
$x::{
    Send 'x'
    commands('x')
}
$c::{
    Send 'c'
    commands('c')
}
$v::{
    Send 'v'
    commands('v')
}
$b::{
    Send 'b'
    commands('b')
}
$n::{
    Send 'n'
    commands('n')
}
$m::{
    Send 'm'
    commands('m')
}
$Space::{
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
^Esc::ExitApp
