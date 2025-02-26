Time Calculator
Description
The Time Calculator project is a small Python script designed to calculate the resulting time after adding a specific duration to a starting time. Additionally, the script can handle calculating subsequent days and determine the final day of the week if a starting day is provided.

Features
Add durations to a start time: The script takes a start time in HH:MM AM/PM format and a duration in HH:MM format, then returns the resulting time in the same format.

Handles days later: If adding the duration results in a day change, the script indicates how many days later the new time occurs.

Day of the week calculation: If a starting day of the week is provided, the script calculates and returns the corresponding day of the week for the new time.

Usage
The script contains a main function called add_time that performs the calculations. The function accepts three parameters:

start: The start time in HH:MM AM/PM format.

duration: The duration to add in HH:MM format.

start_day (optional): The starting day of the week (e.g., 'Monday').