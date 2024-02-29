import timeit

from polynomial_hash import rabin_karp_search
from knut_mor_pratt import kmp_search
from boyer_moor import boyer_moor_search

from download_files import download_google_docs 

if __name__ == "__main__":
    article1_url = 'https://docs.google.com/document/d/1CfyzkVug5VmLAoXT6nM4J5O7FgfuVnlU-WpkXl88fhM/edit?usp=sharing'
    article2_url = 'https://docs.google.com/document/d/1mezqmExmcNZfm17ovofhU95ns-IJBRgzQuC5GcNr7gM/edit?usp=sharing'
    article1_text = download_google_docs(article1_url)
    article2_text = download_google_docs(article2_url)
    pattern1 = 'Фундаментальні знання допомагають дізнатися, що всередині, як воно працює і чому одне рішення краще, аніж інше у конкретній ситуації'
    pattern2 = 'Основна перевага цієї структури полягає у сталому часі додавання нового елементу'


    boyer_moor_time1 = timeit.timeit(lambda: boyer_moor_search(article1_text, pattern1 ), number = 1)
    index_1 = lambda: boyer_moor_search(article1_text, pattern1)
    boyer_moor_time2 = timeit.timeit(lambda: boyer_moor_search(article2_text, pattern2 ), number = 1)
    index_2 = lambda: boyer_moor_search(article2_text, pattern2)
    boyer_time_dsnt_exst = timeit.timeit(lambda: boyer_moor_search(article1_text, pattern2 ), number = 1)
    #for index 3 result = -1, as pattern doesn't exist
    #index_3 = lambda: boyer_moor_search(article1_text, pattern2)


    KMT_time_1 = timeit.timeit(lambda: kmp_search(article1_text, pattern1 ), number = 1)
    index_1_k = lambda: kmp_search(article1_text, pattern1)
    KMT_time_2 = timeit.timeit(lambda: kmp_search(article2_text, pattern2 ), number = 1)
    index_2_k = lambda: kmp_search(article2_text, pattern2)
    KMT_time_dsnt_exst = timeit.timeit(lambda: kmp_search(article1_text, pattern2 ), number = 1)
    #index_3_k = lambda: kmp_search(article1_text, pattern2)


    rabin_karp_time_1 = timeit.timeit(lambda: rabin_karp_search(article1_text, pattern1 ), number = 1)
    index_1_r = lambda: rabin_karp_search(article1_text, pattern1)
    rabin_karp_time_2 = timeit.timeit(lambda: rabin_karp_search(article2_text, pattern2 ), number = 1)
    index_2_r = lambda: rabin_karp_search(article2_text, pattern2)
    rabin_karp_time_dsnt_exst = timeit.timeit(lambda: rabin_karp_search(article1_text, pattern2 ), number = 1)
    #index_3_r = lambda: rabin_karp_search(article1_text, pattern2) 


    print(f"| {'Algorithm':<15} | {'In article_1':<15} | {'Index_1':<15} | {'In article_2':<15} | {'Index_2':<15} | {'Not found':<15} |")
    print(f"| {'-'*15} | {'-'*15} | {'-'*15} | {'-'*15} | {'-'*15} | {'-'*15} |")

    print(f"| {'Boyer_moor':<15} | {boyer_moor_time1:15.5f} | {index_1():15} | {boyer_moor_time2:15.5f} | {index_2():15} | {boyer_time_dsnt_exst:15.5f} |")
    print(f"| {'KMP':<15} | {KMT_time_1:15.5f} | {index_1_k():15} | {KMT_time_2:15.5f} | {index_2_k():15} | {KMT_time_dsnt_exst:15.5f} |")
    print(f"| {'Rabin_Karp':<15} | {rabin_karp_time_1:15.5f} | {index_1_r():15} | {rabin_karp_time_2:15.5f} | {index_2_r():15} | {rabin_karp_time_dsnt_exst:15.5f} |")


'''
Висновок: найшвидший алгоритм Боєра-Мура, найповільніший Рабіна-Карпа. На повну перевірку тексту,
в разі якщо підрядка немає, займає більше всього часу. Загалом, все одно всі алгоритми швидкі. 

Результати: 

| Algorithm       | In article_1    | Index_1         | In article_2    | Index_2         | Not found       |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| Boyer_moor      |         0.00012 |            1656 |         0.00019 |            6093 |         0.00030 |  
| KMP             |         0.00049 |            1656 |         0.00178 |            6093 |         0.00317 |  
| Rabin_Karp      |         0.00134 |            1656 |         0.00407 |            6093 |         0.00745 |
'''
    
  