from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app import db, login_manager
from flask_login import LoginManager

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

mem_table = Table('mems', db.Model.metadata,
	Column('users_id', Integer, ForeignKey('users.id')),
	Column('projects_id', Integer, ForeignKey('projects.id')))

req1_table = Table('reqs1', db.Model.metadata,
	Column('issuer_id', Integer, ForeignKey('users.id')),
	Column('pending_id', Integer, ForeignKey('pending.id')))

req2_table = Table('reqs2', db.Model.metadata,
	Column('issuee_id', Integer, ForeignKey('users.id')),
	Column('pending_id', Integer, ForeignKey('pending.id')))

rev_table = Table('revs', db.Model.metadata,
	Column('review_id', Integer, ForeignKey('reviews.id')),
	Column('cont_id', Integer, ForeignKey('users.id')))

class Review(db.Model):
	__tablename__ = 'reviews'
	id = db.Column(db.Integer, primary_key=True)
	rev = db.Column(db.String(300))
	num_rev = db.Column(db.Integer)
	job_type = db.Column(db.String(300))
	cont_name = db.Column(db.String(300))
	client_name = db.Column(db.String(300))
	proj_name = db.Column(db.String(300))
	cont = relationship("User", secondary=rev_table, back_populates="reviews",lazy='dynamic')

class Pending(db.Model):
	__tablename__ = 'pending'
	id = db.Column(db.Integer, primary_key=True)
	req_type = db.Column(db.String(300))
	cont_name = db.Column(db.String(300))
	client_name = db.Column(db.String(300))
	proj_name = db.Column(db.String(300))
	issuer = relationship("User", secondary=req1_table, back_populates="issued_req",lazy='dynamic')
	issuee = relationship("User", secondary=req2_table, back_populates="received_req",lazy='dynamic')

	def __init__(self, req_type,issuer,issuee,cont_name,client_name,proj_name):
		self.req_type = req_type
		self.issuer=issuer
		self.issuee=issuee
		self.cont_name = cont_name
		self.client_name = client_name
		self.proj_name = proj_name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	company_name = db.Column(db.String(64))
	email = db.Column(db.String(120), index=True, unique=True)
	user_type = db.Column(db.String(120))
	password = db.Column(db.String(120))
	projs = relationship("Project", secondary=mem_table, back_populates="members", lazy='dynamic')
	about = db.Column(db.String(150))
	rating = db.Column(db.Integer)
	issued_req = relationship("Pending", secondary=req1_table, back_populates="issuer",lazy='dynamic')
	received_req = relationship("Pending", secondary=req2_table, back_populates="issuee",lazy='dynamic')
	reviews = relationship('Review', secondary=rev_table,back_populates='cont',lazy='dynamic')

	def __repr__(self):
		return '<User %r>' % (self.username)

	def __init__(self, user, pw, email, utype):
		self.username = user
		self.password = pw
		self.email = email
		self.user_type = utype

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

class Project(db.Model):
	__tablename__ = 'projects'
	id = db.Column(db.Integer, primary_key = True)
	proj_name = db.Column(db.String(140),unique=True)

	demo_stps = db.Column(db.String(300))
	framing_stps = db.Column(db.String(300))
	plumb_stps = db.Column(db.String(300))
	elec_stps = db.Column(db.String(300))
	window_stps = db.Column(db.String(300))
	drywall_stps = db.Column(db.String(300))
	paint_stps = db.Column(db.String(300))
	floor_stps = db.Column(db.String(300))
	cab_stps = db.Column(db.String(300))
	counter_stps = db.Column(db.String(300))
	tiles_stps = db.Column(db.String(300))
	app_stps = db.Column(db.String(300))
	status = db.Column(db.String(300))

	Owner = db.Column(db.String(300))
	Demolition = db.Column(db.String(300))
	Framing = db.Column(db.String(300))
	Plumbing = db.Column(db.String(300))
	Electrical = db.Column(db.String(300))
	Windows = db.Column(db.String(300))
	Drywall = db.Column(db.String(300))
	Painting = db.Column(db.String(300))
	Flooring = db.Column(db.String(300))
	Cabinets = db.Column(db.String(300))
	Countertops = db.Column(db.String(300))
	Tiles = db.Column(db.String(300))
	Appliances = db.Column(db.String(300))
	Windows = db.Column(db.String(300))

	members = relationship("User", secondary = mem_table, back_populates = "projs",lazy='dynamic')
