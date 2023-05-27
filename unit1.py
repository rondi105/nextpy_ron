import functools
def add_letter(x,y):
    return x + y + y
def double_letter(string):
    return string[0]+functools.reduce(add_letter, string)

def check_4(a):
    return a%4==0
def four_dividers(number):
    return list(filter(check_4,range(number+1)[1:]))

def add_digits(x, y):
    return int(x) + int(y)
def sum_of_digits(number):
    return functools.reduce(add_digits, str(number))

def combine_coins(coin, numbers): return ', '.join([coin + str(i) for i in numbers])

def longest_name(filename):
    print(max([name.strip() for name in open('names.txt')], key=len))

def len_sum(filename):
    print(sum(len(name.strip()) for name in open('names.txt')))

def short_words(filename):
    minlen=min([len(name.strip()) for name in open('names.txt')])
    words=filter(lambda x:len(x)==minlen,[(name.strip()) for name in open('names.txt')])
    print(*words, sep='\n')

def word_lens(filename):
    newfile=open("name_length.txt","w")
    lens=[str(len(name.strip()))+"\n" for name in open('names.txt')]
    for length in lens : newfile.write(str(length))

def input_len(filename):
    inlen = int(input("Enter name length: "))
    words = filter(lambda x: len(x) == inlen, [(name.strip()) for name in open('names.txt')])
    print(*words, sep='\n')




def main():
   input_len("names.txt")


if __name__ == '__main__':
    main()

