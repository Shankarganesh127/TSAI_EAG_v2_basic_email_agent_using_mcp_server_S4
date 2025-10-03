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
        # Get SMTP configuration from environment variables (already set in venv)
        smtp_host = os.environ.get("SMTP_HOST")
        smtp_port = int(os.environ.get("SMTP_PORT"))
        smtp_user = os.environ.get("SMTP_USER")
        smtp_pass = os.environ.get("SMTP_PASS")
        from_addr = os.environ.get("SMTP_FROM")

        # Check required settings
        if not all([smtp_host, smtp_port, smtp_user, smtp_pass, from_addr]):
            missing = [name for name, val in [
                ("SMTP_HOST", smtp_host), ("SMTP_PORT", smtp_port),
                ("SMTP_USER", smtp_user), ("SMTP_PASS", smtp_pass), ("SMTP_FROM", from_addr)
            ] if not val]
            return {"content": [TextContent(
                type="text",
                text=f"Missing required SMTP environment variables: {', '.join(missing)}"
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