from.import db

class User (db.Model):
  id = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(80))
  lastname = db.Column(db.String(80))
  age = db.Column(db.Integer)
  sex = db.Column(db.String(20))
  image = db.Column(db.String(80))

  def __init__ (self,firstname,lastname,age,sex,image):
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      self.sex = sex
      self.image = image

  def __repr__ (self):
      return '<User %r>' % self.firstname