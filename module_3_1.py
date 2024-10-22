calls = 0

def count_calls():
    global  calls
    calls = calls + 1

def string_info(string):
    count_calls()
    string_work = (len(string),string.upper(),string.lower())
    return string_work

def is_contains(string,list_to_search):
    count_calls()
    new_list_to_search = [i.lower() for i in list_to_search]
    if string.lower() in new_list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)