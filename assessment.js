// // # **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// // # The app needs to handle recipes from different African countries, each with its
// // # unique ingredients, preparation time, cooking method, and nutritional
// // # information. Consider creating a `Recipe` class, and think about how you might
// // # create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// // # `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// // # methods.




class Recipe {
  constructor(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info) {
    this.recipe_name = recipe_name;
    this.ingredients = ingredients;
    this.preparation_time = preparation_time;
    this.cooking_method = cooking_method;
    this.nutritional_info = nutritional_info;
  }

  display_recipe() {
    console.log(` ${this.recipe_name}, Ingredients: ${this.ingredients}, Preparation Time: ${this.preparation_time}, Cooking Method: ${this.cooking_method}, Nutrition Information: ${this.nutritional_info}`);
  }
}

class MoroccanRecipe extends Recipe {
  constructor(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info, spices) {
    super(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info);
    this.spices = spices;
  }

  display_recipe() {
    super.display_recipe();
    console.log(`Spices: ${this.spices}`);
  }
}

class EthiopianRecipe extends Recipe {
  constructor(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info, spices) {
    super(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info);
    this.spices = spices;
  }

  display_recipe() {
    super.display_recipe();
    console.log(`Spices: ${this.spices}`);
  }
}

class NigerianRecipe extends Recipe {
  constructor(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info, spices) {
    super(recipe_name, ingredients, preparation_time, cooking_method, nutritional_info);
    this.spices = spices;
  }

  display_recipe() {
    super.display_recipe();
    console.log(`Spices: ${this.spices}`);
  }
}

const moroccan_chicken_recipe = new MoroccanRecipe('Couscous:', ['steamed wheat, spiced stew'], 30, 'fry', 'proteins', 'ginger');
moroccan_chicken_recipe.display_recipe();

const ethiopian_recipe = new EthiopianRecipe("Awaze beef:", ["berbere and pepper"], 20, "pan fried", "carbohydrates", 'cumin, & ginger');
ethiopian_recipe.display_recipe();

const nigerian_recipe = new NigerianRecipe("Jollof rice:", ["rice, tomato and onion"], 25, "fried", "proteins", "pepper & spices");
nigerian_recipe.display_recipe();


// # **Wildlife Preservation:** You're a wildlife conservationist working on a
// # program to track different species in a national park. Each species has its own
// # characteristics and behaviors, such as its diet, typical lifespan, migration
// # # patterns, etc. Some species might be predators, others prey. You'll need to
// # create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// # these classes might relate to each other through inheritance.

  // class Species{
  // constructor(name, diet, lifespan, migration_patterns){
  // this.name = name
  // this.diet = diet
  // this.lifespan = lifespan
  // this.migration_patterns = migration_patterns
  // }
  // get_species_info(){
  //   return (`${this.name} feeds on ${this.diet}, it has a lifespan of ${this.lifespan} and has ${this.migration_patterns} migrations`)
  // }
  // }

  // class Predator extends Species{
  // constructor(name, diet, lifespan, migration_patterns,hunting_method ){
  //   super(name, diet, lifespan, migration_patterns)
  //   this.hunting_method = hunting_method
  // }
  // get_species_info(){
  //   return super.get_species_info();
  // }
  // get_defense_mechanism(){
  //   return(`${this.name} hunting method: ${this.hunting_method}`);

  // }
  // }

  // const animal1 = new Predator("Cheetah", "meat", "20yrs", "North to South", "spot and stalk")
  // console.log(animal1.get_species_info());
  // console.log(animal1.get_defense_mechanism());

  // class Prey extends Species {
  // constructor(name, diet, lifespan, migration_patterns, defense_mechanism) {
  //   super(name, diet, lifespan, migration_patterns);
  //   this.defense_mechanism = defense_mechanism;
  // }

  // get_species_info() {
  //   console.log(super.get_species_info());
  // }
  // get_defense_mechanism(){
  //   console.log(`${this.name} Defense Mechanism: ${this.defense_mechanism}`);

  // }
  // }

  // const animal2 = new Prey("Antelope", "grass", "20 years", "seasonal", "lying on the ground");
  // animal2.get_species_info();
  // animal2.get_defense_mechanism();



// class Recipe{
//     constructor(name, ingredients, preparation_time, cooking_method, nutritional_information){
//         this.name = name;
//         this.ingredients = ingredients;
//         this.preparation_time = preparation_time;
//         this.cooking_method = cooking_method;
//         this. nutritional_information = nutritional_information;
//     }
//     display_recipe(){
//         console.log(`${this.name} is prepared using ${this.ingredients}`);
//     }
// }

// class MoroccanRecipe extends Recipe{
//     constructor(name, ingredients, preparation_time, cooking_method, nutritional_information){
//         super(name, ingredients, preparation_time,cooking_method, nutritional_information);
//     }

//     display_recipe(){
//         super.display_recipe()
//     }
// }

// class EthiopianRecipe extends Recipe{
//     constructor(name, ingredients, preparation_time, cooking_method, nutritional_information){
//         super(name, ingredients, preparation_time,cooking_method, nutritional_information);
//     }

//     display_recipe(){
//         super.display_recipe()
//     }
// }

// class NigerianRecipe extends Recipe{
//     constructor(name, ingredients, preparation_time, cooking_method, nutritional_information){
//         super(name, ingredients, preparation_time,cooking_method, nutritional_information);
//     }

//     display_recipe(){
//         super.display_recipe()
//     }
// }

//  const moroccan_recipe = new MoroccanRecipe("Couscous", "steamed wheat and spiced stew", "30min", "boil", "protein");
//  moroccan_recipe.display_recipe();
  
//   const ethiopian_recipe = new EthiopianRecipe("Awaze beef", "berbere, pepper, cumin, & ginger", "20 minutes", "pan fried", "carbohydrates");
//   ethiopian_recipe.display_recipe();
  
//   const nigerian_recipe = new NigerianRecipe("Jollof rice", "rice, tomato, onion, pepper, and spices", "25 minutes", "fried", "proteins");
//   nigerian_recipe.display_recipe();



class Species {
  constructor(name, lifespan) {
      this.name = name;
      this.lifespan = lifespan;
  }

  species_info() {
      return `${this.name} can live for ${this.lifespan}`;
  }

  calculate_remaining_lifespan(age) {
      const remaining_lifespan = this.lifespan - age;
      if (remaining_lifespan > 0) {
          console.log("Remaining Lifespan:", remaining_lifespan, "years");
      } else {
          console.log("Expected Lifespan Reached");
      }
  }
}

class Predator extends Species {
  constructor(name, lifespan, diet) {
      super(name, lifespan);
      this.diet = diet;
  }

  display_characteristics() {
      super.calculate_remaining_lifespan();
  }
}

class Prey extends Species {
  constructor(name, lifespan, migration_patterns) {
      super(name, lifespan);
      this.migration_patterns = migration_patterns;
  }

  display_characteristics() {
      super.calculate_remaining_lifespan();
  }
}

const lion = new Predator("Lion", 15, "Carnivore");
lion.calculate_remaining_lifespan(8);

const gazelle = new Prey("Gazelle", 10, "Seasonal migration");
gazelle.calculate_remaining_lifespan(5);

