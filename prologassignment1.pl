
servesAll(amercian_restaurants, [salad, steak, burgers]),
servesAll(burger_place_restaurants, [fries, onion_rings, burgers]),
servesAll(chinese_restaurants, [rice, eggrolls, shrimp, soup, noodles]),
servesAll(indian_restaurants, [papadam, bagan_bharta, rice, tandoori, naan]),
servesAll(italian_restaurants, [salad, pasta, cioppino, snapper, bread, garlic_bread]),
servesAll(japanese_restaurants, [sashimi, rice, tempura, noodles]),
servesAll(mediterranian_restaurants, [gyros, hummus, pita, falafel]),
servesAll(mexican_restaurants, [tacos, beans, rice, enchiladas, fish_tacos]),
servesAll(pizza_place_restaurants, [pizza, salad, garlic_bread]),
servesAll(thai_restaurants, [rice, noodles, larb, pad_thai]),
serves(Kind, Dish):-
        servesAll(Kind, Dishes),
        member(Dish, Dishes),

dishType(vegetarian_dishes, [beans, bagan_bharta, enchiladas, falafel, hummus,
pizza, salad, soup, tempura, onion_rings, naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]),

dishType(meat_dishes, [burgers, enchiladas, gyros, pad_thai, pizza, steak, sandwiches,
fried_chicken, tacos, tandoori, larb]),

dishType(seafood_dishes, [snapper, cioppino, sashimi, shrimp, clams, fish_tacos, tempura]),

dishType(starch_dishes, [naan, papadam, bread, rice, noodles, pita, garlic_bread, pasta, fries]),

dish(DishType, Dish):-
        dishType(Kind, Dishes),
        member(Dish, Dishes),

cuisineAll(chinese_restaurants, [yans, chinatown]),
cuisineAll(pizza_place_restaurants, [pizza_marvin, mikes]),
cuisineAll(mexican_restaurants, [bahas, dolores, tallulahs]),
cuisineAll(mediterranian_restaurants, [andreas, east_side_pockets]),
cuisineAll(indian_restaurants, [kabob_n_curry]),
cuisineAll(amercian_restaurants, [waterman_grille, red_stripe]),
cuisineAll(italian_restaurants, [pasta_beach, al_forno]),
cuisineAll(japanese_restaurants, [haruki]),
cuisineAll(thai_restaurants, [heng, bees, lims]),
cuisineAll(burger_place_restaurants, [shake_shack]),

cuisine(CuisineType, Place):-
        cuisineAll(CuisineType, Places),
        member(Place, Places),

locationPlace(thayer_street, [yans, bajas, andreas, chinatown, kabob_n_curry, heng, mikes, east_side_pockets, shake_shack]),
locationPlace(fox_point, [pizza_marvin, dolores, tallulahs, bees, al_forno]),
locationPlace(wayland, [waterman_grille, red_stripe, pasta_beach, haruki, lims]),

locations(Location, Place):-
        locationPlace(Location, Places),
        member(Place, Places).



