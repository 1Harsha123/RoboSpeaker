# RoboSpeaker
This Python script aims to create a text-to-speech application. It begins by importing the necessary modules, pyttsx3 and os.

The initial print statement serves as a greeting message for the user.

The script then enters an indefinite loop using a while(True) loop. Within this loop, the user is prompted to input text that they want the program to speak.

If the user inputs "quit," the program initializes the pyttsx3 engine and says "Okay, Goodbye" before exiting the loop and terminating the program.

If the user inputs any other text, the script initializes the pyttsx3 engine and speaks the input text. The engine.runAndWait() function ensures that the text is spoken by the system.

The loop continues indefinitely until the user inputs "quit," at which point the program says goodbye and terminates.
