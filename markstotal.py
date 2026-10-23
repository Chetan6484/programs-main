#program to find total marks 
def calculate_total_marks(**kwargs):
  total = 0
  for subject, mark in kwargs.items():
    print(f'subject:',mark)
    total += mark
  return total
result = calculate_total_marks(math=85, english=90, science=88)
print(f'Total Marks:',result)
