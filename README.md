# WPA Cracking Project

## Introduction
This project explores the process of WPA (Wi-Fi Protected Access) cracking. WPA is a security protocol designed to secure wireless computer networks. Despite its robust encryption mechanisms, WPA can be susceptible to attacks if weak passwords are used. This project demonstrates a basic approach to identifying available networks and attempting to connect to them using a Python script.

## Project Objectives
The primary objectives of this project are:
- To understand the process of scanning for Wi-Fi networks using Python.
- To develop a script that can connect to a Wi-Fi network using an SSID and password.
- To highlight the ethical and legal considerations associated with Wi-Fi cracking.
- To provide a detailed explanation of WPA cracking and the steps involved.

## Methodology

### Tools and Technologies
The following tools and technologies were used in this project:
- **Python**: A versatile programming language that is widely used for scripting and automation.
- **nmcli**: A command-line tool for managing network connections on Linux, used to scan for and connect to Wi-Fi networks.
- **subprocess**: A Python module that allows for spawning new processes, connecting to their input/output/error pipes, and obtaining their return codes.

### WPA Cracking Overview
WPA cracking involves attempting to gain unauthorized access to a Wi-Fi network protected by WPA security. The process typically involves the following steps:
1. **Network Scanning**: Identifying available Wi-Fi networks and gathering information such as SSID, signal strength, and security type.
2. **Handshake Capture**: Capturing the four-way handshake between the client and the access point during the authentication process.
3. **Password Cracking**: Using various techniques, such as dictionary attacks or brute-force attacks, to crack the WPA passphrase from the captured handshake.

### Script Explanation
The `Wifi-Hacking.py` script consists of two main functions: `scan_networks` and `connect_to_network`.

#### scan_networks Function
This function uses the `nmcli device wifi list` command to scan for available Wi-Fi networks. The results are captured and decoded from bytes to a string format for readability. This function helps in identifying the networks within range.

#### connect_to_network Function
This function uses the `nmcli device wifi connect` command to connect to a specified Wi-Fi network. The function takes the SSID and password of the target network as input parameters. The success of the connection attempt is determined by the correctness of the provided credentials.

#### Main Script Workflow
The main part of the script performs the following steps:
1. Scans for available Wi-Fi networks and displays them to the user.
2. Prompts the user to enter the SSID and password of the desired network.
3. Attempts to connect to the specified network using the provided credentials.
4. Displays the result of the connection attempt to the user.

## Results
The script successfully scans for available Wi-Fi networks and attempts to connect to a specified network using the provided SSID and password. The results of these operations are displayed to the user, indicating whether the connection attempt was successful or not.

## Ethical Considerations
It is crucial to highlight that unauthorized access to Wi-Fi networks is illegal and unethical. This project and its script should only be used for educational purposes and on networks for which the user has explicit permission to access. Ethical hacking practices must be adhered to at all times to avoid legal consequences and respect the privacy and security of others.

## Downloading the Code
The code for this project is available on GitHub. You can download it using the following steps:
1. Visit the GitHub repository at: [https://github.com/HoussamEddineBoukhalfa/WPA_Cracking](https://github.com/HoussamEddineBoukhalfa/WPA_Cracking)
2. Click on the `Code` button.
3. Select `Download ZIP` to download the repository as a ZIP file.
4. Extract the ZIP file to your desired location on your computer.
5. Navigate to the extracted folder and open the `Wifi-Hacking.py` script.

## Conclusion
This project demonstrates a basic method for scanning and attempting to connect to Wi-Fi networks using Python and `nmcli`. While the script serves educational purposes in understanding network connections, it also emphasizes the importance of ethical considerations in network security.

## Future Work
Future improvements to this project could include:
- Enhancing error handling to provide more detailed feedback to the user.
- Implementing a graphical user interface (GUI) to improve usability.
- Adding support for other operating systems, such as Windows and macOS.
- Extending the script to include functionality for more advanced network management tasks.
- Incorporating advanced WPA cracking techniques such as handshake capture and dictionary attacks.

## References
- WPA (Wi-Fi Protected Access) Overview: [Wikipedia](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access)
- nmcli Tool Documentation: [NetworkManager/nmcli](https://developer.gnome.org/NetworkManager/stable/nmcli.html)
- Python subprocess Module: [Python Documentation](https://docs.python.org/3/library/subprocess.html)
- Aircrack-ng Suite: [Aircrack-ng](https://www.aircrack-ng.org/)
