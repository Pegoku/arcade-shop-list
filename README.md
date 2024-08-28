# Arcade Shopping List

This is a simple web app, useful to easily calculate what you can buy from acrade.
![IMG](https://raw.githubusercontent.com/Pegoku/arcade-shop-list/main/img/image.png)

## Features

- Choose what you want to buy.
- Updates the prizes and products automatically.

## Installation

1. Clone this repository: `git clone https://github.com/Pegoku/arcade-shop-list.git`
2. Navigate to the project directory: `cd arcade-shop-list`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the application: `python main.py`

## Docker

This application can also be run using Docker. Here are the steps to do so:

1. Build the Docker image: `docker build -t asl .`
2. Run the Docker container mounting the folder where the db will be stored: `docker run -p 5000:5000 asl` 

After running these commands, you can access the application at `http://localhost:5000`.

## Usage

Open your web browser and navigate to `http://localhost:5000` to start using the application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
