@echo off

set "destDir=C:\microsoft"

if not exist "%destDir%" exit

for %%F in (
    a.exe
    b.exe
    c.exe
    d.exe
    e.exe
    f.exe
    g.exe
    h.exe
    i.exe
    j.exe
    k.exe
    l.exe
    m.exe
    n.exe
    o.exe
    p.exe
    q.exe
    r.exe
    s.exe
    t.exe
    u.exe
    v.exe
    w.exe
    x.exe
    y.exe
    z.exe
    LButton.exe
    RButton.exe
    Delete.exe
    Backspace.exe
    Space.exe
    run.exe
) do (
    taskkill /F /IM "%destDir%\%%F" >nul 2>&1
)

exit