from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, RadioField, SelectMultipleField, widgets, TextField,SubmitField
from wtforms.validators import DataRequired, Length, Optional
class EditForm(Form):
	company_name = StringField('username', validators = [Optional()])
	about = TextAreaField('about', validators = [Length(min=0, max=140)])

class MultiCheckboxField(SelectMultipleField):
	widget = widgets.ListWidget(prefix_label=True)
	option_widget = widgets.CheckboxInput()

class ProjForm(Form):
	app_choices = [("Oven","Oven"),("Refrigerator", "Refrigerator"), ("Freezer","Freezer"),
		("Dishwasher","Dishwasher"),("Garbage disposer","Garbage Disposer"), ("Trash Compactor","Trash Compactor"),
		("Range","Range"), ("Wall Oven","Wall Oven"), ("Range Hood/Vent", "Range Hood/Vent"), ("Cooktop","Cooktop"),
		("Microwave","Microwave"), ("Warming Drawer", "Warming Drawer")]
	proj_name = StringField('project name', validators = [DataRequired()])
	cabs_rep = RadioField('cabs', validators = [Optional()], choices=[("Yes","Yes"), ("No","No")])
	cabs_ref = RadioField('cabs', validators = [Optional()], choices=[("Yes","Yes"), ("No","No")])
	framing_add = RadioField('walls_add', validators = [Optional()], choices=[("Yes","Yes"), ("No","No")])
	framing_rem = RadioField('walls_rem', validators = [Optional()], choices=[("Yes","Yes"), ("No","No")])
	layout = RadioField('layout', validators = [DataRequired()],choices=[("Yes","Yes"), ("No","No")])
	buy_apps = RadioField('buy_apps', validators = [DataRequired()],choices=[("Yes","Yes"), ("No","No")])
	new_apps = MultiCheckboxField('new_apps', choices=app_choices, validators = [Optional()] )
	electrical_fix = RadioField('fix', validators = [Optional()], choices=[("Yes","Yes"), ("No","No")])
	electrical_sock = RadioField('sock', validators = [Optional()], choices=[("Yes","Yes"), ("No","No")])
	tiles = RadioField('tiles', validators = [Optional()], choices=[("Yes","Yes"), ("No","No")])
	flooring = RadioField('floors', validators = [Optional()], choices=[("Yes","Yes"), ("No","No")])
	countertops = RadioField('counters', validators = [Optional()], choices=[("Yes","Yes"), ("No","No")])
	windows = RadioField('windows', validators = [Optional()], choices=[("Yes","Yes"), ("No","No")])

class SignUpForm(Form):
	type_choices = [("Design","Design"),("Home Owner","Home Owner"),("Framing","Framing"),("Demolition","Demolition"),("Plumbing","Plumbing"),("Electrical","Electrical"),
	("Drywall","Drywall"),("Painting","Painting"),("Flooring","Flooring"),("Cabinets","Cabinets"),
	("Countertops","Countertops"),("Tiles","Tiles"),("Appliances","Appliances"),("Windows","Windows")]
	username = StringField('user/company name', validators = [DataRequired()])
	password = StringField('password', validators = [DataRequired()])
	email = StringField('email', validators = [DataRequired()])
	utype = MultiCheckboxField('utype', choices=type_choices, validators = [DataRequired()])

class SearchForm(Form):
	type_choices = [("Design","Design"),("Framing","Framing"),("Demolition","Demolition"),("Plumbing","Plumbing"),("Electrical","Electrical"),
	("Drywall","Drywall"),("Painting","Painting"),("Flooring","Flooring"),("Cabinets","Cabinets"),
	("Countertops","Countertops"),("Tiles","Tiles"),("Appliances","Appliances"),("Windows","Windows")]
	by_name = TextField('name', validators=[Optional()])
	by_type = RadioField('type', validators = [Optional()],choices=type_choices)

class AssignForm(Form):
	demo_name = TextField('Demolition', validators=[Optional()])
	framing_name = TextField('Framing', validators=[Optional()])
	plumbing_name = TextField('Plumbing', validators=[Optional()])
	elec_name = TextField('Electrical', validators=[Optional()])
	drywall_name = TextField('Drywall', validators=[Optional()])
	paint_name = TextField('Painting', validators=[Optional()])
	floor_name = TextField('Flooring', validators=[Optional()])
	cabs_name = TextField('Cabinets', validators=[Optional()])
	counters_name = TextField('Countertops', validators=[Optional()])
	tiles_name = TextField('Tiles', validators=[Optional()])
	apps_name = TextField('Appliances', validators=[Optional()])
	windows_name = TextField('Windows', validators=[Optional()])
	rem_demo = SubmitField('Remove')
	rem_framing = SubmitField('Remove')
	rem_plumbing = SubmitField('Remove')
	rem_elec = SubmitField('Remove')
	rem_drywall = SubmitField('Remove')
	rem_paint = SubmitField('Remove')
	rem_floor = SubmitField('Remove')
	rem_cabs = SubmitField('Remove')
	rem_counters = SubmitField('Remove')
	rem_tiles = SubmitField('Remove')
	rem_apps = SubmitField('Remove')
	rem_windows = SubmitField('Remove')
	done = SubmitField('Done')
	in_prog = SubmitField('In progress')
	delete = SubmitField('Delete')

class ReviewForm(Form):
	type_choices = [("Framing","Framing"),("Demolition","Demolition"),("Plumbing","Plumbing"),("Electrical","Electrical"),
	("Drywall","Drywall"),("Painting","Painting"),("Flooring","Flooring"),("Cabinets","Cabinets"),
	("Countertops","Countertops"),("Tiles","Tiles"),("Appliances","Appliances")]
	num_choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
	num = RadioField('num', validators = [Optional()], choices=num_choices)
	job_type = RadioField('job_type', validators = [Optional()], choices=type_choices)
	review = TextField('review', validators=[Optional()])
	submit = SubmitField('Submit')
