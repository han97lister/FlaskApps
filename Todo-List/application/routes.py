from flask import render_template, redirect, url_for, request

from application import app, db
from application.models import Todo
from application.forms import TodoForm, OrderForm


@app.route('/', methods=['GET', 'POST'])
def index() :
    form = OrderForm()
    totals = {
        "total": Todo.query.count(),
        "total_completed": Todo.query.filter_by(complete=True).count()
    }
    if form.order.data == "id" :
        todos = Todo.query.order_by( Todo.id.desc()).all()
    elif form.order.data == "complete" :
        todos = Todo.query.order_by( Todo.complete.desc()).all()
    elif form.order.data == "incomplete" :
        todos= Todo.query.order_by( Todo.complete ).all()
    else :
        todos = Todo.query.all()
    return render_template( 'index.html', title="Todo List App", todos=todos, form=form, totals=totals)


@app.route('/add', methods = ['GET', 'POST'] )
def add() :
    form = TodoForm()
    if form.validate_on_submit() :
        todo = Todo( task = form.task.data, complete = False
        )
        db.session.add(todo)
        print("HI I'm working")
        db.session.commit()
        return redirect(url_for('index'))
    return render_template( 'add.html',title="Add a new Todo", form=form )

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

@app.route( '/update/<int:todo_id>', methods=['GET', 'POST'] )
def update( todo_id ) :
    form = TodoForm()
    todo_update = Todo.query.get(todo_id)
    if form.validate_on_submit():
        todo_update.task = form.task.data
        db.session.commit()
        return redirect( url_for( 'index' ))
    elif request.method == 'GET' :
        form.task.data == todo_update.task

    return render_template('update.html', title="Update your todo", form=form )

@app.route( '/delete/<int:todo_id>' )
def delete(todo_id) :
    todo_to_delete = Todo.query.get(todo_id)
    db.session.delete( todo_to_delete )
    db.session.commit()
    return redirect( url_for( 'index' )) 

