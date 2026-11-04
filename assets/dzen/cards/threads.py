import sys
from playwright.sync_api import sync_playwright
CSS='''*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;background:#0b1430;color:#fff;font-family:Inter,sans-serif;overflow:hidden}
.w{padding:110px 90px}.k{font:600 30px Inter;letter-spacing:.14em;text-transform:uppercase;color:#E6B72B}
h1{font:700 76px/1.12 Lora,serif;margin:36px 0 70px}
.c{background:#fbf8f1;color:#0b1430;border-radius:28px;padding:56px 60px}
.c .l{font:600 26px Inter;letter-spacing:.12em;text-transform:uppercase;color:#9a7a1c}
.c .r{display:flex;justify-content:space-between;margin-top:30px;font:600 46px/1.2 Inter}
.c .r span:last-child{color:#c0392b}
.c p{margin-top:30px;font:400 32px/1.4 Inter;color:#3a4258}
.f{position:absolute;left:90px;right:90px;bottom:80px;font:500 28px Inter;color:rgba(255,255,255,.75);display:flex;justify-content:space-between}.f b{color:#fff}'''
html=f'''<!doctype html><meta charset=utf-8><style>{CSS}</style><div class=w><div class=k>Дневник · пишу робота сама</div><h1>Человек устаёт.<br>Машина — нет.</h1>
<div class=c><div class=l>Проверка, которую я заложила</div><div class=r><span>Аванс</span><span style='color:#2e7d32'>есть ✓</span></div><div class=r><span>Счёт-фактура</span><span>нет ✕</span></div><p>В конце квартала такое легко пропустить. Робот это подсветит.</p></div></div>
<div class=f><span><b>Юлия Плосконос</b></span><span>бухгалтер, который пишет код</span></div>'''
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350}); pg.set_content(html); pg.wait_for_timeout(300); pg.screenshot(path='threads01.png'); b.close()
