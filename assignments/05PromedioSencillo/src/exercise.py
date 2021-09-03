def main():
    #escribe tu código abajo de esta línea
    n = int(input())
    j = 0
    p = 0.0
    while j<n:
        e = float(input())
        p = p+e
        j = j+1
    r = (p/n)
    print(r)

if __name__ == '__main__':
    main()