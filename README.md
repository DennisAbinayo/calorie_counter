# Calorie Tracker

A simple web application to track daily calorie intake, built with Django and styled using Tailwind CSS.

## Features

- Add food items with their calorie count
- Remove food items from the list
- View total calories consumed
- Reset the tracker

## Technologies Used

- Django
- HTML
- Tailwind CSS (via CDN)

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/calorie-tracker.git
   cd calorie-tracker
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://localhost:8000` to use the application.

## Usage

- Enter a food name and its calorie count in the form and click "Add Food" to add it to your list.
- To remove a food item, click the "Remove" button next to it.
- The total calorie count is displayed at the bottom of the page.
- To reset the tracker and clear all food items, click the "Reset Tracker" button.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

