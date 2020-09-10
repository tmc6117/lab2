#// Author: Tong Chen tmc6117@psu.edu
#// Section: 4
def getLetterGrade(num):
  if num >=93:
    letter = "A"
  elif num >= 90 and num < 93:
    letter = "A-"
  elif num >= 87 and num < 90:
    letter = "B+"
  elif num >= 83 and num < 87:
    letter = "B"
  elif num >= 80 and num < 83:
    letter = "B-"
  elif num >= 77 and num < 80:
    letter = "C+"
  elif num >= 70 and num < 77:
    letter = "C"
  elif num >= 60 and num < 70:
    letter = "D"
  elif num < 60:
    letter = "F"
  return letter

def run():
  num = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(num)}.")

if __name__ == "__main__" :
  run()