import re

file = open('25_easy.txt', 'r', encoding="utf8")
cnt = 1   # для записи номеров строк
for line in file:
    if len(re.findall(r'\d[_-]Максим\sСавелий[_-]\d', line)) > 0:
        print(cnt, len(line) + len(re.findall(r'\d[_-]Максим\sСавелий[_-]\d', line)))
    cnt += 1
