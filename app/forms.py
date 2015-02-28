from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.fields import SelectField
from wtforms.fields import FileField
from wtforms.fields import IntegerField
from wtforms.fields import SubmitField
# other fields include PasswordField
from wtforms.validators import Required

class ProfileForm(Form):
    firstname = TextField('Firstname',validators =[Required("Enter first name")])
    lastname = TextField ('Lastname',validators =[Required("Enter last name")])
    age = IntegerField('Age',validators =[Required("Enter age")])
    sex = SelectField('Sex',choices =[('M','Male'),    ('F','Female')],validators =[Required("Select gender")])
    image = FileField('Image File')
    submit = SubmitField("Submit")