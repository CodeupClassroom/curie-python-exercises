# IPython log file


l = [1, 2, 3]
len(l)
l + [4]
l
l[1:]
l
l
l.append(4)
l
print(l)
l
2 + 2
x = 25
x * 2
l.pop()
l
l.pop()
l.pop()
l.pop()
l
l.pop()
get_ipython().run_line_magic('pinfo', 'l.pop')
l.append(900)
l.append(16)
l.append(23)
l
l
l + [42]
new_list = l + [42]
new_list
print(l + [42])
new_list = print(l + [42])
new_list
2 + 2
type(new_list)
l = [print('one'), print('two'), print('three')]
l
type(l)
type(l[0])
[2 + 2, 16 * 3, 2 ** 19]
range(10)
type(range(10))
list(range(10))
list('abc')
list(14.9)
(1, 2, 3)
my_tuple = (1, 2, 3)
my_tuple = ('a', 'b', 'c')
my_tuple[0]
my_tuple[1]
meal = {'type': 'breakfast', 'contents': 'oatmeal and blueberries', 'beverage': 'coffee'}
meal
13
x = 13
x
meal['contents']
meal['price'] = 9.99
meal
meal['price'] *= 1.2
meal
x = 3
x += 4
x = x + 4
x
x -= 3
x
x /= 2
x
round(4.2)
meal
meal = {}
meal['type'] = 'breakfast'
meal['contents'] = 'oatmeal and blueberries'
meal['beverage'] = 'coffee'
meal['price'] = 11.98
meal
dict(x=123, y=456, z=789)
meal['price'] += 5
int
int(4.2)
float(5)
round(4.5)
round(5.5)
get_ipython().run_line_magic('pinfo', 'round')
round(4.5000001)
round(4.5)
meal
dict(x=123, y=456, z=789)
d1 = dict(x=123, y=456, z=789)
d2 = {'x': 123, 'y': 456, 'z': 789}
d1 == d2
d1 is d2
[x for x in range(10)]
[x + 1 for x in range(10)]
[x + 1 for x in range(10) if x < 7]
[x for x in range(10)]
[x for x in range(10) if x % 2 == 0]
[x ** 2 for x in range(10) if x % 2 == 0]
# numbers greater than 5 doubled
[x * 2 for x in range(10) if x > 5]
# all the odd numbers halved
[x for x in range(10) if x % 2 == 1]
[x / 2 for x in range(10) if x % 2 == 1]
# add three to the even numbers less than 7
[x + 3 for x in range(10)]
[x + 3 for x in range(10) if x % 2 == 0]
[x + 3 for x in range(10) if x % 2 == 0 and x < 7]
cohorts = [
    {'name': 'Ada', 'n_students': 17, 'coolness': 4},
    {'name': 'Bayes', 'n_students': 20, 'coolness': 5},
    {'name': 'Curie', 'n_students': 17, 'coolness': 80},
]
cohorts
[cohort for cohort in cohorts]
# let's see the name of the cohorts with coolness ge 5
[cohort['name'] for cohort in cohorts]
[cohort['name'] for cohort in cohorts if cohort['coolness'] >= 5]
# the coolness of Bayes
[cohort for cohort in cohorts if cohort['name'] == 'Bayes']
# the coolness of Bayes
[cohort['coolness'] for cohort in cohorts if cohort['name'] == 'Bayes']
# the coolness of Bayes
[cohort['coolness'] for cohort in cohorts if cohort['name'] == 'Bayes'][0]
bayes_coolness = [cohort['coolness'] for cohort in cohorts if cohort['name'] == 'Bayes'][0]
[cohort['name'] for cohort in cohorts if cohort['coolness'] >= bayes_coolness]
cohort
[cohort['name'] for cohort in cohorts if cohort['coolness'] >= bayes_coolness]
cohorts
# what's the average number of students?
n_students_by_cohort = [cohort['n_students'] for cohort in cohorts]
n_students_by_cohort
sum(n_students_by_cohort) / len(n_students_by_cohort)
# which *right* triangle with integer sides <= 10 and perimeter of 24
[(a, b, c) for a in range(1, 11) for b in range(1, 11) for c in range(1, 11)]
[(a, b, c) for a in range(1, 11) for b in range(1, 11) for c in range(1, 11)
 if a**2 + b**2 == c**2]
[(a, b, c) for a in range(1, 11) for b in range(1, 11) for c in range(1, 11)
 if a**2 + b**2 == c**2 and a + b + c == 24]
[(a, b, c) for a in range(1, 11) for b in range(1, 11) for c in range(1, 11)
 if a**2 + b**2 == c**2 and a + b + c == 24 and a < b and b < c]
students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]
students
len(students)
students[:2]
# how many pets do people with a preference for light coffee have on average?
[student for student in students if student['coffee_preference'] == 'light']
student = students[0]
student
student['pets']
len(student['pets'])
# how many pets do people with a preference for light coffee have on average?
[len(student['pets']) for student in students if student['coffee_preference'] == 'light']
# how many pets do people with a preference for light coffee have on average?
n_pets = [len(student['pets']) for student in students if student['coffee_preference'] == 'light']
avg_no_pets_for_light_coffee_drinkers = sum(n_pets) / len(n_pets)
avg_no_pets_for_light_coffee_drinkers
numbers = range(1, 100)
[n**2 for n in numbers if n > 50]
results = [n**2 for n in numbers if n > 50]
n
x
[x for n in numbers if < 10]
[x for n in numbers if n < 10]
[x for x in numbers if x < 10]
