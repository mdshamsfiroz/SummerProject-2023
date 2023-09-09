#! /usr/bin/python3

print("content-type: text/html")
print()


import cgi
import subprocess as sp
db = cgi.FieldStorage()
choice = db.getvalue("choice")
image = db.getvalue("image")
tag = db.getvalue("tag")
container = db.getvalue("container")
port = db.getvalue("port")
state = db.getvalue("state")
output="" 
if choice =="1" :
   grap = sp.getstatusoutput("sudo docker")
   if grap[0]==0:
     output="docker already installed"
   
   elif grap[0]==1:
     output1=sp.getoutput("sudo yum install docker-ce --nobest -y")
     output2=sp.getoutput("sudo systemctl start docker")
     output = "{} \n\n {}".format(output1,output2)
   else:
     output = "Something Went Wrong"
elif choice == "2":
  output = sp.getoutput("sudo systemctl {} docker".format(state))
  output  = output + "\n\n Docker Service {}d".format(state)
elif choice == "3":
   output = sp.getoutput("sudo systemctl status docker")
elif choice == "4":
   output= sp.getoutput("sudo  docker image ls")
elif choice == "5":
   output = sp.getoutput("sudo docker ps -a")
elif choice == "6":
   output = sp.getoutput("sudo docker ps")
elif choice == "7":
   output = sp.getoutput("sudo docker pull {}:{}".format(image,tag))
elif choice == "8":
   output = sp.getoutput("sudo docker run -dit -p {} --name {} {}:{}".format(port, container,image,tag))
elif choice == "9":
   c_id = sp.getoutput("sudo docker ps -qf 'name={}'".format(container))
   output = sp.getoutput("sudo docker commit {} {}:{}".format(c_id ,image,tag))
   
elif choice == "10":
   output = sp.getoutput("sudo docker {} {}".format(state,container))
elif choice == "11":
   output = sp.getoutput("sudo docker rmi {}:{}".format(image,tag))
elif choice == "12":
   output = sp.getoutput("sudo docker rm {}".format(container))
elif choice == "13":
   output = sp.getoutput("sudo systemctl {} docker".format(state))
   output = "Docker Service {}".format(state)
else:
   output = "Something went Wrong..."
print("""<style>
   body{
       background-color:rgb(0,0,0,0.8);
      text-align:center;
       justify-content:center;
     }
      pre{
        font-size: 20px;
        color:white;
      font-weight: bold;
      padding -top:0px
}
h1{
color : blue;
padding-bottom:0px;
}
</style>""")
print("""
<body>
<pre>
<h1 style = "">Output</h1>

{}
</pre>
</body>
""".format(output))
       
