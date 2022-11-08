# pytest_example

<a id="markdown-описание" name="Предварительные настройки."></a>

## Предварительные настройки.

Подготовить виртуальное окружение Python.

```
$ python -m venv venv
```

Активировать виртуальное окружение Python.

```
$ .\venv\Scrypt\activate
```

Установить зависимости.

```
$ pip install -r requirements.txt
```

<a id="markdown-описание" name="Запуск тестов."></a>

## Запуск тестов.

Все эллементы коллекции.

```
$ py.test --browser ${browser: default = chrome} --base_url ${base_url: default = http://localhost/addressbook/} --password ${password} test/* 
```

