from flask import Flask, request, render_template
app =Flask(_name_)
@app.route('/register',methods=['GET','POST'])
def register():
 if request.method =='POST':
  name =request.form['name']
  email =request.form['email']
  password =request.form['password']