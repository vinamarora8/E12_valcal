import math

# The E12 Series
series = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
N = len(series)

def close_enough(a):
    a = float(a)
    s = [x - a for x in series]
    s2 = [abs(x) for x in s]
    i = s2.index(min(s2))
    return [series[i], s[i]]

ratio = float(input("Enter the ratio: "))
k = math.floor(math.log(ratio, 10)) # what power of 10
ratio /= 10.**k

raw_vals = [x*ratio for x in series]
close_vals = [close_enough(x) for x in raw_vals]

errors = []
for i in range(N):
    e = close_vals[i][1]/series[i]
    errors.append(e)
    close_vals[i][1] = e
    close_vals[i] = [series[i]] + close_vals[i]

close_vals = sorted(close_vals, key=lambda x: abs(x[2]))

print("|\tR2  / R1 \t|\tERROR\t  |\tACTUAL\t  |")
print("------------------------|-----------------|---------------|")
for i in range(N):
    percentage = round(close_vals[i][2]*100, 2 if abs(close_vals[i][2]) < 1 else 1)
    actual_ratio = close_vals[i][1]/close_vals[i][0]
    print("|\t{} / {}\t|\t{}%\t  |\t{}\t  |".format(close_vals[i][1], close_vals[i][0], percentage, round(actual_ratio, 5)))