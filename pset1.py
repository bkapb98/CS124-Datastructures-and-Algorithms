# code for pset 1
# take in the N being number of people, and M being majors
N, M = map(int, raw_input().split()) 
tenacity = map(int, raw_input().split()) 
major = map(int, raw_input().split()) 

# split by majors, sort three times
dict = {}
for x in zip(major, tenacity):
    try:
        dict[x[0]].append(x[1])
    except:
        dict[x[0]] = [x[1]]
    

def merge(s, t):
    count = 0 
    global allDiff
    v, i, j = [], 0, 0
    while len(s) > i and len(t) > j:
        if s[i] < t[j]:
            v.append(s[i])
            i += 1
        else:
            v.append(t[j])
            count += (len(s) - i)
            j += 1

    v += s[i:]
    v += t[j:]
    return v, count


def mergesort (lst):
    # splits list into tiny bits - based off of mergesort recursive taugh in lecture
    if len(lst) <= 1:
        return lst, 0
    m = len(lst)/2
    left, l_swap = mergesort(lst[:m])
    right, r_swap = mergesort(lst[m:])
    lst, c = merge(left, right)
    total = c + l_swap + r_swap + 0
    return lst, total


# quick tricks to save time in exteme cases
if M <= 1:
    print(0)
else:
    lst, finalpairs = mergesort(tenacity)
    for key in dict:
        lst, count = mergesort(dict[key])
        finalpairs = finalpairs - count
    print finalpairs
