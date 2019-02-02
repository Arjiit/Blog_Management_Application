from flask import Flask, render_template
app = Flask(__name__) #setting app variable to instance of Flask class 

posts = [
	{
		'author': 'arjit yadav',
		'title': 'blog post 1',
		'content': 'first blog post',
		'date_posted': 'Feb 1st 2019'
	},

	{
		'author': 'Jane Doe',
		'title': 'blog post 2',
		'content': 'second blog post',
		'date_posted': 'Feb 2nd 2019'
	},
]

@app.route("/") # / is the home page.
@app.route("/home")
def hello():
    return render_template('home.html', posts = posts) # will

@app.route("/about") 
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
	app.run(debug= True)