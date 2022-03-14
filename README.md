<a id = "anchor"></a>
# Тестування на Python
![logo](https://egorovegor.ru/wp-content/uploads/testirovanie-prilozhenij-python-s-pomoshhyu-pytest.jpg)
### План
1. [Що таке тестування](#t_1)
2. [Різновиди тестів](#t_2)
3. [Assert-тестування](#t_3)
4. [Тестування за допомогою модуля unittest](#t_4)
___
<a id = "t_1"></a>
### Що таке тестування 
Важко уявити сучасний програмний проект без тестування. При цьому тестування здійснюється практично на всіх етапах
розробки продукту: починаючи, безпосередньо, з процесу створення функцій, методів та класів тощо, коли пишуться unit-тести, та закінчуючи
функціональним та навантажувальним тестуванням вже готового, розгорнутого продукту.
### Навіщо треба писати тести?
+ Тести перевіряють працездатність коду та трохи вас заспокоюють. У тих випадках, для яких ви написали тести, можна бути впевненим, що код працює — якщо, 
звичайно, ви його нормально написали. 
+ Тести дозволяють перевіряти взаємодію старого та нового коду. Уявімо ситуацію. У вас є код, він працює. Прийшла людина, написав новий код, 
захотів використати шматочок старого. Щось кудись виніс, десь десь поправив. На випадок, якщо він зламав існуючу функціональність, добре мати тести, які теж зламаються. 
Інакше ви можете виявити це у продакшені в якийсь дуже неприємний момент.
+ Найчастіше тести - єдина зрозуміла документація до коду.
+ Також тести - економія вашого часу.
___
<a id = "t_2"></a>
### Різновиди тестів
+ Тестування __чорної скриньки__ - процес, коли тестувальнику нічого не відомо про те, що всередині. Він як звичайний користувач щось робить, не знаючи жодних 
особливостей реалізації.
+ Тестування __білої скриньки__ означає, що тестувальнику доступна будь-яка необхідна інформація, включаючи вихідний код. Ми в такій ситуації, коли пишемо тест 
на власний код.
+ Тестування __сірої скриньки__ – щось проміжне. Це коли вам відомі якісь деталі реалізації, але не вся.

Також процес тестування можна поділити на __ручний, напівавтоматичний та автоматичний__. 
+ __Ручне тестування__ робить людина. Допустимо, кнопочки в браузері натискає,дивиться, що в нього зламалося чи не зламалося. 
+ __Напівавтоматичне тестування__ – це коли тестувальник запускає тестові сценарії. Можна сказати, що ми з вами перебуваємо у такій ситуації, коли локально свої 
тести запускаємо та проганяємо. 
+ __Автоматичне тестування__ передбачає участі людини: тести повинні запускатися автоматично, а чи не руками.

Також тести можна розділити за рівнем деталізації. Тут їх прийнято ділити на юніт- та інтеграційні тести. 
Юніт-тести перевіряють роботу окремих компонентів системи, а інтеграційні перевіряють зв'язку деяких модулів. Іноді тут ще виділяють системні випробування, 
які перевіряють роботу всієї системи повністю. Але здається, що це скоріше великий варіант інтеграційних тестів.
___
<a id = "t_3"></a>
### Assert-тестування
Інструкції assert в Python – це булеві вирази, які перевіряють, чи є умова істинною (True). 
Вони визначають факти (затвердження) у програмі. Assertion — це перевірка, яку можна увімкнути, а потім вимкнути, завершивши тестування програми.
Assertions (затвердження) - це інструкції, які "затверджують" певний кейс у програмі. У Python вони виступають булевими виразами, які перевіряють, чи є умова істинною 
чи хибною. Якщо воно істинно, то програма нічого не робить і переходить до виконання наступного рядка коду.
Але якщо воно хибне, то програма зупиняється та повертає помилку.
Наступний синтаксис є базовою структурою інструкцій затвердження в Python.
```python
assert condition
```
Якщо потрібно додати повідомлення для виведення за помилкової умови, то синтаксис буде таким.
```python
assert condition, message
```
Це повідомлення дозволить краще зрозуміти, чому код не спрацював.
### Приклад assert
Якщо потрібно симулювати або виконати налагодження коду, щоб дізнатися, що саме відбувається на певному етапі, то затвердження в Python відмінно для цього підходять.
Саме інструмент налагодження зупиняє програму, щойно виникає якась помилка. Він також показує де саме вона сталася.
+ Інструкція assert приймає вираз та необов'язкове повідомлення;
+ Вона використовується для перевірки типів, значень аргументу та виведення функції;
+ А також для налагодження, оскільки зупиняє програму у разі помилки.
Ось приклад роботи тверджень у Python.
```python
def avg(ranks):
    assert len(ranks) != 0
    return round(sum(ranks)/len(ranks), 2)

ranks = [62, 65, 75]
print("Среднее значение:", avg(ranks))
```
У цьому прикладі необхідно, щоб користувач не залишав параметри порожніми. Якщо цього не зробити, з'явиться помилка Assertion Error. Ось приклад виводу:
```python
Среднее значение: 67.33
```
У цьому випадку параметри передані, тому функція повернула потрібний результат.
Тепер спробуймо нічого не передавати.
```python
def avg(ranks):
    assert len(ranks) != 0
    return round(sum(ranks)/len(ranks), 2)

ranks = []
print("Среднее значение:", avg(ranks))
```
Довжина масиву ranks виявилася 0, і python повернув помилку Assertion Error.
```python
Traceback (most recent call last):
  File "C:/Users/asd/AppData/Local/Programs/Python/Python38/wb.py", line 6, in <module>
    print("Среднее значение:", avg(ranks))
  File "C:/Users/asd/AppData/Local/Programs/Python/Python38/wb.py", line 2, in avg
    assert len(ranks) != 0
AssertionError
```
Винятки Assertion Error можна перехоплювати та обробляти як і будь-які інші винятки за допомогою try-except. Але якщо їх обробити неправильно, 
то програма зупиниться та поверне traceback.
Однак у прикладі вище вона повертає помилку з потрібним повідомленням. Її можна написати самостійно. Ось як це робиться.
```python
def avg(ranks):
    assert len(ranks) != 0, 'Список ranks не должен быть пустым'
    return round(sum(ranks)/len(ranks), 2)

ranks = []
print("Среднее значение:", avg(ranks))
```
Другим аргументом до assert у прикладі вище було передано повідомлення, яке пізніше з'явиться у виведенні.
```python
Traceback (most recent call last):
  File "C:/Users/asd/AppData/Local/Programs/Python/Python38/wb.py", line 6, in <module>
    print("Среднее значение:", avg(ranks))
  File "C:/Users/asd/AppData/Local/Programs/Python/Python38/wb.py", line 2, in avg
    assert len(ranks) != 0, 'Список ranks не должен быть пустым'
AssertionError: Список ranks не должен быть пустым
```
### Поширені помилки
Є два важливі моменти щодо тверджень у Python, про які потрібно пам'ятати.
+ Не варто використовувати assert для валідації даних, адже це призводить до появи проблем з безпекою та багів.
+ Важливо не писати такі твердження, які завжди будуть істинними.
### Ключові моменти assert у Python
1. Твердження (Assertion) - це умова або булевий вираз, який має бути істинним.
2. Інструкція assert приймає вираз та необов'язкове повідомлення.
3. Інструкція assert використовується для перевірки типів, значень аргументів та виведення функцій.
4. Це також інструмент для налагодження, адже він зупиняє програму з появою помилки.
5. Насамперед твердження використовуються для повідомлення розробників про помилки, що не відслідковуються. 
Вони не повинні повідомляти про умови помилок, таких як файл не був знайдений, де користувач може спробувати виправитися і повторити дії.
6. Твердження – це внутрішня перевірка для програми. Вони працюють за рахунок оголошення неможливих умов у коді. Якщо ці умови не проходять, то є баг.
___
<a id = "t_4"></a>
### Тестування за допомогою модуля unittest
У Python вбудований модуль unittest, який підтримує автоматизацію тестів, використання загального коду для налаштування та завершення тестів, об'єднання тестів 
у групи, а також дозволяє відокремлювати тести від фреймворку для виведення інформації.
Для автоматизації тестів, unittest підтримує деякі важливі концепції:
+ __Випробувальний стенд__ (_test fixture_) - виконується підготовка, необхідна виконання тестів і всі необхідні дії для очищення після виконання тестів. Це може 
містити, наприклад, створення тимчасових баз даних або запуск серверного процесу.
+ __Тестовий випадок__ (_test case_) – мінімальний блок тестування. Він перевіряє відповіді на різні набори даних. Модуль unittest надає базовий клас TestCase,
який можна використовувати для створення нових тестових випадків.
+ __Набір тестів__ (_test suite_) - кілька тестових випадків, наборів тестів або того й іншого. Він використовується для об'єднання тестів, які мають бути 
виконані разом.
+ __Виконавець тестів__ (_test runner_) - компонент, який керує виконанням тестів і надає користувачу результат. Виконавець може використовувати
графічний або текстовий інтерфейс абоповертатиь спеціальне значення, яке повідомляє про результати виконання тестів.
Ось короткий скрипт для тестування трьох методів рядків:
```python
import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # Проверим, что s.split не работает, если разделитель - не строка
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
```
Тестовий випадок створюється шляхом успадкування від unittest. TestCase. 3 окремих теста визначаються за допомогою методів, ім'я яких починається на test. 
Ця угода говорить виконавцю тестів, що методи є тестами.

Для того, щоб була можливість використовувати компоненти unittest (у тому числі і TestCase), на початку програми потрібно імпортувати модуль unittest стандартним чином.
При виборі імені класу спадкоємця від TestCase можете керуватися наступним правилом: [Ім'яТестованої Сутності] Tests. [Ім'я Тестованої Сутності] - це деяка логічна 
одиниця, тести для якої потрібно написати. Під час написання програм на Python намагайтеся дотримуватися PEP 8 — Style Guide for Python Code – це рекомендації щодо стильового оформлення 
коду.
Для того щоб метод класу виконувався як тест, необхідно, щоб він починався зі слова test. Незважаючи на те, що методи framework'а unittest написані не відповідно до 
PEP 8 (через ідейний він спадкоємець xUnit), ми все ж рекомендуємо дотримуватися правил стилю для Python скрізь, де це можливо. Тому імена тестів починатимемо з 
префіксу test_. Далі, під словом тест розумітимемо метод класу-спадкоємця від TestCase, який починається з префікса test_.

Суть кожного тесту - виклик assertEqual() для перевірки очікуваного результату; assertTrue() або assertFalse() для перевірки умов; assertRaises() для перевірки, 
чи метод породжує виняток. Ці методи використовуються замість звичайного assert для того, щоб виконавець тестів зміг узяти всі результати та оформити звіт.
Методи setUp() і tearDown() (які в даному простому випадку не потрібні) дозволяють визначати інструкції, що виконуються перед та після кожного тесту, відповідно.

Останні 2 рядки показують простий спосіб запуску тестів. unittest.main() надає інтерфейс командного рядка для тестування програми. Будучи запущеним з командного 
рядка, цей скрипт виводить звіт, подібний до цього:
```python
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
### Інтерфейс командного рядка
unittest може бути використаний з командного рядка для запуску модулів з тестами, класів або навіть окремих методів:
```python
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
```
Можна також вказувати шлях до файлу:
```python
python -m unittest tests/test_something.py
```
За допомогою прапорця -v можна отримати детальніший звіт:
```python
python -m unittest -v test_module
```
Для нашого прикладу докладний звіт буде таким:
```python
test_isupper (__main__.TestStringMethods) ... ok
test_split (__main__.TestStringMethods) ... ok
test_upper (__main__.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
__-b (--buffer)__ - виведення програми при провалі тесту буде показано, а не приховано, як звичайно.

__-c (--catch)__ - Ctrl+C під час виконання тесту очікує завершення поточного тесту та потім повідомляє результати на даний момент. 
Друге натискання Ctrl+C викликає звичайний виняток KeyboardInterrupt.

__-f (--failfast)__ - вихід після першого ж невдалого тесту.

__--locals (починаючи з Python 3.5)__ - показувати локальні змінні для тестів, що провалилися.
### Виявлення тестів
unittest підтримує просте виявлення тестів. Для сумісності з виявленням тестів, усі файли тестів повинні бути модулями
або пакетами, імпортованими з директорії верхнього рівня проекту.
Виявлення тестів реалізовано в TestLoader.discover(), але може бути використано з командного рядка:
```python
cd project_directory
python -m unittest discover
```
__-v (--verbose)__ - детальний вивід.

__-s (--start-directory)__ directory_name - директорія  початку виявлення тестів (поточна за замовчуванням).

__-p (--pattern) pattern__ - шаблон назви файлів з тестами (за замовчуванням test*.py).

__-t (--top-level-directory)__ directory_name - директорія верхнього рівня проекту (за замовчуванням рівна start-directory).
### Організація тестового коду

Базові блоки тестування це тестові випадки – прості випадки, які мають бути перевірені на коректність.
Тестовий випадок створюється шляхом успадкування від unittest. TestCase.
Тестуючий код має бути самостійним, тобто не залежати від інших тестів.
Найпростіший підклас TestCase може просто реалізовувати тестовий метод (метод, що починається з test). Вигаданий приклад:
```python
import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))
```
Зауважте, що для того, щоб перевірити щось, ми використовуємо один з assert\*() методів.

Тестів може бути багато, і частина коду налаштування може повторюватися. На щастя, ми можемо визначити код налаштування шляхом реалізації 
методу setUp(), який запускатиметься перед кожним тестом:
```python
import unittest

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
```
Ми також можемо визначити метод tearDown(), який запускатиметься після кожного тесту:
```python
import unittest

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
```
Можна розмістити всі тести в тому ж файлі, що і сама програма (такі як widgets.py), але розміщення тестів в окремому файлі 
(такі як test_widget.py) має багато переваг:
+ Модуль із тестом може бути запущений автономно з командного рядка.
+ Тестовий код може бути легко відокремлений від програми.
+ Менше спокуси змінити тести для відповідності програмному коду без видимої причини.
+ Тестовий код повинен змінюватися набагато рідше, ніж програма.
+ Протестований код може бути легше перероблений.
+ Тести для модулів на C повинні бути в окремих модулях, то чому ж не бути послідовним?
+ Якщо стратегія тестування змінюється, не потрібно змінити код програми.

__Усі методи класу TestCase можна розділити на три групи:__

+ методи, які використовуються при запуску тестів;
+ методи, які використовуються при безпосередньому написанні тестів (перевірка умов, повідомлення про помилки);
+ методи, що дозволяють збирати інформацію про тест.
Розглянемо методи цих груп докладніше. Зупинимося тільки на тих методах, які можуть бути корисні насамперед при розробці тестів. 
За більш детальною інформацією надсилаємо на сайт із офіційною [документацією](https://docs.python.org/3/library/unittest.html#test-cases).
### Методи, які використовуються при запуску тестів.
До цих методів відносяться:

__setUp()__

Метод викликається перед запуском тесту. Як правило, використовується для підготовки оточення для тестування.

__tearDown()__

Метод викликається після завершення роботи тесту. Використовується для "прибирання" за тестом.

__setUpClass()__

Метод діє лише на рівні класу, тобто. виконується перед запуском тестів класу. У цьому синтаксис вимагає наявність декоратора @classmethod.
```python
@classmethod
def setUpClass(cls):
    ...
```
__tearDownClass()__

Запускається після виконання всіх методів класу, що вимагає наявності декоратора @classmethod.
```python
@classmethod
def tearDownClass(cls):
    ...
```
__skipTest(reason)__

Цей метод може бути використаний для пропуску тесту, якщо це необхідно.

### Методи, які використовуються при безпосередньому написанні тестів (перевірка умов, повідомлення про помилки).
__TestCase клас надає набір assert-методів для перевірки та генерації помилок:__
|Приклад | Позначення|
|---|---|
| [assertEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual) |   a==b  |
| [assertNotEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual) | a!=b  |
| [assertTrue(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue) | bool(x) is True |
| [assertFalse(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse) |  bool(x) is False |
| [assertIs(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs) | 	a is b |
| [assertIsNot(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot) | a is not b |
| [assertIsNone(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone) | 	x is None |
| [assertIsNotNone(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone) | x is not None |
| [assertIn(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn) | 	a in b |
| [assertIsInstance(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance) | isinstance(a, b) |
| [assertNotIsInstance(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance) | 	not isinstance(a, b) |

__Assert'и для контролю викидів винятків та warning'ів:__
|Приклад | Значення|
|---|---|
|[assertRaises(exc, fun, *args, **kwds)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)***|Функція fun(*args, **kwds)*** викликає виняток exc|
|[assertRaisesRegex(exc, r, fun, *args, **kwds)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex)***|Функція fun(*args, **kwds)*** викликає виняток exc, повідомлення якого збігається з регулярним виразом r|
|[assertWarns(warn, fun, *args, **kwds](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns)***|Функція fun(*args, **kwds)*** видає повідомлення warn|
|[assertWarnsRegex(warn, r, fun, *args, **kwds)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex)***|Функція fun(*args, **kwds)*** видає повідомлення warn і воно збігається з регулярним виразом r|

__Assert'и для перевірки різних ситуацій:__
|Приклад | Значення|
|---|---|
|[assertAlmostEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual)|round(a-b, 7) == 0|
|[assertNotAlmostEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual)|round(a-b, 7) != 0|
|[assertGreater(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreater)|	a > b|
|[assertGreaterEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreaterEqual)|	a >= b|
|[assertLess(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLess)|	a < b|
|[assertLessEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLessEqual)|a <= b|
|[assertRegex(s, r)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegex)|	r.search(s)|
|[assertNotRegex(s, r)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegex)|not r.search(s)|
|[assertCountEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertCountEqual)|a та b мають однакові елементи (порядок неважливий)|


__Типозалежні assert'и, які використовуються при виклику assertEqual(). Наводяться на той випадок, якщо необхідно використовувати конкретний метод.__
|Приклад | Значення|
|---|---|
|[assertMultiLineEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual)|рядки (strings)|
|[assertSequenceEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual)|посідовності (sequences)|
|[assertListEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual)|списки (lists)|
|[assertTupleEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual)|кортежі (tuplse)|
|[assertSetEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSetEqual)|множини або незмінні множини (frozensets)|
|[assertDictEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual)|словники (dicts)|

__Додатково хотілося б відзначити метод fail().__
__fail(msg=None)__
Цей метод сигналізує у тому, що сталася помилка в тесті.
___
### Методи, що дозволяють збирати інформацію про тест
__countTestCases()__
Повертає кількість тестів в об'єкті класу спадкоємця від TestCase.
__id()__
Повертає рядковий ідентифікатор тесту. Як правило, це повне ім'я методу, що включає ім'я модуля та ім'я класу.
__shortDescription()__
Повертає опис тесту, який є першим рядком docstring'а методу, якщо його немає, то повертає None.
Розширимо код нашого тестового проекту методів рядків , щоб показати деякі з можливостей, які надає клас TestCase.
```python
import unittest


class TestStringMethods(unittest.TestCase):
    """Methods tests"""

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for test"""
        print("Tear down for [" + self.shortDescription() + "]")
        print("")

    def test_upper(self):
        """Upper operation test"""
        print("id: " + self.id())
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """Isupper operation test"""
        print("id: " + self.id())
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """Split operation test"""
        print("id: " + self.id())
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Проверим, что s.split не работает, если разделитель - не строка
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()

```
Запустимо цей модуль у командному рядку:
```python
>python -m unittest -v utest_calc.py
```
Отримаємо наступний результат:
```python
setUpClass
==========
test_isupper (1.TestStringMethods)
Isupper operation test ... Set up for [Isupper operation test]
id: 1.TestStringMethods.test_isupper
Tear down for [Isupper operation test]

ok
test_split (1.TestStringMethods)
Split operation test ... Set up for [Split operation test]
id: 1.TestStringMethods.test_split
Tear down for [Split operation test]

ok
test_upper (1.TestStringMethods)
Upper operation test ... Set up for [Upper operation test]
id: 1.TestStringMethods.test_upper
Tear down for [Upper operation test]

ok
==========
tearDownClass

----------------------------------------------------------------------
Ran 3 tests in 0.004s

OK
```
Як видно з прикладу, спочатку було запущено метод setUpClass(), потім послідовно (в алфавітному порядку) було виконано тести, перед запуском кожного тесту виконувався метод setUp(), після закінчення – tearDown(). Кожен метод містить docstring як коментар у першому рядку. Для доступу до цього опису використовувався метод shortDescription(). У тілі тесту є рядок, що друкує ідентифікатор, що отримується за допомогою функції id().




[Вгору](#anchor)
