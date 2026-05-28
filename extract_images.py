#!/usr/bin/env python3
"""
Извлекает base64-картинки из HTML, сохраняет в папку images/,
заменяет inline-data на file-ссылки — HTML становится лёгким.
"""
import re
import base64
import os

SRC = '/Users/cocame/AI_Projects/index_final.html'
OUT = '/Users/cocame/AI_Projects/index.html'
IMG_DIR = '/Users/cocame/AI_Projects/images'

os.makedirs(IMG_DIR, exist_ok=True)

with open(SRC, 'r', encoding='utf-8') as f:
    content = f.read()

counter = [0]

NAMES = {
    0: 'hero-bg',
    1: 'logo',
    2: 'hue',
    3: 'hoian',
    4: 'bana',
    5: 'danang-city',
    6: 'kalmar',
    7: 'springs',
    8: 'cham',
    9: 'vinwonders',
    10: 'surf',
    11: 'sea',
}

def replace_match(m):
    idx = counter[0]
    full = m.group(0)
    mime_match = re.match(r'data:([^;]+);base64,([A-Za-z0-9+/=]+)', full)
    mime = mime_match.group(1)
    data = mime_match.group(2)
    ext = mime.split('/')[-1].replace('jpeg', 'jpg')
    name = NAMES.get(idx, f'img-{idx}')
    filename = f'{name}.{ext}'
    path = os.path.join(IMG_DIR, filename)
    raw = base64.b64decode(data + '==')
    with open(path, 'wb') as f:
        f.write(raw)
    print(f'  [{idx}] {filename} ({len(raw)//1024} KB)')
    counter[0] += 1
    return f'images/{filename}'

pattern = r'data:[^;]+;base64,[A-Za-z0-9+/=]+'
result = re.sub(pattern, replace_match, content)

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(result)

orig_size = os.path.getsize(SRC)
new_size = os.path.getsize(OUT)
print(f'\nOriginal: {orig_size//1024} KB → New HTML: {new_size//1024} KB')
print(f'Images saved to: {IMG_DIR}')
