calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    tuple = len(string), string.upper(), string.lower()
    return tuple

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            return True
        if i == len(list_to_search) - 1 and string.lower() != list_to_search[i].lower():
            return False

print(string_info('Capybara'))
print(string_info('Carmageddon'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('Taliban', ['ban', 'BaNaN', 'talBAN', 'talIBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
