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

Go Top

## Agile Planning
Link

<img width="1268" alt="Screenshot 2024-07-11 at 7 53 11 AM" src="https://github.com/Shazi-dani/Garage-Management-System/assets/126623880/cd9d5b99-fb13-429e-88ed-12678241aaf7">


## Design
The design of the Garage Management System aims to create a user-friendly platform that streamlines the booking and management of automobile services while generating insightful statistics effortlessly. By focusing on ease of use, the system provides an intuitive interface for customers to register, login, and book services, as well as for administrators to manage these bookings efficiently. The dashboard offers a clear overview of daily tasks, allowing garages to plan and schedule operations effectively. Additionally, the system supports creating detailed service categories and descriptions, enabling precise tracking of time and resources. Comprehensive statistical tools allow users to analyze service performance on a daily, weekly, and monthly basis, providing valuable insights into technician efficiency and service profitability, thus enhancing overall operational efficiency.

## Colour Scheme
The color scheme for the Garage Management System is based on a blue and white contrast, designed to create a clean, professional, and visually appealing user interface. The use of blue conveys trust, reliability, and calmness, which are crucial qualities for a service-oriented platform where users need to feel confident in their interactions. White, on the other hand, adds to the system’s clarity and simplicity, providing a sense of openness and space that enhances readability and reduces visual clutter. This combination ensures that users can navigate through the system effortlessly, with blue highlighting key elements and actions while white offers a pristine background that makes content stand out. The benefits of this color scheme include improved user focus, reduced eye strain during prolonged use, and an overall professional aesthetic that aligns with the system’s purpose of efficient and reliable service management.

## Typography


## Project Features 

* User Module with Authentication & Authorization
* Dashboard
* Settings (Admin panel, User profile settings)
* Supplier Management
* Vehicle/Product Management
* Inventory Management


## 

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
