from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
    picture = FileField ('Photo', validators = [FileRequired(), FileAllowed(['jpg','png'])])