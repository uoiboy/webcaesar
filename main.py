



from flask import Flask, request


app= Flask(__name__)
app.config['DEBUG'] =True


from caesar import rotate_string


form ="""





<!DOCTYPE html> 



<html>
    <head>
        <style>
            form 
                {{
               background-color: #eee;
               padding : 20px;
               margin: 0 auto;
               width: 540px;
               font: 16px sans-serif;
               border-radius: 10px;
            }}


             textarea {{
                  background-color: #eee
                  margin: 10px 0;
                  width: 540px;
                  height: 120px;
             }}
        </style>
    </head>

    <body>
        <form method ="POST">
        <label for="Rotate-by">Rotate by:</label>
       <p> <input  id= "Rotate-by" type ="text" name= "rot" value="0"/></p>               
        
        <textarea  name ="text">{0}</textarea>  
        <p><input type="submit"/></p>    
        </form>


    </body>


    """                    
        
@app.route("/") 
def index():
    return form.format("")


@app.route("/", methods =['post'])
def encrypt ():
    rot = int(request.form['rot'])              
    text = request.form['text']   
    new_string = rotate_string(text, rot)

    return form.format(new_string)
    
app.run()