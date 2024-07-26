# brkc xvzy fpxi wfml
from validate_email import validate_email
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dns import resolver
import smtplib
from smtplib import SMTP
import socks
import socket
import socksmtp

email_sender = 'savingchildrens@gmail.com'
sender_password = 'brkc xvzy fpxi wfml'

with open('/media/richie/Files/Data/BreachCompilation/data/4/d', 'r') as file:
    email_addresses = file.readlines()

for email_address in email_addresses:
    email_receiver = email_address.strip()  # Remove leading/trailing whitespaces

     # Skip empty lines
    if not email_receiver:
        continue
    if not validate_email(email_receiver):
        print(f"Skipping invalid email address: {email_receiver}")
        continue
    def verify(email):
        try:
            mx_record = resolver.resolve('gmail.com', 'MX')
            exchanges = [exchange.to_text().split() for exchange in mx_record]
        except (resolver.NoAnswer, resolver.NXDOMAIN, resolver.NoNameservers):
            exchanges = []
            

        address_to_test = email

        try:
            with socksmtp.SocksSMTP('gmail-smtp-in.l.google.com') as smtp:
                host_exists = True
                smtp.helo() # send the HELO command
                smtp.mail('rizatams0710@gmail.com') # send the MAIL command
                resp = smtp.rcpt(address_to_test)
                if resp[0] == 250: # check the status code
                    deliverable = True
                    send()
                    
                elif resp[0] == 550:
                    deliverable = False
                    print(f'{address_to_test} does not exist')
                    
                else:
                    print(resp[0])
        except smtplib.SMTPServerDisconnected as err:
            print("SMTP connection error") 
    def send():
        subject = 'Your $1 Can Feed 10 Children'
        body = MIMEMultipart('alternative')
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        
        html =  """\
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

            <meta charset="UTF-8">
            <meta content="width=device-width, initial-scale=1" name="viewport">
            <meta name="x-apple-disable-message-reformatting">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta content="telephone=no" name="format-detection">
            <title></title>
            <!--[if (mso 16)]>
            <style type="text/css">
            a {text-decoration: none;}
            </style>
            <![endif]-->
            <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
            <!--[if gte mso 9]>
        <xml>
            <o:OfficeDocumentSettings>
            <o:AllowPNG></o:AllowPNG>
            <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
            <!--[if !mso]><!-- -->
            <link href="https://fonts.googleapis.com/css?family=Montserrat:500,800&display=swap&subset=cyrillic-ext" rel="stylesheet">
            <!--<![endif]-->
        </head>

        <body>
            <div dir="ltr" class="es-wrapper-color">
                <!--[if gte mso 9]>
                    <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
                        <v:fill type="tile" color="#f6f6f6"></v:fill>
                    </v:background>
                <![endif]-->
                <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
                    <tbody>
                        <tr>
                            <td class="esd-structure es-p30t es-p30b es-p20r es-p20l" align="left">
                                <table cellpadding="0" cellspacing="0" width="100%">
                                    <tbody>
                                        <tr>
                                            <td width="560" class="esd-container-frame" align="center" valign="top">
                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                    <tbody>
                                                        <tr>
                                                            <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href=""><img src="https://d1h79zlghft2zs.cloudfront.net/uploads/2019/07/5601-768x234.png" alt="Saving children" style="display: block;" width="265" title="Giving Month"></a></td>
                                                        </tr>
                                                        <tr>
                                                            <td align="center" class="esd-block-text es-m-txt-c es-p15t">
                                                                <h1>Your $1 Can Feed 10 Children!</h1>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                    
                                                        </tr>
                                                        <tr>
                                                            <td align="center" class="esd-block-button">
                                                        
                                                            
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td class="esd-email-paddings" valign="top">
                                <table cellpadding="0" cellspacing="0" class="esd-header-popover es-header" align="center">
                                    <tbody>
                                        <tr>
                                            <td class="esd-stripe" align="center">
                                                <table bgcolor="#ffffff" class="es-header-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                    <tbody>
                                                        <tr>
                                                            <td class="es-p20t es-p20r es-p20l esd-structure" align="left" bgcolor="#79ADE0" style="background-color: #79ade0;">
                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-text">
                                                                                                <p style="font-size: 12px;"><p target="_blank" style="font-size: 12px;"></p>
                                                                                            </td>
                                                                                        </tr>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-spacer" height="20"></td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td class="esd-structure es-p20" align="left">
                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="560" class="es-m-p0r esd-container-frame" valign="top" align="center">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-image es-p10b" style="font-size: 0px;"><a target="_blank" href=""> Global Charity</a></td>
                                                                                        </tr>
                                                                                        <tr>
                                                                                            <p style="font-size: 18px; font-weight: 400; font-family: 'Arial Narrow Bold', sans-serif; line-height: 1.5rem">
                                                                                                We are reaching out to you with a plea born from aching hearts and the weight of desperation.
                                                                                            </p>
                                                                                        </tr>
                                                                                    
                                                                                        <tr>
                                                                                            <p style="font-size: 18px; font-weight: 400; font-family: 'Arial Narrow Bold', sans-serif;line-height: 1.5rem;">
                                                                                                In the quiet corners of Africa, where the sun sets on empty stomachs and rises on uncertain futures, there are children who cling to hope with fragile fingers. They dream of full bellies and brighter tomorrows, but their reality is one of hunger and despair.
                                                                                            </p>
                                                                                        </tr>
                                                                                        <tr>
                                                                                            <td class="esd-block-menu">
                                                                                                <table cellpadding="0" cellspacing="0" width="100%" class="es-menu">
                                                                                                    <tbody>
                                                                                                        <tr class="links">

                                                                                                        </tr>
                                                                                                    </tbody>
                                                                                                </table>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                                <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                                    <tbody>
                                        <tr>
                                            <td class="esd-stripe" align="center">
                                                <table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                    <tbody>
                                                        <tr>
                                                            <td class="esd-structure" align="left">
                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="600" class="esd-container-frame" align="center" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href=""><img class="adapt-img" src="https://tlr.stripocdn.email/content/guids/CABINET_731577d158970b53d7301423b8eb5e39/images/frame_29_xCZ.png" alt style="display: block;" width="600"></a></td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td class="esd-structure es-p30t es-p30b es-p20r es-p20l" align="left">
                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href=""><img src="https://tlr.stripocdn.email/content/guids/CABINET_731577d158970b53d7301423b8eb5e39/images/group_265.png" alt="Giving tuesday" style="display: block;" width="265" title="Giving Month"></a></td>
                                                                                        </tr>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-text es-m-txt-c es-p15t">
                                                                                                <h1>Your $1 Can Feed 10 Children!</h1>
                                                                                            </td>
                                                                                        </tr>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-text es-p15t es-p30b">
                                                                                                <p style="font-size: 18px; font-weight: 400; font-family: 'Arial Narrow Bold', sans-serif;line-height: 1.5rem;">
                                                                                                    For just $1, you can be the light in their darkness. With your generosity, you can provide not just a meal, but a lifeline to ten hungry children. It's a small gesture that carries immense power — the power to transform hunger into hope, and despair into possibility.
                                                                                                </p>
                                                                                            </tr>
                                                                                            </td>
                                                                                        </tr>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-button">
                                                                                                <!--[if mso]><a href="https://viewstripo.email" target="_blank" hidden>
            <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" esdevVmlButton href="https://viewstripo.email" 
                        style="height:51px; v-text-anchor:middle; width:201px" arcsize="50%" stroke="f"  fillcolor="#ed3a4b">
                <w:anchorlock></w:anchorlock>
                <center style='color:#ffffff; font-family:Montserrat, "Google Sans", "Segoe UI", Roboto, Arial, Ubuntu, sans-serif; font-size:18px; font-weight:400; line-height:18px;  mso-text-raise:1px'>Help the Needy</center>
            </v:roundrect></a>
        <![endif]-->
                                                                                            
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td class="esd-structure" align="left">
                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="600" class="esd-container-frame" align="center" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-image" style="font-size: 0px;"><a  href=""><img class="adapt-img" src="https://images.unsplash.com/photo-1611561606608-d8871add9eb7?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDEzfHx8ZW58MHx8fHx8" alt style="display: block;" width="600"></a></td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                                <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                                    <tbody>
                                        <tr>
                                            <td class="esd-stripe" align="center">
                                                <table bgcolor="#2A3C51" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: #2a3c51;">
                                                    <tbody>
                                                        <tr>
                                                            <td class="esd-structure es-p40t es-p30b es-p20r es-p20l" align="left">
                                                                <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="255" valign="top"><![endif]-->
                                                                <table cellpadding="0" cellspacing="0" align="left" class="es-left">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="250" class="esd-container-frame" align="center" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="left" class="esd-block-text es-p10t es-p5b es-m-txt-c">
                                                                                                <h1 style="color: #ffffff;">Donate Today</h1>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                            <td class="es-hidden" width="5"></td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                                <!--[if mso]></td><td width="150" valign="top"><![endif]-->
                                                                <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="150" align="left" class="esd-container-frame">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href=""><img src="https://images.unsplash.com/photo-1509099836639-18ba1795216d?q=80&w=1462&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt style="display: block;" width="150"></a></td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                                <!--[if mso]></td><td width="5"></td><td width="150" valign="top"><![endif]-->
                                                                <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="150" align="left" class="esd-container-frame">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank" href=""><img src="https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2hhcml0eSUyMGluJTIwQWZyaWNhfGVufDB8fDB8fHww" alt style="display: block;" width="150"></a></td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                                <!--[if mso]></td></tr></table><![endif]-->
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                                <table cellpadding="0" cellspacing="0" class="es-content" align="center">
                                    <tbody>
                                        <tr>
                                            <td class="esd-stripe" align="center">
                                                <table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                    <tbody>
                                                        <tr>
                                                            <td class="es-p20t es-p20r es-p20l esd-structure" align="left" bgcolor="#79ADE0" style="background-color: #79ade0;">
                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-spacer" height="20"></td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                                <table cellpadding="0" cellspacing="0" class="es-footer" align="center">
                                    <tbody>
                                        <tr>
                                            <td class="esd-stripe" align="center">
                                                <table bgcolor="#ffffff" class="es-footer-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                    <tbody>
                                                        <tr>
                                                            <td class="esd-structure es-p30t es-p10b es-p20r es-p20l" align="left">
                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-text es-m-txt-c">
                                                                                                <h1 style="color: red;">Donate Today</h1>

                                                                                                <p style="font-size: 18px; font-weight: 400; font-family: 'Arial Narrow Bold', sans-serif;line-height: 1.5rem;">
                                                                                                    Every moment counts. Every dollar matters. Your donation can mean the world to a child who has known nothing but hunger and hardship.<br>
                                                                                                    
                                                                                                </p>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td class="esd-structure es-p20t es-p20r es-p20l esdev-adapt-off" align="left">
                                                                <table width="560" cellpadding="0" cellspacing="0" class="esdev-mso-table">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td class="esdev-mso-td" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td width="174" class="es-m-p0r esd-container-frame" align="center">
                                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                                    <tbody>
                                                                                                        <tr>
                                                                                                            <td align="center" class="esd-block-image" style="font-size: 0px;"><a href=""><img class="adapt-img" src="https://plus.unsplash.com/premium_photo-1661775317533-2163ba4dbc93?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjF8fGNoYXJpdHklMjBpbiUyMEFmcmljYXxlbnwwfHwwfHx8MA%3D%3D" alt style="display: block; border-radius: 0 0 0 50px" width="174"></a></td>
                                                                                                        </tr>
                                                                                                    </tbody>
                                                                                                </table>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                            <td width="20"></td>
                                                                            <td class="esdev-mso-td" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" class="es-left" align="left">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td width="173" class="esd-container-frame" align="center">
                                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                                    <tbody>
                                                                                                        <tr>
                                                                                                            <td align="center" class="esd-block-image" style="font-size: 0px;"><a href=""><img class="adapt-img" src="https://images.unsplash.com/photo-1582307811683-75b18a39ab71?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt style="display: block;" width="173"></a></td>
                                                                                                        </tr>
                                                                                                    </tbody>
                                                                                                </table>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                            <td width="20"></td>
                                                                            <td class="esdev-mso-td" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" class="es-right" align="right">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td width="173" align="center" class="esd-container-frame">
                                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                                    <tbody>
                                                                                                        <tr>
                                                                                                            <td align="center" class="esd-block-image" style="font-size: 0px;"><a  href=""><img class="adapt-img" src="https://images.unsplash.com/photo-1567057419565-4349c49d8a04?q=80&w=1472&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt style="display: block; border-radius: 0 50px 0 0 " width="173"></a></td>
                                                                                                        </tr>
                                                                                                    </tbody>
                                                                                                </table>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td class="esd-structure es-p25t es-p25b es-p20r es-p20l" align="left">
                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <p  style="font-size: 18px; font-weight: 400; font-family: 'Arial Narrow Bold', sans-serif;line-height: 1.5rem;">
                                                                                                Please, if you can, don't turn away. Open your heart to the cries of these children. <span strong style="color: red;">Donate now via PayPal to savingchildrens@gmail.com </span> and be the hero they desperately need.
                                                                                            </p>

                                                                                            <td align="center" class="esd-block-text es-p25b es-m-txt-c" esd-links-underline="none" esd-links-color="#333333">
                                                                                                <h1 style="color: red;"><strong> Donate Today </h1>
                                                                                            </td>

                                                                                        </tr>
                                                                                        
                                                                                        <tr>
                                                                                            

                                                                                            <td align="center" class="esd-block-social" style="font-size:0">
                                                                                                <table cellpadding="0" cellspacing="0" class="es-table-not-adapt es-social">
                                                                                                    <tbody>
                                                                                                        <tr>
                                                                                                            <td align="center" valign="top" class="es-p20r"><img src="https://tlr.stripocdn.email/content/assets/img/social-icons/rounded-black/facebook-rounded-black.png" alt="Fb" title="Facebook" width="32"></td>
                                                                                                            <td align="center" valign="top" class="es-p20r"><img src="https://tlr.stripocdn.email/content/assets/img/social-icons/rounded-black/twitter-rounded-black.png" alt="Tw" title="Twitter" width="32"></td>
                                                                                                            <td align="center" valign="top" class="es-p20r"><img src="https://tlr.stripocdn.email/content/assets/img/social-icons/rounded-black/instagram-rounded-black.png" alt="Ig" title="Instagram" width="32"></td>
                                                                                                            <td align="center" valign="top"><img src="https://tlr.stripocdn.email/content/assets/img/social-icons/rounded-black/youtube-rounded-black.png" alt="Yt" title="Youtube" width="32"></td>

                                                                                                            <p  style="font-size: 18px; font-weight: 400; font-family: 'Arial Narrow Bold', sans-serif;line-height: 1.5rem;">
                                                                                                                <span strong style="color: red;">To donate now, head on to PayPal and send your donations to savingchildrens@gmail.com. </span> Be hero today. Donate.
                                                                                                            </p
                                                                                                        </tr>
                                                                                                    </tbody>
                                                                                                </table>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td class="esd-structure es-p20t es-p20b es-p20r es-p20l" align="left">
                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="560" align="left" class="esd-container-frame">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-text">
                                                                                                <p><a href="#">Privacy Policy</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<a href="#">Terms of Use</a><br><br>No longer want to receive these emails?&nbsp;<a href target="_blank">Unsubscribe</a><br>661 Johanesburg, South Africa</p>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                                <table cellpadding="0" cellspacing="0" class="es-content esd-footer-popover" align="center">
                                    <tbody>
                                        <tr>
                                            <td class="esd-stripe" align="center" esd-custom-block-id="767243">
                                                <table class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: transparent;">
                                                    <tbody>
                                                        <tr>
                                                            <td class="esd-structure es-p20" align="left">
                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                    <tbody>
                                                                        <tr>
                                                                            <td width="560" class="esd-container-frame" align="left">
                                                                                <table cellpadding="0" cellspacing="0" width="100%">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="center" class="esd-block-image es-infoblock made_with" style="font-size:0"><a target="_blank" href="" alt width="125" style="display: block;"></a></td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </td>
                                                                        </tr>
                                                                    </tbody>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </body>

        </html>

        """
        allpart = MIMEText(html, 'html')
        body.attach(allpart)
        context = ssl.create_default_context()


        em.set_content(body)

        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, sender_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            print(f"Email sent to {email_receiver}")
        except Exception as e:
            print(f"Failed to send email to {email_receiver}. Error: {e}")
            
    verify(email_receiver) 