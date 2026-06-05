import urllib.request, urllib.parse, os, time

os.makedirs('imgs', exist_ok=True)

# (filename, key, color)  -- color with spaces is URL-encoded automatically
IMAGES = [
    # iPhone 17 - use 16 as fallback if new
    ('iphone17pro.png',   'iPhone18,1', 'Black Titanium'),
    ('iphone17.png',      'iPhone18,3', 'Black'),
    # iPhone 16
    ('iphone16promax.png','iPhone17,2', 'Black Titanium'),
    ('iphone16pro.png',   'iPhone17,1', 'Black Titanium'),
    ('iphone16.png',      'iPhone17,3', 'White'),
    # iPhone 15
    ('iphone15promax.png','iPhone16,2', 'Black Titanium'),
    ('iphone15pro.png',   'iPhone16,1', 'Black Titanium'),
    ('iphone15.png',      'iPhone15,4', 'Black'),
    # iPhone 14
    ('iphone14pro.png',   'iPhone15,2', 'Silver'),
    ('iphone14.png',      'iPhone14,7', 'Starlight'),
    # iPhone 13-11
    ('iphone13pro.png',   'iPhone14,2', 'Silver'),
    ('iphone13.png',      'iPhone14,5', 'Midnight'),
    ('iphone12pro.png',   'iPhone13,3', 'Silver'),
    ('iphone12.png',      'iPhone13,2', 'White'),
    ('iphone11.png',      'iPhone12,1', 'White'),
    ('iphonexr.png',      'iPhone11,8', 'White'),
    # Watch
    ('watch10.png',       'Watch7,1',   '0'),
    ('watchultra.png',    'Watch7,3',   '0'),
    ('watch7.png',        'Watch6,6',   'Midnight'),
    ('watch3.png',        'Watch3,2',   '0'),
    # AirPods
    ('airpods4.png',      'AirPods2,1', '0'),
    ('airpodspro.png',    'AirPodsPro1,1','0'),
    ('airpodsmax.png',    'AirPodsMax,1','0'),
    # iPad & Mac
    ('ipadmini6.png',     'iPad14,1',   'Starlight'),
    ('macbookpro14.png',  'Mac15,7',    'Silver'),
]

BASE = 'https://img.appledb.dev/device@256'

ok, fail = 0, 0
for fname, key, color in IMAGES:
    color_enc = urllib.parse.quote(color)
    url = f'{BASE}/{key}/{color_enc}.png'
    path = f'imgs/{fname}'
    if os.path.exists(path):
        print(f'SKIP {fname} (already exists)')
        ok += 1
        continue
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
        with open(path, 'wb') as f:
            f.write(data)
        print(f'OK  {fname} ({len(data)//1024}KB)')
        ok += 1
    except Exception as e:
        print(f'ERR {fname}: {e}')
        fail += 1
    time.sleep(0.2)

print(f'\nДонайт: {ok} OK, {fail} ошибок')
if fail == 0:
    print('Всё скачано! Загрузи папку imgs/ на GitHub в store-bot')
else:
    print('Некоторые не скачались - но это не критично, всё равно загружай imgs/ на GitHub')
