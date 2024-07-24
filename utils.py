import requests
async def send_mail(to_email: list[str], user_obj: dict, mail_subject: str, content: str):
    url = "http://54.84.189.207/send_mail"
    payload = {
        "receiver_emails": to_email,
        "Subject": mail_subject,
        "body": content
    }    

    #api
    response = requests.post(url, json=payload)
    response.raise_for_status()


async def post_linkdin_imges(title: str, text_content: str):
    url = "http://54.84.189.207/post_linkedin"
    img_url = ""
    payload = {
        "title": title,
        "image_url": img_url,
        "text_content": text_content
    }

    #api request
    response = requests.post(url, json=payload)
    response.raise_for_status()