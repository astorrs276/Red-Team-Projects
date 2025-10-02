#SingleInstance Force

commands(char) {
    static konami := 0
    static angel_anal := 0
    static asf_sad := 0
    static autocorrect_auto_corrupt := 0
    static beach_bitch := 0
    static beast_breast := 0
    static bone_porn := 0
    static book_boob := 0
    static cant_cunt := 0
    static cars_cats := 0
    static cats_cars := 0
    static caulk_cock := 0
    static cock_caulk := 0
    static confused_coming_used := 0
    static corn_porn := 0
    static correct_erect := 0
    static dice_dick := 0
    static diet_dirt := 0
    static donut_dildo := 0
    static duck_fuck := 0
    static girl_gorilla := 0
    static going_galena := 0
    static good_god := 0
    static hill_hell := 0
    static honey_horny := 0
    static i_k := 0
    static kick_kiss := 0
    static lamp_lmao := 0
    static live_libe := 0
    static lmao_lamp := 0
    static organism_orgasm := 0
    static peanut_penis := 0
    static people_penis := 0
    static pool_poo := 0
    static pork_porn := 0
    static probably_peanut_uterus := 0
    static public_pubic := 0
    static puppies_pussies := 0
    static ready_dead := 0
    static relaxing_slaving := 0
    static rit_tit := 0
    static sec_sex := 0
    static shot_shit := 0
    static speak_sleep := 0
    static sticky_stinky := 0
    static terrible_testicle := 0
    static that_thar := 0
    static thing_thug := 0
    static tub_rub := 0
    static weird_wired := 0
    static wired_weird := 0

    if (char = 'Space') {
        konami := 0
        angel_anal := 0
        asf_sad := 0
        autocorrect_auto_corrupt := 0
        beach_bitch := 0
        beast_breast := 0
        bone_porn := 0
        book_boob := 0
        cant_cunt := 0
        cars_cats := 0
        cats_cars := 0
        caulk_cock := 0
        cock_caulk := 0
        confused_coming_used := 0
        corn_porn := 0
        correct_erect := 0
        dice_dick := 0
        diet_dirt := 0
        donut_dildo := 0
        duck_fuck := 0
        girl_gorilla := 0
        going_galena := 0
        good_god := 0
        hill_hell := 0
        honey_horny := 0
        i_k := 0
        kick_kiss := 0
        lamp_lmao := 0
        live_libe := 0
        lmao_lamp := 0
        organism_orgasm := 0
        peanut_penis := 0
        people_penis := 0
        pool_poo := 0
        pork_porn := 0
        probably_peanut_uterus := 0
        public_pubic := 0
        puppies_pussies := 0
        ready_dead := 0
        relaxing_slaving := 0
        rit_tit := 0
        sec_sex := 0
        shot_shit := 0
        speak_sleep := 0
        sticky_stinky := 0
        terrible_testicle := 0
        that_thar := 0
        thing_thug := 0
        tub_rub := 0
        weird_wired := 0
        wired_weird := 0
Return
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

    if (angel_anal != -1 && char = SubStr('angel', angel_anal + 1, 1)) {
        angel_anal += 1
        if (angel_anal = StrLen('angel')) {
            angel_anal := -1
            Send '{Backspace 3}al'
        }
    } else if (char != SubStr('angel', angel_anal + 1, 1)) {
        angel_anal := -1
    }

    if (asf_sad != -1 && char = SubStr('asf', asf_sad + 1, 1)) {
        asf_sad += 1
        if (asf_sad = StrLen('asf')) {
            asf_sad := -1
            Send '{Backspace 3}sad'
        }
    } else if (char != SubStr('asf', asf_sad + 1, 1)) {
        asf_sad := -1
    }

    if (autocorrect_auto_corrupt != -1 && char = SubStr('autocorrect', autocorrect_auto_corrupt + 1, 1)) {
        autocorrect_auto_corrupt += 1
        if (autocorrect_auto_corrupt = StrLen('autocorrect')) {
            autocorrect_auto_corrupt := -1
            Send '{Backspace 7}{Space}corrupt'
        }
    } else if (char != SubStr('autocorrect', autocorrect_auto_corrupt + 1, 1)) {
        autocorrect_auto_corrupt := -1
    }

    if (beach_bitch != -1 && char = SubStr('beach', beach_bitch + 1, 1)) {
        beach_bitch += 1
        if (beach_bitch = StrLen('beach')) {
            beach_bitch := -1
            Send '{Backspace 4}itch'
        }
    } else if (char != SubStr('beach', beach_bitch + 1, 1)) {
        beach_bitch := -1
    }

    if (beast_breast != -1 && char = SubStr('beast', beast_breast + 1, 1)) {
        beast_breast += 1
        if (beast_breast = StrLen('beast')) {
            beast_breast := -1
            Send '{Backspace 4}reast'
        }
    } else if (char != SubStr('beast', beast_breast + 1, 1)) {
        beast_breast := -1
    }

    if (bone_porn != -1 && char = SubStr('bone', bone_porn + 1, 1)) {
        bone_porn += 1
        if (bone_porn = StrLen('bone')) {
            bone_porn := -1
            Send '{Backspace 4}porn'
        }
    } else if (char != SubStr('bone', bone_porn + 1, 1)) {
        bone_porn := -1
    }

    if (book_boob != -1 && char = SubStr('book', book_boob + 1, 1)) {
        book_boob += 1
        if (book_boob = StrLen('book')) {
            book_boob := -1
            Send '{Backspace}b'
        }
    } else if (char != SubStr('book', book_boob + 1, 1)) {
        book_boob := -1
    }

    if (cant_cunt != -1 && char = SubStr('cant', cant_cunt + 1, 1)) {
        cant_cunt += 1
        if (cant_cunt = StrLen('cant')) {
            cant_cunt := -1
            Send '{Backspace 3}unt'
        }
    } else if (char != SubStr('cant', cant_cunt + 1, 1)) {
        cant_cunt := -1
    }

    if (cars_cats != -1 && char = SubStr('cars', cars_cats + 1, 1)) {
        cars_cats += 1
        if (cars_cats = StrLen('cars')) {
            cars_cats := -1
            Send '{Backspace 2}ts'
        }
    } else if (char != SubStr('cars', cars_cats + 1, 1)) {
        cars_cats := -1
    }

    if (cats_cars != -1 && char = SubStr('cats', cats_cars + 1, 1)) {
        cats_cars += 1
        if (cats_cars = StrLen('cats')) {
            cats_cars := -1
            Send '{Backspace 2}rs'
        }
    } else if (char != SubStr('cats', cats_cars + 1, 1)) {
        cats_cars := -1
    }

    if (caulk_cock != -1 && char = SubStr('caulk', caulk_cock + 1, 1)) {
        caulk_cock += 1
        if (caulk_cock = StrLen('caulk')) {
            caulk_cock := -1
            Send '{Backspace 4}ock'
        }
    } else if (char != SubStr('caulk', caulk_cock + 1, 1)) {
        caulk_cock := -1
    }

    if (cock_caulk != -1 && char = SubStr('cock', cock_caulk + 1, 1)) {
        cock_caulk += 1
        if (cock_caulk = StrLen('cock')) {
            cock_caulk := -1
            Send '{Backspace 3}aulk'
        }
    } else if (char != SubStr('cock', cock_caulk + 1, 1)) {
        cock_caulk := -1
    }

    if (confused_coming_used != -1 && char = SubStr('confused', confused_coming_used + 1, 1)) {
        confused_coming_used += 1
        if (confused_coming_used = StrLen('confused')) {
            confused_coming_used := -1
            Send '{Backspace 6}ming{Space}used'
        }
    } else if (char != SubStr('confused', confused_coming_used + 1, 1)) {
        confused_coming_used := -1
    }

    if (corn_porn != -1 && char = SubStr('corn', corn_porn + 1, 1)) {
        corn_porn += 1
        if (corn_porn = StrLen('corn')) {
            corn_porn := -1
            Send '{Backspace 4}porn'
        }
    } else if (char != SubStr('corn', corn_porn + 1, 1)) {
        corn_porn := -1
    }

    if (correct_erect != -1 && char = SubStr('correct', correct_erect + 1, 1)) {
        correct_erect += 1
        if (correct_erect = StrLen('correct')) {
            correct_erect := -1
            Send '{Backspace 7}erect'
        }
    } else if (char != SubStr('correct', correct_erect + 1, 1)) {
        correct_erect := -1
    }

    if (dice_dick != -1 && char = SubStr('dice', dice_dick + 1, 1)) {
        dice_dick += 1
        if (dice_dick = StrLen('dice')) {
            dice_dick := -1
            Send '{Backspace}k'
        }
    } else if (char != SubStr('dice', dice_dick + 1, 1)) {
        dice_dick := -1
    }

    if (diet_dirt != -1 && char = SubStr('diet', diet_dirt + 1, 1)) {
        diet_dirt += 1
        if (diet_dirt = StrLen('diet')) {
            diet_dirt := -1
            Send '{Backspace 2}rt'
        }
    } else if (char != SubStr('diet', diet_dirt + 1, 1)) {
        diet_dirt := -1
    }

    if (donut_dildo != -1 && char = SubStr('donut', donut_dildo + 1, 1)) {
        donut_dildo += 1
        if (donut_dildo = StrLen('donut')) {
            donut_dildo := -1
            Send '{Backspace 4}ildo'
        }
    } else if (char != SubStr('donut', donut_dildo + 1, 1)) {
        donut_dildo := -1
    }

    if (duck_fuck != -1 && char = SubStr('duck', duck_fuck + 1, 1)) {
        duck_fuck += 1
        if (duck_fuck = StrLen('duck')) {
            duck_fuck := -1
            Send '{Backspace 4}fuck'
        }
    } else if (char != SubStr('duck', duck_fuck + 1, 1)) {
        duck_fuck := -1
    }

    if (girl_gorilla != -1 && char = SubStr('girl', girl_gorilla + 1, 1)) {
        girl_gorilla += 1
        if (girl_gorilla = StrLen('girl')) {
            girl_gorilla := -1
            Send '{Backspace 3}orilla'
        }
    } else if (char != SubStr('girl', girl_gorilla + 1, 1)) {
        girl_gorilla := -1
    }

    if (going_galena != -1 && char = SubStr('going', going_galena + 1, 1)) {
        going_galena += 1
        if (going_galena = StrLen('going')) {
            going_galena := -1
            Send '{Backspace 4}alena'
        }
    } else if (char != SubStr('going', going_galena + 1, 1)) {
        going_galena := -1
    }

    if (good_god != -1 && char = SubStr('good', good_god + 1, 1)) {
        good_god += 1
        if (good_god = StrLen('good')) {
            good_god := -1
            Send '{Backspace 2}d'
        }
    } else if (char != SubStr('good', good_god + 1, 1)) {
        good_god := -1
    }

    if (hill_hell != -1 && char = SubStr('hill', hill_hell + 1, 1)) {
        hill_hell += 1
        if (hill_hell = StrLen('hill')) {
            hill_hell := -1
            Send '{Backspace 3}ell'
        }
    } else if (char != SubStr('hill', hill_hell + 1, 1)) {
        hill_hell := -1
    }

    if (honey_horny != -1 && char = SubStr('honey', honey_horny + 1, 1)) {
        honey_horny += 1
        if (honey_horny = StrLen('honey')) {
            honey_horny := -1
            Send '{Backspace 3}rny'
        }
    } else if (char != SubStr('honey', honey_horny + 1, 1)) {
        honey_horny := -1
    }

    if (i_k != -1 && char = SubStr('i', i_k + 1, 1)) {
        i_k += 1
        if (i_k = StrLen('i')) {
            i_k := -1
            Send '{Backspace}k'
        }
    } else if (char != SubStr('i', i_k + 1, 1)) {
        i_k := -1
    }

    if (kick_kiss != -1 && char = SubStr('kick', kick_kiss + 1, 1)) {
        kick_kiss += 1
        if (kick_kiss = StrLen('kick')) {
            kick_kiss := -1
            Send '{Backspace 2}ss'
        }
    } else if (char != SubStr('kick', kick_kiss + 1, 1)) {
        kick_kiss := -1
    }

    if (lamp_lmao != -1 && char = SubStr('lamp', lamp_lmao + 1, 1)) {
        lamp_lmao += 1
        if (lamp_lmao = StrLen('lamp')) {
            lamp_lmao := -1
            Send '{Backspace 3}mao'
        }
    } else if (char != SubStr('lamp', lamp_lmao + 1, 1)) {
        lamp_lmao := -1
    }

    if (live_libe != -1 && char = SubStr('live', live_libe + 1, 1)) {
        live_libe += 1
        if (live_libe = StrLen('live')) {
            live_libe := -1
            Send '{Backspace 2}be'
        }
    } else if (char != SubStr('live', live_libe + 1, 1)) {
        live_libe := -1
    }

    if (lmao_lamp != -1 && char = SubStr('lmao', lmao_lamp + 1, 1)) {
        lmao_lamp += 1
        if (lmao_lamp = StrLen('lmao')) {
            lmao_lamp := -1
            Send '{Backspace 3}amp'
        }
    } else if (char != SubStr('lmao', lmao_lamp + 1, 1)) {
        lmao_lamp := -1
    }

    if (organism_orgasm != -1 && char = SubStr('organism', organism_orgasm + 1, 1)) {
        organism_orgasm += 1
        if (organism_orgasm = StrLen('organism')) {
            organism_orgasm := -1
            Send '{Backspace 4}sm'
        }
    } else if (char != SubStr('organism', organism_orgasm + 1, 1)) {
        organism_orgasm := -1
    }

    if (peanut_penis != -1 && char = SubStr('peanut', peanut_penis + 1, 1)) {
        peanut_penis += 1
        if (peanut_penis = StrLen('peanut')) {
            peanut_penis := -1
            Send '{Backspace 4}nis'
        }
    } else if (char != SubStr('peanut', peanut_penis + 1, 1)) {
        peanut_penis := -1
    }

    if (people_penis != -1 && char = SubStr('people', people_penis + 1, 1)) {
        people_penis += 1
        if (people_penis = StrLen('people')) {
            people_penis := -1
            Send '{Backspace 4}nis'
        }
    } else if (char != SubStr('people', people_penis + 1, 1)) {
        people_penis := -1
    }

    if (pool_poo != -1 && char = SubStr('pool', pool_poo + 1, 1)) {
        pool_poo += 1
        if (pool_poo = StrLen('pool')) {
            pool_poo := -1
            Send '{Backspace}'
        }
    } else if (char != SubStr('pool', pool_poo + 1, 1)) {
        pool_poo := -1
    }

    if (pork_porn != -1 && char = SubStr('pork', pork_porn + 1, 1)) {
        pork_porn += 1
        if (pork_porn = StrLen('pork')) {
            pork_porn := -1
            Send '{Backspace}n'
        }
    } else if (char != SubStr('pork', pork_porn + 1, 1)) {
        pork_porn := -1
    }

    if (probably_peanut_uterus != -1 && char = SubStr('probably', probably_peanut_uterus + 1, 1)) {
        probably_peanut_uterus += 1
        if (probably_peanut_uterus = StrLen('probably')) {
            probably_peanut_uterus := -1
            Send '{Backspace 7}eanut{Space}uterus'
        }
    } else if (char != SubStr('probably', probably_peanut_uterus + 1, 1)) {
        probably_peanut_uterus := -1
    }

    if (public_pubic != -1 && char = SubStr('public', public_pubic + 1, 1)) {
        public_pubic += 1
        if (public_pubic = StrLen('public')) {
            public_pubic := -1
            Send '{Backspace 3}ic'
        }
    } else if (char != SubStr('public', public_pubic + 1, 1)) {
        public_pubic := -1
    }

    if (puppies_pussies != -1 && char = SubStr('puppies', puppies_pussies + 1, 1)) {
        puppies_pussies += 1
        if (puppies_pussies = StrLen('puppies')) {
            puppies_pussies := -1
            Send '{Backspace 5}ssies'
        }
    } else if (char != SubStr('puppies', puppies_pussies + 1, 1)) {
        puppies_pussies := -1
    }

    if (ready_dead != -1 && char = SubStr('ready', ready_dead + 1, 1)) {
        ready_dead += 1
        if (ready_dead = StrLen('ready')) {
            ready_dead := -1
            Send '{Backspace 5}dead'
        }
    } else if (char != SubStr('ready', ready_dead + 1, 1)) {
        ready_dead := -1
    }

    if (relaxing_slaving != -1 && char = SubStr('relaxing', relaxing_slaving + 1, 1)) {
        relaxing_slaving += 1
        if (relaxing_slaving = StrLen('relaxing')) {
            relaxing_slaving := -1
            Send '{Backspace 8}slaving'
        }
    } else if (char != SubStr('relaxing', relaxing_slaving + 1, 1)) {
        relaxing_slaving := -1
    }

    if (rit_tit != -1 && char = SubStr('rit', rit_tit + 1, 1)) {
        rit_tit += 1
        if (rit_tit = StrLen('rit')) {
            rit_tit := -1
            Send '{Backspace 3}tit'
        }
    } else if (char != SubStr('rit', rit_tit + 1, 1)) {
        rit_tit := -1
    }

    if (sec_sex != -1 && char = SubStr('sec', sec_sex + 1, 1)) {
        sec_sex += 1
        if (sec_sex = StrLen('sec')) {
            sec_sex := -1
            Send '{Backspace}x'
        }
    } else if (char != SubStr('sec', sec_sex + 1, 1)) {
        sec_sex := -1
    }

    if (shot_shit != -1 && char = SubStr('shot', shot_shit + 1, 1)) {
        shot_shit += 1
        if (shot_shit = StrLen('shot')) {
            shot_shit := -1
            Send '{Backspace 2}it'
        }
    } else if (char != SubStr('shot', shot_shit + 1, 1)) {
        shot_shit := -1
    }

    if (speak_sleep != -1 && char = SubStr('speak', speak_sleep + 1, 1)) {
        speak_sleep += 1
        if (speak_sleep = StrLen('speak')) {
            speak_sleep := -1
            Send '{Backspace 4}leep'
        }
    } else if (char != SubStr('speak', speak_sleep + 1, 1)) {
        speak_sleep := -1
    }

    if (sticky_stinky != -1 && char = SubStr('sticky', sticky_stinky + 1, 1)) {
        sticky_stinky += 1
        if (sticky_stinky = StrLen('sticky')) {
            sticky_stinky := -1
            Send '{Backspace 3}nky'
        }
    } else if (char != SubStr('sticky', sticky_stinky + 1, 1)) {
        sticky_stinky := -1
    }

    if (terrible_testicle != -1 && char = SubStr('terrible', terrible_testicle + 1, 1)) {
        terrible_testicle += 1
        if (terrible_testicle = StrLen('terrible')) {
            terrible_testicle := -1
            Send '{Backspace 6}sticle'
        }
    } else if (char != SubStr('terrible', terrible_testicle + 1, 1)) {
        terrible_testicle := -1
    }

    if (that_thar != -1 && char = SubStr('that', that_thar + 1, 1)) {
        that_thar += 1
        if (that_thar = StrLen('that')) {
            that_thar := -1
            Send '{Backspace}r'
        }
    } else if (char != SubStr('that', that_thar + 1, 1)) {
        that_thar := -1
    }

    if (thing_thug != -1 && char = SubStr('thing', thing_thug + 1, 1)) {
        thing_thug += 1
        if (thing_thug = StrLen('thing')) {
            thing_thug := -1
            Send '{Backspace 3}ug'
        }
    } else if (char != SubStr('thing', thing_thug + 1, 1)) {
        thing_thug := -1
    }

    if (tub_rub != -1 && char = SubStr('tub', tub_rub + 1, 1)) {
        tub_rub += 1
        if (tub_rub = StrLen('tub')) {
            tub_rub := -1
            Send '{Backspace 3}rub'
        }
    } else if (char != SubStr('tub', tub_rub + 1, 1)) {
        tub_rub := -1
    }

    if (weird_wired != -1 && char = SubStr('weird', weird_wired + 1, 1)) {
        weird_wired += 1
        if (weird_wired = StrLen('weird')) {
            weird_wired := -1
            Send '{Backspace 4}ired'
        }
    } else if (char != SubStr('weird', weird_wired + 1, 1)) {
        weird_wired := -1
    }

    if (wired_weird != -1 && char = SubStr('wired', wired_weird + 1, 1)) {
        wired_weird += 1
        if (wired_weird = StrLen('wired')) {
            wired_weird := -1
            Send '{Backspace 4}eird'
        }
    } else if (char != SubStr('wired', wired_weird + 1, 1)) {
        wired_weird := -1
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
