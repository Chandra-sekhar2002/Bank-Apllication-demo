# Bank Application - Python Backend Project

## Overview
This project is a backend-only banking application built using Python and SQL. It simulates fundamental banking operations such as account creation, login authentication, balance inquiries, deposits, withdrawals, and viewing transaction history.

## Features
- User registration and login authentication
- Account balance inquiry
- Deposit and withdrawal functionalities
- Transaction history tracking
- Data validation and input error handling
- Backend architecture using Python and SQL

## Technologies Used
- **Programming Language**: Python 3
- **Database**: MySQL or SQLite (based on user setup)
- **Libraries/Tools**: MySQL Connector / SQLite3

## Installation and Setup
### Prerequisites
Make sure the following are installed on your machine:
- Python 3.x
- MySQL or SQLite
- Required Python packages (refer to `requirements.txt`)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bankapplication.git
   ```
2. Navigate to the project folder:
   ```bash
   cd bankapplication
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your database in `config.py`.
5. Run the database setup script:
   ```bash
   python db_setup.py
   ```
6. Run the application:
   ```bash
   python app.py
   ```

## Usage
1. Register a new user or log in.
2. Access banking features like:
   - Checking balance
   - Making deposits
   - Performing withdrawals
   - Viewing transaction history

## Project Structure
```
├── app.py               # Main application script
├── db_setup.py          # Script to initialize the database
├── config.py            # Configuration file for database settings
├── requirements.txt     # Required Python libraries
└── ...                  # Other helper modules and files
```

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Author
**Chandu** – B.Tech (ECE) 2025 | Python Full Stack Developer | Passionate about backend systems and data-driven applications.
