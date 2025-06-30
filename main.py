def lower_triangle(n):
    print("Lower Triangle:")
    for i in range(1, n + 1):
        print("* " * i)
    print()

def upper_triangle(n):
    print("Upper Triangle:")
    for i in range(n, 0, -1):
        print("* " * i)
    print()

def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print()

def main():
    n = int(input("Enter the number of rows: "))
    lower_triangle(n)
    upper_triangle(n)
    pyramid(n)

if __name__ == "__main__":
    main()
