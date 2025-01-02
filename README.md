# EGN Validation Script

## Overview
This Python script validates Bulgarian Personal Identification Numbers (EGN) based on the official rules. It checks if the EGN is correctly formatted, verifies the birth date, gender, and the region of birth based on the provided code. Additionally, it checks the validity of the control number, which is the last digit of the EGN.

## Features
- **Date Validation**: Ensures the date of birth in the EGN is valid.
- **Region Validation**: Matches the region code to a predefined list of Bulgarian regions.
- **Gender Validation**: Determines the gender based on the 9th digit of the EGN.
- **Control Sum Validation**: Verifies the last digit of the EGN using the control sum algorithm.

## Requirements
- Python 3.x

## How to Use
1. Clone or download the script file.
2. Run the script in your terminal or Python environment.
3. Enter a Bulgarian EGN when prompted.
4. The script will print whether the EGN is valid or not.
5. If valid, it will also display the date of birth, gender, and region of the individual.
