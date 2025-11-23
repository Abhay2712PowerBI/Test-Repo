# 🍳 RecipeShare - Recipe Sharing Web App

A modern, responsive Node.js web application for discovering and sharing amazing recipes.

## Features

✨ **Modern & Responsive Design**
- Beautiful gradient hero section
- Card-based recipe layout
- Fully responsive (mobile, tablet, desktop)
- Smooth animations and transitions

🎯 **Core Functionality**
- View all recipes with images
- Detailed recipe pages with ingredients & instructions
- Add new recipes with a beautiful form
- Delete recipes
- Recipe categorization and tags
- Difficulty levels (Easy, Medium, Hard)
- Prep time, cook time, and servings info

## Tech Stack

- **Backend:** Node.js, Express.js
- **Templating:** EJS
- **Styling:** Custom CSS with modern design
- **Data Storage:** In-memory (can be extended to database)

## Installation

1. **Navigate to the project directory:**
   ```bash
   cd "c:\Companies Courses\GIT\Test-Repo\recipe-app"
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the server:**
   ```bash
   npm start
   ```

   Or for development with auto-reload:
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   ```
   http://localhost:3000
   ```

## Project Structure

```
recipe-app/
├── app.js              # Main Express server
├── package.json        # Dependencies & scripts
├── views/              # EJS templates
│   ├── index.ejs       # Home page with recipe grid
│   ├── recipe.ejs      # Single recipe detail page
│   ├── add.ejs         # Add new recipe form
│   └── layout.ejs      # Layout template
└── public/             # Static files
    └── css/
        └── style.css   # Custom styles
```

## Usage

### View Recipes
- Browse all recipes on the home page
- Click "View Recipe" to see full details

### Add a Recipe
1. Click "+ Add Recipe" in the navigation
2. Fill in all required fields:
   - Title, Author, Category
   - Prep time, Cook time, Servings
   - Difficulty level
   - Ingredients (one per line)
   - Instructions (one step per line)
3. Optionally add image URL and tags
4. Click "🎉 Publish Recipe"

### Delete a Recipe
- Click the 🗑️ button on any recipe card
- Or use the "Delete Recipe" button on recipe detail page

## Sample Data

The app comes with 3 pre-loaded recipes:
- Classic Margherita Pizza (Italian)
- Chicken Tikka Masala (Indian)
- Chocolate Chip Cookies (Dessert)

## Customization

### Change Colors
Edit the CSS variables in `public/css/style.css`:
```css
:root {
    --primary-color: #FF6B6B;
    --secondary-color: #4ECDC4;
    --accent-color: #FFE66D;
}
```

### Add Database Support
Replace the in-memory `recipes` array with:
- MongoDB with Mongoose
- PostgreSQL with Sequelize
- SQLite with better-sqlite3

### Add User Authentication
Integrate:
- Passport.js for authentication
- Express-session for session management
- bcrypt for password hashing

## Future Enhancements

- 🔍 Search and filter recipes
- ⭐ Rating system
- 💬 Comments and reviews
- 👤 User profiles and authentication
- 📱 Progressive Web App (PWA)
- 🗄️ Database integration
- 📷 Image upload functionality
- 🔖 Save favorite recipes

## License

MIT License - feel free to use this project for learning or personal use!

---

Made with ❤️ for food lovers
