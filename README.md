![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Project Scope
The Garage Management System will encompass a comprehensive user module with robust authentication and authorization mechanisms, ensuring secure access for various user roles including Admin, Customer, and Garage Technician. The system will feature a customer management interface for registration, profile management, and a self-service portal to view service records and invoices. Employee management will include role assignments and detailed profiles, facilitating efficient operational workflows. A secure JWT-based authentication process will be implemented, along with role-based access control to regulate permissions for different functionalities, thereby ensuring a secure and streamlined user experience.

This project aims to streamline garage operations by providing an efficient platform for booking and managing automobile services. When you first start it, register and login, you will be on the home page which displays a dashboard with upcoming appointments and service details. The core functionality of this system is to enable customers to easily book their vehicles for servicing and other related tasks, allowing the garage to manage and schedule its operations effectively. In vehicle management, admins can add vehicle details including pictures and prices for vehicles that are for sale, and customers can view these vehicles and their details. This feature enhances the service offering by allowing customers to explore and purchase vehicles directly through the system.

Note: The system will track various services and generate statistics on a daily, weekly, and monthly basis. For instance, it can show how many oil changes were performed in a week, the total revenue generated from specific services, and the overall performance of different technicians.

Note: For this system to work effectively, you need to create service categories (e.g., oil change, tire replacement) and when a booking is made, you can choose a service and time slot for that service on a particular date. The description for the service will narrow down the specifics of what needs to be done within the allocated time slot. When you want to see a breakdown of services provided for a particular category, you can navigate to statistics and choose a date range and service category. This will display a tabulated result for each task within the dates chosen, showing hours, minutes, date, and task details in a table, along with totals to show overall time and revenue for the service category within the chosen dates.

Services could include various maintenance and repair tasks, where you can manage multiple services/projects on a daily basis within specific time slots. The description would be crucial here to break down exactly what needs to be done within the time window on a particular date.

The Garage Management System will provide a comprehensive solution for managing garage operations, enhancing customer service, and improving administrative efficiency. This system will help garages to streamline their booking processes, track service performance, and gain valuable insights into their operations, ultimately leading to better time management and increased productivity.

## Project Epics and User Stories

Here are the parent epics, user stories, and associated tasks:

#### Epic 1: Authentication and Authorization

- User Story 1: As a user, I want to be able to register for an account so that I can access the system. (#1)
    - Task 1.1: Design registration form
    - Task 1.2: Implement registration logic
    - Task 1.3: Test registration functionality
- User Story 2: As a user, I want to be able to log in to my account so that I can access the system. (#2)
    - Task 2.1: Design login form
    - Task 2.2: Implement login logic
    - Task 2.3: Test login functionality

#### Epic 2: Dashboard

- User Story 4: As a user, I want to see a dashboard with relevant information so that I can quickly access key features. (#4)
    - Task 4.1: Design dashboard layout
    - Task 4.2: Implement dashboard functionality
    - Task 4.3: Test dashboard functionality
- User Story 5: As a user, I want the dashboard to be customizable so that I can prioritize the information I need. (#5)
    - Task 5.1: Design customization options
    - Task 5.2: Implement customization logic
    - Task 5.3: Test customization functionality

#### Epic 3: Settings

- User Story 6: As an admin, I want to be able to set up an admin panel so that I can manage the system. (#6)
    - Task 6.1: Design admin panel layout
    - Task 6.2: Implement admin panel functionality
    - Task 6.3: Test admin panel functionality
- User Story 7: As a user, I want to be able to update my user profile settings so that I can customize my experience. (#7)
    - Task 7.1: Design profile settings page
    - Task 7.2: Implement profile settings logic
    - Task 7.3: Test profile settings functionality

#### Epic 4: Supplier Management

- User Story 8: As a user, I want to be able to create a new supplier so that I can add new suppliers to the system. (#8)
    - Task 8.1: Design supplier creation form
    - Task 8.2: Implement supplier creation logic
    - Task 8.3: Test supplier creation functionality
- User Story 9: As a user, I want to be able to read supplier details so that I can view supplier information. (#9)
    - Task 9.1: Design supplier details page
    - Task 9.2: Implement supplier details logic
    - Task 9.3: Test supplier details functionality
- User Story 10: As a user, I want to be able to update supplier information so that I can edit existing suppliers. (#10)
    - Task 10.1: Design supplier update form
    - Task 10.2: Implement supplier update logic
    - Task 10.3: Test supplier update functionality
- User Story 11: As a user, I want to be able to delete suppliers so that I can remove unwanted suppliers. (#11)
    - Task 11.1: Design supplier deletion functionality
    - Task 11.2: Implement supplier deletion logic
    - Task 11.3: Test supplier deletion functionality

#### Epic 5: Vehicle/Product Management

- User Story 12: As a user, I want to be able to create a new vehicle/product so that I can add new vehicles/products to the system. (#12)
    - Task 12.1: Design vehicle/product creation form
    - Task 12.2: Implement vehicle/product creation logic
    - Task 12.3: Test vehicle/product creation functionality
- User Story 13: As a user, I want to be able to read vehicle/product details so that I can view vehicle/product information. (#13)
    - Task 13.1: Design vehicle/product details page
    - Task 13.2: Implement vehicle/product details logic
    - Task 13.3: Test vehicle/product details functionality
- User Story 14: As a user, I want to be able to update vehicle/product information so that I can edit existing vehicles/products. (#14)
    - Task 14.1: Design vehicle/product update form
    - Task 14.2: Implement vehicle/product update logic
    - Task 14.3: Test vehicle/product update functionality
- User Story 15: As a user, I want to be able to delete vehicles/products so that I can remove unwanted vehicles/products. (#15)
    - Task 15.1: Design vehicle/product deletion functionality
    - Task 15.2: Implement vehicle/product deletion logic
    - Task 15.3: Test vehicle/product deletion functionality

These epics, user stories, and tasks can be used to organize and track the development of the project on a GitHub board or similar project management tool.

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Agile Planning
[Agile Board](https://github.com/users/Shazi-dani/projects/3)

<img width="1268" alt="Screenshot 2024-07-11 at 7 53 11 AM" src="https://github.com/Shazi-dani/Garage-Management-System/assets/126623880/cd9d5b99-fb13-429e-88ed-12678241aaf7">

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)
## Design
The design of the Garage Management System aims to create a user-friendly platform that streamlines the booking and management of automobile services while generating insightful statistics effortlessly. By focusing on ease of use, the system provides an intuitive interface for customers to register, login, and book services, as well as for administrators to manage these bookings efficiently. The dashboard offers a clear overview of daily tasks, allowing garages to plan and schedule operations effectively. Additionally, the system supports creating detailed service categories and descriptions, enabling precise tracking of time and resources. Comprehensive statistical tools allow users to analyze service performance on a daily, weekly, and monthly basis, providing valuable insights into technician efficiency and service profitability, thus enhancing overall operational efficiency.

## Colour Scheme
The color scheme for the Garage Management System is based on a blue and white contrast, designed to create a clean, professional, and visually appealing user interface. The use of blue conveys trust, reliability, and calmness, which are crucial qualities for a service-oriented platform where users need to feel confident in their interactions. White, on the other hand, adds to the system’s clarity and simplicity, providing a sense of openness and space that enhances readability and reduces visual clutter. This combination ensures that users can navigate through the system effortlessly, with blue highlighting key elements and actions while white offers a pristine background that makes content stand out. The benefits of this color scheme include improved user focus, reduced eye strain during prolonged use, and an overall professional aesthetic that aligns with the system’s purpose of efficient and reliable service management.

## Typography 
The fonts i used for this project were plain, simple & easy to read and look pleasant to the eye. I have used the default [bootstrap css](https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css) as the default typography and styling reference. 

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Entity Relationship Diagrams ERD's
![ERD](https://github.com/user-attachments/assets/9846a463-74bd-4a48-85f4-be8f4e57f883)

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Wireframes

#### Home 

<img width="511" alt="Home" src="https://github.com/user-attachments/assets/e064ce59-a3b7-4119-bd33-99581ae0e47c">

#### Login Page

<img width="578" alt="Login Screen" src="https://github.com/user-attachments/assets/f324df6e-06bb-4ac1-8bce-2de0a301c12e">


#### Register User
<img width="399" alt="Register Screen" src="https://github.com/user-attachments/assets/9cf590f1-d480-4dac-8f2b-8c1f8ab958e8">


#### Admin Login
<img width="585" alt="Admin Login Screen" src="https://github.com/user-attachments/assets/1118ca24-c03c-4574-90d9-f39c2bf7edc3">


#### Admin View
<img width="673" alt="Admin View" src="https://github.com/user-attachments/assets/ea25a66a-63b2-412f-aa19-094de7be096d">


[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Project Features 

* User Module with Authentication & Authorization
* Dashboard
* Settings (Admin panel, User profile settings)
* Supplier Management
* Vehicle/Product Management
* Inventory Management
  
## 1. User Module with Authentication & Authorization
   
#### Customer Management:

○ Capture customer details: first name, last name, display name, company details,
date of birth, email, mobile number, address, and profile image.

○ Self-service portal for customers to view service reminders, invoices, and
records.

○ Secure login and password management for customers.


#### Employee Management:

○ Capture employee details: email, phone number, date of birth, joining date,
designation, and address.

○ Role assignment and secure system access for employees.

#### Authentication:

○ Secure login with email and password for all users.

○ Password reset and recovery options.

#### Authorization:

○ Role-based access control with customizable permissions for viewing, adding,
updating, deleting, and owning data.

○ User roles: Super Admin, Customer, Garage Technician, Accountant, Support
Staff, Branch Admin.

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Steps to Complete:

#### Customer Management:
- Create customer registration forms capturing all required details.
- Develop self-service portal interfaces for customer access.
- Implement secure authentication methods and password management.
#### Employee Management:
- Create employee registration and profile forms.
- Develop role assignment functionality with detailed permissions.
- Implement secure authentication and password management.
#### Authentication:
- Develop secure login pages with email and password inputs.
- Implement password reset and recovery workflows.
#### Authorization:
- Define role-based access control mechanisms.
- Implement permission management for various user roles.

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)


#### User Login

![Login page](https://github.com/user-attachments/assets/ee83bb49-2db5-49cf-babb-5b632ba3bd65)

#### Register User 
![Register](https://github.com/user-attachments/assets/45922c57-1f8a-4ea7-96d0-004b03a45e7d)


[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## 2. Dashboard
 ![Dashboard view for client](https://github.com/user-attachments/assets/d3c80db5-168d-4a9c-a4f1-5f12cf1a8851)
Dashboard View for logged in Client (Showing only the user's appointments)

![Dashboard view for unauthentication users ](https://github.com/user-attachments/assets/4241f3d1-7e60-45aa-ace9-69b81691c854)
Dashboard View for Un Authenticated users (Guest Users) [Showing appointments of all the users on the dashboard] with no appointment registration option
#### Management Reports:

○ Summarize free and paid services.

- Data Visualization:

○ Real-time updates based on inputted service data.

## Steps to Complete:

#### 1. Management Reports:
○ Design report templates for free and paid services.
○ Implement data aggregation and summary views.
#### 2. Data Visualization:
○ Develop real-time data dashboards using charts and graphs.
○ Implement data updating mechanisms to keep information current.

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## 3. Settings (Admin panel, User profile settings)

#### Admin Panel:

○ System name, email address, phone number, and logo upload.

○ Configure business hours, holidays, and special working days.

○ Manage system-wide settings including currency and localization options.

#### User Profile Settings:

○ Update personal information such as email, phone number, and address.

○ Change and manage passwords.
#### Admin Login
 ![Admin Login](https://github.com/user-attachments/assets/c94188bb-555a-439b-99c0-bb901b7ab5cd)

#### Admin View
![Admin Dashboard](https://github.com/user-attachments/assets/28d034b9-4548-45eb-869d-875bd9d99057)

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Steps to Complete:

#### 1. Admin Panel:
- Develop forms for capturing system names, contact details, and logo uploads.
- Create interfaces for setting business hours, holidays, and working days.
- Implement currency and localization settings.

#### 2. User Profile Settings:
- Develop user profile forms to update personal information.
- Implement password change and management functionality

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## 4. Supplier Management

#### Create:

○ Add new supplier information: first name, last name, company details, email,
mobile number, and address.

#### Read:

○ View detailed supplier profiles and communication history.

#### Update:

○ Edit and update supplier details as necessary.

#### Delete:

○ Remove suppliers from the system when no longer needed.

#### Inventory Association:

○ Track parts and inventory received from suppliers for billing and service
purposes.

## Steps to Complete:

- 1. Create:Develop forms for capturing supplier information.
- 2. Read:Create interfaces to view supplier profiles and communication history.
- 3. Update:Implement forms and workflows for updating supplier details.
- 4. Delete:Develop mechanisms for securely removing supplier data.
- 5. Inventory Association:Link suppliers to inventory items and track received parts.
  
[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## 5. Vehicle/Product Management

#### Create:

○ Add and categorize vehicles by type (e.g., car, bike, hatchback), brand (e.g.,
BMW, Audi), and model.

○ Capture product details: unique identifiers, manufacturer details, pricing, and
warranty information.

#### Read:

○ View detailed profiles of vehicles and products.

#### Update:

○ Edit and update vehicle and product details as necessary.

#### Delete:

○ Remove vehicles and products from the system when no longer needed.

## Steps to Complete:

- 1. Create:Develop forms for adding vehicle and product details.
- 2. Read:Create interfaces for viewing detailed vehicle and product profiles.
- 3. Update:Implement forms and workflows for updating vehicle and product details.
- 4. Delete:Develop mechanisms for securely removing vehicle and product data.
  
[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)


## Bugs found during Project

1. When deploying to Heroku, the project was crashing with project settings path issue after deployment.
   Upon investigating and consulting with the mentor, the issue was identified to be the wrong project files structure.
   Fixing the project files structure fixed the issue and the project got live on Heroku.

2. User Authentication was being successful on log In page but was giving CSRF token error. The solution was to 
   add ``{{ csrf_token }}`` within the templates and add domain in the ``CSRF_TRUSTED_ORIGINS``. 

3. Appointment creation page showed list of all users as a dropdown menu for the user field selection. 
   This was not the intended behavior and allowed a user to add appointment for any other user as well. 
   To fix this issue, appointment model will need to be updated and the user value will be extracted from the request 
   instead of getting it from user input.

4. User can register for an appointment for any time slot within 24 hours but it should be allowed to only add appointment
   within the garage working hours. 

5. When trying to run the server on gitpod instance, the host was giving error and it was identified that we needed to explicitly
   add host name in the project settings ``ALLOWED_HOSTS``. 

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Project Run Guide
The project consists of Python/Django backend with HTML/JS front end 
and uses postgres as database. 
To run the application locally for testing, you need to perform following steps:

#### 1. Install Postgresql Server
Ensure that postgresql server is installed and running on your system. You can download and install postgresql from the official postgresql website.
To run the program locally, make sure both ``Python`` and ``pip`` are already installed 

#### 2. Install package requirements
Install the package requirements using the following command
```
pip install -r requirements.txt
```
#### 3. Apply the migrations 
```
python manage.py migrate
```
#### 4. Run the Application and Access in browser
Run the project using the following command and access on address http://127.0.0.1:8000/
```
python manage.py runserver
```
------ 

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Technologies Used
For the backend development, ``Python``/``Django`` has been used along with ``DjangoREST framework`` to implement some of the REST Api end points.
``Postgres`` database was used to build and deploy external database and university provided external database was configured 
with ``Django``. 
For the frontend development, ``HTML``/``CSS`` has been used along with default bootstrap css for templating and styling. 
For building and debugging the project, the provided ``gitpod`` instance was used.

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Deployment
``Heroku`` was used to deploy the project live for users. The university provided credentials were used to host the project 
and serve to users.

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Credits

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)
