start = int(input("Enter a starting number: "))

while start >= 1:
    print(start)
    start -= 1

print("Blast off!")
What this does

If you enter 5, you should get:

Enter a starting number: 5
5
4
3
2
1
Blast off!

If you enter 3:

Enter a starting number: 3
3
2
1
Blast off!

The important part is:

start -= 1
