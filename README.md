# Mini Canteen Ordering System

A command-line Python application that handles menu displays, cart management, and billing calculations for a canteen interface.

## Features

* **Display Menu:** Shows available food items with their ID numbers and prices in INR.
* **Add Food Item:** Allows users to select an item by ID and specify a quantity to add to the cart.
* **Remove Food Item:** Displays current cart contents and lets users delete specific items by list index.
* **View Cart:** Displays current items, quantities, and line-item subtotals.
* **Generate Bill:** Calculates order totals, applies a 10% discount for orders of ₹500 or more, and outputs the final payable amount.

## Requirements

* Python 3.x

## Structure

* **Menu Storage:** Standard Python dictionary mapping item IDs to names and prices.
* **Cart Storage:** Dynamic list containing dictionary records of selected items, prices, and quantities.

## Usage

Run the program via terminal:

```bash
python main.py