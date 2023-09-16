# FileNameTimestampUtility

This script will loop through all files in a given directory, prepend a date and time to each file name and change the created date and time.


## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Examples](#examples)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using this tool, ensure you have the following prerequisites installed:

* Python 3.11 or higher

## Installation

1. Clone this repository to your local machine or download it as a ZIP file.

2. Open a terminal or command prompt.

3. Navigate to the project directory.

4. Install any required dependencies using \`pip\`:

```shell
pip install -r requirements.txt
```


## Usage

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the `main.py` script with the desired options. For example:

```shell
python main.py -d /path/to/directory -D 2023-09-15
```

## Options

* `-d, --directory`: (Optional) Path to the directory to process. If not specified, the current working directory will be used.
* `-D, --date`: (Optional) Date in 'YYYY-MM-DD' format to prepend to file names. If not provided, the current date will be used.


## Examples

1. Process files in the current directory using the current date:

   ```shell
   python main.py
   ```
2. Process files in a specific directory using a custom date:

   ```shell
   python main.py -d /path/to/directory -D 2023-09-15
   ```
3. Process files in a specific directory using the current date:

   ```shell
   python main.py -d /path/to/directory
   ```

## Running Tests

Tests for this project are located in the "tests" folder in the project root directory and use the built-in `unittest` framework. To run the tests, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the tests using the `unittest` test runner. For example:

```shell
python -m unittest discover tests/
```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise messages.
4. Push your changes to your fork.
5. Create a pull request to merge your changes into the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
