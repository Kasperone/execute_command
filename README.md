# WiFi Password Extractor

This is a Python script that retrieves saved WiFi passwords from a Windows machine and sends them via email. It uses the `netsh` command to list and extract WiFi profiles and their stored passwords. This script is intended for educational purposes to understand how network credentials are stored and managed on Windows systems.

## Features
- Extracts all saved WiFi profiles and their passwords.
- Uses the `netsh` command to retrieve stored credentials.
- Sends the extracted data via email.

## Prerequisites
- Python 3.x
- Windows operating system
- Internet connection (for sending emails)

## Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/wifi_password_extractor.git
cd wifi_password_extractor
```

## Usage
Run the script to extract saved WiFi passwords and send them via email.

```bash
python3 wifi_password_extractor.py
```

### Notes:
- Replace `john@gmail.com` and `abc123` in the script with your actual email credentials.
- Ensure that **Less Secure Apps** access is enabled on your Gmail account or use an app-specific password.
- Running this script requires administrator privileges on Windows.

## Example Output:

```
SSID: HomeNetwork
Password: mysecurepassword

SSID: OfficeWiFi
Password: work1234
```

## Troubleshooting
- Ensure you have an active internet connection for sending emails.
- Verify that your email credentials are correct.
- Run the script with administrator privileges to access network profiles.

## License
This project is licensed under the MIT License.

## About
This script is part of the course **Learn Python & Ethical Hacking from Scratch** on Udemy. The course covers Python scripting and its application in ethical hacking, network security, and more.

---

### Disclaimer:
This script is for educational purposes only. Unauthorized access to network credentials is illegal and unethical. Use this script only on systems you have explicit permission to test.