"""Build ../index.html: inline the JSON data files into template.html (run from anywhere)."""
import json, pathlib

src = pathlib.Path(__file__).resolve().parent
page = (src / 'template.html').read_text(encoding='utf-8')
for name in ['sets', 'tests', 'lessons']:
    data = json.loads((src / (name + '.json')).read_text(encoding='utf-8'))
    page = page.replace('/*' + name.upper() + '*/', json.dumps(data, ensure_ascii=False, separators=(',', ':')), 1)
(src.parent / 'index.html').write_text(page, encoding='utf-8')
print('index.html', len(page.encode()), 'bytes')
