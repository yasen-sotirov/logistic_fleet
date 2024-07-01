## Logistic Fleet App
Team: T. Kamenov, G. Dodekov, Y. Sotirov

### 1. Description
Design and implementation of a logistic console application.
The application is intended to be used by an Australian pharmaceutical company to expand their freight transport operations.
The application is planned to be used across all company branch locations.

### 2. Objectives
The main objectives of the software are:

 - Employee registration
 - Shipment registration
 - Creation of routes between company branches
 - Monitoring of the database
### 3. Skeleton
Creating the structure and basic logic of the application:

 - Engine
 - Main
 - Command Factory
 - Application Data
### 4. Class Users
Instances of this class will be used for creating and logging in employees into the system.
User type can be one of **"Manager"**, **"Employee"** or **"Supervisor"**.

### 5. Class Customer
The class parameters accept information about the customer who will send a shipment.

 - First name
 - Last name
 - Email
 - Phone number
### 6. Class Command Factory
Contains all the necessary commands for the functionality of the specific application.

### 7. Class Package
Accepts shipment information:

Starting and ending delivery points, weight, and identification number.
### 8. Class Delivery Route
Creates a route for the shipment to move along and provides delivery time.

### 9. General Program Guidelines
The program has two essential commands without which its functioning would be incorrect:
login - a command used to validate access to the system for every employee in the company;
SetCurrentDateTime - if the command is entered without parameters, it takes the current time as default. Additionally, this command can set a future date and time. This allows simulating a real working process that would otherwise take months.
### 10. Supported Commands:
 - Date & Time

   * SetCurrentDateTime - sets the time with which the application operates has two parameters **"DD/MM/YY"** **"HH:MM:SS"** Example:
         SetCurrentDateTime - without parameters, the command will lead to datetime.now()
         SetCurrentDateTime 25/08/2023 13:00 - this is an example where the params are given to the command to specify future time stamp to simulate the processes
   * CheckCurrentDateTime - provides information about the current day and time. Command does not accept parameters;
   * AddDaysToNow - has one parameter **"int"** adds a specific time to the current day, after which a new delivery will be assigned. Example:
         AddDaysToNow 2 - the int '2' shows how many days will be added to the datetime.now
   
 - Login & Users

   * login - validates an employee within the company. Requires a **"username"** and **"password"**, then checks if the user actually works in the company. If not valid, it throws an error. Example:
         login - after typing this command, on the next line the pointer will wait an input from the user to validate username and password
         Enter username: - this message will be displayed on the first line. It waits a valid username (can be found in models -> class User -> all_users);
         Enter password: - this message will be displayed on the second line. It waits a valid password (can be found in models -> class User -> all_users);
   * logout - a command for every employee to exit the system. Requires the employee's **"username"** and validates if they had a valid entry before, if not, it throws an error. Example:
         logout - after typing this command, on the next line the pointer will wait an input from the user to validate the username that already has been logged in the system. 
         Enter username: - this message will be displayed to validate the username that has been logged. If the username or password are incorrect, the user will not be logout successfully. Otherwise, the confirmation message will be displayed;
   * ViewUsers - displays all employees currently logged into the system. The command does not take any arguments. Any employee can perform this command;
         
 - Customers

   * ViewCustomerByPhoneNumber - Takes two parameters - **"phone number (int)"** and **"shipment ID (int)"**, a command that checks the status of a customer's shipments and whether the provided shipment ID corresponds to their shipment. Any employee can perform this command. Example:
         ViewCustomerByPhoneNumber 0888111222 2001 - first parameter will be the phone number of the customer, the second parameter is unique customer package ID that customer takes after successfully registered delivery package.
         
   * ViewAllCustomers - a command that displays all customers in the system. The command takes no parameters and can only be used by a Manager-level employee. The command does not accept any arguments;
 - Routes
        
   * CreateDeliveryRoute - takes four parameters: **"DD/MM/YY"**, **"HH:MM"**, **"dispatch location"**, **"delivery location"** creates a new route. This command can only be used by a Supervisor-level employee. Example:
         CreateDeliveryRoute 20/08/2023 10:00 SYDNEY BRISBANE 
   * ViewRoutes - a command to display all created routes in the system. This command can only be used by a Supervisor-level employee. Command does not accept any parameters;
   * SearchRoute - takes only one parameter - **"dispatch location"**, a command that checks all available routes in the system with a specified starting location. Example:
         SearchRoute SYDNEY
   * AssignTruckToDeliveryRoute - takes two parameters - **"dispatch location"** and **"route ID"**, a command that assigns a free truck to a specified location that meets the distance requirement equal to or greater than the route distance. 
   Example:
         AssignTruckToDeliveryRoute SYDNEY 3001 
 - Trucks

   * EnrollTruckToLocation - takes two parameters - **"truck type"**, **"request location"**, assigns a truck to a requested location if a free truck of the particular type is available. Example:
          EnrollTruckToLocation Actors SYDNEY
          EnrollTruckToLocation Man SYDNEY
          EnrollTruckToLocation Scania SYDNEY
   * ViewTrucksAtLocation - takes one parameter - **"request location"** displays available vehicles at a specified location. Example:
          ViewTrucksAtLocation MELBOURNE
   * ViewAllTrucks - provides information about available vehicles at each location. The command does not accept any parameters;
   * ViewUnenrollTrucks - provides information about available free trucks. Command does not accept parameters;
   * LoadPackagesToTruck - takes two parameters - **"loading location"**, **"truck ID"** loads packages from the warehouse onto the truck. Example:
          LoadPackagesToTruck SYDNEY 1026
 - Packages:

   * CreateDeliveryPackage - takes seven parameters - **"dispatch location"**, **"delivery location"**, **"package weight"**, **"first name**, **last name"**, **"e-mail"**, **"phone number"** creates a new shipment with valid parameters. If the customer is not in the system, the command creates a new customer with corresponding data - two names, email, phone number. Any employee can perform this command. Example: 
          CreateDeliveryPackage SYDNEY MELBOURNE 1000 Ivan Ivanov ivan@abv.bg 0888111222
   * AssignTruckToDeliveryRoute - the command accept 2 parameters - **"request location"**, **"route ID"**. Command reacts with assignation of a loaded truck at requested location to specific delivery route. This command is restricted to level 'Supervisor'. Example:
          AssignTruckToDeliveryRoute SYDNEY 3001
          
   * ViewPackages - takes one parameter - **"request location"**, a command to display all created shipments in the system based on a specified starting point. Any employee can perform this command. Example: 
          ViewPackages PERTH
   * ViewUnassignedPackages - a command that displays all shipments that have not yet been assigned. The command takes no parameters and can be used by a Manager-level employee.
   
