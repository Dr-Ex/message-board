from flask import g
from flask import render_template
from flask import request
from flask import redirect
import flask_login
from public import website
from public import usermanager
from public import datamanager
from datetime import datetime


# home/index page
@website.route('/')
def index():

	query_string = (
		'SELECT message_id, content, username, time_created '
		'FROM messages INNER JOIN users '
		'USING (user_id) '
		'ORDER BY time_created DESC '
		'LIMIT 100'
	)
	query_results = datamanager.query_db(query_string, [], one=False)

	if request.method == 'POST':
		if request.form['submit'] == 'delete_message':
			query_string = (
				'DELETE FROM messages '
				'WHERE message_id = ?'
			)

			query_result = datamanager.query_db(
				query_string,
				[message_id],
				one=True
			)

	return render_template('index.html', messages=query_results)

# new message page
@website.route('/new-message', methods=['GET', 'POST'])
@usermanager.login_required
def new_message():

	if request.method == 'GET':
		return render_template('new-message.html')

	elif request.method == 'POST':

		content = request.form.get('message')
		current_time = datetime.now()
		user_id = flask_login.current_user.user_id

		query_string = (
			'INSERT INTO messages( content, time_created, user_id ) '
			'VALUES (?,?,?)'
		)

		query_result = datamanager.query_db(
			query_string,
			[content, current_time, user_id],
			one=True
		)

		if query_result == None:
			print('error')
		else:
			print('success')

		return redirect('/')

# sign in page
@website.route('/sign-in', methods=['GET', 'POST'])
def sign_in():

	if request.method == 'GET':
		return render_template('sign-in.html')

	if request.method == 'POST':
		
		username = request.form.get('username')
		password = request.form.get('password')

		user = usermanager.sign_in_user(username, password)

		if user.is_authenticated:
			return redirect('/')
		else:
			return render_template('sign-in.html')	


#sign out page
@website.route('/sign-out')
def sign_out():
	usermanager.sign_out_user()
	return render_template('sign-out.html')

#edit message page
@website.route('/edit-message/<message_id>', methods=['GET', 'POST'])
@usermanager.login_required
def edit_message(message_id = None):

	if request.method == 'GET':

		query_string = (
			'SELECT message_id, content, user_id '
			'FROM messages '
			'WHERE message_id = ?'
		)

		query_result = datamanager.query_db(
			query_string,
			[message_id],
			one=True
		)
		
		return render_template('edit-message.html', message=query_result)

	elif request.method == 'POST':

		message_content = request.form.get('message')
		message_id = request.form.get('message_id')

		query_string = (
			'UPDATE messages '
			'SET content = ? '
			'WHERE message_id = ?'
		)

		query_result = datamanager.query_db(
			query_string,
			[message_content, message_id],
			one=True
		)
		
		return redirect('/')

@website.route('/delete-message/<message_id>', methods=['GET', 'POST'])
@usermanager.login_required
def delete_message(message_id = None):

	if request.method == 'GET':
		query_string = (
			'SELECT message_id, content, user_id '
			'FROM messages '
			'WHERE message_id = ?'
		)

		query_result = datamanager.query_db(
			query_string,
			[message_id],
			one=True
		)

		return render_template('delete-message.html', message=query_result)

	if request.method == 'POST':
		message_id = request.form.get('message_id')

		query_string = (
			'DELETE FROM messages '
			'WHERE message_id = ?'
		)

		query_result = datamanager.query_db(
			query_string,
			[message_id],
			one=True
		)

		return redirect('/')

@website.route('/new-user', methods=['GET', 'POST'])
def new_user():
	if request.method == 'GET':
		return render_template('/new-user.html')

	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		first_name = request.form.get('first_name')
		last_name = request.form.get('last_name')
		email = request.form.get('email')

		query_string = (
			'INSERT INTO users (username, password, first_name, last_name, email) '
			'VALUES (?,?,?,?,?)'
		)

		query_result = datamanager.query_db(
			query_string,
			[username, password, first_name, last_name, email],
			one=True
		)

		return redirect('/sign-in')

@website.route('/edit-user', methods=['GET', 'POST'])
@usermanager.login_required
def edit_user():
	if request.method == 'GET':
		user_id = flask_login.current_user.user_id
		
		query_string = (
			'SELECT username, password, first_name, last_name, email '
			'FROM users '
			'WHERE user_id=?'
		)

		query_result = datamanager.query_db(
			query_string,
			[user_id],
			one=True
		)

		return render_template('/edit-user.html', user_data=query_result)

	if request.method == 'POST':
		user_id = flask_login.current_user.user_id
		username = request.form.get('username')
		password = request.form.get('password')
		first_name = request.form.get('first_name')
		last_name = request.form.get('last_name')
		email = request.form.get('email')

		query_string = (
			'UPDATE users '
			'SET username = ?, password = ?, first_name = ?, last_name = ?, email = ? '
			'WHERE user_id = ?'
		)

		query_result = datamanager.query_db(
			query_string,
			[username, password, first_name, last_name, email, user_id],
			one=True
		)

		return redirect('/')