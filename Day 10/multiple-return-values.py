# Functions with multiple return values

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  f_name = f_name.title()
  l_name = l_name.title()
  return f"{f_name} {l_name}"
    
# print(format_name("aDiTYa", "rAwAt"))
print(format_name(input("Enter your first name: "), input("Enter your last name: ")))
