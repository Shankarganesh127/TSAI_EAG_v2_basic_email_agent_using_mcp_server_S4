# EAG v2 Basic Email Agent (S4)

A simple MCP (Model Context Protocol) server that provides email sending capabilities using AI assistance.

## Features

- Simple email sending via SMTP
- AI-powered email composition using Google Gemini
- Environment variable configuration
- MCP server for tool integration

## Project Structure

- `mcp_server.py` - MCP server with email sending tool
- `talk2mcp.py` - AI client that interacts with MCP tools
- `test_email.py` - Test script demonstrating email functionality
- `main.py` - Basic project entry point

## Setup

The SMTP environment variables are already configured in the virtual environment:

- `SMTP_HOST=smtp.gmail.com`
- `SMTP_PORT=587`
- `SMTP_USER=****@gmail.com`
- `SMTP_PASS=****`
- `SMTP_FROM=****@gmail.com`

For Gmail, ensure you have:
- 2FA enabled on your Google account
- An App Password generated (not your regular password)

## Usage

1. Start the MCP server:
   ```bash
   uv run python mcp_server.py
   ```

2. In another terminal, run the AI client:
   ```bash
   uv run python talk2mcp.py
   ```

3. Test email functionality:
   ```bash
   uv run python test_email.py
   ```

## Email Tool

The MCP server provides a `send_email` tool with parameters:
- `to`: Recipient email address
- `subject`: Email subject
- `body`: Email content

## Technology Stack

- Python 3.13+
- FastMCP for MCP server
- Google Gemini AI for intelligent email composition
- SMTP for email delivery
- python-dotenv for configuration
