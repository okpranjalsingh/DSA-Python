'''
A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward as forward. Examples:

String → "madam", "racecar", "121"
Array → [1, 2, 3, 2, 1]
Number → 121, 1331
'''

def is_palindrome(s):
    s = s.replace(' ', '').lower()

    left, right = 0, len(s) -1

    while left < right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
        return True
    

if __name__ == "__main__":
    test_strigs = ["madam", "racecar", "123321", "python", "A man a plan a canal Panama"]

    for t in test_strigs:
         print(f"'{t}': {is_palindrome(t)}")

