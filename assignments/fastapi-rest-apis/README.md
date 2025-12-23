# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to handle HTTP requests and responses, learning about API endpoints, request/response models, and automatic API documentation.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application

#### Description
Create a basic FastAPI application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a GET endpoint at "/" that returns a JSON response with a welcome message
- Include proper type hints and response models
- Run the server using uvicorn

### 🛠️ Implement CRUD Endpoints for Items

#### Description
Add endpoints to perform Create, Read, Update, and Delete operations on a simple items resource.

#### Requirements
Completed program should:

- Implement GET /items to retrieve all items
- Implement POST /items to create a new item with name and description
- Implement GET /items/{item_id} to retrieve a specific item by ID
- Implement PUT /items/{item_id} to update an existing item
- Implement DELETE /items/{item_id} to remove an item
- Use Pydantic models for request/response validation
- Handle cases where items don't exist (404 errors)

### 🛠️ Add Query Parameters and Path Validation

#### Description
Enhance the API with query parameters for filtering and path validation.

#### Requirements
Completed program should:

- Add query parameter support to GET /items (e.g., limit, skip for pagination)
- Implement path parameter validation (e.g., item_id must be positive integer)
- Add optional query parameters for searching items by name
- Return appropriate HTTP status codes and error messages</content>
<parameter name="filePath">/workspaces/skills-customize-your-github-copilot-experience/assignments/fastapi-rest-apis/README.md