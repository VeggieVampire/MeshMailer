# MeshMailer

MeshMailer is a Python script that integrates with Meshtastic devices to receive messages and forward them via email. This tool allows seamless communication by bridging the Meshtastic network with email notifications.

---

## Features
- Receives messages from Meshtastic devices.
- Dynamically formats email subjects with sender and message preview.
- Sends messages to predefined email recipients.

---

## Prerequisites

### Hardware
- A Meshtastic-compatible device.
- A Raspberry Pi or any system with Python 3 installed.

### Software
- Python 3.7 or higher.
- Meshtastic Python library.
- msmtp (for email sending).

---

## Setup Instructions

### 1. Install Required Libraries

```bash
pip install meshtastic
```

### 2. Configure Email Sending with msmtp

1. Install msmtp:
   ```bash
   sudo apt update
   sudo apt install msmtp
   ```

2. Create a configuration file for msmtp:
   ```bash
   nano ~/.msmtprc
   ```

   Add the following content:
   ```
   defaults
   auth on
   tls on
   tls_starttls on
   tls_trust_file /etc/ssl/certs/ca-certificates.crt
   logfile ~/.msmtp.log

   account gmail
   host smtp.gmail.com
   port 587
   user your-email@gmail.com
   password your-app-password
   from your-email@gmail.com

   account default : gmail
   ```

   Replace `your-email@gmail.com` and `your-app-password` with your Gmail credentials. Use an **App Password** instead of your regular password.

3. Set permissions for the configuration file:
   ```bash
   chmod 600 ~/.msmtprc
   ```

### 3. Clone the MeshMailer Repository

```bash
git clone https://github.com/VeggieVampire/MeshFile.git
cd MeshFile
```

### 4. Configure the Script

Open `receiver.py` and modify the following variables:

- `RECIPIENT_EMAIL`: Set the recipient's email address.
- Update any other configurations as needed.

### 5. Run MeshMailer

Start the script to begin listening for messages and forwarding them via email:

```bash
python3 receiver.py
```

---

## Running as a Service (Optional)

To keep MeshMailer running in the background:

1. Create a systemd service file:
   ```bash
   sudo nano /etc/systemd/system/meshmailer.service
   ```

2. Add the following content:
   ```
   [Unit]
   Description=MeshMailer Service
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /path/to/receiver.py
   Restart=always
   User=pi

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl enable meshmailer.service
   sudo systemctl start meshmailer.service
   ```

---

## Troubleshooting

### Common Issues
- **Email not sent**: Ensure msmtp is correctly configured and the credentials are valid.
- **No messages received**: Verify that your Meshtastic device is connected and detected by the script.

### Checking Logs
- View msmtp logs:
  ```bash
  cat ~/.msmtp.log
  ```
- View MeshMailer output:
  ```bash
  journalctl -u meshmailer.service
  ```

---

## License

MeshMailer is released under the MIT License.

---

## Author

Created by Nick Farrow.
