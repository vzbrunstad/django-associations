# Django Associations

Now that you have some familiarity with reading and validating records from the database, it's time to explore **associations**. 

In this challenge you'll be using the following django associations:

* `ForeignKey #for one to many associations`
* `ManyToManyField #for many to may associations:`
* `ManyToManyField with through #for adding additional fields to a join table`

## Model Attributes

This challenge is focused on modeling the relationships between models, not the models themselves. For that reason unnecessary model attributes are not considered part of this challenge. For example an `Actor` model would likely have `first_name` and `last_name` columns as part of the `actors` table, but in this challenge you only need create the necessary `id` & foreign key columns.


## Release 0: IMDB Example

You will create simple schema for the website [IMDB](http://imdb.com) which catalogs movies and actors.

This schema includes three models:

* Actor
* Role
* Movie

The models can be found in `moviedb/models.py`

The `Role` model joins `Movie` and `Actor.` Via this join model, a movie has many actors and an actor can act in many movies.

Run `createdb imdb` to create the database. Then, set up your models with the appropriate associations. Use the [django documentation](https://docs.djangoproject.com/en/2.1/topics/db/examples/) to help you out. It is important to get comfortable reading through documentation.

After you set up your models run `python3 manage.py makemigrations` and then `python3 manage.py migrate`. If you make alterations to your models you may have to rerun these two commands to update your database and get the tests to pass.

After you set up your models, you can run `python3 manage.py test`. If you get any error messages, let them guide you toward a solution. 


## Release 1: Medium

Run `createdb medium`. After you set up your models run `python3 manage.py makemigrations` and then `python3 manage.py migrate`. If you make alterations to your models you may have to rerun these two commands to update your database and get the tests to pass. 

### Models
* Post
* User
* Comment

### Association Methods
```ruby
post.user # the author of the post
post.comments

user.posts
user.comments

comment.user
comment.post
```

## Release 2: Amazon

Run `createdb amazon`. After you set up your models run `python3 manage.py makemigrations` and then `python3 manage.py migrate`. If you make alterations to your models you may have to rerun these two commands to update your database and get the tests to pass. 

### Models
* Shop
* Product
* Review
* User

### Association Methods
```ruby
shop.owner # should return a User
shop.products # products sold by this shop

product.shop
product.reviews

review.product
review.user

user.reviewed_products
user.shop # if this user owns a shop, returns the shop. For most users this would return nil.
```

## Release 3: Uber Eats

Run `createdb uber_eats`. After you set up your models run `python3 manage.py makemigrations` and then `python3 manage.py migrate`. If you make alterations to your models you may have to rerun these two commands to update your database and get the tests to pass. 

### Models
* Order
* OrderItem (a join model that links orders and menu items)
* MenuItem (e.g. burrito or cesar salad)
* User (customers)
* Driver (employees of Uber Eats)


### Association Methods
```ruby
order.order_items
order.menu_items
order.driver
order.customer # returns a User

driver.orders
driver.customers # returns the Users they are delivering orders to

order_item.order
order_item.menu_item

menu_item.orders # all the orders this MenuItem was featured on

user.orders
user.order_items
user.menu_items
```

