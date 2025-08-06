class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        delimiter = ','
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            delimiter = parts[0][2:]
            numbers = parts[1]

        numbers = numbers.replace('\n', delimiter)
        num_list = [int(n) for n in numbers.split(delimiter) if n]
        negatives = [n for n in num_list if n < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")
        return sum(num_list)
