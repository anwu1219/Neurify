import sys

num, times= sys.argv[1:]
s = ""
for i in range(int(times)):
    s += num + ","
print(s)
