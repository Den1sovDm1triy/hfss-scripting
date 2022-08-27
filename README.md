# HFSS-Scripting
## Задача дифракции на сфере. Моделирование в Ansys HFSS с помощью сриптов на Python

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

В этом проекте мы смоделиуем распространенную задачу падения плоской электромагнитной волны на проводящую сферу. Типовой порядок создания проекта в HFSS Design выглядит следующим образом.

- Создается геометрия для анализа. В нашем случае это сфера
- На геометрию накладываются свойства материалов. В нашем случае мы сделаем сферу идеально проводящей
- Определяем границу моделирования
- Задаем частоту анализа
- Создаем источник электромагнитной волны в проекте
- Запускаем проект на расчет
- Анализируем результаты расчета
- ✨Magic ✨

## Installation | Установка ПО
### скачивание программного обеспечения и начало работы

- Скачать и установить программное обеспечение для моделирования можно с оффициального сайта [Ansys.com](https://www.ansys.com/academic/students/ansys-electronics-desktop-student).
- Возможно в РФ для доступа к сайту вам придется использовать VPN. Либо вы можете воспользоваться официальным сайтом партнера [Cae-expert.ru](https://cae-expert.ru/product/ansys-hfss) 

```sh
cd dillinger
npm i
node app
```

После того, как пакет Ansys Electronics Desktop установлен, его можно запустить и попасть в стандартный рабочий стол, на котором можно выбрать вид Design'a для дальнейшего моделирования. Ниже показано как выглядит софт при первом запуске. Чтобы создать проект для высокочастотной симуляции (HFSS Design) кликаем ПКМ по проекту Project и выбираем Insert HFSS Design.

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_1.png" alt="Figure 1. Ansys Electronics Desktop (HFSS Design)"/>
</p>

После того как открывается окно 3D-Моделера можно создавать различную геометрию для моделирования. 

## Начало работы

Давайте создадим простую сферу, диаметром 3 сантиметра. Для этого из вкладки Draw выбираем Sphere и кликаем в центр системы координат в окне 3Д моделирования, вторым кликам в произвольном месте системы координам создаем сферу произвольного радиуса.

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_2.png" alt="Figure 2. Ansys Electronics Desktop (HFSS Design)"/>
</p>

Чтобы изменить радиус сферы, выберем операцию CreateSphere и изменим ее свойство Radius, установив значение равным 15 мм.

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_3.png" alt="Figure 3. Ansys Electronics Desktop (HFSS Design)"/>
</p>

Теперь на сферу нужно назначить свойство проводника. Это можно сделать двумя способами:
- назначить материал сфера (клик ПКМ по сфере и выбрать Assign Material)
- либо назначить граничное условие идеального проводника (клик ПКМ по сфере и выбрать Assign Boundary - Perfect E и в появившемся диалоговом окне жмем "ОК")

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_4.png" alt="Figure 4. Ansys Electronics Desktop (HFSS Design)"/>
</p>

На этом этап с созданием геометрии можно считать завершенным. Чтобы назначить границу моделирования, мы кликаем ПКМ в дереве проекта по Model - Create Open Region. В появившемся диалоговом окне устанавливаем частоту 10 ГГц (это значит что под указанную частоту будет создана область анализа нужного размера).

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_5.png" alt="Figure 5. Ansys Electronics Desktop (HFSS Design)"/>
</p>

шаг 1, ПКМ по Model - Create Open Region.

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_6.png" alt="Figure 6. Ansys Electronics Desktop (HFSS Design)"/>
</p>

шаг 2, устанавливаем частоту 10 ГГц и нажимаем ОК

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_7.png" alt="Figure 7. Ansys Electronics Desktop (HFSS Design)"/>
</p>

После этого в проекте определяется область моделирования, обозначенная красным кубом вокруг сферы и мы можем переходить к следующему этаму. Кликаем ПКМ по вкладке Analysis и выбираем Add Solution Setup - Advanced... Так мы попадаем в меню настройки точности расчетом и частоты анализа:

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_8.png" alt="Figure 8. Ansys Electronics Desktop (HFSS Design)"/>
</p>

В качестве частоты анализа задаем значение 10 ГГц и нажимаем "ОК".

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_9.png" alt="Figure 9. Ansys Electronics Desktop (HFSS Design)"/>
</p>

В качестве истчника в проекте создадим плоскую электромагнитную волну. Для этогов дереве проекта кликаем ПКМ по Excitation - Assign - Incident Wave - Plane Wave.

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_10.png" alt="Figure 10. Ansys Electronics Desktop (HFSS Design)"/>
</p>

Так как нам в целом не важно, с какого направления должна падать ЭМ волна на сферу, то в появляющихся диалоговых окнах мы просто нажимаем пару раз Next и один раз Finish. После чего при нажатии на созданный источник (Excitation) мы увидим в окне 3D-моделера пару векторов. Вектор E0 показывает плоскость распространения электрической части ЭМ волны, а вектор k показывает направление распространения.

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_11.png" alt="Figure 11. Ansys Electronics Desktop (HFSS Design)"/>
</p>

Все основные этапы анализа проекта завершены и мы переходим к валидации проекта и запуска его на расчет. Чтобы это сделать мы просто переходим во вкладку Simulation и нажимаем последовательно, сначала Validate, а затем - Analyze All.

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_12.png" alt="Figure 12. Ansys Electronics Desktop (HFSS Design)"/>
</p>

Расчеты для такого маленького проекта занимают считанные секунды. После завершения симуляции мы можем построить диаграмму рассеяния ЭМ поля на сфере. Чтобы это сделать последовательно выбираем Results - Far Field Report - 3D Polar. В появившемся диалоговом окне можно выбрать единицы измерения, или построить график в dB.

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_13.png" alt="Figure 13. Ansys Electronics Desktop (HFSS Design)"/>
</p>

А для построения визуализации поля, нужно вернуться в окно 3D-моделера, выбрать любую плокость, кликнуть ПКМ в окне моделера и выбрать Plot Field-E-MagE.

<p align="center">
  <img src="https://github.com/Den1sovDm1triy/hfss-scripting/blob/main/Screenshots/Fig_14.png" alt="Figure 14. Ansys Electronics Desktop (HFSS Design)"/>
</p>

Если у вас будет желание сравнить результаты моделирования с результатами расчетов, которые приводятся в классических учебниках по электродинамике, то рекомендую сходить в интернет с запросом "Дифракция на сфере. Первый проект в HFSS".

## Дополнительная информация

Dillinger uses a number of open source projects to work properly:

- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
