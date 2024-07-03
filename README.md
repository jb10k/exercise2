# exercise2

Скопировать репозиторий \
``` bash
git clone https://github.com/jb10k/exercise2.git
```
Запустить сборку и запуск командой \
``` bash
$ docker compose up -d
```
Проверка работоспобосности приложения встроена в код с помощью healthcheck.

После запуска прложения в браузере ввести `http://localhost:80` или `http://localhost:5000`. \
Либо в терминале ввести `curl http://localhost:80` или `curl http://localhost:5000`.
``` bash
$ curl localhost:80
Hello World!
```
