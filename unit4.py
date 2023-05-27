def translate(sentance):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    generator =(words[word] for word in sentance.split())
    translated=""
    for word in words:
        translated+=next(generator)+" "
    return translated
def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def  first_prime_over(n):
    prime_generator = (x for x in range(n,n+1000) if is_prime(x))
    return next(prime_generator)

def parse_ranges(ranges_string):
    range_tuples = (
        tuple(range_str.split('-')) for range_str in ranges_string.split(',')
    )
    return (
        num for start, stop in range_tuples for num in range(int(start), int(stop) + 1)
    )
def get_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b



def gen_secs():
    x=0
    while x<60:
        yield x
        x=x+1

def gen_minutes():
    x=0
    while x<60:
        yield x
        x=x+1

def gen_hours():
    x=0
    while x<24:
        yield x
        x=x+1

def gen_time():
    for hour in gen_hours():
        for min in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, min, sec)
def gen_years(start=2019):
    year = start
    while True:
        yield year
        year += 1
def gen_months():
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    yield days_in_month[month]

def gen_date():
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            for day in range(1, next(gen_days(month, leap_year)) + 1):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield "%02d/%02d/%04d %02d:%02d:%02d" % (day, month, year, hour, minute, second)

def main():
    print(translate("el gato esta en la casa"))
    print(first_prime_over(1000000))
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))
    fibo_gen = get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    gen = gen_date()
    for i in range(0, 10000001):
        date = next(gen)
        if i % 1000000 == 0:
            print(date)


if __name__ == '__main__':
    main()
