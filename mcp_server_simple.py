from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent
import os
import smtplib
import ssl
from email.message import EmailMessage

# Create MCP server instance
mcp = FastMCP("EAG v2 Basic Email Agent")

@mcp.tool()
async def send_email(
    to: str,
    subject: str,
    body: str
) -> dict:
    """Send a simple email via SMTP.

    Args:
        to: Email address of the recipient
        subject: Email subject line
        body: Email body content

    Returns:
        dict with status message
    """
    try:
        # Get SMTP configuration from environment variables
        smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_user = os.getenv("SMTP_USER", "")
        smtp_pass = os.getenv("SMTP_PASS", "")
        from_addr = os.getenv("SMTP_FROM", smtp_user)

        # Check required settings
        if not smtp_host or not smtp_user or not smtp_pass or not from_addr:
            return {"content": [TextContent(
                type="text",
                text="Missing SMTP configuration. Set environment variables: SMTP_HOST, SMTP_USER, SMTP_PASS, SMTP_FROM"
            )]}

        # Create email message
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = from_addr
        msg["To"] = to
        msg.set_content(body)

        # Send email
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls(context=context)
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)

        return {"content": [TextContent(
            type="text",
            text=f"Email sent successfully to {to}"
        )]}

    except Exception as e:
        return {"content": [TextContent(
            type="text",
            text=f"Failed to send email: {str(e)}"
        )]}

if __name__ == "__main__":
    print("Starting EAG v2 Basic Email Agent MCP server...")
    mcp.run(transport="stdio")