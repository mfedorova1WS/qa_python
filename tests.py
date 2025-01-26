from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_favorites_is_empty_list_by_default(self):
        books_collector = BooksCollector()
        assert books_collector.favorites == []

    def test_set_book_genre_genre_success(self, books_collector):
        book_name = "Властелин колец"
        genre = "Фантастика"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.books_genre[book_name] == genre

    def test_set_book_genre_invalid_genre(self, books_collector):
        book_name = "Властелин колец"
        invalid_genre = "Несуществующий жанр"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, invalid_genre)
        assert books_collector.books_genre[book_name] == ''

    def test_get_book_genre_existing_book(self, books_collector):
        book_name = "Властелин колец"
        genre = "Фантастика"
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_no_such_genre(self, books_collector):
        result = books_collector.get_books_with_specific_genre('NonExistentGenre')
        assert result == []

    def test_get_books_genre_filled(self, books_collector):
        books_collector.add_new_book("Book1")
        books_collector.add_new_book("Book2")
        books_collector.set_book_genre("Book1", "Фантастика")
        books_collector.set_book_genre("Book2", "Ужасы")
        expected_result = {"Book1": "Фантастика", "Book2": "Ужасы"}
        result = books_collector.get_books_genre()
        assert result == expected_result

    def test_get_books_for_children_all_allowed(self, books_collector):
        books_collector.add_new_book("Book1")
        books_collector.add_new_book("Book2")
        books_collector.set_book_genre("Book1", "Фантастика")
        books_collector.set_book_genre("Book2", "Комедии")
        result = books_collector.get_books_for_children()
        assert result == ["Book1", "Book2"]

    def test_add_book_in_favorites_successful(self,books_collector):
        books_collector.add_new_book("Book1")
        books_collector.add_book_in_favorites("Book1")
        favorites = books_collector.get_list_of_favorites_books()
        assert favorites == ["Book1"]

    def test_delete_book_from_favorites_successful(self, books_collector):
        books_collector.add_new_book("Book1")
        books_collector.add_book_in_favorites("Book1")
        books_collector.delete_book_from_favorites("Book1")
        favorites = books_collector.get_list_of_favorites_books()
        assert favorites == []

    def test_get_list_of_favorites_books_after_adding_two_books(self, books_collector):
        books_collector.add_new_book("Book1")
        books_collector.add_new_book("Book2")
        books_collector.add_book_in_favorites("Book1")
        books_collector.add_book_in_favorites("Book2")
        favorites = books_collector.get_list_of_favorites_books()
        assert favorites == ["Book1", "Book2"]

