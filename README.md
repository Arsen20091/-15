# BST: основные операции

Реализованы:

- `TreeNode` для узла дерева
- `BinarySearchTree.insert(key, value)`
- `BinarySearchTree.search(key)`
- `BinarySearchTree.delete(key)`
- `BinarySearchTree.height()`
- `BinarySearchTree.is_balanced()`

## Требования

- Python `3.8+`
- `uv` (рекомендуется для запуска)

## Запуск демо

```bash
uv run python demo.py
```

Если `uv` не установлен, можно запустить напрямую:

```bash
python3 demo.py
```

## Проверка методов (тесты)

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
```

Fallback без `uv`:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Поведение методов

- `insert`: добавляет новую пару ключ/значение; при повторном ключе обновляет значение.
- `search`: возвращает значение по ключу или `None`, если ключ не найден.
- `delete`: удаляет узел по ключу (лист, узел с одним ребенком, узел с двумя детьми).
- `height`: возвращает высоту в узлах (`0` для пустого дерева, `1` для дерева из одного узла).
- `is_balanced`: проверяет, что для каждого узла разница высот левого и правого поддерева не больше `1`.
