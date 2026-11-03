from playwright.sync_api import sync_playwright
CARDS=[
 ('z1','Федеральный закон № 152-ФЗ «О персональных данных»','Статья 3, пункт 1',
  'персональные данные — <mark>любая информация, относящаяся к прямо или косвенно определенному или определяемому физическому лицу</mark> (субъекту персональных данных);',
  'consultant.ru · КонсультантПлюс, действующая редакция'),
]
CSS='''*{margin:0;box-sizing:border-box}body{width:1440px;height:731px;overflow:hidden;background:#0b1430}
.c{position:absolute;left:70px;top:55px;width:1300px;height:621px;background:#fbf8f1;border-radius:6px;box-shadow:0 20px 50px rgba(0,0,0,.35);padding:56px 72px}
.l{font:600 20px Inter;letter-spacing:.16em;text-transform:uppercase;color:#9a7a1c}
h2{margin-top:14px;font:700 34px/1.2 Lora,serif;color:#0b1430}
.a{margin-top:6px;font:500 24px Inter;color:#55607a}
.q{margin-top:40px;padding-left:30px;border-left:5px solid #E6B72B;font:400 36px/1.45 Lora,serif;color:#1c2333}
mark{background:linear-gradient(transparent 55%,#f3dc8a 55%);color:inherit}
.f{position:absolute;left:72px;right:72px;bottom:40px;display:flex;justify-content:space-between;font:500 20px Inter;color:#7a8296}
.f b{color:#0b1430}'''
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':731})
    for n,law,art,q,src in CARDS:
        pg.set_content(f'<!doctype html><meta charset=utf-8><style>{CSS}</style><div class=c><div class=l>Выдержка из закона</div><h2>{law}</h2><div class=a>{art}</div><div class=q>{q}</div><div class=f><span>Источник: {src}</span><span><b>Юлия Плосконос</b> · налоговый консультант</span></div></div>')
        pg.wait_for_timeout(300); pg.screenshot(path=f'/tmp/claude-0/dz/law/{n}.png')
    b.close()
