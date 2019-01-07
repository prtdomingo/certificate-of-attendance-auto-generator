import cv2
import csv_reader as csvr
import email_sender as esender
import os

# Script Settings
isDebug         = True # Setting this into True will prevent the script to send the actual email to intended recipients
attendee_list   = csvr.read_csv("src/csv/ListOfAttendees-Test.csv") 
template_path   = "src/template/globalaibootcamp-template.png" # Specify email template path
imageWxH        = (1360, 1024)
font            = cv2.FONT_HERSHEY_SIMPLEX
fontScale       = 2
fontColor       = (0,0,0) # Black
lineType        = 2

# Email Details
emailSubject = "INSERT EVENT NAME"

def generate_email_body(name):
    return ("***This email and attachment is automatically generated using a script. *** <br><br>"
            "Hi " + name + ", <br><br>"
            "INSERT YOUR EMAIL BODY HERE"
           )

def send_certificate():
    """ 
    Iterate through the attendee list from the CSV file,
    Insert the attendee name on the center of the certificate image,
    then opens Outlook Application and sends the email to the recipients that includes the certificate attachment
    """
    for attendee in attendee_list:
        img = cv2.imread(template_path)
        imgResize = cv2.resize(img, imageWxH)

        name = attendee[0]        
        email = attendee[1]
        textSize = cv2.getTextSize(name, font, 2, 2)[0]

        # Center text on image based on image and text size
        textX = int((imgResize.shape[1] - textSize[0]) / 2)
        textY = int((imgResize.shape[0] + textSize[1]) / 2)

        # Insert attendee name on certificate template
        cv2.putText(imgResize, name, (textX, textY), font, fontScale, fontColor, lineType)

        try:
            # Use Attendee Name as File Name and save it on certificate folder
            certificatePath = os.path.join(os.getcwd(), "certificate", name.replace(" ", "").replace(".", "").lower() + ".png")
            cv2.imwrite(certificatePath, imgResize)

            emailBody = generate_email_body(name)

            esender.send_email(email, emailSubject, emailBody, certificatePath, not isDebug)
        except Exception as e:
            print(e)


if __name__ == "__main__":

    if not os.path.exists("certificate"):
        os.mkdir("certificate")

    send_certificate()
