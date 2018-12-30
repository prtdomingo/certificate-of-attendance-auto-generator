import os

def outlook_is_running():
    import win32ui
    try:
        win32ui.FindWindow(None, "Microsoft Outlook")
        return True
    except win32ui.error:
        return False

def open_outlook():
    try:
        os.startfile("outlook")
    except:
        print("Outlook didn't open successfully")

def send_email(emailTo, subject, body, attachment, shouldSend=True):
    import win32com.client
    from win32com.client import Dispatch

    if not outlook_is_running():
        open_outlook()

    outlook = win32com.client.Dispatch("Outlook.Application")
    email = outlook.CreateItem(0x0)
    email.Subject = subject
    email.BodyFormat = 2
    email.HTMLBody = body
    email.To = emailTo

    if attachment:
        email.Attachments.Add(attachment)

    if shouldSend:
        email.Send()
    else:
        email.display()


if __name__ == "__main__":
    send_email("email@email.com", "Test Subject", "Test Body", None, False)