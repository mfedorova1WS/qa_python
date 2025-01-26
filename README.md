## Реализованные тесты

### Класс TestBooksCollector

#### Метод test_add_new_book_add_two_books
Проверяет добавление двух книг в коллекцию и проверяет, что количество книг в коллекции равно двум.

#### Метод test_favorites_is_empty_list_by_default
Проверяет, что список избранных книг изначально является пустым списком.

#### Метод test_set_book_genre_genre_success
Проверяет успешность установки жанра для книги.

#### Метод test_set_book_genre_invalid_genre
Проверяет обработку попытки установить неверный жанр для книги.

#### Метод test_get_book_genre_existing_book
Проверяет получение жанра для существующей книги.

#### Метод test_get_books_with_specific_genre_no_such_genre
Проверяет возврат пустого списка, если указан несуществующий жанр.

#### Метод test_get_books_genre_filled
Проверяет правильность возвращения словаря жанров книг.

#### Метод test_get_books_for_children_all_allowed
Проверяет возвращение всех книг, подходящих для детей.

#### Метод test_add_book_in_favorites_successful
Проверяет успешное добавление книги в избранное.

#### Метод test_delete_book_from_favorites_successful
Проверяет успешное удаление книги из избранного.


## Как запустить тесты
Для запуска тестов необходимо выполните следующую команду в корневой директории проекта:
pytest -v tests.py
