from functools import wraps
from flask import request, Response, Flask, redirect, url_for, render_template
import os
from werkzeug import secure_filename
from glob import glob
#lifted from http://flask.pocoo.org/docs/0.10/patterns/fileuploads/
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "."

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/uploaded_file",methods=["GET","POST"])
def uploaded_file():
    return "success"

@app.route('/get_csv', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = "delete_"+secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file'))
    return render_template("upload.html")

def shutdown_server():
    for File in glob("*"):
        if File.startswith("delete"):
            os.remove(File)
    func = request.environ.get("werkzeug.server.shutdown")
    print func
    if func is None:
        raise RuntimeError("Not running with Werkzeug Server")
    func()

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == '1234'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/success",methods=["GET","POST"])
def success():
    return "success"

@app.route('/secret-page',methods=["GET"])
@requires_auth
def secret_page():
    return "success"

@app.route("/shutdown",methods=["POST"])
def shutdown():
    shutdown_server()
    return "Server shutting down..."

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="POST":
        return redirect(url_for("success"))
    return render_template("form.html")

if __name__ == '__main__':
        app.run(debug=True)
