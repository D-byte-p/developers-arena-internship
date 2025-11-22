# Week 2 Project: Student Grade Calculator

marks = float(input("Enter your marks (0-100): "))

if marks >= 90 and marks <= 100:
    print("Grade: A 🏆")
    print("Excellent! Keep it up! 💯")
elif marks >= 75:
    print("Grade: B ⭐")
    print("Great work! You're doing very well! 😊")
elif marks >= 60:
    print("Grade: C 👍")
    print("Good! But you can do even better! 💪")
elif marks >= 40:
    print("Grade: D 📝")
    print("You passed, but more effort is needed! 📚")
elif marks >= 0:
    print("Grade: F ❌")
    print("Don’t worry! Work hard and you will improve! 💖")
else:
    print("Invalid marks entered! Please enter 0-100.")
