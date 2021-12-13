# Skincare Survey


![Skincare Survey]

[View the live project here](https://lukyhet.github.io/Project_three/)

## Introduction

Our app is a survey that gathers information for companies interested in launching new skincare products or lines of skincare products. It was made facilitate the acces of market information to skincare sellers form skincare consumers. The target audience is comapnies and entrepeneurs that are interested in creating and launching new skincare lines or products.

<details>


Skincare Survey app is a tool created for comercial purposes. It has ten different questions about the skincare habits and preferences of a target skincare consumer group

This Trivia was made as the second milestone project to achieve the Diploma in Software Development at the Code Institute. 

The purpose of this project is the application of a survey that gathers information and gives results obtained through 10 questions about skincare preferences and habits. The main goal is to build an app/back end site that responds to the users' actions, allowing the user to analize the data and use it for their comercial goals.


## UX
###  User Demographic
The user for this website is: 

- Companies or etrepeneurs that want to create and sell new skincare products to young and adult skincare consumers. The consumers are people who has a skincare concern and who are interested in purchasing new skincare products to tackle their skincare problems. 


#### User Goals

- To apply a survey/research aimed to gather information in order tht will help the client/user to define what skincare product would be best to create and sell according to the preferences of the potential consumers. 
- Have an efficient and concise instrument (survey) to apply.
- Have clear results and data to work with.


## Features 

This is a back end application made using python. 

The app that displays ten different questions about skincare habits and preferences, some of them offer answer options and others are simple yes or no questions. The client/user can use the app both for applying the survey meaning collecting the data, and producing the results. The app can both read the information from the base google sheets skincare_survey document and write on it, updating it form the app.

The app has some questions that offer several options of answers, in the case of a tie the app can report it in the results, showing for example the two or three most prefered skincare products.


#### Wireframes
  

- This project is a back end app and it does not involve aesthetic design, the blueprints of the project or initial work was done by creating the questions and answer options that would collect the specific data to offer valuable results for clients interested in launching a successful new skincare product.


## Debugging

Some of the problems detected by gitpod have to do with non fatal errors like long lines of code that are related to the lenght of the questions and answer options.

A bug related to printing a result in case of a tie instead of a blanck space was detected and fixed by including lines of code that would print if the options are equal in value (==) and stil mayor than other options (>=).

`if (acids_list_len == serum_list_len) and (acids_list_len == moisturizer_list_len):
        print('All products sold equally')
    else:
        print('Most selling product is %s' % most_common)`

Other kind of bugs that was about defining functions. It was necessary to double check on the correct definition of functions.

The last bug that appeared was related to the deployment of the app in Heroku, there was an incompatibility between versions of the packagest installes at the requirements.txt file. The solution was to run the command:

`pip3 freeze > requirements.txt`


### Features to Implement in the future

- **Recommendations**

- We would like to include an option in the app that would process the results and come with recommended options for skincare products.
     

## Main Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wikipedia") provided by the CI template for this project.
- [JS](https://en.wikipedia.org/wiki/JavaScript "Link to JS Wikipedia") provided by the CI template for this project.
- [PY](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to PY Wikipedia")


### Frameworks, Libraries & Programs Used

- [GitPod](https://gitpod.io/ "Link to GitPod homepage")
     - GitPod was as workspace for writing code,
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub is being used to store this repository.



</details>


## Testing


The PEP8 Validator, was used to validate all the code of this repository and every warning was corrected until the code came up clean in the validator mentioned.

-PEP8 Validator ![PY](http://pep8online.com/checkresult)



## Deployment

This project was deployed in Github [View the live project here](https://lukyhet.github.io/Repository-Two/).

    
## Credits 

### Content

- 

### Code 

Several sources were consulted and their guides followed, for example:

- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page") 

### Media

- Google sheets [Google Sheets](https://docs.google.com/spreadsheets/u/0/ "Link to Google Sheets") 
- Heroku [Heroku](https://id.heroku.com/login "Link to Heroku")
- Google Cloud Platform [Google Cloud](https://console.cloud.google.com/home/dashboard?project=skincaresurvey "Link to Google Cloud Platform")


## Acknowledgements

- I want to thank and recognize once again the amazing job of my mentor Antonio Rodriguez who has guided me in a really clear and commited way during this project. 
- I also want to mention and thank the student tutors service at Code Institute.


[Back to top](#Skincare Survey)

***



-----