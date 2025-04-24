import matplotlib.pyplot as plt
from matplotlib_venn import venn3

even_numbers = [number for number in range(1, 31) if number % 2 == 0]
multpl_5 = [number for number in range(1,31) if number % 5 == 0]
perf_squares = [number for number in range(1,31) if(number**0.5).is_integer()]

set1 = set(even_numbers)
set2 = set(multpl_5)
set3 = set(perf_squares)
# print(set1)
# print(set2)
# print(set3)

venn3([set1, set2, set3], ('Парні', 'Кратні 5','Повні квадрати'))
# set1 = set([11,12,13,14,15,16,17,18,19])
# set2 = set([2,4,6,8,10,12,14,16,18])
# set3 = set([3,6,9,12,15,18])


# venn3([set1, set2, set3], ('>10', 'Парні', 'Кратні 3'))


plt.show()
