# SEQUENCE control Structure
# Code runs top to bottom
# Code runs in order of operator precedence (PEMDAS)

print("Hello, World!")
print("One plus one is", str(1 + 1)) # order of operations (PEDMDAS)
print(str(float(str(int(3.3))))) # function calls run from the inside to the out
print("Goodbye, World!")

# SELECTION == conditional
# name = input("What is your name?")

# # if condition (if this then that)
# if name == "Bob":
#     print("Howdy, Bob. Great to see you.")

# print("My name is Python.")

might_rain_today = False
if might_rain_today:
    print("Bring an umbrella")
    print("Bring an umbrella")
    print("Bring an umbrella")
    print("Bring an umbrella")
    print("Bring an umbrella")

print("Have a great day!")


might_flood = False

if might_rain_today:
    print("Bring an umbrella")
    if might_flood:
        print("Pay attention to TXDOT alerts")



number = 15

# Avoid when possible (unless the granularity helps)
if number % 5 == 0:
    if number % 3 == 0:
        print("This number is divisible by both 3 and 5")

# And or OR make compound logical statements
if number % 5 == 0 and number % 3 == 0:
            print("This number is divisible by both 3 and 5")


# if / else 
direction = "up"

if direction == "right":
    print("Take a right turn")
else:
    print("Take a turn in another direction")

print("Keep on going")


# Scenario is editing a blog post
is_admin = True
is_author = True

if is_admin or is_author:
    print("You may edit this blog post")
else:
    print("Access denied")



if True:
    print("If the True is True this prints")
else:
    print("Will this ever run in a million years?")


if len("banana") > 3:
    print("Banana has more than 3 letters")
else:
    print("Banana has length of", str(len("banana")))


## if / else if / else
## if / else if / else if / else if / else

light_color = "Yellow"

# if light_color == "Green":
#     print("Go")
# else:
#     print("Stop")

# One example
if light_color == "Green":
    print("Go")
elif light_color == "Red":
    print("Stop")
elif light_color == "Yellow":
    print("Depends")
else
    print("Look for traffic cop's directions or treat as a stop sign")


you_can_stop_safely = False

if light_color == "Green":
    print("Go")
elif light_color == "Red":
    print("Stop")
elif light_color == "Yellow":
    if you_can_stop_safely:
        print("Come to a full and complete stop before the crosswalk.")
    else:
        print("Keep going")
    print("Whew")
else
    print("Look for traffic cop's directions or treat as a stop sign")







# ITERATION == loops