const express = require('express');
const bodyParser = require('body-parser');
const methodOverride = require('method-override');
const path = require('path');

const app = express();
const PORT = 3000;

// Sample recipe data (in-memory storage)
let recipes = [
    {
        id: 1,
        title: "Classic Margherita Pizza",
        author: "Chef Mario",
        prepTime: "20 mins",
        cookTime: "15 mins",
        servings: 4,
        difficulty: "Easy",
        image: "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=800",
        ingredients: [
            "2 1/4 cups all-purpose flour",
            "1 cup warm water",
            "2 tsp active dry yeast",
            "1 tsp sugar",
            "2 tbsp olive oil",
            "1 tsp salt",
            "1 cup tomato sauce",
            "8 oz fresh mozzarella",
            "Fresh basil leaves"
        ],
        instructions: [
            "Mix yeast, sugar, and warm water. Let sit for 5 minutes.",
            "Add flour, salt, and olive oil. Knead until smooth.",
            "Let dough rise for 1 hour.",
            "Roll out dough and add sauce and cheese.",
            "Bake at 475°F for 12-15 minutes.",
            "Top with fresh basil and serve hot."
        ],
        category: "Italian",
        tags: ["vegetarian", "dinner"]
    },
    {
        id: 2,
        title: "Chicken Tikka Masala",
        author: "Chef Priya",
        prepTime: "30 mins",
        cookTime: "40 mins",
        servings: 6,
        difficulty: "Medium",
        image: "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800",
        ingredients: [
            "2 lbs chicken breast, cubed",
            "1 cup yogurt",
            "2 tbsp tikka masala spice",
            "3 cloves garlic, minced",
            "1 inch ginger, grated",
            "1 can (14 oz) tomato sauce",
            "1 cup heavy cream",
            "2 tbsp butter",
            "Fresh cilantro"
        ],
        instructions: [
            "Marinate chicken in yogurt and half the spices for 2 hours.",
            "Grill or pan-fry chicken until cooked.",
            "In a pan, sauté garlic and ginger in butter.",
            "Add tomato sauce and remaining spices.",
            "Stir in cream and simmer for 10 minutes.",
            "Add chicken and cook for 5 more minutes.",
            "Garnish with cilantro and serve with rice or naan."
        ],
        category: "Indian",
        tags: ["spicy", "dinner", "popular"]
    },
    {
        id: 3,
        title: "Chocolate Chip Cookies",
        author: "Baker Susan",
        prepTime: "15 mins",
        cookTime: "12 mins",
        servings: 24,
        difficulty: "Easy",
        image: "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=800",
        ingredients: [
            "2 1/4 cups all-purpose flour",
            "1 cup butter, softened",
            "3/4 cup granulated sugar",
            "3/4 cup brown sugar",
            "2 eggs",
            "2 tsp vanilla extract",
            "1 tsp baking soda",
            "1/2 tsp salt",
            "2 cups chocolate chips"
        ],
        instructions: [
            "Preheat oven to 375°F.",
            "Cream together butter and sugars.",
            "Beat in eggs and vanilla.",
            "Mix in flour, baking soda, and salt.",
            "Fold in chocolate chips.",
            "Drop spoonfuls onto baking sheet.",
            "Bake for 10-12 minutes until golden."
        ],
        category: "Dessert",
        tags: ["sweet", "baking", "kids-friendly"]
    }
];

// Middleware
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(methodOverride('_method'));

// Routes
app.get('/', (req, res) => {
    res.render('index', { recipes });
});

app.get('/recipes/:id', (req, res) => {
    const recipe = recipes.find(r => r.id === parseInt(req.params.id));
    if (recipe) {
        res.render('recipe', { recipe });
    } else {
        res.redirect('/');
    }
});

app.get('/add', (req, res) => {
    res.render('add');
});

app.post('/recipes', (req, res) => {
    const newRecipe = {
        id: recipes.length + 1,
        title: req.body.title,
        author: req.body.author,
        prepTime: req.body.prepTime,
        cookTime: req.body.cookTime,
        servings: req.body.servings,
        difficulty: req.body.difficulty,
        image: req.body.image || "https://images.unsplash.com/photo-1495521821757-a1efb6729352?w=800",
        ingredients: req.body.ingredients.split('\n').filter(i => i.trim()),
        instructions: req.body.instructions.split('\n').filter(i => i.trim()),
        category: req.body.category,
        tags: req.body.tags ? req.body.tags.split(',').map(t => t.trim()) : []
    };
    recipes.push(newRecipe);
    res.redirect('/');
});

app.delete('/recipes/:id', (req, res) => {
    recipes = recipes.filter(r => r.id !== parseInt(req.params.id));
    res.redirect('/');
});

// Start server
app.listen(PORT, () => {
    console.log(`🍳 Recipe Sharing App running at http://localhost:${PORT}`);
});
