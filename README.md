![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Project Scope
The DT Autos Garage Management System will encompass a comprehensive user module with robust authentication and authorization mechanisms, ensuring secure access for various user roles including Admin, Customer, and Garage Technician. The system will feature a customer management interface for registration, profile management, and a self-service portal to view service records and invoices. Employee management will include role assignments and detailed profiles, facilitating efficient operational workflows. A secure JWT-based authentication process will be implemented, along with role-based access control to regulate permissions for different functionalities, thereby ensuring a secure and streamlined user experience.

This project aims to streamline garage operations by providing an efficient platform for booking and managing automobile services. When you first start it, register and login, you will be on the home page which displays a dashboard with upcoming appointments and service details. The core functionality of this system is to enable customers to easily book their vehicles for servicing and other related tasks, allowing the garage to manage and schedule its operations effectively. In vehicle management, admins can add vehicle details including pictures and prices for vehicles that are for sale, and customers can view these vehicles and their details. This feature enhances the service offering by allowing customers to explore and purchase vehicles directly through the system.

Note: The system will track various services and generate statistics on a daily, weekly, and monthly basis. For instance, it can show how many oil changes were performed in a week, the total revenue generated from specific services, and the overall performance of different technicians.

Note: For this system to work effectively, you need to create service categories (e.g., oil change, tire replacement) and when a booking is made, you can choose a service and time slot for that service on a particular date. The description for the service will narrow down the specifics of what needs to be done within the allocated time slot. When you want to see a breakdown of services provided for a particular category, you can navigate to statistics and choose a date range and service category. This will display a tabulated result for each task within the dates chosen, showing hours, minutes, date, and task details in a table, along with totals to show overall time and revenue for the service category within the chosen dates.

Services could include various maintenance and repair tasks, where you can manage multiple services/projects on a daily basis within specific time slots. The description would be crucial here to break down exactly what needs to be done within the time window on a particular date.

The DT Autos Management System will provide a comprehensive solution for managing garage operations, enhancing customer service, and improving administrative efficiency. This system will help garages to streamline their booking processes, track service performance, and gain valuable insights into their operations, ultimately leading to better time management and increased productivity.

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

- User Story 3: As a user, I want to see a dashboard with relevant information so that I can quickly access key features. (#4)
    - Task 3.1: Design dashboard layout
    - Task 3.2: Implement dashboard functionality
    - Task 3.3: Test dashboard functionality
- User Story 4: As a user, I want the dashboard having information about appointments so that I can prioritize the information I need. (#5)
   
#### Epic 3: Settings

- User Story 5: As an admin, I want to be able to set up an admin panel so that I can manage the system. (#6)
    - Task 5.1: Design admin panel layout
    - Task 5.2: Implement admin panel functionality
    - Task 5.3: Test admin panel functionality
- User Story 6: As a user, I want to be able to update my user profile settings so that I can customize my experience. (#7)
    - Task 6.1: Design profile settings page
    - Task 6.2: Implement profile settings logic
    - Task 6.3: Test profile settings functionality

#### Epic 4: Supplier Management

- User Story 7: As a user, I want to be able to create a new supplier so that I can add new suppliers to the system. (#8)
    - Task 7.1: Design supplier creation form
    - Task 7.2: Implement supplier creation logic
    - Task 7.3: Test supplier creation functionality
- User Story 8: As a user, I want to be able to read supplier details so that I can view supplier information. (#9)
    - Task 8.1: Design supplier details page
    - Task 8.2: Implement supplier details logic
    - Task 8.3: Test supplier details functionality
- User Story 9: As a user, I want to be able to update supplier information so that I can edit existing suppliers. (#10)
    - Task 9.1: Design supplier update form
    - Task 9.2: Implement supplier update logic
    - Task 9.3: Test supplier update functionality
- User Story 10: As a user, I want to be able to delete suppliers so that I can remove unwanted suppliers. (#11)
    - Task 10.1: Design supplier deletion functionality
    - Task 10.2: Implement supplier deletion logic
    - Task 10.3: Test supplier deletion functionality

#### Epic 5: Vehicle/Product Management

- User Story 11: As a user, I want to be able to create a new vehicle/product so that I can add new vehicles/products to the system. (#12)
    - Task 11.1: Design vehicle/product creation form
    - Task 11.2: Implement vehicle/product creation logic
    - Task 11.3: Test vehicle/product creation functionality
- User Story 12: As a user, I want to be able to read vehicle/product details so that I can view vehicle/product information. (#13)
    - Task 12.1: Design vehicle/product details page
    - Task 12.2: Implement vehicle/product details logic
    - Task 12.3: Test vehicle/product details functionality
- User Story 13: As a user, I want to be able to update vehicle/product information so that I can edit existing vehicles/products. (#14)
    - Task 13.1: Design vehicle/product update form
    - Task 13.2: Implement vehicle/product update logic
    - Task 13.3: Test vehicle/product update functionality
- User Story 14: As a user, I want to be able to delete vehicles/products so that I can remove unwanted vehicles/products. (#15)
    - Task 14.1: Design vehicle/product deletion functionality
    - Task 14.2: Implement vehicle/product deletion logic
    - Task 14.3: Test vehicle/product deletion functionality

These epics, user stories, and tasks can be used to organize and track the development of the project on a GitHub board or similar project management tool.

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Agile Planning
[Agile Board](https://github.com/users/Shazi-dani/projects/3)

<img width="1268" alt="Screenshot 2024-07-11 at 7 53 11 AM" src="https://github.com/Shazi-dani/Garage-Management-System/assets/126623880/cd9d5b99-fb13-429e-88ed-12678241aaf7">

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)
## Design
The design of the DT Autos Management System aims to create a user-friendly platform that streamlines the booking and management of automobile services while generating insightful statistics effortlessly. By focusing on ease of use, the system provides an intuitive interface for customers to register, login, and book services, as well as for administrators to manage these bookings efficiently. The dashboard offers a clear overview of daily tasks, allowing garages to plan and schedule operations effectively. Additionally, the system supports creating detailed service categories and descriptions, enabling precise tracking of time and resources. Comprehensive statistical tools allow users to analyze service performance on a daily, weekly, and monthly basis, providing valuable insights into technician efficiency and service profitability, thus enhancing overall operational efficiency.

## Colour Scheme
The color scheme for the DT Autos Management System is based on a blue and white contrast, designed to create a clean, professional, and visually appealing user interface. The use of blue conveys trust, reliability, and calmness, which are crucial qualities for a service-oriented platform where users need to feel confident in their interactions. White, on the other hand, adds to the system’s clarity and simplicity, providing a sense of openness and space that enhances readability and reduces visual clutter. This combination ensures that users can navigate through the system effortlessly, with blue highlighting key elements and actions while white offers a pristine background that makes content stand out. The benefits of this color scheme include improved user focus, reduced eye strain during prolonged use, and an overall professional aesthetic that aligns with the system’s purpose of efficient and reliable service management.

## Typography 
The fonts i used for this project were plain, simple & easy to read and look pleasant to the eye. I have used the default [bootstrap css](https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css) as the default typography and styling reference. 

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Entity Relationship Diagrams ERD's
![ERD](https://github.com/user-attachments/assets/9846a463-74bd-4a48-85f4-be8f4e57f883)

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Wireframes

## Home 
<img width="536" alt="Screenshot 2024-07-27 at 9 06 50 PM" src="https://github.com/user-attachments/assets/f0c1ce17-8947-41b5-8a83-89cea19fd8c7">

#### Services (Home)
<img width="536" alt="Services" src="https://github.com/user-attachments/assets/30e51567-f5cd-46ad-b71c-7f1205d42a80">

#### About us (Home)
<img width="536" alt="Screenshot 2024-07-27 at 9 07 45 PM" src="https://github.com/user-attachments/assets/8461ce15-7035-4c2a-8a25-53c926a21f8e">

#### Home Page Footer 
<img width="536" alt="Screenshot 2024-07-27 at 9 10 21 PM" src="https://github.com/user-attachments/assets/2423cba3-b153-41a1-98e4-5c44e24f1e29">

#### Contact us
<img width="536" alt="Screenshot 2024-07-27 at 9 18 40 PM" src="https://github.com/user-attachments/assets/79cf936b-cae2-4d65-83a8-d7dd1988a8a2">

#### Register User
<img width="536" alt="Screenshot 2024-07-27 at 9 17 50 PM" src="https://github.com/user-attachments/assets/e62022dc-3273-44cb-a59e-dc93b710920b">

#### Login Page
<img width="536" alt="Screenshot 2024-07-27 at 9 19 35 PM" src="https://github.com/user-attachments/assets/601a5870-bc92-4185-bd83-cbceef1c6448">

#### Login Pop-up
<img width="536" alt="Screenshot 2024-07-27 at 9 20 31 PM" src="https://github.com/user-attachments/assets/dbce0f61-ff7d-4204-82a2-14f7ee9620b9">

#### After Login view
<img width="536" alt="Screenshot 2024-07-27 at 9 23 12 PM" src="https://github.com/user-attachments/assets/0655a438-36e4-4f33-a040-a930bf88da80">

#### Book Appointment
<img width="536" alt="Screenshot 2024-07-27 at 9 24 59 PM" src="https://github.com/user-attachments/assets/5547865c-2e59-4d83-bf9e-76e9ac889770">

#### Edit Appointment
<img width="536" alt="Screenshot 2024-07-27 at 9 42 33 PM" src="https://github.com/user-attachments/assets/ff194919-4b06-41fb-8bbc-c2b292ce4cbd">

#### Delete Appointment
<img width="536" alt="Screenshot 2024-07-27 at 9 26 23 PM" src="https://github.com/user-attachments/assets/6b327b52-7f6d-4228-a129-a09ae2e9a5cf">

#### Add Vehicles for Sale
<img width="536" alt="Screenshot 2024-07-27 at 10 00 34 PM" src="https://github.com/user-attachments/assets/e5dea7e4-e945-459d-a137-109744b15766">

#### Admin Login
<img width="585" alt="Admin Login Screen" src="https://github.com/user-attachments/assets/1118ca24-c03c-4574-90d9-f39c2bf7edc3">

#### Admin View
<img width="673" alt="Admin View" src="https://github.com/user-attachments/assets/ea25a66a-63b2-412f-aa19-094de7be096d">

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Project Features 

* Home Page 
* User Module with Authentication & Authorization
* Dashboard
* Settings (Admin panel, User profile settings)
* Vehicle/Product Management
* Supplier Management
* Inventory Management

## 1. Home Page of Garage Management System
The home page of the Garage Management System is designed to provide an informative and user-friendly experience for visitors. It effectively communicates the range of services offered, the garage's commitment to quality, and provides easy navigation to other important sections of the website.The home page of the Garage Management System (GMS) features a clean and organized layout, emphasizing various services offered by the garage. The navigation bar at the top provides easy access to different sections of the website, such as "Services," "Cars for Sale," "Book Now," and "Contact Us." Below is a detailed description of the main features and sections visible on the home page:
[You can see here: Home Page ](https://garage-management-system-78c320f4e5b8.herokuapp.com/)


<img width="1248" alt="Screenshot 2024-07-27 at 10 33 42 PM" src="https://github.com/user-attachments/assets/02b39c66-6786-4f2e-8159-7e8fe409fd0f">

## Nevigation Bar 
The navigation bar makes it easy to navigate the features of site.Nevigation bar shows the Logo & Having access to 
* Services
* Cars for sale,
* Book Appointment
* Contact Us


By Clicking on **Services** websites proceeds us to services of Concern Garage. When we Click on **Cars for Sale** we nevegate to the List of Cars showcase for Sale.On clicking **Book Now** we nevegate Login / Register Screen, After Login Successfuly we nevigate to appointment Page. & on Clicking the **Contact Us** we can type any kind of Queries. So it's very easy to nevigate the other features through this nevigation.

<img width="1279" alt="Screenshot 2024-07-27 at 10 18 30 PM" src="https://github.com/user-attachments/assets/ba4c7683-8b70-4805-b969-6701c433d5d8">

## Services 
Detailed view of services Provided by The Garage including Certified Mechanics, Comrihensive Car inspection, Precision oil & brake checks, Emergency Recovery, Breakdown Assistance , Professional Tyre Services, Seamless Battery replacement. This also contain a **Button** at the bottom for **Schedule Service** . By clicking this button we can directly nevigate to the Login Page & than Book Appointment.

[You can see here: Services ](https://garage-management-system-78c320f4e5b8.herokuapp.com/#services)

<img width="882" alt="Screenshot 2024-07-27 at 11 05 49 PM" src="https://github.com/user-attachments/assets/ba98f2cb-d0bf-4425-9889-e544f95907e1">

## About Us

Home page include information about the DT Autos. 
<img width="1279" alt="Screenshot 2024-07-27 at 10 17 39 PM" src="https://github.com/user-attachments/assets/66edd7ee-925d-49d0-b2aa-aaedf5a67b75">

## 2. User Module with Authentication & Authorization

#### Book Now > Register > Login

**Registration Form of user**

The user which is not registered can easily register himself by filling these details. 

<img width="1262" alt="Screenshot 2024-07-27 at 11 18 27 PM" src="https://github.com/user-attachments/assets/c5e093b2-2239-4f55-9c5d-8af30fe147ed">

**Login Page**

Registered user can easily access through his UserName & Password.

<img width="1280" alt="Screenshot 2024-07-27 at 12 31 47 PM" src="https://github.com/user-attachments/assets/aa0d100c-8e5b-4daf-a67d-e9ca64f9974a">

**Login Pop-up**

<img width="462" alt="Screenshot 2024-07-28 at 2 11 11 PM" src="https://github.com/user-attachments/assets/86d00d1f-4be8-4a89-88e5-d236f84e9891">


## User Dashboard View

After Login User proceed to his Dashboard View. Through this Registered user can easily Create, Edit & Delete his Bookings.This page have Three Buttons **Register a new appointment** , **Edit** & **Delete**.  
<img width="1280" alt="Screenshot 2024-07-27 at 9 35 00 PM" src="https://github.com/user-attachments/assets/16d635ee-78ec-4441-b2fb-764ac246b673">

## Book appointment

Any User can create a new appointment by simply Clicking on given button Ecxept Technician.Technician cannot create  appointment only admin and customers can create appointment. Technician can delete or update appointment.

<img width="1248" alt="Screenshot 2024-07-28 at 5 15 12 AM" src="https://github.com/user-attachments/assets/673478ec-eef0-43c9-8bd1-3c8c24f1ec66">

## Steps to Complete

 **Appointment Form**
 User can create a new appointment by filling This form completely. 
 
 **1:Form**
 <img width="1280" alt="Screenshot 2024-07-28 at 5 17 25 AM" src="https://github.com/user-attachments/assets/d8237de0-84b6-4eab-87de-6d88326e6573">
 **2:Add Vehicle Details**
 
 By clicking on vehicle a Dropdown is accessible to select the Vehicle Name & Model.
 <img width="1280" alt="Screenshot 2024-07-27 at 9 32 47 PM" src="https://github.com/user-attachments/assets/a34f86e5-f7be-4e04-8a3f-01a3bae57c45">
**3:Add Service type**

User can add Service type that Which kind of service user needed the most.Here is also a dropdown through which he select the Service.  
<img width="1280" alt="Screenshot 2024-07-27 at 9 32 56 PM" src="https://github.com/user-attachments/assets/c9eff2dc-e395-4c6e-a000-0c1096b5bb99">
**4:Add Time & Date**

User Friendly Calender & Time integration is added.To make user comfirtable and make his experience better. User can select Appropriate Time & Date for his service.User cannot select backdate and only can choose time during working hours
<img width="1280" alt="Screenshot 2024-07-27 at 9 33 29 PM" src="https://github.com/user-attachments/assets/da0a9a27-93cc-40aa-b933-0fb2eb0901b3">
**5:Add Description**

User Also add Description for his Booking if there any kind of acknowledgement which is necessary to deliver to the Garage members or service provider.

User can add in this **Description Box**.
<img width="1280" alt="Screenshot 2024-07-28 at 5 29 31 AM" src="https://github.com/user-attachments/assets/3080b86c-0f61-484c-87d8-d979514add66">

**7: Edit Appointment**

User can Edit any appointment & add any changes to this by clicking on Editing Button
<img width="1280" alt="Screenshot 2024-07-27 at 9 35 24 PM" src="https://github.com/user-attachments/assets/47860b12-b714-4eaa-b6b0-cf3080299f5d">
## Email Integration

Email integration add for the user satisfactioon.User receive confirmation Email to that email which he given during Registeration. He can receive e-mail for 
* Registration or Signup Confirmation
* Login Confirmation
* Appointment Confirmation
* Edit already existing appointment

<img width="488" alt="Screenshot 2024-07-28 at 5 52 31 AM" src="https://github.com/user-attachments/assets/50f7e245-6258-4388-a8e3-70ea83c7839d">
<img width="488" alt="Screenshot 2024-07-28 at 5 52 43 AM" src="https://github.com/user-attachments/assets/d2fe8d35-a9a1-42ae-948b-cff3380af8a9">
<img width="488" alt="Screenshot 2024-07-28 at 5 52 52 AM" src="https://github.com/user-attachments/assets/472f2295-9b8e-4bcd-9fe2-19cae4eb610f">

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Cars for Sale
User can view all the vehicles for sale and request purshase here. Every vehicle deatiled box consist of his name , model, colour, Image view & Price. User can easily make purchase here.
<img width="1280" alt="Screenshot 2024-07-28 at 7 22 34 AM" src="https://github.com/user-attachments/assets/c6a3f522-6449-47bf-b7f7-9fd7f868a639">


## 3. Dashboard
There two dashboard views one for the user and other for the admin 
#### User Dashboard View

After Login User proceed to his Dashboard View where he can easily Create, Watch, Edit & Delete his Bookings.This page have Three Buttons **Register a new appointment** , **Edit** & **Delete**.  
<img width="1280" alt="Screenshot 2024-07-27 at 9 35 00 PM" src="https://github.com/user-attachments/assets/16d635ee-78ec-4441-b2fb-764ac246b673">

#### Admin Dashboard View
After Login Admin can inquire all the activities .Admin can watch users, mechanics, vehiclas, Appointments & Purchase interest etc. Real-time updates based on inputted service data.
<img width="1280" alt="Screenshot 2024-07-28 at 6 43 19 AM" src="https://github.com/user-attachments/assets/2319d9dc-2844-4705-be7b-15db623cee52">

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## 4. Vehicle/Product Management

**Create:**
User can Add and categorize vehicles by type (e.g., car, bike, hatchback), brand (e.g.,
BMW, Audi), and model.He can Add Image of product/ Vehicle. Also Capture product details Like unique identifiers, manufacturer details, pricing, and
warranty information.
<img width="1280" alt="Screenshot 2024-07-28 at 6 43 51 AM" src="https://github.com/user-attachments/assets/d52ee6a8-c2d7-49d0-a910-50298a3a12c9">

**Read:**
○ View detailed profiles of vehicles and products.
<img width="1247" alt="Screenshot 2024-07-28 at 6 45 10 AM" src="https://github.com/user-attachments/assets/0de5d776-648c-4bd7-8274-e64b2ab635af">

**Update/Edit/Delete**

○ Edit and update vehicle and product details as necessary.
○ Remove vehicles and products from the system when no longer needed.

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## 5. Settings (Admin panel, User profile settings)

#### Admin Panel:

○ System name, email address, phone number, and logo upload.

○ Configure business hours, holidays, and special working days.

○ Manage system-wide settings including currency and localization options.

#### User Profile Settings:

○ Update personal information such as email, phone number, and address.

○ Change and manage passwords.

## Admin Login

Admin can login by using the Username "admin" & Password is also "admin" . Admin User can use the Link given here [Garage Management System Admin](https://garage-management-system-78c320f4e5b8.herokuapp.com/admin)



 ![Admin Login](https://github.com/user-attachments/assets/c94188bb-555a-439b-99c0-bb901b7ab5cd)

 
 
 ## Change Theme
Here User can change theme of this site by clicing on Sun & Moon.

https://github.com/user-attachments/assets/790259d7-3da6-47b1-934f-62b9b351eedf

## 1. Admin Panel:
Admin Pannel interface provides the tools necessary to effectively manage a garage, including handling appointments, tracking customer interests, managing services, and overseeing user accounts. The recent actions feature enhances accountability and transparency by keeping a log of the admin's activities.
<img width="1280" alt="Screenshot 2024-07-28 at 6 43 19 AM" src="https://github.com/user-attachments/assets/6e134979-534c-415d-a9dd-c942c7b572a9">

## Admin Side Detailed view of
* Appointments
* Purchase Interests
* Users
* Services
* Vehicles
* My Action

#### Appointments: 
View, add, or change appointments. This section allows you to manage the scheduling and details of customer appointments for various services.

<img width="1248" alt="Screenshot 2024-07-28 at 12 12 48 PM" src="https://github.com/user-attachments/assets/dafa3ebf-88d9-40e9-a62e-f35d189b21ad">

#### Purchase Interests: 
Track and manage customer purchase interests. This feature helps you keep a record of potential vehicle purchases and customer preferences.When customer press **“request purchase“** button on website then a purchase interest create at the admin site.

<img width="1248" alt="Screenshot 2024-07-28 at 12 13 03 PM" src="https://github.com/user-attachments/assets/87a0fd7c-d60d-4af3-b7f7-d1b1bd37d036">

#### Services: 
Manage the services offered by the garage. You can add new services or update existing ones, including maintenance and repair services.

<img width="1248" alt="Screenshot 2024-07-28 at 12 13 21 PM" src="https://github.com/user-attachments/assets/1267c154-34cc-4ec9-92aa-5494cdf3a8b6">

#### Vehicles: 
Manage the vehicles in the system. This section allows you to add new vehicles, update vehicle information, and track service history.

<img width="1248" alt="Screenshot 2024-07-28 at 12 12 35 PM" src="https://github.com/user-attachments/assets/bf17b384-d9e1-4cb9-93cc-2e1abfa96261">

#### Users: 
Manage user accounts. You can add new users, change existing user details, and control user access and permissions within the system.

<img width="1248" alt="Screenshot 2024-07-28 at 12 15 47 PM" src="https://github.com/user-attachments/assets/bbcab5f1-ec97-43a3-b5f2-f8b5be1137e3">

#### My Actions: 
Displays a list of recent actions performed by the logged-in admin user. This includes details of appointments made, users added or removed, and other significant activities. This helps in tracking the admin's recent activities and changes within the system.

<img width="1248" alt="Screenshot 2024-07-28 at 12 17 29 PM" src="https://github.com/user-attachments/assets/c604cfb7-84bf-417d-b7de-38cb73e76fa5">

## Contact Us
User can conatct admin bu clicking  **Contact Us** in nevigation  bar.
<img width="1280" alt="Screenshot 2024-07-27 at 1 10 12 PM" src="https://github.com/user-attachments/assets/17cb1cc9-7dfa-431a-9c31-2b62d0110299">

## Logo Functionality 
User on any page can go back to the Home page by clicking on logo .



https://github.com/user-attachments/assets/125c24c9-e713-4d49-b583-b35de8e1b36e



## Site Footer
The footer consists of company deatils like adress , email , Location etc Also working Hours are mention here according to which a user can make his appointment clear.
<img width="1280" alt="Screenshot 2024-07-27 at 9 32 00 PM" src="https://github.com/user-attachments/assets/595a7caa-5865-4f88-9431-495ae38615fa">


[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Things To done in Future 

**Supplier Management & Inventory**
**Note:** Due to time constraints, it was not possible to implement the supplier management and inventory features at this time. However, we plan to develop and enhance these features in future updates.

####  Supplier Management

**Create:** Add new supplier information: first name, last name, company details, email,
mobile number, and address.
**Read:**  View detailed supplier profiles and communication history.
**Update:**  Edit and update supplier details as necessary.
**Delete:**  Remove suppliers from the system when no longer needed.
All these are The task to done in Future
<img width="939" alt="Screenshot 2024-07-28 at 1 21 38 PM" src="https://github.com/user-attachments/assets/dc1ea053-d035-4840-b129-9aea002ed9f9">

  
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

## Lighthouse Testing 

Tests in Lighthouse were Funtionaloty of every feature is tested.

#### Home page testing

![Home Page testing](https://github.com/user-attachments/assets/151e2b2a-f9a5-48e8-9d65-7b90f11bc866)

#### Register Testing

![register page testing](https://github.com/user-attachments/assets/e183f205-c003-4b2b-be7e-570e988b6f87)


#### Login Testing

![Login Testing](https://github.com/user-attachments/assets/ec46dd84-dccc-42d5-968c-96c5d68a2d20)

#### Create Appointment page testing

![create appointmemnt ](https://github.com/user-attachments/assets/6b376442-a6ce-45b4-9b26-e24049a9c1bc)

#### Appointments dashboard lighthouse testing

![Appointments](https://github.com/user-attachments/assets/bb948851-ac76-4a55-b4a5-a75759e15778)

#### Appointments Edit Page testing 

![Edit Page testing](https://github.com/user-attachments/assets/20830036-58e2-4f71-b1f1-39b9a0bac8b7)

#### Delete Testing

![Delete Testing](https://github.com/user-attachments/assets/cd016c3e-3287-4f56-af26-931dba4c0cf0)

#### Vehicles for sale testing

![Vehicles for sale](https://github.com/user-attachments/assets/cb6f0733-efa0-4827-b71b-6ff2bb4057b2)

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Technologies Used

- [**Django/Jinja**](https://docs.djangoproject.com/en/5.0/) - main Framework of the project and 
   DjangoREST framework to implement some of the REST Api end points.
- [**Python**](https://www.python.org/) - main BackEnd programming language of the project
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/HTML) - templates programming language of this project (FrontEnd)
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS) - styling the project via external CSS file `./static/css/style.css`
- [**Java Script**](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - dynamic templates programming language of this project (FrontEnd)
- [**jQuery**](https://api.jquery.com/) - API for JavaScript - dynamic templates programming language of this project (FrontEnd)
- [**Bootstrap v. 5.3**](https://getbootstrap.com/) - styling framework used in this project (FrontEnd)
- [**Heroku**](https://heroku.com) - to deploy this project
- [**Balsamiq**](https://balsamiq.com/support/) - to create wireframes
- [**Git**](https://git-scm.com/doc) - to make commitments of progress and push the results back to GitHub
- [**GitHub**](https://github.com/) - to keep the track of version control
- [**Gitpod**](https://gitpod.com/) - online IDE - CodeAnywhere was initially used to create this project
- [**Postgres**](https://www.postgresql.org/) - Postgres database was used to build and deploy external database and institute provided external database was configured.
- [**ChatGPT**](hhttps://chatgpt.com/) - Use ChatGPT for creating website logo.
- [**MDB Snippets**](https://mdbootstrap.com/snippet) - Use MDB Snippets for creating icons.

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Deployment
To ensure users are able to view live version of "DT Autos garage" project.

I followed the following steps:

1:Register & Log In with heroku

2: Navigate to New > Create New App

3: Select Name of the app that is unique

4: Navigate to Settings > Reveal Config Vars

5: Add all variables from env.py to ConfigVars of Heroku App

6: Add variable pair PORT:8000

7: For the testing deployment add variable pair COLLECT_STATIC:1

8:  Add the Heroku app URL into ALLOWED HOSTS in settings.py

9: In root create file name Procfile

10:Navigate to Deploy > GitHub > Connect

11: Navigate to Deploy > Deploy Branch

12: Optionally, you can enable automatic deploys

See the deployment log - if the deployment was successful, you will be prompted with option to see live page

[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)

## Credits

* Code Institute course content without that I had no base to begin a project. https://codeinstitute.net/ie/

* Get ideas formaking my Readme.md best from @kera-cudmore readme template. https://github.com/
* The Code Institute Tutors and specially my mentor @rory_patrick who assisted me with troubleshooting when I was stuck on a particularly difficult bug.

* The Slack community - for someone always been there no matter the time and with advice or direction. https://slack.com
 
* StackOverflow for all the information to assit with my project .https://stackoverflow.com

* Google Images- for providing good quality free copyright images

* Youtube Tutorials - For better understating and learning django framework, python,database authentication and for main project idea.(https://www.youtube.com/watch?v=opzK3E4Xx6o&list=WL&index=8&t=917s,https://www.youtube.com/watch?v=lERvLBEfCaY&t=833s,)

* Copied Code / Code assistance
As stated in Technologies / Support Used I used and sort out help and code from numerous sources as well as fonts and images. However, I did exclusively get inspiration from Love running and coders coffee house for the full website. Stack over flow and Tutor Support played a huge roll in my overall development.


[Go Top](https://github.com/Shazi-dani/Garage-Management-System/edit/main/README.md)
