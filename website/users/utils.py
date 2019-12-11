import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from website import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(10)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static\profile_pictures', picture_fn)

    # resizing the picture uploaded
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@pythontrack.com', recipients=[user.email])
    msg.body = f'''To reset your password, click the link below:
{url_for('users.reset_password', token=token, _external=True)}

If you did not make this request, ignore this message. 
    '''
    mail.send(msg)