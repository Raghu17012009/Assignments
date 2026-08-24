start=int(input("Enter the start of range: "))
end=int(input("Enter the end of the range: "))

test_number=int(input("Enter a test number: "))

if test_number in range(start,end+1):
    print("Test number is strictly in the range: True")