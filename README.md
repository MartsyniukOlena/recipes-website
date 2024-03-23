___
# Gourmet: Ultimate Culinary Destination

Gourmet is a vibrant recipe-sharing platform and community hub for culinary enthusiasts worldwide. Users can discover a diverse array of recipes, share their culinary creations, and connect with fellow food lovers in the dynamic Gourmet Club.

Gourmet is targeted towards all culinary enthusiasts, from seasoned chefs to aspiring home cooks or those who are searching for inspiration to prepare tasty family food.

The live link can be found here - https://gourmet-website-52ef5f18a789.herokuapp.com/

![mockup](readme-media/mockup.png)

## Features

The Gourmet website offers several key features for its users.

### Existing Features
___

__Navigation Bar:__

The Navigation Bar is featured on all pages of the website. It is fixed, so the user should not scroll up to switch between the pages.  It enhances user experience by enabling quick access to different parts of the website and helps users find desired content without hassle.

Navbars are different for registered and not registered users.

The navbar includes the Logo with the link to the home page, Home page, Recipes page, Gourmet Club, Search form, Sign-in, Sign-up pages, and a short text indicating "You are not logged in".

![Navigation bar](readme-media/navbar.png)

The navbar includes the Logo with the link to the home page, Home page, Recipes page, Gourmet Club, Actions(My Recipes, Favourites, Add recipe), Search form, Log out page, a short text indicating "You are logged in as "username".

![Navigation bar](readme-media/navbar-loggedin.png)

__Footer:__

It is featured on all pages of the website.

![Footer](readme-media/footer.png)

Footer provides the copyright paragraph that protects intellectual property and also assures users that the content is up-to-date.

Social Media Links (Facebook, Twitter, Instagram, YouTube) allow users to follow the website on various platforms easily.This feature is useful for anyone interested in staying connected with Gourmet.

__Home Page__

- __Features Section:__

This section introduces the main features of the Gourmet platform, inviting users to explore its offerings.
It encourages user engagement by presenting clear calls-to-action to sign up, browse recipes, and learn more about the community.

![Features Section](readme-media/explore-gourmet.png)

- __Carousel:__

The carousel showcases visually appealing images related to the website's content, representing different types of dishes and ingredients.
It captivates users' attention with visually striking images, creating a memorable first impression, provides a dynamic and interactive element to the homepage, improving visual appeal and engagement.

![Carousel](readme-media/hero-1.png)
![Carousel](readme-media/hero2.png)
![Carousel](readme-media/hero3.png)

- __Featured Recipes Section:__

The section showcases selection of featured recipes, enticing users to explore more content, highlights noteworthy recipes, driving traffic to specific content pages and increasing user interaction, enhances content discovery by presenting a variety of recipes with accompanying images, titles, and excerpts.

![Featured Recipes](readme-media/featured.png)

#### Recipes Page

- __Recipe Entries Display:__

The page displays a list of recipe entries, each presented as a card with details such as title, image, cooking time, servings, author, and creation date. It provides users with a visually appealing layout for browsing multiple recipes at once.
Recipe titles are clickable, linking to the detailed view of each recipe. It enables seamless navigation to individual recipe pages for users interested in exploring further details or instructions.

![Recipe Entries Display](readme-media/recipes.png)

- __Pagination Navigation:__

Pagination allows users to navigate through multiple pages of recipe entries, when the number of recipes exceeds the display capacity of a single page. Each row contains a maximum of three cards.
It improves user experience by breaking down large sets of recipes into manageable pages, preventing overwhelming scrolling.

![Pagination Navigation](readme-media/pagination.png)

__Gourmet Club__

- __Club Image and Content Display:__

The page provides information about the club, its purpose and activities.
It includes the date when the club information was last updated that indicates the currency of the club's information, ensuring users are aware of the latest updates.

![Club](readme-media/club.png)

- __Event Registration Form:__

It allows users to register for upcoming club events by filling out a form, making it convenient for users to express interest and ask for details.
Facilitates event planning and management by capturing attendee information in an organized manner.

![EventForm](readme-media/join-us.png)

__My Recipes__

This page is for displaying a user's list of recipes, separated into published and draft recipes.

- __Published and Drafted Recipes Display:__

The page allows the user to easily access and review their recipes in one place, provides clickable titles to view detailed information about each recipe.

![My recipes](readme-media/my-recipes.png)


__Favorite Recipes:__

It gathers and presenting all recipes that the user likes for later access. It enhances user experience by providing an organized and visually appealing way to browse through favorite recipes.

![Favorite Recipes](readme-media/my-recipes.png)


__Adding Recipes__

The form provides a structured interface for users to input details about their recipe.
It standardizes the submission process, ensuring that all necessary information is collected in a systematic manner. This helps maintain data consistency and makes it easier for users to share their recipes.

![Add Recipe]()


__Recipe Detail Page__

The page displays detailed information about a specific recipe, including its title, excerpt, cooking time, servings, author, creation date, and featured image, igredients, instructions.
Provides users with comprehensive information about the recipe, helping them decide whether to try it. The inclusion of cooking time and servings allows users to assess the feasibility of preparing the recipe for their needs.

![Recipe Card](readme-media/recipes-detail.png)
![Content](readme-media/content.png)

Edit and Delete Options allow authenticated users who authored the recipe to edit or delete it.
It gives recipe authors control over their content, enabling them to make updates or remove outdated recipes as needed.

Add to Favorites allows users to add the recipe to their list of favorite recipes.
It enables users to bookmark recipes they enjoy for quick access later.

![Edit-Delete Recipe](readme-media/edit-delete-like.png)

Comments Section Facilitates user interaction by providing a platform for leaving comments on the recipe.
Encourages community engagement and discussion around the recipe.

Registered users can leave a comment, edit or delete it. It maintains the quality and relevance of the comment section.

![Comments](readme-media/comments.png)

__User Authentication__

- __Sign In Section:__ allows existing users to sign in to their accounts and personalized content.
Users can input their credentials (username and password) to authenticate themselves.

![Sign In](readme-media/sign-in.png)

- __Sign Out Section:__ allows authenticated users to sign out of their accounts. Displays a confirmation message asking users if they are sure they want to sign out.

![Sign Out](readme-media/sign-out.png)

- __Sign Up Section:__ enables new users to create an account.
Users can input necessary information (username, email, password) to register for an account.
If users already have an account, they are prompted to sign in instead.

![Sign Up](readme-media/sign-up.png)


__Delete Recipe and Comment Modal:__ provides a user-friendly way to confirm deletion actions, reducing the risk of accidental deletions and enhancing the user experience by prompting for confirmation before irreversible actions are taken.

![Delete Recipe](readme-media/recipe-delete-modal.png)
![Delete Comment](readme-media/coment-delete-modal.png)


## UX Design

### The user experience (UX) of all pages:

- Navigation bar: 

Navigation bar to direct users to different sections of the website.
Search Functionality: Search form allowing users to find specific recipes quickly.

- User Authentication Pages (Sign Up, Sign In, Sign Out):

Form Design: User-friendly forms for sign-up and sign-in processes with clear labels and instructions.

- Home Page:

Visuals: Features images of delicious food, enticing users to explore further.
Content: Highlights featured recipes to engage users.
Call to Action: Prompts users to sign up, browse recipes, or join the community.

- Recipe List Page:

Grid Layout: Recipes displayed in grid layout with images, titles, and brief descriptions.
Pagination: If there are many recipes, pagination controls to manage the content.

- Recipe Detail Page:

Recipe Presentation: Clear presentation of the recipe including title, image, cooking time, servings, author information, instructions, ingredients.
Interaction: Ability for users to favorite recipes, leave comments.

- Activity Feed: Overview of user's recent activity, such as recipes posted and drafted or recipes favorited.

- Add Recipe Page:

Form Design: Intuitive form for users to input recipe details, including title, excerpt, ingredients, instructions, images, servings, cooking time, status.
Validation: Validation checks to ensure all required fields are filled out correctly.
Image Upload: Option to upload images of the recipe for visual appeal.

- Club Page:

Club: Information about upcoming events, workshops, or cooking classes.
Joining Options: Clear instructions and forms for users to join the club.

### Messages:

Messages are used to provide feedback to users after performing actions, such as signing in, signing out, loging in, adding, editing, or deleting a recipe or comment. These messages are displayed using Django's built-in message framework (django.contrib.messages), ensuring that users are informed about the outcome of their actions.
Different message levels (e.g., messages.SUCCESS, messages.ERROR) are used to convey the nature of the message, whether it's a success message or an error message.
Messages enhance the user experience by providing immediate feedback, helping users understand the result of their interactions with the platform.

### Modal Dialogs:

Modal dialogs are used for confirmation prompts when performing critical actions like deleting a recipe or comment. These dialogs ensure that users confirm their intent before proceeding with potentially irreversible actions.


### Style

Body Font: Poppins, sans-serif a fallback font.

Colors:
#000000: Black

#FFFFFF: White

#E69C24: Amber

#234E5A: Dark Slate Blue

#00AB8C: Caribbean Green

#E84610: Cinnabar

#650000: Maroon

rgb(172, 175, 175): Dusty Gray

rgb(222, 146, 168): Pink Lavender

Images

Several static image are used on the website(three images depicting food and spices for carousel, a default image for recipes if the user doesn't upload their, placeholder for Club page, logo and favicon). Users can add images for thier recipes.

Fonts

the "Poppins" font is used for the website body, which was imported from Google Fonts. In case the main font fails to load properly, the backup font "Sans Serif" is used to ensure consistent readability across the site.

## Technologies

- [Django](https://www.djangoproject.com/) - web framework used for building the website.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - an authentication system for Django used for handling user authentication, registration, 
  account management.
- [Gunicorn](https://gunicorn.org/) - served as a production-ready server for running Django applications.
- [Psycopg2](https://www.psycopg.org/docs/) - enabled Django to interact with PostgreSQL databases.
- [PostgreSQL](https://www.postgresql.org/) - relational database management system.
- [Heroku](https://dashboard.heroku.com/login) - cloud-based platform used for deploying the site.
- [Responsinator](http://www.responsinator.com/) - program used to check how the site looks on the different devices.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - used during all website development for checking outcomes and for testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) - used to add heart symbol to Favorities button and navbar tab.
- [GitHub](https://github.com/) - stores, manages and allows to share the code.
- [Google Fonts](https://fonts.google.com/) - used to import fonts.
- [pep8ci](https://pep8ci.herokuapp.com/) - checked the Python code to ensure adherence to PEP8 standards.
- [Jshint](https://jshint.com/) - validated javascript code.
- [W3C Validator](https://validator.w3.org/) - validated html code.
- [W3C Validator](https://jigsaw.w3.org/css-validator/validator) - validated css code.
- [ColorsSpace](https://mycolor.space/) - Used to create colour palette.
- [Favicon](https://favicon.io/) - used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database diagram.
- [Grammarly](https://app.grammarly.com/) - used to check grammar and edit text.
- [Summernote](https://summernote.org/) - an editor to styly recipes.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - a library that integrates Bootstrap 5 with Django forms through Django-Crispy-Forms. It provides 
   Bootstrap 5 styling for Django forms.
- [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) - it was used to serve static files efficiently in production environments.
- [Cloudinary](https://cloudinary.com/) - it was used for storing and serving media files in the application.
- [Bootstrap 5.0.2](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - used to create responsive, mobile-first front-end website.

## Testing

### Responsiveness Testing

The primary goal of responsiveness testing was to ensure that a website provides user experience across different devices and platforms. For this reasons testing was performed with Responsinator and Chrome Dev Tools.
The resuts are the following:

![Responsiveness Testing](readme-media/responsivness-testing.png)

### Compatibility Testing:

The website was tested in different browsers - Chrome, Firefox, Edge
The website was tested in Windows and Android.


### Bugs resoled and unresolved:

Resolved bugs:
    - Add Itegrity Error to the add_recipe view to inform a user that the recipe with the same title exists so the user chooses the different title.

Unresolved bugs:
    No unresolved bugs.


### Performance Testing:

Performance testing was done with Lighthouse. The current results are the following:

Desktop
Home Page
![Home Page]()
Recipes Page
![]()
Gourmet Club Page
![]()
My Recipes Page
![]()
Favorities
![]()
Add Recipe
![]()
Sign In
![]()
Sign Up
![]()
Log Out
![]()
Search Reslts
![]()
Edit Recipe
![]()

Mobile
Home Page
![Home Page]()
Recipes Page
![]()
Gourmet Club Page
![]()
My Recipes Page
![]()
Favorities
![]()
Add Recipe
![]()
Sign In
![]()
Sign Up
![]()
Log Out
![]()
Search Reslts
![]()
Edit Recipe
![]()