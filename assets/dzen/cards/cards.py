from playwright.sync_api import sync_playwright
CARDS={
'c19':('Чек-лист · перед проверкой учёта','Три вопроса, с которых я начинаю',[('1','Что именно тревожит?','Деньги, долги, налоги, документы'),('2','За какой период?','Квартал, год, «с ухода прошлого бухгалтера»'),('3','Какой результат нужен?','Спокойствие, проверка, передача учёта, ответ на требование')],'Потом смотрю в 1С: расчёты с контрагентами · НДС · закрытие месяца'),
'c22':('Мой чек-лист · 1С:Бухгалтерия 3.0','5 отчётов перед декларацией по НДС',[('1','Экспресс-проверка учёта','Отчёты → Анализ учёта → Экспресс-проверка'),('2','Анализ учёта по НДС','Откуда каждая сумма в декларации'),('3','ОСВ по счёту 19','Старые остатки — забытые вычеты'),('4','ОСВ 68.02 против декларации','Оборот за квартал = итог декларации'),('5','Сверка с контрагентами','Расхождения по суммам и датам')],'Это мой рабочий чек-лист, а не требование закона'),
}
CSS='''*{margin:0;box-sizing:border-box}body{width:1440px;height:731px;background:#0b1430;font-family:Inter,sans-serif;color:#fff;overflow:hidden}
.w{padding:56px 80px}.k{font:600 22px Inter;letter-spacing:.16em;text-transform:uppercase;color:#E6B72B}
h1{font:700 48px/1.15 Lora,serif;margin:14px 0 30px}
.r{display:flex;align-items:flex-start;gap:24px;margin-bottom:%dpx}.n{flex:0 0 56px;height:56px;border-radius:50%%;background:#E6B72B;color:#0b1430;font:700 28px Inter;display:flex;align-items:center;justify-content:center}
.t b{display:block;font:600 30px Inter}.t span{font:400 22px Inter;color:rgba(255,255,255,.75)}
.f{position:absolute;left:80px;right:80px;bottom:40px;display:flex;justify-content:space-between;font:500 20px Inter;color:rgba(255,255,255,.7);border-top:2px solid rgba(230,183,43,.6);padding-top:16px}.f b{color:#fff}'''
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1440,'height':731})
    for k,(kick,h,rows,foot) in CARDS.items():
        gap=26 if len(rows)<=3 else 12
        rs=''.join(f'<div class=r><div class=n>{n}</div><div class=t><b>{t}</b><span>{d}</span></div></div>' for n,t,d in rows)
        pg.set_content(f'<!doctype html><meta charset=utf-8><style>{CSS%gap}</style><div class=w><div class=k>{kick}</div><h1>{h}</h1>{rs}</div><div class=f><span>{foot}</span><span><b>Юлия Плосконос</b> · vpluse.pro</span></div>')
        pg.wait_for_timeout(300); pg.screenshot(path=f'{k}.png')
    b.close()
