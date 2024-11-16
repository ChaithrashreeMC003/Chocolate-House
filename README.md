
# Chocolate House Application

## Overview
A Python application to manage a fictional chocolate house's operations:
- Seasonal flavors
- Ingredient inventory.
- Customer suggestions and allergy concerns

## Setup Instructions

### Local Setup
1. Clone the repository:
   ```
   git clone <repo_url>
   cd project
   ```
2. Install dependencies:
   ```
   python -m venv venv
   venv/Scripts/activate
   pip install django
   ```
3. Run the application:
   ```
   python manage.py runserver
   ```
4. Access the application at `http://127.0.0.1:8000/`.

## API Endpoints
1. **Seasonal Flavors**
   - `GET /flavors`: Get all flavors
2. **Inventory**
   - `GET /inventory`: Get all inventory items
   - `POST /inventory`: Add an inventory item
3. **Customer Suggestions**
   - `GET /suggestions`: Get all suggestions
   - `POST /suggestions`: Add a suggestion
