# # **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# # The app needs to handle recipes from different African countries, each with its
# # unique ingredients, preparation time, cooking method, and nutritional
# # information. Consider creating a `Recipe` class, and think about how you might
# # create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# # `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# # methods.

# # class Recipe:
# #     def __init__(self,name, ingrediates, preparation_time, cooking_method, nutritional_information):
# #         self.name = name
# #         self.ingrediates = ingrediates
# #         self.preparation_time = preparation_time
# #         self.cooking_method = cooking_method
# #         self.nutritional_information = nutritional_information
       
# #     def display_recipe(self):
# #         print(f"{self.name} is prepared using {self.ingrediates}")

# # class MoroccanRecipe(Recipe):
# #     def __init__(self, name, ingrediates, preparation_time, cooking_method, nutritional_information):
# #         super().__init__(name, ingrediates, preparation_time, cooking_method, nutritional_information)
        
# #     def display_recipe(self):
# #         return super().display_recipe()  
    
# # class EthiopianRecipe(Recipe):
# #     def __init__(self, name, ingrediates, preparation_time, cooking_method, nutritional_information):
# #         super().__init__(name, ingrediates, preparation_time, cooking_method, nutritional_information)
        
# #     def display_recipe(self):
# #         return super().display_recipe()  
    
# # class NigerianRecipe(Recipe):
# #     def __init__(self, name, ingrediates, preparation_time, cooking_method, nutritional_information):
# #         super().__init__(name, ingrediates, preparation_time, cooking_method, nutritional_information)
        
# #     def display_recipe(self):
# #         return super().display_recipe()  

# # moroccan_recipe = MoroccanRecipe("Couscous","steamed wheat and spiced stew", "30min", "boil","protein")
# # moroccan_recipe.display_recipe()  

# # ethiopian_recipe = EthiopianRecipe("Awaze beef", "berbere, pepper, cumin, & ginger", "20 minutes"," pan fried", "carbohydrates")
# # ethiopian_recipe.display_recipe()

# # nigerian_recipe = NigerianRecipe("Jollof rice", " rice, tomato, onion, pepper, and spices","25 minutes", "fried","proteins")
# # nigerian_recipe.display_recipe()




# class Recipe:
#     def __init__(self,recipe_name, ingredients, preparation_time, cooking_method, nutritional_info):
#         self.recipe_name = recipe_name
#         self.ingredients = ingredients
#         self.preparation_time = preparation_time
#         self.cooking_method = cooking_method
#         self.nutritional_info = nutritional_info

#     def display_recipe(self):
#         print(f" {self.recipe_name} Ingredients: {self.ingredients}, Preparation Time: {self.preparation_time}, Cooking Method: {self.cooking_method},Nutrition Information: {self.nutritional_info}")


# class MoroccanRecipe(Recipe):
#     def __init__(self,recipe_name, ingredients, preparation_time, cooking_method, nutritional_info, spices):
#         super().__init__(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info)
#         self.spices = spices

#     def display_recipe(self):
    
#         super().display_recipe()
#         print(f"Spices: {self.spices}")


# class EthiopianRecipe(Recipe):
#     def __init__(self,recipe_name, ingredients, preparation_time, cooking_method, nutritional_info, spices):
#         super().__init__(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info)
#         self.spices = spices

#     def display_recipe(self):
    
#         super().display_recipe()
#         print(f"Spices: {self.spices}")

# class NigerianRecipe(Recipe):
#     def __init__(self,recipe_name, ingredients, preparation_time, cooking_method, nutritional_info, spices):
#         super().__init__(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info)
#         self.spices = spices

#     def display_recipe(self):
    
#         super().display_recipe()
#         print(f"Spices: {self.spices}")

# moroccan_chicken_recipe = MoroccanRecipe('Couscous:',['steamed wheat, spiced stew'],30,'fry','proteins','ginger')                 

# moroccan_chicken_recipe.display_recipe()


# ethiopian_recipe = EthiopianRecipe("Awaze beef:", ["berbere and pepper"], 20," pan fried", "carbohydrates",'cumin, & ginger')
# ethiopian_recipe.display_recipe()

# nigerian_recipe = NigerianRecipe("Jollof rice:", [" rice, tomato and onion"], 25, "fried","proteins", "pepper & spices")
# nigerian_recipe.display_recipe()



# # class EthiopianRecipe(Recipe):
# #     def __init__(self, recipe_name, ingredients, preparation_time, cooking_method, nutritional_info, serving_size):
# #         super().__init__(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info)
# #         self.serving_size = serving_size

# #     def display_recipe(self):
        
# #         super().display_recipe()
# #         print(f"Serving Size: {self.serving_size}")
# # ethiopian_injera_recipe = EthiopianRecipe(['teff flour', 'water', 'baking powder', 'salt'],
# #                                           180, 'Cooking on a griddle', 'Gluten-free', 6)

# # ethiopian_injera_recipe.display_recipe()

# # class NigerianRecipe(Recipe):
# #     def __init__(self, ingredients, prep_time, cooking_method, nutrition, cuisine_type):
# #         super().__init__(ingredients, prep_time, cooking_method, nutrition)
# #         self.cuisine_type = cuisine_type

# #     def display_recipe(self):
       
# #         super().display_recipe()

# #         print(f"Cuisine Type: {self.cuisine_type}")# Create an object of NigerianRecipe
# # nigerian_jollof_rice_recipe = NigerianRecipe(['rice', 'tomatoes', 'pepper', 'onions', 'chicken', 'pices'], 120, 'Cooking on stove', 'High in carbs', 'West African')

# # nigerian_jollof_rice_recipe.display_recipe()


# # **Wildlife Preservation:** You're a wildlife conservationist working on a
# # program to track different species in a national park. Each species has its own
# # characteristics and behaviors, such as its diet, typical lifespan, migration
# # # patterns, etc. Some species might be predators, others prey. You'll need to
# # create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# # these classes might relate to each other through inheritance.

# class Species:
#     def __init__(self, name, diet, lifespan, migration_patterns):
#         self.name = name
#         self.diet = diet
#         self.lifespan = lifespan
#         self.migration_patterns = migration_patterns
    
#     def species_info(self):
#         return (f"{self.name} feeds on{self.diet}, it has a lifespan of {self.lifespan} and migrates {self.migration_patterns}")

# class Predator (Species):
#     def __init__(self, name, diet, lifespan, migration_patterns, hunting_method):
#         super().__init__(name, diet, lifespan, migration_patterns)
#         self.hunting_method = hunting_method

#     def species_info(self):
#         return super().species_info()
        
# animal1 = Predator("Cheetah", "meat", "30yrs", "North to South", "spot and stalk")
# print(animal1.species_info())

# class Prey(Species):
#     def __init__(self, name, diet, lifespan, migration_patterns, defense_mechanism):
#         super().__init__(name, diet, lifespan, migration_patterns)
#         self.defense_mechanism = defense_mechanism

#     def species_info(self):
#         return super().species_info()
        
# animal2 = Prey("Antellope", "grass", "20yrs", "seasonal", "lying flat on ground")
# print(animal2.species_info())

    
    



class Species:
    def __init__(self, name, lifespan):
        self.name = name
        self.lifespan = lifespan

    def species_info(self):
        return (f"{self.name} can live for {self.lifespan}")
                
    def calculate_remaining_lifespan(self, age):
        remaining_lifespan = self.lifespan - age
        if remaining_lifespan > 0:
            print("Remaining Lifespan:", remaining_lifespan, "years")
        else:
            print("Expected Lifespan Reached")


class Predator(Species):
    def __init__(self, name, lifespan, diet):
        super().__init__(name, lifespan)
        self.diet = diet

    def display_characteristics(self):
        super().calculate_remaining_lifespan()
        # return("Diet:", self.diet)
        # # return("Behavior: Predator")

    # def species_info(self):
    #     print super().species_info()


class Prey(Species):
    def __init__(self, name, lifespan, migration_patterns):
        super().__init__(name, lifespan)
        self.migration_patterns = migration_patterns

    def display_characteristics(self):
        super().calculate_remaining_lifespan()
        # print("Migration Patterns:", self.migration_patterns)
        # print("Behavior: Prey")


# Example usage
lion = Predator("Lion", 15, "Carnivore")
lion.calculate_remaining_lifespan(8)
# lion.display_characteristics
# lion.species_info
# lion.species_info

gazelle = Prey("Gazelle", 10, "Seasonal migration")
gazelle.calculate_remaining_lifespan(5)



class Species:
    def __init__(self, name, lifespan):
        self.name = name
        self.lifespan = lifespan

    def species_info(self):
        return (f"{self.name} can live for {self.lifespan}")
                
    def calculate_remaining_lifespan(self, age):
        remaining_lifespan = self.lifespan - age
        if remaining_lifespan > 0:
            print("Remaining Lifespan:", remaining_lifespan, "years")
        else:
            print("Expected Lifespan Reached")


class Predator(Species):
    def __init__(self, name, lifespan, diet):
        super().__init__(name, lifespan)
        self.diet = diet

    def display_characteristics(self):
        super().calculate_remaining_lifespan()

class Prey(Species):
    def __init__(self, name, lifespan, migration_patterns):
        super().__init__(name, lifespan)
        self.migration_patterns = migration_patterns

    def display_characteristics(self):
        super().calculate_remaining_lifespan()


lion = Predator("Lion", 15, "Carnivore")
lion.calculate_remaining_lifespan(8)

gazelle = Prey("Gazelle", 10, "Seasonal migration")
gazelle.calculate_remaining_lifespan(5)




class Artist:
    def __init__(self, name, country, musical_style, instrument):
        self.name = name
        self.country = country
        self.musical_style = musical_style
        self.instrument = instrument
    def perform(self):
        return (f"{self.name} from {self.country} is performing {self.musical_style} music on {self.instrument}.")
class Performance:
    def __init__(self, artist, start_time, end_time):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time
    def get_duration(self):
        return self.end_time - self.start_time
class Stage:
    def __init__(self, name):
        self.name = name
        self.performances = []
    def add_performance(self, performance):
        self.performances.append(performance)
    def get_total_duration(self):
        total_duration = sum(performance.get_duration() for performance in self.performances)
        return total_duration
class MainStage(Stage):
    def __init__(self):
        super().__init__("Main Stage")
        self.special_effects = []
    def add_special_effect(self, effect):
        self.special_effects.append(effect)

artist1 = Artist("Artist 1", "Country A", "Afrobeat", "Drums")
artist2 = Artist("Artist 2", "Country B", "Reggae", "Guitar")

performance1 = Performance(artist1, 14, 15)
performance2 = Performance(artist2, 16, 17)

main_stage = MainStage()
main_stage.add_performance(performance1)
main_stage.add_performance(performance2)
main_stage.add_special_effect("Fireworks")
for performance in main_stage.performances:
    performance.artist.perform()

total_duration = main_stage.get_total_duration()
print(f"Total duration on {main_stage.name}: {total_duration} hours")
print(f"Special effects on {main_stage.name}: {main_stage.special_effects}")








