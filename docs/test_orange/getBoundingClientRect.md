
# `getBoundingClientRect()`

### Назначение

Метод DOM-элемента, возвращает его текущую **геометрию на странице**:

* `x`, `y` — координаты относительно viewport
* `width`, `height` — размеры элемента
* `top`, `right`, `bottom`, `left` — позиции границ

### Пример использования в Playwright

```python
handle = sidepanel.element_handle()
rect = handle.evaluate("el => el.getBoundingClientRect()")
print(rect)
# {
#   'x': 0, 'y': 0, 'width': 256, 'height': 720,
#   'top': 0, 'right': 256, 'bottom': 720, 'left': 0
# }
```
