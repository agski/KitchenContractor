from app import app, models, db
from .forms import EditForm, ProjForm, SignUpForm, SearchForm, AssignForm, ReviewForm
from flask import Flask, session, request, flash, url_for, redirect, render_template, abort ,g
from flask_login import login_user , logout_user , current_user , login_required
 

@app.before_request
def before_request():
    g.user = current_user

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = db.session.query(models.User).filter_by(username=username,password=password).first()
    if registered_user is None:
        print('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    print('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/register' , methods=['GET','POST'])
def register():
	form = SignUpForm()
	if request.method == 'GET':
		return render_template('register.html',form=form)
	if form.validate_on_submit():
		utype=""
		for item in form.utype.data:
			utype += item+", "
		utype=utype[:-2]
		user = models.User(user = form.username.data , pw = form.password.data, email = form.email.data, utype = utype)
		db.session.add(user)
		db.session.commit()
		print('User successfully registered')
		return redirect(url_for('login'))
	else:
		print('Please fill out all required fields')
		return render_template('register.html', form=form)

@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
	return render_template('index.html', title='Home', user=user)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/project/<project_name>',methods=['GET','POST'])
@login_required
def project(project_name):
	form = AssignForm()
	user = g.user
	curr_project = models.Project.query.filter_by(proj_name=project_name).first()
	members = curr_project.members.all()
	if form.validate_on_submit():
		if form.done.data:
			curr_project.status = "Completed"
			db.session.commit()
		if form.in_prog.data:
			curr_project.status = "In progress"
			db.session.commit()
		if form.delete.data:
			pending = models.Pending.query.filter_by(proj_name=curr_project.proj_name).all()
			for pend in pending:
				db.session.delete(pend)
			db.session.delete(curr_project)
			db.session.commit()
			return redirect(url_for('user',username=g.user.username))
		if form.rem_demo.data:
			assigned = models.User.query.filter_by(username=curr_project.Demolition).first()
			curr_project.members.remove(assigned)
			curr_project.Demolition = None
			db.session.commit()
		elif form.rem_framing.data:
			assigned = models.User.query.filter_by(username=curr_project.Framing).first()
			curr_project.members.remove(assigned)
			curr_project.Framing = None
			db.session.commit()
		elif form.rem_plumbing.data:
			assigned = models.User.query.filter_by(username=curr_project.Plumbing).first()
			curr_project.members.remove(assigned)
			curr_project.Plumbing = None
			db.session.commit()
		elif form.rem_elec.data:
			assigned = models.User.query.filter_by(username=curr_project.Electrical).first()
			curr_project.members.remove(assigned)
			curr_project.Electrical = None
			db.session.commit()
		elif form.rem_drywall.data:
			assigned = models.User.query.filter_by(username=curr_project.Drywall).first()
			curr_project.members.remove(assigned)
			curr_project.Drywall = None
			db.session.commit()
		elif form.rem_paint.data:
			assigned = models.User.query.filter_by(username=curr_project.Painting).first()
			curr_project.members.remove(assigned)
			curr_project.Painting = None
			db.session.commit()
		elif form.rem_floor.data:
			assigned = models.User.query.filter_by(username=curr_project.Flooring).first()
			curr_project.members.remove(assigned)
			curr_project.Flooring = None
			db.session.commit()
		elif form.rem_cabs.data:
			assigned = models.User.query.filter_by(username=curr_project.Cabinets).first()
			curr_project.members.remove(assigned)
			curr_project.Cabinets = None
			db.session.commit()
		elif form.rem_counters.data:
			assigned = models.User.query.filter_by(username=curr_project.Countertops).first()
			curr_project.members.remove(assigned)
			curr_project.Countertops = None
			db.session.commit()
		elif form.rem_tiles.data:
			assigned = models.User.query.filter_by(username=curr_project.Tiles).first()
			curr_project.members.remove(assigned)
			curr_project.Tiles = None
			db.session.commit()
		elif form.rem_apps.data:
			assigned = models.User.query.filter_by(username=curr_project.Appliances).first()
			curr_project.members.remove(assigned)
			curr_project.Appliances = None
			db.session.commit()
		elif form.rem_windows.data:
			assigned = models.User.query.filter_by(username=curr_project.Appliances).first()
			curr_project.members.remove(assigned)
			curr_project.Windows = None
			db.session.commit()
		cont = None
		cont_type = ""
		if form.demo_name.data != '':
			cont = models.User.query.filter_by(username=form.demo_name.data).first()
			cont_type = 'Demolition'
		elif form.framing_name.data != '':
			cont = models.User.query.filter_by(username=form.framing_name.data).first()
			cont_type = 'Framing'
		elif form.plumbing_name.data != '':
			cont = models.User.query.filter_by(username=form.plumbing_name.data).first()
			cont_type = 'Plumbing'
		elif form.elec_name.data != '':
			cont = models.User.query.filter_by(username=form.elec_name.data).first()
			cont_type = 'Electrical'
		elif form.drywall_name.data != '':
			cont = models.User.query.filter_by(username=form.drywall_name.data).first()
			cont_type = 'Drywall'
		elif form.paint_name.data != '':
			cont = models.User.query.filter_by(username=form.paint_name.data).first()
			cont_type = 'Painting'
		elif form.floor_name.data != '':
			cont = models.User.query.filter_by(username=form.floor_name.data).first()
			cont_type = 'Flooring'
		elif form.cabs_name.data != '':
			cont = models.User.query.filter_by(username=form.cabs_name.data).first()
			cont_type = 'Cabinets'
		elif form.counters_name.data != '':
			cont = models.User.query.filter_by(username=form.counters_name.data).first()
			cont_type = 'Countertops'
		elif form.tiles_name.data != '':
			cont = models.User.query.filter_by(username=form.tiles_name.data).first()
			cont_type = 'Tiles'
		elif form.apps_name.data != '':
			cont = models.User.query.filter_by(username=form.apps_name.data).first()
			cont_type = 'Appliances'
		elif form.windows_name.data != '':
			cont = models.User.query.filter_by(username=form.windows_name.data).first()
			cont_type = 'Windows'
		if cont != None:
			if cont_type in cont.user_type:
				if models.Pending.query.filter(models.Pending.req_type==cont_type, models.Pending.issuer.any(username=user.username), models.Pending.issuee.any(username=cont.username)).first() != None:
					print('request already exists')
				else:
					req = models.Pending(req_type=cont_type,issuer=[user],issuee=[cont],cont_name=cont.username,client_name=user.username,proj_name=project_name)
					print(cont_type)
					print(req.req_type)
					db.session.add(req)
					db.session.commit()
					print('request successfully sent')
			else:
				print('Wrong contractor category')
		else:
			print('User account does not exist')

	demo_cont=curr_project.Demolition
	framing_cont=curr_project.Framing
	plumb_cont=curr_project.Plumbing
	elec_cont=curr_project.Electrical
	drywall_cont=curr_project.Drywall
	paint_cont=curr_project.Painting
	floor_cont=curr_project.Flooring
	cabs_cont=curr_project.Cabinets
	counter_cont=curr_project.Countertops
	tiles_cont=curr_project.Tiles
	apps_cont=curr_project.Appliances
	windows_cont = curr_project.Windows

	demo=curr_project.demo_stps.split(",")[:-1]
	framing=curr_project.framing_stps.split(",")[:-1]
	plumb=curr_project.plumb_stps.split(",")[:-1]
	elec=curr_project.elec_stps.split(",")[:-1]
	drywall=curr_project.drywall_stps.split(",")[:-1]
	paint=curr_project.paint_stps.split(",")[:-1]
	floor=curr_project.floor_stps.split(",")[:-1]
	cabs=curr_project.cab_stps.split(",")[:-1]
	counter=curr_project.counter_stps.split(",")[:-1]
	tiles=curr_project.tiles_stps.split(",")[:-1]
	apps=curr_project.app_stps.split(",")[:-1]
	windows=curr_project.window_stps.split(",")[:-1]
	return render_template('project.html', status = curr_project.status, owner=curr_project.Owner,projName=project_name,demo=demo,framing=framing,plumb=plumb,
		elec=elec, drywall=drywall,paint=paint,floor=floor,cabs=cabs,windows=windows,
		counter=counter,tiles=tiles,apps=apps,demo_cont=demo_cont, windows_cont=windows_cont,framing_cont=framing_cont,
		plumb_cont=plumb_cont,elec_cont=elec_cont,drywall_cont=drywall_cont,paint_cont=paint_cont,floor_cont=floor_cont,
		cabs_cont=cabs_cont,counter_cont=counter_cont,tiles_cont=tiles_cont,apps_cont=apps_cont,form=form)

@app.route('/review/<username>',methods=['GET', 'POST'])
@login_required
def review(username):
	user = models.User.query.filter_by(username=username).first()
	form = ReviewForm()
	if request.method == 'GET':
		return render_template('review.html',user=user,form=form)
	if form.validate_on_submit():
		rev = models.Review(job_type=form.job_type.data,cont_name=username,client_name=g.user.username,
			rev=form.review.data,num_rev=form.num.data,cont=[user])
		db.session.add(rev)
		db.session.commit()
		print('review submitted')
		return redirect(url_for('user',username=g.user.username))
	else:
		print('Fill out all fields')
		return render_template('review.html',user=user,form=form)


@app.route('/findContractors', methods=['GET', 'POST'])
@login_required
def findContractors():
	form = SearchForm()
	if request.method == 'GET':
		return render_template('FindCont.html',form=form)
	if form.validate_on_submit():
		conts=[]
		name = form.by_name.data
		if name != "":
			cont = models.User.query.filter_by(username=name).first()
			if cont == None or cont.user_type == 'Home Owner':
				print('User %s not found.' % name)
				return redirect(url_for('findContractors'))
			conts+= [cont]
		else:
			all_conts = models.User.query.all()
			utype = form.by_type.data
			for cont in all_conts:
				if utype in cont.user_type:
					conts += [cont]
		return render_template('FindCont.html',form=form,conts=conts)
	else:
		return render_template('FindCont.html',form =form)


@app.route('/user/<username>',methods=['GET', 'POST'])
@login_required
def user(username):
	user = models.User.query.filter_by(username=username).first()
	form_edit = EditForm()
	if request.method == 'POST':
		if g.user.user_type != "Home Owner":
			action = request.form['submit'].split(',')
			req = models.Pending.query.filter(models.Pending.proj_name == action[0],models.Pending.issuee.any(username=user.username)).first()
			proj = models.Project.query.filter(models.Project.proj_name == action[0], models.Project.members.any(username=req.client_name)).first()
			if action[1] == 'Accept':
				if proj.status == 'Completed':
					print('project has been marked as Completed')
					req = user.received_req.filter_by(proj_name=action[0]).first()
					db.session.delete(req)
					db.session.commit()
				else:
					proj.members.append(g.user)
					cont_type = req.req_type
					if cont_type == 'Demolition':
						if proj.Demolition != None:
							print("Contractor already assigned for project")
						else:
							proj.Demolition = user.username
					elif cont_type == 'Framing':
						if proj.Framing != None:
							print("Contractor already assigned for project")
						else:
							proj.Framing = user.username
					elif cont_type == 'Plumbing':
						if proj.Plumbing != None:
							print("Contractor already assigned for project")
						else:
							proj.Plumbing = user.username
					elif cont_type == 'Electrical':
						if proj.Electrical != None:
							print("Contractor already assigned for project")
						else:
							proj.Electrical = user.username
					elif cont_type == 'Drywall':
						if proj.Drywall != None:
							print("Contractor already assigned for project")
						else:
							proj.Drywall = user.username
					elif cont_type == 'Painting':
						if proj.Painting != None:
							print("Contractor already assigned for project")
						else:
							proj.Painting = user.username
					elif cont_type == 'Flooring':
						if proj.Flooring != None:
							print("Contractor already assigned for project")
						else:
							proj.Flooring = user.username
					elif cont_type == 'Cabinets':
						if proj.Cabinets != None:
							print("Contractor already assigned for project")
						else:
							proj.Cabinets = user.username
					elif cont_type == 'Countertops':
						if proj.Countertops != None:
							print("Contractor already assigned for project")
						else:
							proj.Countertops = user.username
					elif cont_type == 'Tiles':
						if proj.Tiles != None:
							print("Contractor already assigned for project")
						else:
							proj.Tiles = user.username
					elif cont_type == 'Appliances':
						if proj.Appliances != None:
							print("Contractor already assigned for project")
						else:
							proj.Appliances = user.username
					elif cont_type == 'Windows':
						if proj.Windows != None:
							print("Contractor already assigned for project")
						else:
							proj.Windows = user.username
					db.session.delete(req)
					db.session.commit()
			else:
				req = user.received_req.filter_by(proj_name=action[0]).first()
				db.session.delete(req)
				db.session.commit()
		else:
			action = request.form['cancel'].split(',')
			req = models.Pending.query.filter(models.Pending.proj_name == action[0],models.Pending.issuee.any(username=action[1]),models.Pending.issuer.any(username=action[2]),models.Pending.req_type==action[3]).first()
			db.session.delete(req)
			db.session.commit()
	
	projs = user.projs.all()
	if user == None:
		print('User %s not found.' % username)
		return redirect(url_for('index'))
	proj_descrip_curr = []
	proj_descrip_past = []
	for proj in projs:
		work_type = ''
		if proj.Owner == username:
			work_type += ' Owner,'
		if proj.Demolition == username:
			work_type += ' Demolition,'
		if proj.Framing == username:
			work_type += ' Framing,'
		if proj.Plumbing == username:
			work_type += ' Plumbing,'
		if proj.Electrical == username:
			work_type += ' Electrical,'
		if proj.Drywall == username:
			work_type += ' Drywall,'
		if proj.Painting == username:
			work_type += ' Painting,'
		if proj.Flooring == username:
			work_type += ' Flooring,'
		if proj.Cabinets == username:
			work_type += ' Cabinets,'
		if proj.Countertops == username:
			work_type += ' Countertops,'
		if proj.Tiles == username:
			work_type += ' Tiles,'
		if proj.Appliances == username:
			work_type += ' Appliances,'
		if proj.Windows == username:
			work_type += ' Windows,'

		if proj.status == "In progress":	
			proj_descrip_curr.append({'name':proj.proj_name,'role': work_type[1:-1]})
		else:
			proj_descrip_past.append({'name':proj.proj_name,'role': work_type[1:-1]})

	pending_reqs = []
	pending = []
	reviews = []
	if user.user_type == "Home Owner":
		pending_reqs = user.issued_req.all()
		for pend in pending_reqs:
			pending.append({'user':pend.cont_name, 'proj':pend.proj_name, 'type':pend.req_type})
	else:
		reviews = models.Review.query.filter(models.Review.cont.any(username=user.username))
		pending_reqs = user.received_req.all()
		for pend in pending_reqs:
			pending.append({'user':pend.client_name, 'proj':pend.proj_name, 'type':pend.req_type})

	if user.user_type == "Home Owner":
		return render_template('user.html',user=user,projs_curr=proj_descrip_curr,projs_past=proj_descrip_past,pending=pending_reqs)
	else:
		return render_template('user_cont.html',reviews=reviews,user=user,projs_curr=proj_descrip_curr,projs_past=proj_descrip_past,pending=pending)

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
	form = EditForm()
	if form.validate_on_submit():
		if form.company_name.data !='':
			g.user.company_name= form.company_name.data
		if form.about.data !='':
			g.user.about = form.about.data
		db.session.commit()
		print('Changes have been saved')
		return redirect(url_for('user',username=g.user.username))
	else:
		form.company_name.data = g.user.company_name
		form.about.data = g.user.about
	return render_template('edit.html', form=form)

@app.route('/newProject', methods = ['GET','POST'])
@login_required
def newProject():
	form = ProjForm()
	if request.method == 'GET':
		return render_template('newProject.html', form=form)
	if form.validate_on_submit():
		steps = dict(demo_stps="",framing_stps="",plumb_stps="",elec_stps="",drywall_stps="",paint_stps="",
		floor_stps="",cab_stps="",tiles_stps="",counter_stps = "",app_stps="",window_stps="")
		proj_name = form.proj_name.data

		if form.cabs_rep.data == 'Yes':
			steps['demo_stps'] += "Tear out cabinets,"
			steps['demo_stps']+= "Remove appliances - store those to be reused,"
			steps['cab_stps'] += "Order cabinets,"
			steps['cab_stps'] += "Install new cabinets,"
		elif form.cabs_ref.data == 'Yes':
			steps['cab_stps'] += "Reface cabinets,"
		if form.framing_add.data == 'Yes':
			steps['framing_stps'] += "Add new wall framing,"
			steps['drywall_stps'] += "Hang drywall on new walls,"
			steps['plumb_stps'] += "Add new wall plumbing,"
			steps['elec_stps'] += "Add new wall electrical work,"
			steps['paint_stps'] += "Prime new wall(s),"
			steps['paint_stps'] += "Paint new wall(s),"
		if form.framing_rem.data == 'Yes':
			steps['demo_stps'] += "Remove wall(s) and associated cabinets/fixtures,"
		if form.layout.data == 'Yes':
			steps['elec_stps'] += "Complete electrical work for appliances,"
			steps['plumb_stps'] += "Complete plumbing for appliances,"
		if form.buy_apps.data == "Yes":
			if form.cabs_rep.data == "No":
				steps['demo_stps']+= "Remove appliances - store those to be reused,"
			steps['app_stps'] += "Purchase new appliances,"
		for app in form.new_apps.data:
			steps['app_stps'] += "Install " + str(app) + ","
		if form.electrical_fix.data == "Yes":
			steps['elec_stps'] += "Remove old light fixtures,"
			steps['elec_stps'] += "Install new light fixtures,"
		if form.electrical_sock.data == "Yes":
			steps['elec_stps'] += "Install/alter power sockets,"
		if form.flooring.data == "Yes":
			steps['floor_stps'] += "Purchase new flooring material,"
			steps['floor_stps'] += "Install new floors,"
			steps['demo_stps'] += "Remove old floors,"
		if form.tiles.data == 'Yes':
			steps['tiles_stps']+= "Install tiles,"
		if form.countertops.data == "Yes":
			steps['demo_stps'] += "Remove old countertops,"
			steps['counter_stps'] += "Order new countertops,"
			steps['counter_stps'] += "Install new countertops,"
		if form.windows.data == "Yes":
			steps['window_stps'] += "Order new windows,"
			steps['demo_stps'] += "Remove old windows,"
			steps['window_stps'] += "Install new windows,"
		project = models.Project(Owner=g.user.username,proj_name = form.proj_name.data, demo_stps=steps['demo_stps'], framing_stps=steps['framing_stps'],
			plumb_stps=steps['plumb_stps'],elec_stps=steps['elec_stps'],window_stps=steps['window_stps'],drywall_stps=steps['drywall_stps'],
			paint_stps=steps['paint_stps'],floor_stps=steps['floor_stps'],cab_stps=steps['cab_stps'],counter_stps=steps['counter_stps'],
			tiles_stps=steps['tiles_stps'], app_stps=steps['app_stps'], members = [g.user],status="In progress")
		db.session.add(project)
		db.session.commit() 
		print('Project has been created')
		return redirect(url_for('user', username=g.user.username))
	else:
		print('Please fill out all required fields')
		return render_template('newProject.html', form=form)

		