# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):
        return True

    else:
        return False


string_1 = "elbow"
string_2 = "below"

if find_anagrams(string_1, string_2):
    print("words are anagrams.")
else:
    print("words are not anagrams.")
print(find_anagrams(string_1, string_2))
