from flask import Flask, redirect, url_for, session,request
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.client import OAuth
import os
from dotenv import load_dotenv
from config import Config
from flask_migrate import Migrate
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from flask import jsonify


app = Flask(__name__)
app.config.from_object(Config)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
oauth = OAuth(app)
migrate = Migrate(app, db)
mail = Mail(app)


load_dotenv()
google = oauth.remote_app(
    'google',
    consumer_key=os.getenv('GOOGLE_ID'),
    consumer_secret=os.getenv('GOOGLE_SECRET'),
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_method='POST',
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100))
    last_name= db.Column(db.String(100))
    email= db.Column(db.String(100))
    name=db.Column(db.String(100))
    
@app.route('/')
def index():
    if 'google_token' in session:
        me = google.get('userinfo')
        if me.status == 200:
            user_info = me.data
            print(user_info)
            user = User.query.filter_by(google_id=user_info['id']).first()
            if user is None:
                user = User(google_id=user_info['id'], email=user_info['email'])
                db.session.add(user)
                db.session.commit()
            return f'Hello, {user_info["email"]}'
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('google_token')
    return redirect(url_for('index'))

@app.route('/login/callback')
def authorized():
    response = google.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args.get('error_reason'),
            request.args.get('error_description')
        )
    
    session['google_token'] = (response['access_token'], '')
    print('Token received:', session['google_token'])
        # Print session data for debugging
    print('Session contents:', session)
    return redirect("http://localhost:8501/")


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return 'File uploaded successfully'

@app.route('/contact', methods=['POST'])
def contact():
    # Ensure the request contains the file
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    name = request.form.get('name')
    subject = request.form.get('subject')
    email = request.form.get('email')
    message = request.form.get('message')

    # Check if all required fields are present
    if not all([name, email, message, subject]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        # Create the email message
        msg = Message(
            subject=subject,
            sender=app.config['MAIL_USERNAME'],
            recipients=['srvroysisodiyaa@gmail.com'],
            body=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        )

        # Add the file attachment if it exists
        if file and file.filename:
            msg.attach(file.filename, file.content_type, file.read())

        # Send the email
        mail.send(msg)
        return jsonify({'success': 'Email sent successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    
    app.run(debug=True)
