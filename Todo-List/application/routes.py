from flask import render_template, redirect, url_for

from application import app, db
from application.models import Todo


@app.route('/')
def index() :
    to_do_list = Todo.query.all()
    return render_template( 'index.html', list = to_do_list)

@app.route('/add')
def add() :
    new_task = Todo( task = "New Task" )
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route( '/complete/<int:todo_id>' )
def complete( todo_id ) :
    todo_to_update = Todo.query.get( todo_id )
    todo_to_update.complete = True
    db.session.commit()
    return redirect( url_for( 'index' )

@app.route( '/incomplete/<int:todo_id>' )
def incomplete( todo_id ) :
    todo_to_update = Todo.query.get( todo_id )
    todo_to_update.complete = False
    db.session.commit()
    return redirect( url_for('index')

@app.route( '/update/<task>' )
def update( task ) :
    todo_update = Todo.query.first()
    todo_update.task = task
    return redirect( url_for( 'index' ))

@app.route( '/delete/<int>:todo_id' )
def delete() :
    todo_to_delete = Todo.query.get( todo_id )
    db.session.delete( todo_to_delete )
    db.session.commit()
    return redirect( url_for( 'index' )) 

