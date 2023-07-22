# Question Guidance Program

This program is designed to guide a user through a list of questions and encrypted answers. Each question and answer is coded to ensure the confidentiality of the content without the appropriate key.

## How it Works

1. The program presents the user with a series of questions stored in an encrypted list.
2. For each question, the user is prompted to provide an answer.
3. When the user submits an answer, the program checks if it matches the pre-coded answer for that specific question.
4. If the answer is correct, the program moves on to the next question; otherwise, it asks the user to try again.
5. The process continues until all questions are answered correctly.

## Encryption of Questions and Answers

The encryption of questions and answers is done using a unique key generated for each session of the program. This key is randomly generated at the beginning of the process and used to encode and decode questions and answers throughout the session. Thus, even if the question file is directly accessed, it is impossible to decrypt the content without the appropriate key.

## Usage Instructions

1. Make sure you have Python (version >= 3) installed on your system.
2. Download the program file `surprise_minifyed.py`.
3. Be sure that numpy is installed on your system, by running the following prompt:
    ```
   pip3 list
   ```
4. If you cannot see `numpy` on the list, then run : 
   ```
   pip3 install numpy
   ```
5. Run the program in a terminal using the following command:

   ```
   python3 surprise_minifyed.py
   ```

6. Follow the instructions displayed on the screen to respond to the encrypted questions.
7. If an answer is incorrect, the program will ask you to try again until all questions are correctly answered.

## Security Note

While the program uses encryption to hide the questions and answers, it is essential to remember that this is not an absolute security method. The questions and answers are not stored securely, and if someone directly accesses the question file, they could potentially guess or compromise the data. Use this program for non-critical purposes and avoid storing sensitive information.

## Disclaimer

This program is intended for educational or entertainment purposes. It should not be used in a context where data security and confidentiality are essential. The author cannot be held responsible for any damage or harm resulting from the use of this program.

## Contributions

Contributions to improve this program are welcome! If you have suggestions or ideas to enhance it, feel free to submit a pull request or open an issue on the project's GitHub repository.

Enjoy this fun Surprise Program !
