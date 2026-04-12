
# `element_size(locator: Locator) -> dict[str, int]`

## Назначение

Функция `element_size()` возвращает фактические размеры элемента на странице(ширину и высоту) на основе его геометрии в layout браузера.

Используется для:

- проверки размеров UI-элементов
- сравнения размеров до и после действий
- ожидания изменения layout
- диагностики поведения интерфейса
- тестирования анимаций и адаптивных элементов

---

## Сигнатура функции

```python
def element_size(locator: Locator) -> dict[str, int]:
````

## Реализация

```python
def element_size(locator: Locator) -> dict[str, int]:
    box = locator.bounding_box()

    if box is None:
        raise RuntimeError("Element has no bounding box")

    return {
        "width": int(box["width"]),
        "height": int(box["height"]),
    }
```

## Параметры

### locator — `Locator`

Playwright `Locator`, указывающий на элемент, размеры которого необходимо получить.

Пример:

```python
sidepanel = page.get_by_role("navigation", name="Sidepanel")

size = element_size(sidepanel)
```

## Возвращаемое значение

Возвращает словарь:

```python
dict[str, int]
```

Структура:

```python
{
    "width": int,
    "height": int
}
```

Пример:

```python
{
    "width": 256,
    "height": 720
}
```

Значения возвращаются в **целых пикселях**.

---

## Как работает функция

Функция использует метод:

```python
locator.bounding_box()
```

Этот метод возвращает геометрические параметры элемента:

```python
{
    "x": float,
    "y": float,
    "width": float,
    "height": float
}
```

Фактически используется механизм браузера, аналогичный:

```javascript
element.getBoundingClientRect()
```

После получения значений:

```python
int(box["width"])
int(box["height"])
```

дробная часть отбрасывается.

Пример:

```
83.1875 → 83
```

Это делает сравнения размеров стабильнее.

---

## Исключения

### RuntimeError

Выбрасывается, если:

```python
box is None
```

Это возможно, если элемент:

* скрыт (`display: none`)
* не отрисован
* находится вне viewport
* отсутствует в DOM

Ошибка:

```
RuntimeError: Element has no bounding box
```

---

## Примеры использования

### Получение размеров элемента

```python
size = element_size(sidepanel)

assert size["width"] == 256
assert size["height"] == 720
```

### Сравнение размеров до и после действия

```python
size_before = element_size(sidepanel)

toggle_button.click()

size_after = element_size(sidepanel)

assert size_after["width"] < size_before["width"]
```

### Проверка изменения layout

```python
sidepanel.get_by_role("button").click()

size = element_size(sidepanel)

assert size["width"] == 83
```

---

## Преимущества использования bounding_box()

По сравнению с `evaluate()`:

```python
locator.evaluate(
    "el => ({width: el.clientWidth, height: el.clientHeight})"
)
```

метод `bounding_box()`:

### Быстрее

Не выполняется JavaScript-код.

### Надёжнее

Меньше зависит от состояния DOM и JS-контекста.

### Точнее

Возвращает реальные размеры элемента в layout браузера.

---

## Ограничения

Функция работает только если элемент:

* видим
* имеет layout
* присутствует в DOM

Если элемент скрыт:

```css
display: none;
```

или не отрисован, `bounding_box()` вернёт:

```python
None
```

---

## Рекомендации по использованию

Использовать функцию, когда:

* требуется проверить реальные размеры элемента
* используются анимации
* layout вычисляется динамически
* CSS-свойства нестабильны
* требуется точная геометрия элемента

---

## Когда лучше использовать другие методы

В некоторых случаях проверка размеров не является оптимальным решением.

Рекомендуется использовать:


### Проверку CSS-класса

Если UI имеет состояние:

```python
expect(sidepanel).to_have_class("collapsed")
```

Это быстрее и стабильнее.


### Проверку CSS-свойств

Если важно значение стиля:

```python
expect(sidepanel).to_have_css("width", "83px")
```

---

## Связанные методы Playwright

* `locator.bounding_box()`
* `locator.evaluate()`
* `locator.wait_for()`
* `page.wait_for_function()`
* `expect(locator).to_have_css()`

---

## Итог

Функция `element_size()` — это вспомогательная утилита для получения
**фактических размеров элемента**, основанных на его геометрии в layout браузера.

Используется в ситуациях, когда:

* требуется точная проверка размеров
* CSS или state-проверки недостаточны
* необходимо работать с динамическими элементами

```