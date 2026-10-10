# vpluse-site

Статические файлы сайта ВПЛЮСЕ (vpluse.pro) для Tilda.

- `assets/` — картинки, стили (`vpx.min.css`) и скрипт (`vpx.min.js`), раздаются через jsDelivr:
  `https://cdn.jsdelivr.net/gh/vplusepro-art/vpluse-site@<коммит>/assets/...`
- `pages/` — код блоков T123 для каждой страницы Tilda (адрес и SEO указаны в комментарии в начале файла).

Страницы ссылаются на файлы по хешу коммита, поэтому CDN сразу отдаёт нужную версию.
