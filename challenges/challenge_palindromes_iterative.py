def is_palindrome_iterative(word):
    if word is None or len(word) == 0:
        return False
    is_palindrome = True
    for i in range(0, len(word) // 2):
        if word[i] != word[-(i + 1)]:
            is_palindrome = False
    return is_palindrome
