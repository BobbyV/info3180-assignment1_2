from.import db
from random import randint
import views
from marshmallow import Schema, fields

class User (db.Model):
  id = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(80))
  lastname = db.Column(db.String(80))
  age = db.Column(db.Integer)
  sex = db.Column(db.String(20))
  image = db.Column(db.String(180))
  userid = db.Column(db.Interger)
  profile_add_on = db.Column(db.Date())
  high_score = db.Column(db.Integer)
  tdollars = db.Column(db.Numeric)

  def __init__ (self,firstname,lastname,age,sex,image):
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      self.sex = sex
      self.image = image
      self.userid = randit(1000000,999999)
      self.profile_add_on = view.timeinfo()
      
  class Meta:
    fields = ('firstname', 'lastname', 'age', 'sex', 'image', 'userid', 'profile_add_on', 'high_score', 'tdollars')

class ProfileSchema(Schema):
  name = fields.Method("name")

  def __repr__ (self):
      return '<User %r>' % (self.firstname,self.lastname)