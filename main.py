from my_functions.py import estimate_max_hr
from my_functions.py import build_person

if __name__ == "__main__":
    supervisor = build_person("Jan", "Bauer", "male", 35)
print(supervisor)
# {'first_name': 'Jan', 'last_name': 'Bauer', 'age': 35, 'estimate_max_hr': 190}

