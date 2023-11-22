import cv2
import random

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "stone" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "stone")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Initialize OpenCV webcam capture
cap = cv2.VideoCapture(0)

# Dictionary to map numerical key presses to game choices
choices = {1: "stone", 2: "paper", 3: "scissors"}

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Display game instructions
    cv2.putText(frame, "Press 1 for Stone, 2 for Paper, 3 for Scissors", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show the webcam feed
    cv2.imshow("Stone-Paper-Scissors", frame)

    # Check for key press
    key = cv2.waitKey(1)

    # If a valid key is pressed (1, 2, or 3)
    if key in [49, 50, 51]:
        user_choice = choices[int(chr(key))]
        computer_choice = random.choice(["stone", "paper", "scissors"])

        result = determine_winner(user_choice, computer_choice)

        # Display user and computer choices and the game result
        cv2.putText(frame, f"Your choice: {user_choice}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(frame, f"Computer choice: {computer_choice}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(frame, result, (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Show the result for a few seconds
        cv2.imshow("Stone-Paper-Scissors", frame)
        cv2.waitKey(3000)

    # If the 'q' key is pressed, exit the game
    if key == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
