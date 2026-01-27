def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        min = t - 3000
        self.requests.append(t)
        return self.num_of_list_in_range(self.requests, min, t)

    def num_of_list_in_range(self, numbers, min, max):
        return sum(1 for number in numbers if min <= number <= max)
