def is_valid_score(score):
    return(score >= 0 and score <= 100)

score = int(input("Enter a score (0-100): "))

if is_valid_score(score):
    print("Valid score")
else:
    print("Invalid score - must be between 0 and 100.")