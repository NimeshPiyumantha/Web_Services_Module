# import main_second
# import main_third

# print(type(main_third))
# print(main_third.name)

# print("File Name main.py")
# if(__name__ == "__main__"):
#     print("Main Method inside main.py")

import main_second
from main_third import name
import main_third

print(type(main_third))
print(name)

print("File Name main.py")
if(__name__ == "__main__"):
    print("Main Method inside main.py")