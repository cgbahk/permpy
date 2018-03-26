"""
find counterexample of inverse statement of Theorem of Lagrange
for finite group G, find integer h s.t. divides |G|, but no subgroup of G is with order h

tried S4 with h = 8 : exists with <(23),(12)(34)>
trying S5

"""

import permpy as pp
from span import span

elements = list()

# 211
elements.append(pp.Permutation(2143))
elements.append(pp.Permutation(1324))
elements.append(pp.Permutation(1243))
elements.append(pp.Permutation(4231))
elements.append(pp.Permutation(3214))
elements.append(pp.Permutation(1432))

# 31
elements.append(pp.Permutation(2314))
elements.append(pp.Permutation(2431))
elements.append(pp.Permutation(3241))
elements.append(pp.Permutation(1342))

# 4
elements.append(pp.Permutation(2341))
elements.append(pp.Permutation(2413))
elements.append(pp.Permutation(3421))

checklist = {1: 1, 2: 0, 3: 0, 4: 0, 6: 0, 8: 0, 12: 0, 24: 0}
passNo = 1

for i in range(1, 1 << len(elements)):
    ii = i
    generators = ()

    # setting generators
    for j in range(0, len(elements)):
        if ii & 1:
            generators += (elements[j],)
        ii = ii >> 1

    checked = len(span(*generators))
    if checked == 8:
        print(generators)
        break
    if checklist[checked] == 0:
        checklist[checked] = 1
        passNo += 1
        if passNo == 8:
            print("all pass")
            break

# output
for key, val in checklist.items():
    print(key, ':', val)
