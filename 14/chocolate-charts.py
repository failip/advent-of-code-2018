recipe_index = 0
recipes = {}
end_string = open('input', 'r').readline()
for char in '37':
    recipes[recipe_index] = int(char)
    recipe_index += 1
end_length = int(end_string) + 10

elf_one_index = 0
elf_two_index = 1
while recipe_index < end_length:
    new_recipe = recipes[elf_one_index] + recipes[elf_two_index]
    if new_recipe > 9:
        new_recipe = str(new_recipe)
        for char in new_recipe:
            recipes[recipe_index] = int(char)
            recipe_index += 1
    else:
        recipes[recipe_index] = new_recipe
        recipe_index += 1
    elf_one_index += recipes[elf_one_index] + 1
    elf_two_index += recipes[elf_two_index] + 1
    while elf_one_index >= recipe_index:
        elf_one_index -= recipe_index
    while elf_two_index >= recipe_index:
        elf_two_index -= recipe_index 

string_recipes = ''
for i in range(end_length-10,end_length):
    string_recipes += str(recipes[i])
print('Part One:')
print(string_recipes)


while not (end_string in string_recipes):
    new_recipe = recipes[elf_one_index] + recipes[elf_two_index]
    if new_recipe > 9:
        new_recipe = str(new_recipe)
        for char in new_recipe:
            recipes[recipe_index] = int(char)
            recipe_index += 1
    else:
        recipes[recipe_index] = new_recipe
        recipe_index += 1
    elf_one_index += recipes[elf_one_index] + 1
    elf_two_index += recipes[elf_two_index] + 1
    while elf_one_index >= recipe_index:
        elf_one_index -= recipe_index
    while elf_two_index >= recipe_index:
        elf_two_index -= recipe_index
    string_recipes = ''
    for i in range(recipe_index - 7, recipe_index):
        string_recipes += str(recipes[i])
print('Part Two:')
print(recipe_index - 7)