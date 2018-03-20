"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from forms import ProfileForm
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


'''@app.route('/profile', methods=['POST', 'GET'])
def profile():
    profileForm = ProfileForm()

    # Validate file upload on submit
    if request.method == 'POST':
        # Get file data and save to your uploads folder
        if profileForm.validate_on_submit():
            """first = profileForm.firstname.data
            last = profileForm.lastname.data
            gender = profileForm.gender.data
            email = profileForm.email.data
            location = profileForm.location.data
            bio = profileForm.biography.data"""
            
            pic = request.files['photo']
            filename = secure_filename(pic.filename)
            pic.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            
        flash('File saved', 'success')
        return redirect(url_for('home'))
    return render_template('profile.html', form = profileForm)'''
    
@app.route('/profile', methods=['POST', 'GET'])
def profile():
    profileForm = ProfileForm()

    # Validate file upload on submit
    if request.method == 'POST':
        # Get file data and save to your uploads folder
        if profileForm.validate_on_submit():
            pic = request.files['photo']
            filename = secure_filename(pic.filename)
            pic.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        flash('File Saved', 'success')
        return redirect(url_for('home'))
    return render_template('profile.html', form = profileForm)

@app.route('/profiles')
def profiles():
    """Render the website's about page."""
    return render_template('profiles.html')

@app.route('/profiles/<userId>')
def userProfile():
    """Render the website's about page."""
    return render_template('userProfile.html')
    
###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
