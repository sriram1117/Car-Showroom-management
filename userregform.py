#!C:/Users/JJ/AppData/Local/Programs/Python/Python310/Python.exe

print("content-type:text/html \r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LOGIN FORM</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-image: url(./images/betta-fish-isolated-on-blank-background-with-copy-space-free-photo.jpg);
            background-size: cover;
        }

        .container {
            top: 50%;
            left: 50%;
            position: absolute;
            transform: translate(-50%, -50%);
        }

        .card {
            padding: 60px 40px 50px 40px;
            background-color: black;
            border-radius: 10px;
        }

        #name {
            border-radius: 20px;
            width: 200px;
            border: none;
            background: transparent;
            border-bottom: 1px solid white;
            padding: 6px;
            margin-bottom: 20px;
            color: aliceblue;
        }

        #button {
            margin-top: 30px;
            border: 20px;
            padding: 10px 20px;
            background-color: blue;
            color: white;
            margin-left: 50px;
            border-radius: 30px;
        }

        #button:hover {
            background-color: greenyellow;
            color: black;
            cursor: pointer;
        }

        a {
            font-size: 15px;

        }

        .user {
            border-radius: 50%;
            position: absolute;
            margin-left: 100px;
            margin-top: -40px;
        }
    </style>
</head>

<body>
    <div class="modal-body">
        <form action="" name="login_form" method="post" >
            <div class="container">
                <img class="user" src="./image/WhatsApp Image 2023-12-07 at 11.22.08 AM.jpeg" alt="" height="70px"
                    width="70px">
                <div class="card">
                    <input type="text" placeholder="name" name="name" id="name"><br>
                    <input type="email" placeholder="Email" name="email" id="name"><br>
                    <input type="text" placeholder="Username" name="uname" id="name"><br>
                    <input type="password" placeholder="Password" name="pass" id="name"><br>
                    <input type="int" placeholder="Phone" name="phone" id="name"><br>
                    <input type="submit" value="Submit" name="submit" id="button">

                </div>
            </div>
        </form>
    </div>
    <div>
        <img style="width: 100%;height: 654px;" src="./image/peakpx.jpg" alt="">
    </div>
</body>

</html>
      """)

import pymysql
import cgi,cgitb
import smtplib

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="empdb")
cur=conn.cursor()

form=cgi.FieldStorage()
pname=form.getvalue("name")
pmail=form.getvalue("email")
puname=form.getvalue("uname")
ppwd=form.getvalue("pass")
pphone=form.getvalue("phone")
psubmit=form.getvalue("submit")

if psubmit!= None:
    q="""insert into user_data(name,email,uname,pass,phone) values('%s','%s','%s','%s','%s')""" %(pname,pmail,puname,ppwd,pphone)
    cur.execute(q)
    conn.commit()
    print("""
                <script>
                alert("Data inserted successfully")
                </script>
                """)
    conn.close()
    fromaddr = "sidsriram1100@gmail.com"
    password = "arvs xbil drei dhzx"
    toaddr = pmail
    subject = "Your Valid Password"
    body = """ Username: '%s' \nPassword: '%s' """ % (puname, ppwd)
    msg = """Subject:{}\n\n{}""".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(toaddr, password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()

conn.close()

