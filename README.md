# Skincare Survey


![Skincare Survey](assets/readme_files/SkincareSurvey.png)

[View the live project here](https://lukyhet.github.io/Project_three/)


## Introduction

Our app offers the possibility to apply a survey that gathers important information for companies interested in launching new skincare products. The app works by collecting possible customers preferences through a 10 questions survey. The survey asks about the potential customer skincare habits, age and skin type to compile it and give results that can show what is the most common skin type, the most favourite skincare product or the customers packaging preferences. This resulst have the potential to be used in market studies for companies intested in the data and it was made to facilitate their access to the skincare markets information directly taken from skincare consumers. The target audience is companies, entrepreneurs, students and researchers that are interested in having access to data about skincare consumers preferences.


<details>

Skincare Survey app is a tool created for comercial research purposes. It is an automated survey that has ten different questions about the skincare habits and preferences of a skincare consumer group.

This app was made as the third milestone project to achieve the Diploma in Software Development at the Code Institute. 

The purpose of this project is the automation of a survey that gathers information and gives results obtained from the 10 answers to the same number of questions about skincare preferences and habits. The main goal is to build a back end site using python that responds to the users actions, allowing the user to analize the data and use it for their comercial or research goals.

![Skincare Survey](assets/readme_files/SkincareSurvey2.png)


## UX
###  User Demographic
The user for this website is: 

- Companies, entrepreneurs, students and researchers that want collect skincare consumers market data to create and sell new skincare products to young and adult skincare consumers, or just for research purposes. The skincare consumers are people who has a skincare concern and who are interested in purchasing new skincare products to tackle their skin problems. 


#### User Goals

- To apply a survey/research tool aimed to gather information from potential consumers/users to help define what skincare product would be best to create and sell according to the preferences of the potential consumers. 
- Gather information for research pouposes. 
- Have an efficient and automated instrument (survey) to apply that also automates the process of updating the database.
- Have clear results and data to work with.


## Features 

This is a back-end application made using python. 

The app applies a survey that poses 10 different questions about skincare habits and preferences, some of them offer answer options and others are simple yes or no questions. The client/user can use the app both for applying the survey meaning collecting the data, and producing the results. The app can both read the information from the base (google sheets skincare_survey document) and write on it, updating it form the app.

The functions in the app contain validation code that accepts only the correct kind of input from the user.

As the survey app asks some questions that offer several options of answers, in the case of a tie the app can report it in the results, showing for example the two or three most prefered skincare products.


#### Wireframes
  

- This project is a back-end app and it does not involve aesthetic design, the blueprints of the project or initial work was done by creating the questions and answer options that would collect the specific data to offer valuable results for clients interested in launching a successful new skincare product or for skincare consumers market researchers.


## Debugging

Some of the problems detected by gitpod have to do with non fatal errors like long lines of code that are related to the lenght of the questions and answer options.

A bug related to printing a result in case of a tie instead of a blanck space was detected and fixed by including lines of code that would print if the options are equal in value (==) and stil mayor than other options (>=).

`if (acids_list_len == serum_list_len) and (acids_list_len == moisturizer_list_len):
        print('All products sold equally')
    else:
        print('Most selling product is %s' % most_common)`

Other kind of bugs that were detected had to do with validation of input in the functions. It was necessary adjust and correct.

Other bug was related to the deployment of the app in Heroku, there was an incompatibility between versions of the packagest installed at the requirements.txt file. The solution was to run the command:

`pip3 freeze > requirements.txt`


### Features to Implement in the future

- **Recommendations**

- We would like to include an option in the app that would add a third step after processing the data  and then come up with recommended options for potentially successful skincare products, but we are conscious that the process to come to those sugestions requires to collect more data and perhaps other market reading strategies.
     

## Main Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wikipedia") provided by the CI template for this project.
- [JS](https://en.wikipedia.org/wiki/JavaScript "Link to JS Wikipedia") provided by the CI template for this project.
- [PY](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to PY Wikipedia")main code source of this back-end project.


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
     - In google Cloud we have enabled the Google Sheets API (which writes and reads in Google Sheets) and Google Drive API (which access our data stored in google drive).
-[google-auth](https://google-auth.readthedocs.io/en/master/ "Link to documentation about the libary") 
Dependancy used in this project as google authentication library for google API for python.
-[gspread](https://docs.gspread.org/en/latest/ "Link to documentation of the libary") 
Used in this project as pythons API for google sheets.




</details>


## Testing


The PEP8 Validator was used to validate all the code of this repository and the errors detected were corrected.


-PEP8 Validator ![PY](http://pep8online.com/checkresult)

![Skincare Survey python code validation](assets/readme_files/ValidationPy1.png)

![Skincare Survey python code validation](assets/readme_files/ValidationPy5.png)

![Skincare Survey python code validation](assets/readme_files/ValidationPy8.png)



## Deployment

This project was deployed in Github [View the live project here](https://lukyhet.github.io/Repository-Two/).

### Deploying on GitHub Pages

To deploy this site from the GitHub repository, the following steps were taken:


-  Once in our github account, click in the [GitHub Repository](https://lukyhet.github.io/Project_three/ "Link to repository").
-  In the repository, select Settings from the menu items.
-  Scroll down the Settings page to the "Pages" section.
-  Under "Source" click the drop-down menu labelled "None" and select "Main".
-  Upon selection, the page will automatically refresh meaning that the website is now deployed.
-  Scroll back down to the "Pages" section to retrieve the deployed link.

     
### Deploying on Heroku

The Skincare Survey app was deployed in Heroku - [View the heroku app here](https://skincare-survey.herokuapp.com/ "Link to Heroku app")


**In the terminal** 

-. Add the requirements by writing this command in the terminal: "pip3 freeze --local > requirements.txt"
-. Git add . and git commit your changes.

**Go to your heroku account**

. Log into [Heroku](https://dashboard.heroku.com/apps). If you don't have an account create one.

. In the top right corner click "new" and select "Create new app".

. Create a name for your app. It must be unique.

. Choose Region - Ex: "Europe".

. Click "Create App".

**Your project page**

. In the Resources Tab, Add-ons, look for "Heroku Postgres" and select it.

. Go to menu in the top of the page and choose "settings".

. Go to "Config Vars" and click "Reveal Config Vars". 

. Add the below variables to the list

    * Database URL will be added automaticaly
    * In the field for Key we write CREDS, then paste the content of our creds.json file as value, ten click add. 
    * Go to the right side of the page and Add the buildpack "Python". Save the changes.
    * Go to add buildpack again in the right side of the page and add node.js. Save the changes. Check that python is on top and node.js underneath, if not, drag and change the order.

. Go to the menu and click in the deployment method, select gitHub. Click "connect to GitHub"
. Enter your GitHub repository name and click search and then click "connect".
.Choose to manually or automatically deploy then we should see "The app was successfully deployed message".
. Click in "view" to take a look at your app. If you need to restart in click "Run Program".

**Go back to your code**

12. Procfile needs to be created in your app
```
web: gunicorn PROJ_NAME.wsgi
```

13. In settings in your app add Heroku to ALLOWED_HOSTS

14. Add and commit the changes in your code and push to github

**Final step - deployment**

15. Next go to "Deploy" in the menu bar on the top 

16. Go to section "deployment method", choose "GitHub"

17. New section will appear "Connect to GitHub" - Search for the repository to connect to

18. type the name of your repository and click "search"

19. once Heroku finds your repository - click "connect"

20. Scroll down to the section "Automatic Deploys"

21. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

22. Click "Deploy branch"

Once the program runs:
you should see the message "the app was sussesfully deployed"

23. Click the button "View"

The live link can be found [here](https://mileage-tracker-app.herokuapp.com/).

    
## Credits 


### Code 

Several sources were consulted and their guides followed, for example:

- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
-[Stack Overflow](https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python/ "Link to Stack Overflow ansers about fixing long lines errors in Python")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page") 


### Media

- Google sheets [Google Sheets](https://docs.google.com/spreadsheets/u/0/ "Link to Google Sheets") 
- Heroku [Heroku](https://id.heroku.com/login "Link to Heroku")
- Google Cloud Platform [Google Cloud](https://console.cloud.google.com/home/dashboard?project=skincaresurvey "Link to Google Cloud Platform")
- Google Drive [Google Drive](https://www.google.com/intl/es/drive/ "Link to Google Drive")


## Acknowledgements

- I want to thank and recognize once again the amazing job of my mentor Antonio Rodriguez who has guided me in a clear way during this project. 
- I also want to mention and thank the student tutors service at Code Institute.


[Back to top](#Skincare Survey)

***



-----