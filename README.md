# 3_bars
## Описание
По данным из json-файла скрипт рассчитывает:

* самый большой бар;
* самый маленький бар;
* самый близкий бар

## Использование
Скрипт принимает на вход:

* путь до json-файла;
* долготу;
* широту

```sh
$ python3.5 ./bars.py ./bars.json 37.685499 55.765914
```

Указываются либо все перечисленные параметры, либо не указывается ни один дополнительный параметр. При некорректном составе параметров выводится сообщение об ошибке:
```sh
Error: incorrect parameters are transferred.
It is necessary to transfer a file name, longitude and latitude,
or not to transfer anything.
```
## Пример
```sh
$ python3.5 ./bars.py ./bars.json 37.685499 55.765914
Smallest bar (seats count): БАР. СОКИ (0)
Biggest bar (seats count): Ночной клуб «Орфей» (1000):
Closest bar:  Хилл Фиш
```