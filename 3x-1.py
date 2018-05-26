import sys

while True:
    maybe_num = sys.stdin.readline()

    # just crash out
    num = int(maybe_num)

    counter = 0

    while num > 1:
        counter += 1
        sys.stdout.write(str(num))
        if num % 2 == 0:
            num = num / 2
            sys.stdout.write(" -")
        else:
            num = num * 3 + 1
            sys.stdout.write(" +")

        num = num / 2 if num % 2 == 0 else num * 3 + 1
        sys.stdout.write("> ")
        if num == 1:
            sys.stdout.write(str(num))

    print 
    print counter


