# DRC PDF Cracker

DRC PDF Cracker is a Python-based tool that performs brute-force password cracking on encrypted PDF files using a wordlist. The tool utilizes multiple threads for efficient password guessing and provides progress updates through a rich command-line interface.

## Features

- **Brute-force PDF Password Cracking**: Attempts to crack PDF passwords using a wordlist.
- **Multi-threaded Execution**: Speeds up the process by utilizing multiple threads.
- **Rich CLI Interface**: Provides a visually appealing interface with progress bars and status messages.
- **Automatic Installation of Dependencies**: Checks and installs missing dependencies like `rich`, `pikepdf`, and `pyfiglet`.

## Requirements

- Python 3.x
- Pip (Python package manager)
- A wordlist file for password guessing
- A password-protected PDF file to crack


## Auto install Requriements 

The script will automatically check for required dependencies and install any missing ones.

If the script detects that pip is not installed, it will attempt to install pip automatically. If Python is missing, it will provide an error message prompting the user to install Python.

---

## Installing Python and Pip

### On Windows:

1. **Download Python**:
   - Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Download and install Python for Windows (ensure you check the box to "Add Python to PATH" during installation).

2. **Verify Python and Pip**:
   - Open Command Prompt and type the following to check if Python and `pip` are installed:
     ```bash
     python --version
     pip --version
     ```
   - If `pip` is not installed, run the following command to install it:
     ```bash
     python -m ensurepip --upgrade
     ```

### On Linux (Ubuntu/Debian-based distributions):

1. **Install Python**:
   - Open Terminal and run:
     ```bash
     sudo apt update
     sudo apt install python3
     ```

2. **Install Pip**:
   - Run the following to install `pip`:
     ```bash
     sudo apt install python3-pip
     ```

3. **Verify Installation**:
   - Check if Python and `pip` are installed:
     ```bash
     python3 --version
     pip3 --version
     ```

### On macOS:

1. **Install Python**:
   - macOS usually comes with Python pre-installed, but you can install the latest version using Homebrew:
     ```bash
     brew install python
     ```

2. **Install Pip**:
   - `pip` should come with the Python installation. If it's not installed, use the following command:
     ```bash
     python3 -m ensurepip --upgrade
     ```

3. **Verify Installation**:
   - Check if Python and `pip` are installed:
     ```bash
     python3 --version
     pip3 --version
     ```

## Installation

1. Clone the repository or download the script.
   ```bash
   git clone https://github.com/Hapi-iz/Drc-pdf-cracker.git
   cd Drc-pdf-cracker

---

## Usage

Once everything is set up, you can start cracking PDF files by running the following command in **Command Prompt**:

```bash
python drcpdf.py -p <path_to_pdf> -w <path_to_wordlist> -v -mp 4
```

### Arguments:
- `-p <path_to_pdf>`: Path to the PDF file you want to crack.
- `-w <path_to_wordlist>`: Path to the wordlist file you want to use.
- `-mp <num_threads>`: Number of threads for multi-threading (default is 4).

---

## Wordlist

You can use any wordlist for cracking the PDF. A popular wordlist is available on GitHub:

- [Wordlists by kkrypt0nn](https://github.com/kkrypt0nn/wordlists.git)

**Credit**: Wordlist used in this tool is from the above repository. It's not owned by me.

---

## Troubleshooting

### Issue 1: **Python not recognized as a command**
**Solution**:  
Ensure that Python is added to the system's PATH. During installation, there is an option to "Add Python to PATH". If you missed that, you can add it manually:
- Go to **System Properties > Environment Variables**, and in the "System variables" section, add Python's path (e.g., `C:\Python39`) to the `Path` variable.

### Issue 2: **Module not found when running the script**
**Solution**:  
This is usually because the required dependencies are not installed. Run the following command to install the necessary packages:
```bash
pip install -r requirements.txt
```
Make sure to do this in the folder where the repository is located.

### Issue 3: **Tool not working or hangs while cracking**
**Solution**:  
- Ensure that the wordlist you are using is large enough.
- Try reducing the number of threads (`-mp` flag) if the tool hangs due to resource limitations.


### Issue 4: **PDF is not being cracked**
**Solution**:  
If the password is too complex or not in the wordlist, the tool will not be able to find the password. Ensure that the wordlist you're using contains a good set of possible passwords.

---

## License

MIT License. See the LICENSE file for more details.

---

## Credits

- **Wordlist**: The wordlist used in this tool is from the [kkrypt0nn Wordlists](https://github.com/kkrypt0nn/wordlists.git). Thanks to the author for providing these useful resources.

---

Feel free to create issues or contribute to this project if you find any bugs or improvements.

---
