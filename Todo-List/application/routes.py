from flask import render_template, redirect, url_for, request

from application import app, db
from application.models import Todo
from application.forms import TodoForm


@app.route('/')
def index() :
    all_todos = Todo.query.all()
    return render_template( 'index.html', all_todos = all_todos )

@app.route('/add', methods = ['GET', 'POST'] )
def add() :
    form = TodoForm()
    if form.validate_on_submit() :
        new_todo = Todo( task = request.form.get( "name") )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template( 'add.html', form=form )

@app.route( '/complete/<int:todo_id>' )
def complete( todo_id ) :
    todo_to_update = Todo.query.get( todo_id )
    todo_to_update.complete = True
    db.session.commit()
    return redirect( url_for( 'index' ))


@app.route( '/incomplete/<int:todo_id>' )
def incomplete( todo_id ) :
    todo_to_update = Todo.query.get( todo_id )
    todo_to_update.complete = False
    db.session.commit()
    return redirect( url_for( 'index' ))

@app.route( '/update/<task>' )
def update( task ) :
    todo_update = Todo.query.first()
    todo_update.task = task
    return redirect( url_for( 'index' ))

@app.route( '/delete/<int>:todo_id' )
def delete() :
    todo_to_delete = Todo.query.first( )
    db.session.delete( todo_to_delete )
    db.session.commit()
    return redirect( url_for( 'index' )) 

