def compute_lps(pattern):
    lps = [0] * len(pattern)
    lenght = 0
    i = 1 

    while i < len(pattern):
        if pattern[i] == pattern[lenght]:
            lenght += 1
            lps[i] = lenght
            i += 1
        else:
            if lenght != 0:
                lenght = lps[lenght - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    M = len(pattern)
    N = len(text)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j
    return - 1


if __name__ == '__main__':
    #raw = "Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження підрядка в тексті."
    raw = "Ensure that your Python environment supports Unicode"
    pattern = "environment"

    print(kmp_search(raw, pattern))
    
