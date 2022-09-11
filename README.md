### Books Management system

## Simple Library Management System

## Version 1.0.0

- create/delete/edit/search and show: book (number, title, author, edition, submission date)
- create/delete/edit/show Users (ID, username, password)
- create/delete/edit/show author (ID, name)

### version 1.0.0: API
- Book
  - Columns: ID, title, edition, submission date, (author), (posted_by)
  - URI:
    - GET:
      - `/books`: list of books
      - `/books/:id` Book with ID
      - `/books?filter=value`: title, author
    - POST: `/books` create
    - DELETE: `/books` delete
    - PATCH: `/books` Edit
- User
  - Columns: ID, username, password
  - URI:
    - GET: `/users` list of users
    - POST: `/users` create
    - DELETE: `/users` Edit
    - PATCH: `/users` Edit
- author
  - Columns: ID, name
  - URI:
    - GET: `/authors` list of authors
    - POST: `/authors` create
    - DELETE: `/authors` Edit
    - PATCH: `/authors` Edit

## version 2

- Authentication
- unit testing
