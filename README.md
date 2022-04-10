# Skincare Survey


![Skincare Survey](assets/readme_files/SkincareSurvey.png)

[View the live project here](https://lukyhet.github.io/Project_three/)

## Introduction

Our app offers the possibility to apply a survey that gathers crucial information for companies interested in launching new skincare products. The app works by collecting possible customers preferences through a 10 questions survey. The survey asks about the potential customer skincare habits, age and skin type to compile it and give results that can show what is the most common skin type, the most favourite skincare product or the customers packaging preferences. This resulst have the potential to be used in market studies for companies intested in the data and it was made to facilitate their access to the skincare markets information directly taken from skincare consumers. The target audience is companies, entrepreneurs, students and researchers that are interested in having access to skincare consumers preferences.


<details>

Skincare Survey app is a tool created for comercial research purposes. It has ten different questions about the skincare habits and preferences of a skincare consumer group.

This app was made as the third milestone project to achieve the Diploma in Software Development at the Code Institute. 

The purpose of this project is the application of a survey that gathers information and gives results obtained through 10 questions about skincare preferences and habits. The main goal is to build an app/back end site that responds to the users actions, allowing the user to analize the data and use it for their comercial or research goals.


## UX
###  User Demographic
The user for this website is: 

- Companies, entrepreneurs, students and researchers that want collect skincare consumers market data to create and sell new skincare products to young and adult skincare consumers, or just for research purposes. The consumers are people who has a skincare concern and who are interested in purchasing new skincare products to tackle their skincare problems. 


#### User Goals

- To apply a survey/research tool aimed to gather information from potential consumers/users to help define what skincare product would be best to create and sell according to the preferences of the potential consumers. 
- Gather information research pouposes. 
- Have an efficient and concise instrument (survey) to apply.
- Have clear results and data to work with.


## Features 

This is a back end application made using python. 

The app applies a surve that poses ten different questions about skincare habits and preferences, some of them offer answer options and others are simple yes or no questions. The client/user can use the app both for applying the survey meaning collecting the data, and producing the results. The app can both read the information from the base google sheets skincare_survey document and write on it, updating it form the app.

The functions in the app contain validation code that accepts only the correct kind of input from the user.

The app has some questions that offer several options of answers, in the case of a tie the app can report it in the results, showing for example the two or three most prefered skincare products.


#### Wireframes
  

- This project is a back end app and it does not involve aesthetic design, the blueprints of the project or initial work was done by creating the questions and answer options that would collect the specific data to offer valuable results for clients interested in launching a successful new skincare product or for skincare consumers market researchers.


## Debugging

Some of the problems detected by gitpod have to do with non fatal errors like long lines of code that are related to the lenght of the questions and answer options.

A bug related to printing a result in case of a tie instead of a blanck space was detected and fixed by including lines of code that would print if the options are equal in value (==) and stil mayor than other options (>=).

`if (acids_list_len == serum_list_len) and (acids_list_len == moisturizer_list_len):
        print('All products sold equally')
    else:
        print('Most selling product is %s' % most_common)`

Other kind of bugs that were detected had to do with validation of input in the functions. It was necessary adjust and correct.

The last bug that appeared was related to the deployment of the app in Heroku, there was an incompatibility between versions of the packagest installed at the requirements.txt file. The solution was to run the command:

`pip3 freeze > requirements.txt`


### Features to Implement in the future

- **Recommendations**

- We would like to include an option in the app that would add a third step after processing the data  and then come up with recommended options potentially successful skincare products.
     

## Main Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wikipedia") provided by the CI template for this project.
- [JS](https://en.wikipedia.org/wiki/JavaScript "Link to JS Wikipedia") provided by the CI template for this project.
- [PY](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to PY Wikipedia")


### Frameworks, Libraries & Programs Used

- [GitPod](https://gitpod.io/ "Link to GitPod homepage")
     - GitPod was as workspace for writing code,
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub is being used to store this repository.
- [Heroku](https://heroku.com/ "Link to Heroku")
     - Heroku is being used to deploy and host the app.
- [Google Sheets](https://docs.google.com/ "Link to Google Sheets")
     - Google Sheets is being used to host and consolidate the information of the survey.
- [Google Cloud](https://console.cloud.google.com/home/dashboard?project=skincaresurvey "Link to Google Cloud Platform")
     - Google Sheets is being used to store the information of the survey.




</details>


## Testing


The PEP8 Validator, was used to validate all the code of this repository and most warnings were corrected with the exception of those last ones that reported line too long (114 > 79 characters) because of the lack of time for this project.

-PEP8 Validator ![PY](http://pep8online.com/checkresult)



## Deployment

This project was deployed in Github [View the live project here](https://lukyhet.github.io/Repository-Two/). And the app was deployed in Heroku - [View the heroku app here](https://skincare-survey.herokuapp.com/ "Link to Heroku app")

    
## Credits 


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