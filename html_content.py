def get_html_content(name, position, team):
    html_content = f'''<!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Participant Credentials - Developers Day 2025</title>
            
        </head>
        <body
            style="height: 100%; align-items: center; background-color: white; margin: 0; font-family: 'Arial', sans-serif; display: flex;">
            
            <style>
                .action-button:hover {{
                    background-color: #7a1f1c !important;
                    color: #ffffff !important;
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                }}
            </style>
            
            <div style="max-width: 600px; margin: 10px auto; width: 100%;">
                <div style="margin: 0px 5px; padding: 0px;">
                    <div
                        style="margin: 5px 0px 0px 0px; background: linear-gradient(to bottom right, #40b6c8, #22373e); color: #FFFFFF; padding: 20px; border-radius: 12px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);">

                        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" align="center" style="text-align:center; padding:20px 0 40px 0;">
                            <tr>
                                <td align="center" style="width:33%; padding:0 10px;">
                                <img src="https://i.postimg.cc/gjTGrWFL/ACM-Logo.png" alt="ACM Logo" style="height:8em; display:block;">
                                </td>
                                <td align="center" style="width:33%; padding:0 10px;">
                                <span style="font-size:30px; font-weight:bolder; display:inline-block; color:#ffffff;">Congratulations!</span>
                                </td>
                                <td align="center" style="width:33%; padding:0 10px;">
                                <img src="https://lh5.googleusercontent.com/y6A7W7FAUqkWtc8DUrZZCpNNYgqMp2K5HXv00FUtdMye_sWgv06XE8k3QpubBitjIr7Ry293MQjpgjaB8yv7_zvtsIlL2PtzAlcdqjc3ibzMLXrz42LgsC5mMJnJ9VFppdxhzbFRBEZA6wficA6YY6o" alt="FAST NUCES Logo" style="height:7em; display:block;">
                                </td>
                            </tr>
                        </table>

                        <div style="padding: 0 20px;">
                            <p style="margin: 0 0 20px 0; text-align: justify; line-height: 1.6; font-size: 15px;">
                                <strong style="color: #FFFFFF; font-size:18px">Dear {name.strip()}</strong>,
                                <br><br>
                                We are pleased to inform you that you have been selected as a {position.strip()} of Team {team.strip()} at ACM-FAST NUCES Karachi for the 2026-2027 term. Your skills, dedication, and enthusiasm stood out during the selection process, and we’re excited to have you on board.
                                <br><br>
                                As a token of our appreciation, we’ve attached a special GIF that celebrates your selection. Feel free to share it on LinkedIn or your social platforms to mark this milestone!
                        </div>

                        <div style="border-top: 1px solid rgba(255,255,255,0.2); margin-top: 25px; padding: 25px 0 15px;">
                            <div style="text-align: center;">
                                <p style="margin: 0 0 15px 0; font-size: 15px; letter-spacing: 0.5px; color: FFFFFF;">
                                    STAY CONNECTED
                                </p>
                                <div style="margin:10px">
                                    <a href="https://www.linkedin.com/company/acmnuceskhi" target="_blank" class="social-icon"
                                        style="display: inline-block; transition: all 0.3s ease;">
                                        <img src="https://img.icons8.com/color/36/linkedin.png" alt="LinkedIn"
                                            style="width: 36px; height: 36px;">
                                    </a>
                                    <a href="https://www.facebook.com/acmnuceskhi" target="_blank" class="social-icon"
                                        style="display: inline-block; transition: all 0.3s ease;">
                                        <img src="https://img.icons8.com/color/36/facebook-new.png" alt="Facebook"
                                            style="width: 36px; height: 36px;">
                                    </a>
                                    <a href="https://www.instagram.com/acmnuceskhi" target="_blank" class="social-icon"
                                        style="display: inline-block; transition: all 0.3s ease;">
                                        <img src="https://img.icons8.com/color/36/instagram-new--v1.png" alt="Instagram"
                                            style="width: 36px; height: 36px;">
                                    </a>
                                </div>
                        
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>

        </html>'''
    return html_content

