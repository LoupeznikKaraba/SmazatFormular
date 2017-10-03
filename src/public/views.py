"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template,redirect,url_for,flash
from .forms import LogUserForm, secti,masoform,TestForm
from ..data.database import db
from ..data.models import LogUser,Emaily
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

@blueprint.route('/testForm', methods=['GET','POST'])
def Formular():
    form = TestForm()
    if form.validate_on_submit():
        Emaily.create(**form.data)
        flash("Ulozeno",category="INFO")
    return render_template('public/testForm.tmpl', form=form)

@blueprint.route('/testList', methods=['GET'])
def FormularList():
    pole = db.session.query(Emaily).all()
    return render_template('public/testList.tmpl', pole=pole)

@blueprint.route('/smazEmail/<id>', methods=['GET'])
def FormularDel(id):
    iddel = db.session.query(Emaily).filter_by(id=id).first()
    Emaily.delete(iddel)
    return redirect(url_for('public.FormularList'))
