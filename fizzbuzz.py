import unittest


def fizzHandler(number):
    if number % 3 == 0:
        return 'Fizz'


def buzzHandler(number):
    if number % 5 == 0:
        return 'Buzz'


def fizzbuzzHandler(number):
    if number % 15 == 0:
        return 'FizzBuzz'


def numberHandler(number):
    return str(number)


def createFizzbuzz(handlers):
    def fizzbuzz(number):
        return next(handler(number) for handler in handlers if handler(number))

    return fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        handlers = [fizzbuzzHandler, fizzHandler, buzzHandler, numberHandler]
        self.fizzbuzz = createFizzbuzz(handlers)

    def test_should_return_1_when_input_1(self):
        expected = '1'

        actual = self.fizzbuzz(1)

        self.assertEqual(actual, expected)

    def test_should_return_2_when_input_2(self):
        expected = '2'

        actual = self.fizzbuzz(2)

        self.assertEqual(actual, expected)

    def test_should_return_Fizz_when_input_3(self):
        expected = 'Fizz'

        actual = self.fizzbuzz(3)

        self.assertEqual(actual, expected)

    def test_should_return_Fizz_when_input_6(self):
        expected = 'Fizz'

        actual = self.fizzbuzz(6)

        self.assertEqual(actual, expected)

    def test_should_return_Buzz_when_input_5(self):
        expected = 'Buzz'

        actual = self.fizzbuzz(5)

        self.assertEqual(actual, expected)

    def test_should_return_Buzz_when_input_10(self):
        expected = 'Buzz'

        actual = self.fizzbuzz(10)

        self.assertEqual(actual, expected)

    def test_should_return_FizzBuzz_return_input_15(self):
        expected = 'FizzBuzz'

        actual = self.fizzbuzz(15)

        self.assertEqual(actual, expected)

    def test_should_return_FizzBuzz_when_input_30(self):
        expected = 'FizzBuzz'

        actual = self.fizzbuzz(30)

        self.assertEqual(actual, expected)


unittest.main()
