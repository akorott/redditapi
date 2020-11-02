import random

test = open('quotes.txt')

quote_list = []
for line in test:
    quote_list.append(line)

print(len(quote_list))

quote_today = random.randint(1, len(quote_list)-1)
print(quote_today)

print(quote_list[quote_today])