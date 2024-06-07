#!C:/Users/JJ/AppData/Local/Programs/Python/Python310/Python.exe
import smtplib

print("content-type:text/html \r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BYERISCHE MOTOREN WERKE AG</title>

    <link rel="website icon" type="png" href="./caro/600px-BMW.svg.png">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

    <style>
        .im {
            height: 60px;
            width: 60px;
            padding-left: 8px;
            float: left;
            margin-top: -15px;
        }

        h1 {
            text-align: center;
        }

        .form-container {
            /* background-color: #f4f4f4; */
            padding: 20px;
            /* border-radius: 1px; */
        }


        .bubbles {
            position: relative;
            top: 0;
            left: 0;
            width: 70%;
            height: 100%;
        }

        .bubbles li {
            position: absolute;
            list-style: none;
            display: flex;
            width: 20px;
            height: 20px;
            background: rgb(221, 211, 245);
            animation: animate 25s linear infinite;
            bottom: -800px;
        }

        .bubbles li:nth-child(1) {
            left: 25%;
            width: 80px;
            height: 80px;
            animation-delay: 0;
        }

        .bubbles li:nth-child(2) {
            left: 10%;
            width: 20px;
            height: 20px;
            animation-delay: 2s;
            animation-duration: 12s;
        }


        .bubbles li:nth-child(3) {
            left: 70%;
            width: 20px;
            height: 20px;
            animation-delay: 4s;
        }

        .bubbles li:nth-child(4) {
            left: 40%;
            width: 60px;
            height: 60px;
            animation-delay: 0s;
            animation-duration: 18s;
        }

        .bubbles li:nth-child(5) {
            left: 65%;
            width: 20px;
            height: 20px;
            animation-delay: 0s;
        }

        .bubbles li:nth-child(6) {
            left: 75%;
            width: 110px;
            height: 110px;
            animation-delay: 3s;
        }

        .bubbles li:nth-child(7) {
            left: 35%;
            width: 150px;
            height: 150px;
            animation-delay: 7s;
        }

        .bubbles li:nth-child(8) {
            left: 50%;
            width: 25px;
            height: 25px;
            animation-delay: 15s;
            animation-duration: 45s;
        }


        .bubbles li:nth-child(9) {
            left: 20%;
            width: 15px;
            height: 15px;
            animation-delay: 2s;
            animation-duration: 35s;
        }


        .bubbles li:nth-child(10) {
            left: 85%;
            width: 150px;
            height: 150px;
            animation-delay: 0s;
            animation-duration: 12s;
        }


        @keyframes animate {
            0% {
                transform: translateY(0) rotate(0deg);
                opacity: 1;
                border-radius: 0;
            }

            100% {
                transform: translateY(-1000px) rotate(720deg);
                opacity: 0;
                border-radius: 50%;
            }
        }

        /* .bubbles */
        .slideanim {
            visibility: hidden;
        }

        .slide {
            animation-name: slide;
            -webkit-animation-name: slide;
            animation-duration: 1s;
            -webkit-animation-duration: 1s;
            visibility: visible;
        }

        @keyframes slide {
            0% {
                opacity: 0;
                transform: translateY(70%);
            }

            100% {
                opacity: 1;
                transform: translateY(0%);
            }
        }

        @-webkit-keyframes slide {
            0% {
                opacity: 0;
                -webkit-transform: translateY(70%);
            }

            100% {
                opacity: 1;
                -webkit-transform: translateY(0%);
            }
        }

        @media screen and (max-width: 768px) {
            .col-sm-4 {
                text-align: center;
                margin: 25px 0;
            }

            .btn-lg {
                width: 100%;
                margin-bottom: 35px;
            }
        }

        @media screen and (max-width: 480px) {
            .logo {
                font-size: 150px;
            }
        }

        .f{
        width:900px;
        margin-left:200px;
        }
    </style>

</head>

<body id="mypage" data-spy="scroll" data-target=".navbar" data-offset="60">

    <h1><img src="./caro/600px-BMW.svg.png" alt="" class="im">
        BYERISCHE MOTOREN WERKE AG</h1>
    <nav class="navbar navbar-inverse navbar-fixed-center active">
        <div class="container-fluid">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar"></button>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </div>
        <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
                <li class="active"><a href="./userBYERISCHE MOTOREN WERKE AG.py"> <span
                            class="glyphicon glyphicon-home"></span> HOME</a></li>
                <li><a href="./userABOUT_US.py"> <span class="glyphicon glyphicon-globe"></span> ABOUT_US</a></li>
                <li><a href="./userCARS.py"> <span class="glyphicon glyphicon-info-sign"></span> CARS </a></li>
                <li><a href="./userSERVICE.py"> <span class="glyphicon glyphicon-wrench"></span> SERVICE</a></li>
                <li><a href="./userCONTACT.py"> <span class="glyphicon glyphicon-phone"></span> CONTACT</a></li>
            </ul>
        </div>
    </nav>

    <div class="f">
        <form onsubmit="return login()" name="loginform" enctype="multipart/form-data">
                        <div class="form-group">
                            <label for="name">Your Name</label>
                            <input type="text" class="form-control" id="name" name="name" placeholder="Enter your name" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email Address</label>
                            <input type="email" class="form-control" id="email" name="email" placeholder="Enter your email" required>
                        </div>
                        <div class="form-group">
                            <label for="phone">Phone Number</label>
                            <input type="tel" class="form-control" id="phone" name="phone" placeholder="Enter your phone number"
                                required>
                        </div>
                        <div class="form-group">
                            <label for="car_model">Car Model</label>
                            <select class="form-control" id="car_model" name="car" required>
                                <option value="" disabled selected>Select a BMW model</option>
                                <option value="bmw1series">Select a BMW model</option>
                                <option value="bmw1series">BMW X1</option>
                                <option value="bmw3series">BMW X3</option>
                                <option value="bmw5series">BMW X4</option>
                                <option value="bmw5series">BMW X5 </option>
                                <option value="bmw5series">BMW X7</option>
                                <option value="bmw5series">BMW iX</option>
                                <option value="bmw5series">BMW XM</option>
                                <option value="bmw5series">BMW Z4</option>
                                <option value="bmw5series">BMW 3 Series</option>
                                <!-- Add more options as needed -->
                            </select>
                        </div>
                        <div class="form-group">
                                <label for="Date">Date</label>
                                <input type="date" class="form-control" id="date" name="date">
                        </div>
                        <div class="form-group">
                        <center>
                            <input type="SUBMIT" class="btn btn-primary" name="sub" style="width:300px;"></button>
                        </center>
        </form>
    </div><br><br>
</div>
    """)
print("""
    <footer style="background-color: black">
        <div class="footer">
            <div class="container">
                <div class="row">
                    <i>
                        <div class="col-sm-3">
                                <h3 style="color: white;text-align: center;">QUICK LINKS</h3>
                            <h4 style="margin-left: 50px;"><a href="./BYERISCHE MOTOREN WERKE AG.html"
                                    style="text-decoration: none; color:white;"><span
                                        class="glyphicon glyphicon-home"></span>HOME</a><br>
                                <a href="./ABOUT_US.html" style="text-decoration: none; color:white;"><span
                                        class="glyphicon glyphicon-globe"></span> ABOUT_US</a><br>
                                <a href="./CARS.html" style="text-decoration: none; color:white;"> <span
                                        class="glyphicon glyphicon-info-sign"></span> CARS</a><br>
                                <a href="./SERVICE.html" style="text-decoration: none; color:white;"> <span
                                        class="glyphicon  glyphicon-wrench"></span>
                                    SERVICE</a><br>
                                <a href="./CONTACT.html" style="text-decoration: none; color:white;"> <span
                                        class="glyphicon glyphicon-phone"></span> CONTACT_US</a>
                            </h4>
                        </div>
                        <div class="col-sm-3">
                                <h3 style="color: white;text-align: center;">CONTACT</h3>
                            <h4 style="margin-left: 70px;"><a href="" style="text-decoration: none; color:white;"><span
                                        class="glyphicon glyphicon-envelope"></span>
                                    Email</a><br>
                                <a href="" style="text-decoration: none; color:white;"><span
                                        class="glyphicon glyphicon-earphone"></span>
                                    CELL</a>
                            </h4>
                        </div>
                        <div class="col-sm-3">
                                <h3 style="color: white;text-align: center;">SOCIAL MEDIA</h3>
                            <h4 style="margin-left: 60px;">
                                <a href="" style="text-decoration: none; color:white;">FACEBOOK</a><br>
                                <a href="" style="text-decoration: none; color:white;"><span
                                        class="fa fa-instgram "></span>
                                    INSTAGRAM</a>
                            </h4>
                        </div>
                    </i>
                    <div class="col-sm-3">
                        <img src="./caro/600px-BMW.svg.png" alt=""
                            style="width: 100p;height: 100px;margin-top: 25px;margin-left: 50px;">
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <script>
        $(function () {
            $(document).scroll(function () {
                var $nav = $(".navbar-fixed-top");
                $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
            });
        });
    </script>
</body>

</html>
      """)
import smtplib
import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="empdb")
cur = conn.cursor()

form = cgi.FieldStorage()
pname = form.getvalue("name")
pemail = form.getvalue("email")
pcell = form.getvalue("phone")
pmodel = form.getvalue("car")
pdate = form.getvalue("date")
psubmit = form.getvalue("sub")

if psubmit != None:
    q = """insert into test_drive(name,email,phone,car_midel,date) 
               values('%s','%s','%s','%s','%s')""" % (pname, pemail, pcell, pmodel, pdate)
    cur.execute(q)
    conn.commit()

    print("""
        <script>
        alert("booking sucessfully")
        </script>
        """)
    fromaddr = "sidsriram1100@gmail.com"
    password = "arvs xbil drei dhzx"
    toaddr = pemail
    subject = "car tesy drive was successfully booked"
    body = """ NAME: '%s' \nMODEL: '%s' \nTEST DRIVE DATE: '%s' """ % (pname, pmodel, pdate)
    msg = """Subject:{}\n\n{}""".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(toaddr, password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()

conn.close()