import meshtastic
import meshtastic.serial_interface
import os

# Email configuration (msmtp must be pre-configured as described earlier)
RECIPIENT_EMAIL = "recipient@example.com"

# Function to send email
def send_email(subject, body):
    """
    Sends an email using msmtp.
    """
    email_command = f'echo -e "Subject: {subject}\\n\\n{body}" | msmtp {RECIPIENT_EMAIL}'
    os.system(email_command)
    print(f"Email sent to {RECIPIENT_EMAIL}")

# Callback function to handle received messages
def on_receive(packet, interface):
    """
    Callback for handling incoming packets.
    """
    try:
        print(f"Received packet: {packet}")
        
        # Extract message content
        text = packet.get('payload', {}).get('text', "No message content")
        sender = packet.get('fromId', "Unknown sender")
        
        # Format subject and body
        subject = f"{sender}: {text[:50]}"  # Limit subject length to avoid truncation
        email_body = f"Message from {sender}:\n\n{text}"
        
        # Send email
        send_email(subject, email_body)
        
    except Exception as e:
        print(f"Error handling packet: {e}")

# Main function
def main():
    try:
        # Initialize Meshtastic interface
        interface = meshtastic.serial_interface.SerialInterface()
        interface.onReceive = on_receive
        print("Listening for incoming messages...")
        
        # Keep the script running
        while True:
            pass
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'interface' in locals():
            interface.close()

if __name__ == "__main__":
    main()
