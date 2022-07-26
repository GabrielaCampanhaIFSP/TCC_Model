from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/boschmap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    EDV=db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(80),unique=True,nullable=False)
    Email = db.Column(db.String(120),unique=True,nullable=False)
    Phone = db.Column(db.String(20),unique=True,nullable=False)
    Password = db.Column(db.String(80),nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

class ResponsibleSector(db.Model):
    IDResponsibleSector=db.Column(db.Integer,db.ForeignKey('user.EDV'),primary_key=True,nullable=True)
    User= db.relationship('user',backref=db.backref('posts', lazy=True))

class ResponsibleBuilding(db.Model):
    IDResponsibleBuilding=db.Column(db.Integer,db.ForeignKey('user.EDV'),primary_key=True,nullable=True)
    User= db.relationship('user',backref=db.backref('posts', lazy=True))

class Sector(db.Model):
    IDSector = db.Column(db.Integer,primary_key=True,nullable=True)
    Name = db.Column(db.String(80),unique=True,nullable=False)
    Description = db.Column(db.String(120),unique=True,nullable=False)
    FK_Responsible = db.Column(db.Integer,db.ForeignKey('responsible_sector.IDResponsibleSector'),nullable=True)
    ResponsibleSector= db.relationship('responsibleSector',backref=db.backref('posts', lazy=True))

class Building(db.Model):
    IDBuilding = db.Column(db.Integer,primary_key=True,nullable=True)
    Name = db.Column(db.String(80),unique=True,nullable=False)
    Lat = db.Column(db.Integer,nullable=True)
    Long = db.Column(db.Integer,nullable=True)
    Entrance = db.Column(db.String(80),nullable=False)
    Description = db.Column(db.String(120),nullable=False)
    Imagem = db.Column(db.String(120),nullable=False)
    FK_Responsible = db.Column(db.Integer, db.ForeignKey('responsible_building.IDResponsibleBuilding'),
                               nullable=True)
    ResponsibleBuilding = db.relationship('responsibleBuilding', backref=db.backref('posts', lazy=True))

class Floor(db.Model):
    IDFloor = db.Column(db.Integer,primary_key=True,nullable=True)
    Description = db.Column(db.String(120), nullable=False)
    FK_Building = db.Column(db.Integer, db.ForeignKey('building.IDBuilding'),nullable=True)
    building = db.relationship('building', backref=db.backref('posts', lazy=True))