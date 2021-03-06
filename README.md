# DATAPOEM_assignment

Name: vishnu sai bhonsle,
SRN: R18cs081,
branch: CSE,
University: REVA University.

# Section-1 

# Problem statement:(first question)

Create a product list API that must return X number of products. It should include name, price, description, date of manufacture, stocks and any other fields that you might think are relevant. The products can be stored in any DB of your choice (Must have at least 200 products). And develop a web app that must reflect the contents of the product list API and must fulfill three basic functional requirements.
1. Create a login system where users can signup or login. On logging in, it shows them their profile and wallet. They can add money to this wallet using an API. (Dummy transaction.) 
2.  In the profile screen, users can enter a location and it will show the weather in that location.
3.  The user should be able to view the dummy products in a dashboard and can buy them using the money in the wallet. This should cause his wallet to be updated along with the stock of the product

# Solution:

1) In this web application users can able to login or signup using their user name and password.

 2) After login, the user can view the name, wallet balance and be able to add money to the wallet by using our dummy transition page.

3) The user can access weather details by entering the name of the location on profile page.


4)  the user can buy products on the products page using their wallet amount and a notification will be given to the user on their transition status.

# Stacks used to develop web application are:

1) HTML,CSS ,JS -  frontend
2) Flask (python)- Backend
3) Firestore(firebase)- Database

# Hosting link:

http://vishnudatapoem.pythonanywhere.com/

# Results:

## Login page and singup pages:

![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img1.png?raw=true)
![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img2.png?raw=true)
![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img3.png?raw=true)


## Profile page and features:

### profile page:
![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img4.png?raw=true)
### weather api:
![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img5.png?raw=true)
![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img6.png?raw=true)

### Add Money to wallet:

![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img10.png?raw=true)

## product page:
![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img7.png?raw=true)

### product display API -

#### - https://vishnudatapoem.pythonanywhere.com/products

![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img7.png?raw=true)

### After successfull transtation

![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img8.png?raw=true)

### In case of unsuccessfull transtation

![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img9.png?raw=true)


# Section-2 

# Problem statement:(third question)

The system should have the following specifications1. It should have the two models as APIs.
2. Usage with only backend - for simplicity, we should be able to use Postman ( API
hitting tool ) by sending input values of the ML model as parameters (with model
number ) in the API call and the results of the model can be displayed on the terminal
after being predicted by the models

# Solution:

## part -1

Dataset--https://www.kaggle.com/laleeth/salary-predict-dataset

1) in this API we used linear regression(model) method to predict the salary by taking experience,test_score,interview_score as input

Result:

![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img12.png?raw=true)

Due to limitation in free hosting server unable to host api in server

![alt text](https://github.com/vishnu4044/DATAPOEM_assignment/blob/main/images/img11.png?raw=true)


