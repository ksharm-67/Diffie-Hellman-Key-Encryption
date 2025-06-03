# Diffie-Hellman-Key-Encryption

DESCRIPTION:

Using existing libraries to perform key exchange and encryption using a 256-bit key. To generate the key, we will implement the Diffie-Hellman algorithm. We will then use a symmetric encryption scheme (AES) to encrypt and decrypt any given data.

===================================================================

REQUIREMENTS:

Python 3.6 or higher

pycryptodome library for AES encryption and decryption

===================================================================

INSTALLATION:

Install Python 3 if it is not already installed. You can download it from Python.org.

Install the required dependencies using pip:

pip install pycryptodome

===================================================================

USAGE:

Run the program from the command line, providing the necessary arguments.

Command Line Arguments

--iv : Initialization Vector (IV) in hexadecimal format.

--g_e : Exponent value for g.

--g_c : Constant to be subtracted from 2^g_e.

--N_e : Exponent value for N.

--N_c : Constant to be subtracted from 2^N_e.

--x : Private key.

--gy_modN : Public key received from the other party.

--ciphertext : The ciphertext (hex string) to be decrypted.

--plaintext : The plaintext string to be encrypted.

===================================================================

Example Usage

To run the program, use the following command:

python your_script.py --iv "B22C53917AAC5D8FD63AB794541C54E2" \
    --g_e 2048 --g_c 3 --N_e 2048 --N_c 5 --x 12345 --gy_modN 67890 \
    --ciphertext "7656210bb5362111e89f08e5538fcadd24ee8f337f768644b28d82bb5325f361" \
    --plaintext "AdvancingCryptographyTechniquesFor2025Success"

===================================================================

Expected Output

The program prints the decrypted plaintext and the encrypted text in uppercase hexadecimal format, separated by a comma.

Example output:

AdvancingCryptographyTechniquesFor2025Success, 76 56 21 0B B5 36 21 11 E8 9F 08 E5 53 8F CA DD 24 EE 8F 33 7F 76 86 44 B2 8D 82 BB 53 25 F3 61

===================================================================

Troubleshooting

If you encounter an error related to missing dependencies, ensure pycryptodome is installed using pip install pycryptodome.

If decryption fails, check that the IV and ciphertext are correctly provided and formatted.
