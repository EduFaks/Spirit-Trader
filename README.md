# Spirit Trader

## Overview
This repository contains a real-time cryptocurrency price tracking application. It utilizes Python and Flask for the backend, with Flask-SocketIO for WebSocket communication. The frontend is a dynamic webpage using Chart.js to display live cryptocurrency data fetched from the Kraken API.

## Features
- **Real-Time Data Fetching**: Leverages the Kraken API to obtain live cryptocurrency price data.
- **WebSocket Integration**: Employs Flask-SocketIO for real-time communication between the backend and frontend.
- **Dynamic Charting**: Utilizes Chart.js on the frontend to dynamically plot cryptocurrency prices.
- **Responsive Dark-Themed UI**: Features a dark-themed user interface with a sidebar for account summary and neon-styled chart lines.

## TODO
- **Implement Kraken Trade API**: Allowing bot to buy and sell crypto.
- **Create Machine Learning Bot**: Using recent crypto prices and news to trade upon.

## Technologies Used
- **Backend**: Python, Flask
- **Real-Time Communication**: Flask-SocketIO
- **Frontend**: HTML, CSS, JavaScript
- **Charting Library**: Chart.js
- **Date Handling**: Moment.js with Chart.js Adapter

## Installation and Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/EduFaks/Spirit-Trader.git
   cd spirit-tracker
   
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
   
3. **Run the Flask app**
    ```bash
   python main.py
   
4. Open `http://localhost:5000` in a web browser.

## Usage
- Displays real-time prices for cryptocurrencies.
- Ajust bot parameters to allow trading (COMING)
- Sidebar shows values for account balance, earnings, and losses.

## Customization
- Modify `KrakenGateway` in Python for different API endpoints.
- Adjust Chart.js settings in HTML for chart customization.
- Change HTML/CSS for layout and style modifications.

## Contributing
Feel free to fork the repository and submit pull requests.

## License
Open source under the MIT License.