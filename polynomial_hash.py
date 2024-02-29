def polynomial_hash(s, base=256, modulus=101):

    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0

    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(m_string, substring):
    substring_len = len(substring)
    string_len = len(m_string)

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    curent_slice_hash = polynomial_hash(m_string[:substring_len], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_len - 1) % modulus

    for i in range(string_len - substring_len +1):
        if substring_hash == curent_slice_hash:
            if m_string[i:i +substring_len] == substring:
                return i
        if i < string_len - substring_len:
            #substracting the lefmpst char
            curent_slice_hash = (curent_slice_hash - ord(m_string[i]) * h_multiplier) % modulus
            # adding the rightmost char
            curent_slice_hash = (curent_slice_hash * base + ord(m_string[i + substring_len])) % modulus
            if curent_slice_hash < 0:
                curent_slice_hash += modulus

    return -1


if __name__ == '__main__':
    main_string = "Being a developer is not easy"
    substring = "developer"

    position = rabin_karp_search(main_string, substring)
    if position != -1:
        print(f"Substring found at index {position}")
    else:
        print("Substring is not not found")

