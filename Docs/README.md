## Simple Library Management System

Using: PHP, MySQL, ReactJs, Redux, Styling framework

and UML, ERD ...etc 

Note: BFF(Backend For Frontend) VS Normal backend 

### Business Rules
 
#### Minimize Rules 


- Authentication
  1. Login / Logout

- Librarian/admin 
  2. Add book(number, title, author, edition, submission date)
  3. Edit book
  4. Delete book

- User
  1. Search Book with book name [or/ other information]
  2. Show book with details

#### Extra Rules

- Authentication
    1. time login?
    2.  FB, Google Authentication API

- Librarian/admin 
  1. Author Information Management (CRUD)  
  2. Publisher
     1. Publisher Information Management (CRUD)
     2. Publisher Bills/supply book(CRUD: order supply)
  3. User
     1. Accept/Reject Order Borrow
     2. Confirmation the user returns the book (Borrow Order)
  
- User
  1. Order
     1. Buy Book transaction
     2. Barrow Book transaction
     3. View Orders

- Login 

### Technical Step (implementation)

- Database 
  - [X] ERD
  - [X] DDL (Mapping)
  - [ ] DML
  - [ ] DCL

- UML
  - [ ] Class Diagram

- Development
  - [ ] HTML
    - [ ] X Page... @TODO
    
  - [ ] PHP
    - [ ] X Page... @TODO
    - [ ] Models
      - [ ] Orders
      - [ ] Books
      - [ ] Login
      - [ ] User (Create, Update)

  - [ ] ReactJs, Redux and Styling framework
    - [x] layout 
    - [x] Login Page
    - [x] Books Page
      - [X] Search
      - [X] Order / Borrow
      - [X] Edit Book (admin)
      - [X] Remove Book (admin)
    - [ ] Users Page
      - [ ] Add/Change Address Page/Section
      - [ ] View Orders / Borrow Page/Section
        - [ ] return Borrow
    - [ ] admin Page