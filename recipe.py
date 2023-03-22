import requests

def recipe_search(ingredient):
    app_id = 'laurahill207@hotmail.com'
    app_key = 'xxxxxxxxx'
    result = requests.get(
'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,app_key)
)
# method to get access to the database and return results from 0 - 15
def basic_search(ingredient):
    id = 'bc7182eb'
    key = 'ae53400b50540675de6131d635744446'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}&from=0&to=15'.format(ingredient, id,
    key)
    print(url)
    response = requests.get(url)
    return response.json()

url= 'https://api.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_APP_KEY}'
# method to get list of recipes containing ingredient entered
def results(ingredient):
    recipe_number = 0
    data = basic_search(ingredient)

response = requests.get(url)
recipe_search = response.json()
return response['recipes']
    for recipe in data['hits']:
        label = (recipe['recipe']['label'] )
        url = (recipe['recipe']['url'] )
        recipe_number = recipe_number +1
        print('Recipe {}, is {}, and the url is {}'.format(recipe_number,label,url))

# method to filter list by calories
def calories(calorie_input):
    data = basic_search(ingredient)
    recipe_number= 0
    for recipe in data['hits']:
        calories = (recipe['recipe'] ['calories'])
        label = (recipe ['recipe'] ['label'])
        url = (recipe['recipe'] ['url'])
        if calories < calorie_input:
            recipe_number = recipe_number + 1
            print(' {} is {} calories, the link for the recipe is: {}' .format(label, int(calories), url))

def run():
    ingredient = input('Please enter an ingredient: ')
    requests = recipe_search(ingredient)
for result in requests:
    recipe = result['recipe']
# method to filter list by cooking time in minutes#
def cook_time(time_input):
    data = basic_search(ingredient)
    recipe_number= 0
    for recipe in data['hits']:
        time = (recipe['recipe'] ['totalTime'])
        label = (recipe ['recipe'] ['label'])
        url = (recipe['recipe'] ['url'])
        if time > 0 and time < int(time_input):
            recipe_number = recipe_number + 1
            print(' Recipe {}: {} takes {} minutes to prepare, the link for the recipe is: {}'.format(recipe_number,label, int(time), url))

print("Here are some recipes including {}." .format(ingredient))
print(recipe['label'])
print(recipe['uri'])
print()
# method to filter the recipes
def filter(filter):
    if str(filter) == 'c':
        calorie_input = int(input("how many calories would you like to have for your recipe? "))
        calories(calorie_input)
    if str(filter) == 't':
        meal_input = input('how many minutes have you got ?')
        cook_time(meal_input)

if none:
    print("There are no recipes with this ingredient. Please try another.")
# Main program #
ingredient = input('Enter an ingredient ')
basic_search(ingredient)
results(ingredient)
input_filter = input("you can filter your results by choosing \n c = calories  \n t = time taken  \nplease enter a choice c or t  ")
filter(input_filter)


run()
