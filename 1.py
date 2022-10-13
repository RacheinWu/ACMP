def main():
    for m in range(1,10):
        string = ''
        for n in range(1,m+1):
            string = string + '  ' + aXb(m,n)

        print(string)


def aXb(a,b):
    string = '{a} * {b} = {anser}'.format(a=str(a),b=str(b),anser=a*b)
    return string


if __name__ == "__main__":
    main()