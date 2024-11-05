from data import Book
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books(self):
        books = [Book("John Wick","To Kill a Mockingbird"),
                 Book("John Wick", "Fancy Nancy"),
                 Book("John Wick", "Diary of a Wimpy Kid")]
        expected = ["Diary of a Wimpy Kid","Fancy Nancy","To Kill a Mockingbird"]
        result = lab6.selection_sort_books(books)
        sorted = [book.title for book in books]
        self.assertEqual(expected, sorted)

    def test_selection_sort_books2(self):
        books = []
        expected = []
        result = lab6.selection_sort_books(books)
        sorted = [book.title for book in books]
        self.assertEqual(expected, sorted)


    # Part 2
    def test_swap_case(self):
        word =  "Hello"
        expected = "hELLO"
        result = lab6.swap_case(word)
        self.assertEqual(expected, result)

    def test_swap_case2(self):
        word =  "el!lo"
        expected = "EL!LO"
        result = lab6.swap_case(word)
        self.assertEqual(expected, result)

    # Part 3
    def test_str_translate(self):
        word = "pinkie"
        old = "i"
        new = "y"
        expected = "pynkye"
        result = lab6.str_translate(word, old, new)
        self.assertEqual(result, expected)

    def test_str_translate2(self):
        word = "calculus"
        old = "l"
        new = "z"
        expected = "cazcuzus"
        result = lab6.str_translate(word, old, new)
        self.assertEqual(result, expected)

    # Part 4
    def test_histogram(self):
        input_string = "pink blue blue"
        expected = {"pink": 1, "blue": 2}
        result = lab6.histogram(input_string)
        self.assertEqual(result, expected)

    def test_histogram2(self):
        input_string = ""
        expected = {}
        result = lab6.histogram(input_string)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
