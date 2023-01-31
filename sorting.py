pangram="The quick brown fox jumps over the lazy dog"

letter=sorted(pangram)
print(letter)

numbers=[2.3,2.4,4,3.9]
sorted_numbers=sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter=sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)
print(missing_letter)

names=["Graham",
       "John",
       "terry",
       "eric",
       "Terry",
       "michael"]
#names.sort()
names.sort(key=str.casefold)
print(names)





