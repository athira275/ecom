from flask import Flask,render_template,redirect,url_for,request,flash,session
from werkzeug.utils import secure_filename
from dbconnection.datamanipulation import* # type: ignore
import os
app=Flask(__name__)
upload_folder='./static'
app.config['UPLOAD_FOLDER']=upload_folder
app.config['MAX_CONTENT_LENGTH']=16*1024*1024
ALLOWED_EXTENSIONS={'jpg','png','PNG'}
def is_allowed(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS
app.secret_key='supersecretkey'



@app.route("/fileupload")
def fileupload():
    return render_template('upload.html')

@app.route("/uploadAction",methods=["post"])
def uploadAction():
    if request.method=='POST':
        if len(request.files)>0:
            file=request.files['file']
        if file and is_allowed(file.filename):
            filename=secure_filename(file.filename)
            r=sql_edit_insert('insert into file_tb values(NULL,?,?)',(filename,request.form['name']))
        if(r>0):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            flash('inserted sucessfully..')
        else:
            msg='uploading failed'
            return render_template('upload.html',msg=msg)
    return redirect(url_for('fileupload'))

@app.route("/viewimage")
def viewimage():
    image=sql_query('select * from file_tb')
    return render_template('viewimage.html',a=image)


if __name__ == '__main__':
    app.run(debug=True)
