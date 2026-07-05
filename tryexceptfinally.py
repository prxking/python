#registrationsystem age(5-50), name min 3 characters student marks from 0 to 100 using class and try except

class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidMarksError(Exception):
    pass

class RegistrationSystem:

    def register_student(self):
        try:
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            marks = int(input("Enter student marks: "))
            
            if len(name) < 3:
                raise InvalidNameError("Name must be at least 3 characters long.")
            if age < 5 or age > 50:
                raise InvalidAgeError("Age must be between 5 and 50.")
            if marks < 0 or marks > 100:
                raise InvalidMarksError("Marks must be between 0 and 100.")
                
            print(f"Student {name} registered successfully with age {age} and marks {marks}.")
            
        except ValueError:

            print("Registration failed: Age and marks must be valid numbers.")
        except (InvalidNameError, InvalidAgeError, InvalidMarksError) as e:
            print(f"Registration failed: {e}")
        finally:
            print("Registration process completed.\n")


system = RegistrationSystem()
system.register_student()