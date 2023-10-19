# Profit Calculator Application

The Profit Calculator is a simple Python application built using the Tkinter library that helps you keep track of your business's financial transactions and calculate your daily profit. This README provides an overview of the application and how to use it.

## Table of Contents
- [Getting Started](#getting-started)
- [Features](#features)
- [Usage](#usage)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Saving Data](#saving-data)
- [Calculations](#calculations)
- [License](#license)

## Getting Started

To use the Profit Calculator application, make sure you have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/downloads/).

To run the application, follow these steps:

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the application files.

3. Run the following command to start the application:

   ```bash
   python profit_calculator.py
   ```

The application window will open, allowing you to input financial transactions and perform calculations.

## Features

The Profit Calculator application offers the following features:

- **Balance Tracking:** Keep track of your current balance as you input financial transactions.

- **Add and Subtract:** Easily add or subtract money from your balance with the "Add" and "Subtract" buttons.

- **Clear and Backspace:** Clear the current input or remove the last character.

- **Calculate Change:** Calculate change by entering the amount given by a customer.

- **Calculate Money In:** Calculate the total money in today, which excludes the starting balance.

- **Total Profit:** View the total profit for the day.

- **Total Money Out:** View the total money spent for the day.

- **Set Starting Balance:** Set your starting balance at the beginning of the day.

- **End Day:** Save daily transaction data, including the starting balance and operations.

## Usage

- To add or subtract money, click the "Add" or "Subtract" buttons, or use keyboard shortcuts (A for Add, S for Subtract).

- To clear the input field, click "Clear" or press the "C" key.

- To remove the last character in the input field, click "Backspace" or press the "B" key.

- To calculate the change, click "Calculate Change" and enter the amount given by the customer.

- To calculate money in today, click "Calculate Money In."

- To view the total profit for the day, click "Total Profit."

- To view the total money spent for the day, click "Total Money Out."

- To set your starting balance, enter the amount in the "Starting Balance" field and click "Set Starting Balance."

- To end the day and save the data to a file, click "End Day."

## Keyboard Shortcuts

The application provides keyboard shortcuts for quick data entry and actions:

- **A:** Add money
- **S:** Subtract money
- **C:** Clear
- **B:** Backspace

## Saving Data

The application saves daily transaction data to a text file in the format "profit_data_YEAR-MONTH-DAY.txt." The file contains information about the starting balance, individual operations (addition or subtraction), and the total profit for the day.

## Calculations

The application calculates the following values:

- **Total Profit:** Money In - Money Out
- **Total Money Out:** Total money spent
- **Total Money In Today:** Money In - Starting Balance
- **Change:** Amount Given - Money In

## License

This Profit Calculator application is open-source software released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software as per the terms of the license.

Please feel free to contribute to this project or report any issues on [GitHub](https://github.com/rshah2001/business_calc).

Happy tracking your business finances with Profit Calculator!
