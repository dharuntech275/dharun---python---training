# Student Marks Analysis Program

# Input: Number of students
n = int(input("Enter number of students: "))

total_marks = 0
failed_count = 0

# Processing marks
for i in range(n):
    mark = int(input(f"Enter mark for student {i+1}: "))
    
    # Validate mark range
    if mark < 0 or mark > 100:
        print("Invalid mark! Please enter marks between 0 and 100.")
        continue
    
    total_marks += mark
    
    # Check fail condition
    if mark < 40:
        failed_count += 1

# Calculations
average = total_marks / n
passed_count = n - failed_count

# Output
print("\n----- Result -----")
print("Total Marks:", total_marks)
print("Average Marks:", average)
print("Passed Students:", passed_count)
print("Failed Students:", failed_count)

# Time Complexity: O(n)
# Space Complexity: O(1)