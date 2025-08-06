class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        num_list = numbers.split(',')
        return sum(int(n) for n in num_list)
