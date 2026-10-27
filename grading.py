score = float(input("Enter score: "))

if score >= 90:
    print("A. Congratulations, you passed!")
elif 80 <= score <= 89:
    print("A-. Congratulations, you passed!")
elif 70 <= score <= 79:
    print("B. Congratulations, you passed!")
elif 60 <= score <= 69:
    print("B-. Congratulations, you passed!")
elif 50 <= score <= 59:
    print("C. Congratulations, you passed!")
elif 40 <= score <= 49:
    print("C-. OOPS, try again!")
elif 30 <= score <= 39:
    print("D. OOPS, try again!")
elif 20 <= score <= 29:
    print("D-. OOPS, try again!")
else:
    print("E. OOPS, try again!")
