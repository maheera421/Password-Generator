# Password-Generator

# 🚀 Code Description:

This code is a Password Generator that allows users to create strong, randomized passwords based on their preferences. Here's how it works:

1. It starts by importing an external module named `data`.

2. The program displays a welcome message along with instructions to the user.

3. It prompts the user to input:
   - `nr_letters`: The number of letters they want in the password.
   - `nr_symbols`: The number of symbols they want in the password.
   - `nr_numbers`: The number of numbers they want in the password.

4. The code then initializes an empty list called `password_list`.

5. It populates `password_list` with characters based on the user's input:
   - It adds `nr_letters` random letters from the `data.letters` character set.
   - It appends `nr_symbols` random symbols from the `data.symbols` character set.
   - It appends `nr_numbers` random numbers from the `data.numbers` character set.

6. The code shuffles the elements in `password_list` to ensure randomness in the password.

7. It creates the final password by concatenating the shuffled elements in `password_list`.

8. The generated password is displayed to the user.

# 🔐 Code Specifications:

- The code uses an external module named `data` which is private and is not included in the code posted on GitHub. Users must request access to this module separately for the code to work correctly.

- Users can customize the length and composition of the password by specifying the number of letters, symbols, and numbers they want.

- The code ensures that the generated password is random by shuffling the elements in `password_list`.

- The final password is displayed to the user.

