# trulyTales
Blog Application using Django Python

![Screenshot 2023-08-01 at 9 53 38 PM](https://github.com/AkshayTakke/trulyTales/assets/54357275/f3fa6302-050d-4e8e-b3a8-d7ea214ce255)

<b>1.	Introduction<b>

In the introduction, the goals of the blogging web application are explained, with a focus on the goal of providing a dynamic and interesting platform for both writers and viewers. It talks about the app's benefits, like how users can sign up, create blog posts, sort them into categories, and share them on social media. The report shows how important it is for users to be able to share their thoughts and stories with a friendly group.

<b>2.	Research and Planning</b>

During the research and planning phase, I looked closely at current blogging platforms, surveyed users, and talked to bloggers to find out what they needed. The study shows what the research found, such as the most common problems bloggers and readers have and how the app's features solve those problems. The planning process includes information about the development schedule, how resources will be used, and how to measure the success of the application.

<b>3.	Choice of Framework and Technologies</b>

<b>Python</b>

Python version 3.11.1 will be added to this web project. Python is used to build web services on the server. This whole web app was made with Python and Django. Python is used in all parts of the project. Python was used to make the settings, files, and data models for the web app. A virtual setting is used to build the web application.

<b>Django Framework</b>

Django is a high-level, Python-based, open-source web framework that adheres to the Model-View-Controller (MVC) architectural pattern. It is made to help developers build web apps quickly, efficiently, and with a codebase that is clean and easy to manage. Django gives developers a powerful set of tools, libraries, and conventions that make it easier to do common web development chores. This lets developers focus on the logic of the application rather than the infrastructure that supports it.

<b>SQLite</b>

SQLite is a compact, self-contained, and server-less relational database management system (RDBMS) that is open-source. It is designed for embedded systems, mobile devices, and small to medium-sized applications that do not necessarily require a full-featured database server. SQLite is written in the C programming language and is extensively used because it is user-friendly, efficient, and simple to integrate into other programmes.

<b>PythonAnywhere:</b>

PythonAnywhere is a cloud-based integrated development environment (IDE) and web hosting infrastructure that enables users to compose, execute, and host Python applications. It offers a user-friendly interface and eliminates the need for users to set up and administer their own Python environments and servers, making it a popular option for both novice and seasoned developers.

<b>Html:</b> 

HTML stands for "Hypertext Markup Language." It is the most important part of a web page. It gives websites their structure and material, which lets them be shown on the internet and let people connect with them. HTML uses tags to describe the parts of a web page, with each tag standing for a different part or section. These tags are surrounded by angle brackets and tell the computer how to show the text.

<b>CSS:</b>

Cascading Style Sheets, or CSS for short, is a stylesheet language that modifies the visual appearance and structure of HTML files. In CSS, selectors identify certain HTML elements for which to apply styles, and declarations specify those styles. Elements, classes, IDs, and even element relationships (parent, child, sibling, and descendant) are all valid targets for selectors. Because of this granularity, designers may apply unique styles to certain regions of a page.

<b>UX Design</b>

![Flow_Diagram](https://github.com/AkshayTakke/trulyTales/assets/54357275/45ad9c7a-47ea-4929-9771-baf9a0de4625)


<b>Workflow</b>

<b>Homepage of Blog Application</b>

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/86eef074-7c62-4c09-a108-c6f03144149d)

 
The homepage contains three distinct sections. The homepage's right navigation bar displays the login, and Register sources, while the middle of navigation bar contains the search bar. Using the search bar located in the middle of the homepage, if the user may execute a search based on the blog posted on the website. User can see the list of all categories. On this homepage, all users blogs will be visible.

The homepage contains three distinct sections. The homepage's right navigation bar displays the login, and Register sources, while the middle of navigation bar contains the search bar. Using the search bar located in the middle of the homepage, if the user may execute a search based on the blog posted on the website. User can see the list of all categories. On this homepage, all users blogs will be visible.


<b>Login Page of User:</b>

In this login page, user should entered his username and password to login his blog account

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/b97b747b-5142-4a62-bc86-21b0de18bf76)

<b>Registration Page:</b>

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/ddee83e1-1526-43b9-91ad-a8d14d5c1543)

On this page, a new user can make an account and sign up for the job site. The person has to fill out all of the forms. Some validations are done at this point. If any of the validations don't match, like if the user's password and confirm password aren't the same, the user will see a message. It shouldn't be just a bunch of numbers, and it shouldn't be the same as our personal information. It must have at least eight characters. Emails need to be written correctly. Here are some examples of approval errors.

<b>Validations for registration page:</b>

In this figure, if you directly click on the register button it will show you the message as “Please fill in this field”.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/715b88fa-fd07-47b4-aadc-664c0cfeb508)

In the picture below, if the user entered their email address in the wrong style, the login page would show the following mistake message.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/29b485d6-70cc-4d42-a121-77cc7f4498a3)

The image below demonstrates that the new user has successfully created his account.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/d9600f54-6272-47cf-925e-6e008b0a41a6)

<b>Dashboard:</b>

When user login to the his account and click on his account there are three section i.e. Dashboard, Add Profile and Logout.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/0f790ce5-fec0-4169-b606-13895d70a952)

When a user clicks on his dashboard, he can view his details, edit his details, and view the blogs that he has posted.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/8d812742-42fe-4a27-b891-c2c0e29d7e35)

When a user wants to modify his profile, he can click the edit icon to make changes to his information and select the choose file option to submit his profile photograph.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/98e3b280-00f2-43a2-84b6-3a0710d53685)

After uploading a profile picture, it will be altered in the upper right corner as well as the dashboard.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/1d2a8784-916f-43fd-9230-3d28a86c7a2e)

<b>Add Posts</b>

User can click on Add Posts.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/a7fc5515-79c4-4073-80b9-ff9747c9cfee)

When a user clicks on a blog post, the image below will be displayed. When a user uploads a post, he will be able to format it using the following features, which are detailed in their respective descriptions.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/bedaa3d6-e88c-47fd-9d81-0c129422ffb7)


User can post related to food, travel and etc. user need to add title about post, description and category. After adding this details user can upload his post by clicking on submit button.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/b11eba57-ded3-4bbf-8d32-5d08aea2a301)

If you add any post, user will not be able to see in the all categories option. It will be only visible after admin will verify the post. 

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/beffb348-2e99-4eb0-a5b6-978fdc1fedfa)


![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/e88b84bd-f901-4866-b07e-d5fc57b73353)

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/2aa2d78e-eeb8-44ce-935c-b6d23b904869)


Now we can see the travel post in the All category section, it will only possible after verifying the post by admin.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/49b30704-948d-4db6-9ac7-c6427c2d0a7d)

If you click on read more  you will see the post which you have uploaded.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/5005c69d-8ca1-4ac2-b485-5097172fb3e5)

<b>Django Administrator:</b>

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/262e1b23-b77a-4e6d-a236-2feee9fb290e)

To access the admin interface, use the provided link: "http://127.0.0.1:8000/admin/login/?next=/admin/ ". The username and password are identical to the local SQLite login credentials.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/ec949b73-6536-4b5b-926a-587a05f89108)

In the illustration above, once the administrator logs in, he can view and add data as required by the web application.![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/55daee0d-22fb-4a10-87b6-afe66e923ca1)

<b>Blog Category</b>

Clicking "ADD BLOG_Category" will add the blog category to this section.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/65e91c98-106b-4faf-9be5-8cbb12ed3a7d)

In this section, the admin may see a list of all blog categories as well as the total number of blog categories.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/1c873f52-5fcf-4450-9017-7d829744787c)


The administrator may alter his password by selecting the "Change Password" option from the right corner. Once there, the administrator will be prompted to enter both his old and new passwords while adhering to the requirements outlined in the image that follows.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/b80673a6-07de-480d-bfa5-7c37210cf76a)


When the administrator clicks the logout button, he will be sent to the screen shown below.

![image](https://github.com/AkshayTakke/trulyTales/assets/54357275/61899849-ff3f-4b09-a914-a096fae830d7)


<b>Security threats and Measures</b>

<b>Content Moderation:</b>
Threat: Users may post inappropriate or malicious content, leading to reputational damage and legal issues for your blog.
Measure: Implement content moderation mechanisms, such as user flagging and automated content analysis, to identify and review potentially harmful content before it gets published.

<b>Secure Administrator Access:<b>
Threat: Unauthorized access to the administrator dashboard could lead to the compromise of the entire blog.
Measure: Enforce strong passwords, enable two-factor authentication (2FA) for administrators, and limit access to the dashboard based on IP addresses.

<b>Secure API Endpoints:<b>
Threat: Exposed or poorly secured API endpoints may allow attackers to access sensitive data or perform unauthorized actions.
Measure: Use Django REST framework and secure API endpoints with authentication and authorization mechanisms like OAuth or token-based authentication.

<b>Session Fixation:<b>
Threat: Attackers could exploit session vulnerabilities and hijack users' sessions.
Measure: Use Django's built-in session security features, enable session expiration, and regenerate session IDs upon login/logout.

<b>Guarding Your Data: Preventing Unauthorized Access</b>
Threat: Hackers may try to sneak harmful commands into your blog's database using user inputs.
Security Measure: Django automatically checks and filters user inputs to stop such attacks, keeping your data safe.

<b>Shielding from Harmful Scripts: Keeping Your Pages Secure</b>
Threat: Malicious actors may try to inject harmful scripts into your web pages.
Security Measure: Django's built-in protection blocks such scripts and ensures user-generated content is sanitized for safety.

<b>Keeping Actions Intentional: Foiling Unwanted Requests</b>
Threat: Attackers can trick your users into making unintended actions on your blog.
Security Measure: Django's CSRF protection ensures that only genuine requests are accepted, preventing unauthorized actions.

<b>How to run the project:</b>

<b>Step 1: Install Virtual Environment</b>
pip install virtualenv

<b>Step 2: Activate the Virtual Environment</b>
virtualenv env
Windows: env\Scripts\activate
Mac: source env/bin/activate

<b>Step 3: Install Django and Other Dependencies</b>
pip install -r requirements.txt

<b>Step 4: Run the Development Server</b>
python manage.py runserver

<b>Step 5: Access Your Django Project</b>
http://127.0.0.1:8000/




