import winsound
from itertools import combinations

def yonatan():
    freqs = {"la": 220,"si": 247,"do": 261,"re": 293,"mi": 329,"fa": 349,"sol": 392, }
    notes ="sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    actual=[x.split(",") for x in notes.split("-")]
    for note in actual:
        winsound.Beep(int(freqs[note[0]]),int(note[1]))

def bill_combs():
    import itertools
    moneylst = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    count_right = 0
    for i in range(5, 20):
        correct = set(itertools.combinations(moneylst, i))
        for comb in correct:
            if sum(comb) == 100:
                print(comb)
                count_right += 1
    print("there are only " + str(count_right) + " combinations to create 100 dollars")

class MusicNotes:
    def __init__(self):
        self.notes = {
            'La': [55, 110, 220, 440, 880],
            'Si': [61.74, 123.48, 246.96, 493.92, 987.84],
            'Do': [65.41, 130.82, 261.64, 523.28, 1046.56],
            'Re': [73.42, 146.84, 293.68, 587.36, 1174.72],
            'Mi': [82.41, 164.82, 329.64, 659.28, 1318.56],
            'Fa': [87.31, 174.62, 349.24, 698.48, 1396.96],
            'Sol': [98, 196, 392, 784, 1568]
        }
        self.notes_iter = self.generate_notes()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.notes_iter)

    def generate_notes(self):
        for octave in range(5):
            for note in self.notes:
                yield self.notes[note][octave]


def check_id_valid(id_number):
    digits = [int(digit) for digit in str(id_number)]
    multiplied_digits = []
    for i in range(len(digits)):
        digit = digits[i]
        multiplier = 2 if i % 2 == 0 else 1
        multiplied_digits.append(digit * multiplier)

    summed_digits = []
    for digit in multiplied_digits:
        if digit <= 9:
            summed_digits.append(digit)
        else:
            summed_digits.append(digit // 10 + digit % 10)

    total_sum = sum(summed_digits)
    return total_sum % 10 == 0


class IDIterator:
    def __init__(self, id_number):
        self._id = id_number

    def __iter__(self):
        return self

    def __next__(self):
        if self._id == 999999999:
            raise StopIteration
        self._id += 1
        while not check_id_valid(self._id):
            self._id += 1
        return self._id


def id_generator(id_number):
    while id_number < 999999999:
        id_number += 1
        while not check_id_valid(id_number):
            id_number += 1
        yield id_number


def id_func():
    id_number = int(input("Enter ID: "))
    generator_or_iterator = input("Generator or Iterator? (gen/it)? ")

    if generator_or_iterator == "it":
        iterator = IDIterator(id_number)
        for _ in range(10):
            print(next(iterator))
    elif generator_or_iterator == "gen":
        generator = id_generator(id_number)
        for _ in range(10):
            print(next(generator))
def main():
    bill_combs()
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
      print(freq)
    id_func()


if __name__ == '__main__':
    main()
