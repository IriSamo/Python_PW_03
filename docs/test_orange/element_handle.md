
# `element_handle() -> Optional[ElementHandle]`

### Назначение

Возвращает низкоуровневый объект `ElementHandle`, представляющий DOM-элемент.
Позволяет выполнять:

* произвольные JS-выражения (`evaluate`)
* доступ к реальному layout (`getBoundingClientRect`)
* взаимодействие с элементом напрямую (`click`, `hover`, `scroll_into_view_if_needed`)

### Сигнатура

```python
element_handle() -> Optional[ElementHandle]
```

### Пример использования

```python
sidepanel = page.get_by_role("navigation", name="Sidepanel")
handle = sidepanel.element_handle()

if handle:
    size = handle.evaluate("el => ({width: el.getBoundingClientRect().width, height: el.getBoundingClientRect().height})")
    print(size)
```

### Особенности

* Может вернуть `None`, если элемент отсутствует в DOM.
* Полезен для `wait_for_function` или низкоуровневых операций.
* Необходимо проверять, что элемент всё ещё существует, иначе `ElementHandle` станет недействительным.