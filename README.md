# DRC PDF Brute Force Cracker

A tool to crack PDF passwords using a wordlist in a brute force manner. This tool is designed for ethical purposes only.

## Disclaimer
We are not responsible for any illegal use of this tool. Please use it ethically and in compliance with all applicable laws. Use this tool only for educational purposes and with your own files.

## Features
- Brute force cracking of PDF files
- Configurable wordlist and thread count
- Verbose output for better understanding of progress

---

## Requirements

- **Python 3.6+** (Python 3.8 or newer recommended)
- **Operating System**: Windows
- **Dependencies**: You can install the required dependencies via `requirements.txt`.

---

## Setup Instructions (Windows)

1. **Download the Repository**  
   Download or clone the repository to your local machine.

2. **Install Python**  
   - If Python is not already installed, download and install Python from the [official website](https://www.python.org/downloads/).  
   - During installation, make sure to check the "Add Python to PATH" checkbox.

3. **Install Dependencies**  
   - Open **Command Prompt** (Press `Win + R`, type `cmd`, and hit Enter).
   - Navigate to the folder where the repository is located:
     ```bash
     cd path\to\your\repository
     ```
   - Run the following command to install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Setup Script**  
   - Run the `setup_drcpdf.bat` script by double-clicking it. This will automatically configure your environment.

---

## Usage

Once everything is set up, you can start cracking PDF files by running the following command in **Command Prompt**:

```bash
python drc_pdf_cracker.py -p <path_to_pdf> -w <path_to_wordlist> -v -mp 4
```

### Arguments:
- `-p <path_to_pdf>`: Path to the PDF file you want to crack.
- `-w <path_to_wordlist>`: Path to the wordlist file you want to use.
- `-v`: Enable verbose output (shows detailed cracking process).
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
- Use the verbose flag (`-v`) to check the current status of the brute-forcing process.

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
