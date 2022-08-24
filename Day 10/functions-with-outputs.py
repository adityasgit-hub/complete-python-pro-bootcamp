# Functions with Outputs

def format_name(f_name, l_name):
  f_name = f_name.title()
  l_name = l_name.title()
  return (f"{f_name} {l_name}")
    
# name = format_name("aDiTYa", "rAwAt")
name = format_name(input("Enter your first name: "), input("Enter your last name: "))
print(name)
