# TheHypeShop #

### Full Stack Frameworks with Django Milestone Project 4 ###
By: Melville Ng

## Demo ##
Website site link can be found [here]( https://mel-thehypestore.herokuapp.com/)

## Aim ##
The aim of this project is to build an E-commerce website with Django. Through the website, user is able to buy apparel. 
Currently, I am selling my own apparel so creating a website for it. I can reach out to more target audience. 
The Target audience are people like me who like streetwear product. Furthermore, creating this website can help me to 
reach out to more people and gain more reputation in Singapore or International.

## UI ##
The intention to make the website modern looking, easy to navigate and comfortable on the eyes. 
Colours of white and grey are chosen to suit the different colourway of the product. 
Different colour of the button is used to make the site look livelier.

## UX ##
The website can store what the shop owner wants to sell to be available to view by customer. 
The website also able to create an account.
Bootstrap breakpoints are responsive for small, medium and large screens for the navigation bar. 
When the screen, reaches medium or small screen the navigation bar will change to be a hamburger icon on the top right corner of the website. 
Drop down menu will appear when u press the hamburger icon which will link you to different pages of the website. 
On large screen device the navigation bar will display all the link at the top.


## ER Diagram ##
ER Diagram can be found [here](https://github.com/melvilleng/CI_P4_TheHypeStore/blob/master/static/image/project%204%20er%20diagrams.PNG)

## User Stories ##
* As a Customer - I want to be able to see all the products so that I can buy.
* As a Customer – I want to be able to view individual product details so that I can know the price, description, look at the image and available sizes.
* As a Customer – I want to sort a specific category so that I can see the difference category product.
* As a Customer – I want to be able to search a product by its name so that I can easily find it.
* As a Customer – I want to be able to select size of the product when buying so that I can buy size I want.
* As a Customer – I want to be able to view the item in my cart so that I can tell the total cost of purchase. 
* As a Customer – I want to be able to adjust the quantity of the item in my cart so that I can change the quantity before buying.
* As a Customer – I want to fill safe and secure of my personal and payment details so that I can provide the require information to purchase.
* As a Customer – I want to be able to write a review so that I can leave a review for the shop.
* As a Site User – I want to be able to register an account so that I view my profile.
* As a Site User – I want to be able to login and log out so that I can access my profile.
* As a Site User – I want to be able reset password so that if I forgot my password I can reset it.
* As a Site User – I want to be able to view my profile so that I can view my order history and personal detail.
* As a Store Owner – I want to be able to add a product so that I can add new item to the store.
* As a Store Owner – I want to be able to update a product so that I can change the details in it.
* As a Store Owner – I want to be able to delete a product so that I can remove items that are not in stock anymore.

## Feature ##
* Navigation bar is on the top of the page. On mobile and tablet, the store logo remains on the left
Hand side and the burger logo is on the right-hand side.
On large screen device, the left-hand side has the company logo and when clicked it will bring you to the home page. Followed by The Hype Shop, Products and Reviews are also at the left hand side of the navigation bar. At the middle is the search bar.
On the right-hand side of the navigation bar are as follows:
* (when the site user is not logged in)
1.	Login
2.	Sign Up
3.	Cart
* (when the site user is logged in)
1.	Profile
2.	Log Out
3.	Cart
* (when staff or admin is logged in)
1.	Profile
2.	Log Out
3.	Cart
* The Footer is on every page except on stripe page and cart page. The footer will link back to home, there a search bar there, there two Icon that link to the Facebook or Instagram account.
* On the Login page, the user can login with username or email that the user has sign up for. If the site user does not have an account, he can sign up for it. There a forget Password link where they can click and request for a new password.
* On the Sign-up page, the new site user can sign up for an account by entering email, username, first name, last name, address, zip code, country, city, contact, password.
* On the profile page the user can see his profile on the left and order history on the right.
* The cart page can only be access if the user is logged in, at the cart page the user can click continue shopping to bring back to the product page or check out the item in cart.
* The product is where the site user can see all the product listed on the shop the can click on the view more and it will bring them to a more detail product page show the size and description and price where they can add to cart from. The detail product page u are able to click on the size chart and a size chart will pop up. U can also leave a review for the product and it will be display on the overall shop review.
* Just below the Nav bar the site user can sort between different category like shirts, pants, hoodie.
* The search bar they can search the product by its name to find for it. 
* There a back to the top button.
* When the staff or site admin login, they can see the creating listing on the nav bar where they can create listing to upload product to the website. They can write detail about the product like name, price, description.
* The staff or site admin also can edit or delete the product on the product page.

Future features
* Add a subscription feature

* Add rating feature to the review.

* Add a chat bot so the seller and buyer can contact each other through the website instead of email.

## Wireframes ##
Wireframes was created to help me to visualise and design a layout for my website. The wireframe can 
be view via this [link](https://github.com/melvilleng/CI_P4_TheHypeStore/tree/master/misc/wireframes).

## Technologies Used ##
Below are a list of framework, programming languages and tools used for the website:
* HTML
* CSS
* Javascript
* Jquery
* Bootstrap
* Python
* Django
* Postgres
* Font Awesome
* Gitpod
* Git
* Github
* Heroku
* DBeaver

### Testing ###
* Home Page:
    When I click on the The Hype Shop, Product, Reviews, Login, Sign up and Cart page button it will redirect me to the individual pages.
    The search feature is working. Tested with typing tee and only tee related product name will be shown.
* Sign up page
    Tested with filling in email, username, first name, last name, address, zip code, country, city, contact, password and press sign up.
    It will bring me to the page where ask the site user to verify the email address. A verifying confirmation email will be sent to the site user email address. Once the site user presses the link that was provided the site user will be ask to press confirm. Once confirm a message alert will show the email has been verified. The site user can now login. 

* Login Page
    After typing in the username or email and password I have register earlier I am able to be redirect to the home page.

   Press on the sign-up button it will redirect me to the sign-up page.
* Test on the forgot password feature and I can reset my password.

    After sign in the navbar got change to Profile, Logout ,cart on the right and on the left still remain the same.

* My Profile Page
The earlier Information I key in has been shown on the personal information table and on the right I can see the order history.
* Product Page
I am able to see all the product that the store offer when I click on the category and press on shirts. Only the shirts will appear. Likewise for pants and hoodie.
Once I click on view more it will bring me to the product detail page where when I press the sizes chart a size chart will pop up. 
Tested the back button and bring me back to the overall product page. 
Click on another product view more and try adding the item into cart.
Once I click the add to cart button I am bring to the cart page. 
* Cart Page
Tested the continue shopping button it will bring me back to the overall product page. Now I try adding another item to cart. The 2nd item got added successfully. The total sum for both the item are correct. 
Try the update quantity feature and the quantity change along with the price and total. All showing correct amount.
Tested the delete feature and the item was remove from cart.
Once I press the checkout button it will bring me to the stripe payment page. After typing in the email, card information (4242 4242 4242 4242) , the MM/YY and the CVC and name. I click on the pay button.
At the stripe payment page I tested the back button and it will bring me back to the cart.
So after pressing on the checkout button again and filling up the card information. The site will be redirect to the user profile page where they can see they order reflected in the order history and the flash message of your order has been place.
* Review
On each product details page at the button there a leave review section. Tested by filling in the require fill and click submit. After the site will be redirect to the review page where all the review will be at. The product name, item and by which user that leave a review and their review that they give for the product they brought.
* Logout
After that I tested the logout feature and the user account was logout.

* Testing with staff account or admin.(username=staff,password=m0n9b8v7)
With the staff account I click on the creating listing. 
Filling in all the forms and upload picture successfully. 
Tested the submit button and the product was listing on the overall product page.
The edit button on the listing will bring me to the edit listing page where I can edit each attribute. 
Tested one by one and all updated on what I change.
Tested the delete button and the listing is deleted.
Test the logout feature and the staff was logged out.





* Tested the website on mobile

The website was tested on different web browser and different mobile device. Device and browsers tested on are:

Ipad Safari MacBook Air – Google Chrome Safari Window laptop google chrome Microsoft Edge Iphone Safari Samsung S10 Google Chrome Samsung Web Browser




### Bugs ###
Have problem to get the total sum at the cart page. Only able to solve this issue after adding one price that will change and another just fixed to the item original price.
Have problem with getting to the stripe check out page after deployment to Heroku and fix it by changing the site link from the admin panel.




### Deployment ###
This project is deployed to Heroku and  is coded on Gitpod and respositories are on GitHub. The database that was initially use are on Django's sqlite and was transferred into Postgres when deploying to Heroku.

Heroku:
Create a new app and a Procfile that will allow the app to be deployed on Heroku.
Will need Django secret key, UploadCare secret & public keys, Stripe secret, publishable, endpoint secret keys, database url, email password and user in your .env file to be place at Heroku config.
On Gitpod I will login to Heroku first after that I will git push to Heroku master. 

## Credit ##
* Stockx
* [Original Fook](https://www.originalfook.com/)
* Stackoverflow
* Special thanks to my [lecturer](https://github.com/kunxin-chor/) for the guidance.

