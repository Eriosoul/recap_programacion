systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list
# Syntax: reversed_list = systems[start:stop:step]
reversed_list = systems[::-1]

# updated list
print('Updated List:', reversed_list)

word = "121"
print(word)
quit_space = word.replace(" ", "").lower()
rev = quit_space[::-1]
print(rev)

if quit_space == rev:
    print("La palabra es palindroma")
else:
    print("La palabra no es palidnroma")