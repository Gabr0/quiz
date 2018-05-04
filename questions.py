"""Simple question program by gabr0."""


class Question:
    """Basic question generator."""

    answer = None
    text = None


class Add(Question):
    """Sum question generator."""

    def __init__(self, num1, num2):
        """Declare text and answer."""
        self.text = '{} + {}'.format(num1, num2)
        self.answer = num1 + num2


class Multiply(Question):
    """Multiplication question generator."""

    def __init__(self, num1, num2):
        """Declare text and answer."""
        self.text = '{} x {}'.format(num1, num2)
        self.answer = num1 * num2
