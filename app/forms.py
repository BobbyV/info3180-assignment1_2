from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.fields import SelectField
from wtforms.fields import FileField
# other fields include PasswordField
from wtforms.validators import Required

class ProfileForm(Form):
    firstname = TextField('Firstname',validators =[Required()])
    lastname = TextField ('Lastname',validators =[Required()])
    age = TextField('Age',validators =[Required()])
    sex = SelectField('Sex',choices =[('M','Male'),    ('F','Female')],validators =[Required()])
    image = FileField('Image')