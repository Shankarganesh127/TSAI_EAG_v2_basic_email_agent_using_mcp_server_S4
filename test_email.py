#!/usr/bin/env python3
"""
Simple test script to send an email about the EAG v2 Basic Email Agent project.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_project_email():
    """Send an email about this project"""

    # Email configuration
    recipient = "shankar7ganesh.uk@gmail.com"  # You can change this
    subject = "EAG v2 Basic Email Agent Project Update"
    body = """
Hello,

This is an automated email from the EAG v2 Basic Email Agent project.

Project Details:
- Name: EAG v2 Basic Email Agent (S4)
- Purpose: MCP server providing email sending capabilities
- Technology: Python, FastMCP, SMTP, Google Gemini AI
- Features: Simple email sending via SMTP with AI-powered decision making

The project includes:
- mcp_server.py: MCP server with email sending tool
- talk2mcp.py: Client that uses Gemini AI to interact with MCP tools
- Simple SMTP configuration via environment variables

To use this project:
1. Set up SMTP environment variables (SMTP_HOST, SMTP_USER, SMTP_PASS, SMTP_FROM)
2. Run the MCP server: uv run python mcp_server.py
3. Run the client: uv run python talk2mcp.py

This is a basic agent that can send emails using AI assistance.

Best regards,
EAG v2 Basic Email Agent
"""

    # Print configuration for debugging (masking password)
    print("Email Configuration:")
    print(f"SMTP Host: {os.environ.get('SMTP_HOST', 'Not set')}")
    print(f"SMTP Port: {os.environ.get('SMTP_PORT', 'Not set')}")
    print(f"SMTP User: {os.environ.get('SMTP_USER', 'Not set')}")
    print(f"SMTP Pass: {'*' * len(os.environ.get('SMTP_PASS', '')) if os.environ.get('SMTP_PASS') else 'Not set'}")
    print(f"From Address: {os.environ.get('SMTP_FROM', 'Not set')}")
    print(f"Recipient: {recipient}")
    print(f"Subject: {subject}")

    # For now, just print the email content (since we don't have SMTP configured)
    print("\nEmail Body:")
    print(body)

    print("\nNote: To actually send this email, ensure your SMTP credentials are correct.")
    print("The MCP server will use these environment variables automatically.")

if __name__ == "__main__":
    send_project_email()