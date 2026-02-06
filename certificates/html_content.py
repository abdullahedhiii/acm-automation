def get_html_content(template_path, name, comp):
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Replace placeholders with actual values
    html_content = template.format(participant_name=name, competition_name=comp)

    return html_content

def get_confirmation_content(template_path, params, comp):
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    table_content = f'''
            <div style="background-color:#400000e1; border:3px solid #2920004e; border-radius:8px; padding:15px 20px; margin-top:20px;">
                <p style="margin:5px 0; color:#F0C93D;"><strong>Member 1:</strong> <span style="color:#FFFFFF;">{params["LeaderName"]}</span></p>
            </div>'''
    if params["Member1Name"] != "":
        table_content += f'''
          <div style="background-color:#400000e1; border:3px solid #2920004e; border-radius:8px; padding:15px 20px; margin-top:20px;">
              <p style="margin:5px 0; color:#F0C93D;"><strong>Member 1:</strong> <span style="color:#FFFFFF;">{params["Member1Name"]}</span></p>
          </div>'''
    if params["Member2Name"] != "":
        table_content += f'''
          <div style="background-color:#400000e1; border:3px solid #2920004e; border-radius:8px; padding:15px 20px; margin-top:20px;">
              <p style="margin:5px 0; color:#F0C93D;"><strong>Member 2:</strong> <span style="color:#FFFFFF;">{params["Member2Name"]}</span></p>
          </div>'''
  
    # Replace placeholders with actual values
    html_content = template.format(teamname=params["TeamName"], competitionname = comp, table = table_content)

    return html_content

# def get_html_content(name, position, team):
#     html = f'''<!DOCTYPE html>
#         <html lang="en">

#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>Participant Credentials - Developers Day 2025</title>
            
#         </head>
#         <body
#             style="height: 100%; align-items: center; background-color: white; margin: 0; font-family: 'Arial', sans-serif; display: flex;">
            
#             <style>
#                 .action-button:hover {{
#                     background-color: #7a1f1c !important;
#                     color: #ffffff !important;
#                     transform: translateY(-2px);
#                     box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
#                 }}
#             </style>
            
#             <div style="max-width: 600px; margin: 10px auto; width: 100%;">
#                 <div style="margin: 0px 5px; padding: 0px;">
#                     <div
#                         style="margin: 5px 0px 0px 0px; background: linear-gradient(to bottom right, #40b6c8, #22373e); color: #FFFFFF; padding: 20px; border-radius: 12px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);">

#                         <table role="presentation" width="100%" cellpadding="0" cellspacing="0" align="center" style="text-align:center; padding:20px 0; ">
#                             <tr>
#                                 <td align="center">
#                                 <img src="https://acm-official-website-2025.vercel.app/assets/acm-logo-png-0d25f367.png" alt="ACM Logo" style="height:9em; display:block;">
#                                 </td>
#                             </tr>
#                         </table>

#                         <div style="border-top: 1px solid rgba(255,255,255,0.2); padding:30px 25px; font-size:15px; line-height:1.6; text-align:justify;">
#                             <p>
#                                 <strong style="color: #FFFFFF; font-size:18px">Dear {name}</strong>,
#                                 <br><br>
#                                 We are pleased to inform you that you have been selected as a {position} of Team {team} at ACM-FAST NUCES Karachi for the 2026-2027 term. Your skills, dedication, and enthusiasm stood out during the selection process, and we’re excited to have you on board.
#                                 <br><br>
#                                 As a token of our appreciation, we’ve attached a special image that celebrates your selection. Feel free to share it on LinkedIn or your social platforms to mark this milestone!
#                             </p>
#                             <img src="cid:image1" style="max-width:100%; height:auto;"">
#                         </div>

                        

#                         <div style="border-top: 1px solid rgba(255,255,255,0.2); padding: 25px 0 15px;">
#                             <div style="text-align: center;">
#                                 <p style="margin: 0 0 15px 0; font-size: 15px; letter-spacing: 0.5px; color: FFFFFF;">
#                                     STAY CONNECTED
#                                 </p>
#                                 <div style="margin:10px">
#                                     <a href="https://www.linkedin.com/company/acmnuceskhi" target="_blank" class="social-icon"
#                                         style="display: inline-block; transition: all 0.3s ease;">
#                                         <img src="https://img.icons8.com/color/36/linkedin.png" alt="LinkedIn"
#                                             style="width: 36px; height: 36px;">
#                                     </a>
#                                     <a href="https://www.facebook.com/acmnuceskhi" target="_blank" class="social-icon"
#                                         style="display: inline-block; transition: all 0.3s ease;">
#                                         <img src="https://img.icons8.com/color/36/facebook-new.png" alt="Facebook"
#                                             style="width: 36px; height: 36px;">
#                                     </a>
#                                     <a href="https://www.instagram.com/acmnuceskhi" target="_blank" class="social-icon"
#                                         style="display: inline-block; transition: all 0.3s ease;">
#                                         <img src="https://img.icons8.com/color/36/instagram-new--v1.png" alt="Instagram"
#                                             style="width: 36px; height: 36px;">
#                                     </a>
#                                 </div>
                        
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </body>

#         </html>'''
#     return html

# def get_html_content(name, position, team):


def get_image_content(name, position, team, date, image_path):
    html = f"""
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        body {{
          margin: 0;
          padding: 0;
        }}
        .container {{
          position: relative;
          width: 100%;
        }}
        .container img {{
          display: block;
          width: 100%;
          height: auto;
        }}
        .overlay {{
          position: absolute;
          top: 20%;   /* adjust as per letterhead */
          left: 15%;
          width: 75%;
          font-family: Calibri, sans-serif;
          font-size: 22px;
          color: black;
          line-height: 1.6;
        }}
        .overlay p {{
          margin-bottom: 15px;
        }}
        .overlay b {{
          font-weight: bold;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <img src="file:///{image_path}" alt="Letterhead">
        <div class="overlay">
          <p><strong>{date}</strong></p>
          <p>Dear {name},</p>
          <p>
            <b>Congratulations</b> on your selection to the
            <b>Extended Executive Committee</b> for the 2025-26 term of the
            <b>NUCES KHI ACM Student Chapter!</b> We are excited to welcome you as
            the <b>{position}</b> of <b>Team {team}</b> and look forward to your leadership
            in driving the team’s success.
          </p>
          <p>
            Your role will be pivotal in fulfilling the operational responsibilities expected
            from your team, and we believe your strategic insights and leadership will contribute
            greatly to our goals. With your expertise, we are confident that you will guide your
            team to deliver their best, ensuring that our objectives are met effectively.
          </p>
          <p>
            We are committed to fostering a collaborative and supportive environment, and your
            leadership will play a crucial role in helping us grow as a cohesive unit.
          </p>
          <p>
            Once again, congratulations and welcome to the team! We’re excited to see the
            impact we will make together.
          </p>
          <p>Best Regards,</p>
          
        </div>
      </div>
    </body>
    </html>
    """
    return html


