''' Author: Chris Whipple
    Date:  6/26/26
    Assignment:  Milestone 7 - Function Development
    Description:    Task:   Step 1: Data Specifications
                            Create three separate dictionaries to store the following data. In each dictionary, the Course Number must serve as the Key.

                            Step 2: Program Logic

                            Input: Prompt the user to enter a Course Number (e.g., CSC101).
                            Retrieval: Use that input to look up the corresponding values across your dictionaries.
                            Output: Display the Room Number, Instructor, and Meeting Time. If the course does not exist, provide a friendly error message.
    
                    
                    Deliverables: Submit your .py file and a screenshot of the VS Code terminal showing the script successfully capturing input and printing the calculated results.
'''
def get_course_info(course_number, info_dict):
   return info_dict.get(course_number, "Course not found.")

# import necessary libraries
import math 

# Define variables
room_numbers = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Gather input from the user and assign it to variables
course_number = input("Enter a Course Number (e.g., CSC101): ")

# Check if the course exists and display its information

try: 
        course_exists = room_numbers[course_number] and instructors[course_number] and meeting_times[course_number]
        room_number = get_course_info(course_number, room_numbers)             # Retrieve the room number for the course
        instructor = get_course_info(course_number, instructors)               # Retrieve the instructor for the course
        meeting_time = get_course_info(course_number, meeting_times)           # Retrieve the meeting time for the course
        print()
        print(f"Course: {course_number}")
        print(f"Room Number: {room_number}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
        print()
except KeyError:
        print(f"\nNo course information found for {course_number}. Please check the course number and try again.\n")
    


