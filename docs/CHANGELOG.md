# Changelog

Все значимые изменения в проекте `geometric_lib` документируются в этом файле.

Формат основан на [Keep a Changelog](https://keepachangelog.com/ru/1.1.0/),
версионирование — по [Semantic Versioning](https://semver.org/lang/ru/).

## [Unreleased]

### Added
- Юнит-тесты для круга (`tests/test_circle.py`).
- Юнит-тесты для прямоугольника (`tests/test_rectangle.py`).
- Юнит-тесты для квадрата (`tests/test_square.py`).
- Юнит-тесты для треугольника (`tests/test_triangle.py`).
- Обновлена документация (`docs/`).

### Changed
- Реструктурирован проект: фигуры вынесены в пакет `figures/`,
  тесты — в пакет `tests/`.

### Fixed
- (пока нет)

---

## [0.1.0] — 2026-09-29

Первая версия библиотеки: реализованы фигуры и подготовлена
инфраструктура для тестирования.

### Added
- `figures/rectangle.py` — площадь и периметр прямоугольника.
- `figures/triangle.py` — площадь и периметр треугольника.
- `figures/circle.py` — площадь и периметр круга (существовал ранее).
- `figures/square.py` — площадь и периметр квадрата (существовал ранее).
- `.gitignore` — исключены `__pycache__/`, `*.pyc`, настройки IDE.
- `docs/README.md` — базовая документация.

### Changed
- Проект переструктурирован: все фигуры перенесены в пакет `figures/`
  (коммит `4b7d08e`).

---

## Соответствие коммитам

| Хэш | Сообщение | Что сделано |
|---|---|---|
| `2702fd6` | Updated_tests | Обновлены тесты |
| `86b372a` | Updated_docs | Обновлена документация |
| `58fa23b` | Added_tests_circle_and_triangle | Добавлены тесты для круга и треугольника |
| `7247a0f` | Added_tests_rectangle_and_square | Добавлены тесты для прямоугольника и квадрата |
| `9738239` | Added_gitignore | Добавлен `.gitignore` |
| `4b7d08e` | Changed_project_structure | Фигуры вынесены в `figures/` |
| `11de6e2` | Added_rectangle | Добавлен файл `rectangle.py` |
| `e3b2ea8` | Added_triangle | Добавлен файл `triangle.py` |
| `74046bb` | (initial) | Начальный коммит |