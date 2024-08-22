# Caesar Cipher Encoder/Decoder

## Overview

The Caesar Cipher Encoder/Decoder is a Python application that implements the Caesar cipher algorithm, a classic substitution cipher that shifts letters of the alphabet by a fixed number of positions. This project provides both encoding and decoding functionalities, allowing users to securely encode and decode messages using this simple cryptographic technique.

## Features

- **Encoding**: Shift each letter of the input text forward in the alphabet by a specified number of positions.
- **Decoding**: Shift each letter of the encoded text backward in the alphabet to retrieve the original message.
- **Flexible Shifts**: Handles shift values greater than the alphabet length by wrapping around.
- **Interactive Interface**: Prompts users to input their message, choose encoding or decoding, and specify the shift amount.

## Usage

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/caesar-cipher.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd caesar-cipher
    ```

3. **Run the Script**:

    ```bash
    python caesar_cipher.py
    ```

4. **Follow the Prompts**:
    - **Type 'encode'** to encrypt a message.
    - **Type 'decode'** to decrypt a message.
    - Enter the message you wish to encode or decode.
    - Provide the shift number (e.g., `3`) to apply the cipher.

## Example

**Encoding:**

- **Input Message**: `hello`
- **Shift Number**: `5`
- **Output**: `mjqqt`

**Decoding:**

- **Input Message**: `mjqqt`
- **Shift Number**: `5`
- **Output**: `hello`

## Code Explanation

The script uses a list of alphabet letters (with repetitions for wrapping) and applies the Caesar cipher logic:
- For encoding, letters are shifted forward.
- For decoding, letters are shifted backward.

The program runs in a loop, allowing multiple operations until the user decides to exit.

## Contribution

Feel free to fork this repository, submit pull requests, or open issues for enhancements and bug fixes. Contributions and feedback are greatly appreciated!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Your Name](https://github.com/yourusername)
