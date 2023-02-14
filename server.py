from flask import Flask,render_template,request,redirect
import csv
#render_template allows us to send a html file path as a templates rather than string
app=Flask(__name__) #instantiating an app of the flask class
#print(__name__) #prints main as the name is the main file


#<name> represents a paramater so is a placeholder for whatever name we will pass
#post id represents an integer we enter after the name
@app.route('/') #anytime we hit / define a function called hello_world and return hello_worldC:\path
def my_home(): # is the username we passed  but if nothing passed its None
    #flask converts string to html
    return render_template('index.html') #passing the username to html
#any path used in the render templates method must be a file in the templates folder
#static folder is needed for js and css files

@app.route('/<string:page_name>')
def html_page(page_name): #for all the other routes we have apart from home route
    return render_template(page_name)



#the webpage prints out hellow_world or hello_whatver
#enviroment variables Flask_App and FLask_env are set ,flask_env set to development so its in debug mode
#debug mode can save and change info in real time wihtout exiting server

'''
#create another route for another directory like /blog
@app.route('/blog')#different rooute
def blog(): #http://127.0.0.1:5000/blog route will now appear
    return 'These are my thoughts on blogs'

#another route for /blog/2020/dogs
@app.route('/blog/2020/dogs')#different rooute
def blog_dog(): #http://127.0.0.1:5000/blog/2020/dogs route will now appear
    return 'mein dog'
'''
def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2: #mode append
        email=data['email'] #is in dit format
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
def write_to_file(data):
    with open('database.txt',mode='a') as database: #mode append
        email=data['email'] #is in dit format
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict() #converts form output into dict
            write_to_csv(data)
            return redirect('duplicate.html')
        except:
            return 'did not save to database'
    else:
        return 'something in the way went wrong' #if tis not a post method
