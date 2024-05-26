# SDK for CORD Blockchain

This is a sample project created for demonstrating a connection with the CORD Blockchain.

## Setup

1. Ensure you have Python 3.12 installed on your system.
2. Clone the repository.
3. Navigate to the project directory.
4. Set up a virtual environment:
    ```sh
    python3 -m venv cord-py
    ```
5. Activate the virtual environment:
    - On Unix or MacOS, run:
        ```sh
        source cord-py/bin/activate
        ```
    - On Windows, run:
        ```sh
        .\cord-py\Scripts\activate
        ```
6. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Project

Before running the project, ensure that the CORD Blockchain is running on your system.

1. Run the main script:
    ```sh
    python src/main.py
    ```

## Testing

To run the tests, execute the following command:
```sh
python -m unittest discover test
  ```

## About the Project

This project includes several Python scripts that interact with the CORD Blockchain:

1.`main.py`: The main entry point for the application.

2.`balance_query.py`: Queries the balance of a specific account.

3.`transaction.py`: Handles transactions.

4.`substrate_connection.py`: Manages the connection to the Substrate node.

5.`config.py`: Contains configuration variables.
## Contributing
Contributions are welcome! Please read our contributing guidelines before getting started.

## License
This project is licensed under the terms of the MIT license.




