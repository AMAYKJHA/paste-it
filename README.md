# 📝 PasteIt

A simple web app that allows users to paste and store text content securely in the cloud — accessible from **any device, anywhere** with an internet connection.

## 🌐 Features

- 🚀 Paste and save any text instantly
- 📱 Access your saved text from any device
- 🔒 Persistent storage in the cloud
- 🖥️ Clean, minimal interface
- 🎯 Unique slugs for easy sharing of pasted content
- 🗑️ Option to delete saved content

<p align="center">
  <img src="img/homepage.png" alt="App Screenshot" width="600"/>
</p>

## 📦 Tech Stack

- **Python / Flask** – Backend framework
- **HTML/CSS** – Frontend 
- **MySQL** – Data storage (depending on your setup)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AMAYKJHA/paste-it.git
cd paste-it
```

### 2. Install Dependencies

Make sure you have Python installed. Then, install the required dependencies:


### 3. Set Up the Database

1. Create a MySQL database named `pasteit`.
2. Run the following SQL script to create the required table:

```sql
CREATE TABLE pastes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

3. Update the `database.py` file with your MySQL credentials.

### 4. Run the Application

Start the Flask development server:

```bash
python app.py
```

Visit the app at [http://127.0.0.1:5000/pasteit](http://127.0.0.1:5000/pasteit).

## 🛠️ Project Structure

```
pasteit/
├── app.py          # Main Flask application
├── database.py     # Database connection and operations
├── templates/      # HTML templates
├── static/         # CSS, JS, and images
├── README.md       # Project documentation
└── requirements.txt # Python dependencies
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📧 Contact

For any inquiries or feedback, feel free to reach out:

- **GitHub**: [AMAYKJHA](https://github.com/AMAYKJHA)
