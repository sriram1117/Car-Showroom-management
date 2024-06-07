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

    <div class="">
        <img src="./folder/img5.jpg" alt="" style="width: 100%; height: 500px;margin-top: -35px;">
    </div>

    <div class="container">
        <div class="container-fluid">
            <ul class="bubbles">
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
            </ul>
        </div>
        <table class="table table-bordered">
            <h3 style="text-align: center;">Key Highlights of BMW Cars</h3>
            <th style="text-align: justify;" colspan="400">The key Highlights of BMW Cars include a diverse range of
                models like the
                popular BMW X7 and BMW X5,
                offering options in
                Petrol, Diesel, Electric. With upcoming models like the BMW M3 and BMW X6 on the horizon, BMW continues
                to keep its
                customers excited and hooked for its upcoming launches. They also boasts an extensive network of 59
                showrooms and 37
                service centers to ensure customer satisfaction.
            </th>
            <tr style="text-align: center;">
                <td colspan="4">Popular BMW Car Models</td>
                <td> BMW X7, BMW X5, BMW X1, BMW Z4, BMW XM</td>
            </tr>
            <tr style="text-align: center;">
                <td colspan="4">Best Mileage</td>
                <td>i7 (560 KM)</td>
            </tr>
            <tr style="text-align: center;">
                <td colspan="4">Most Expensive BMW Car</td>
                <td>XM (Rs.2.60 Crore)</td>
            </tr>
            <tr style="text-align: center;">
                <td colspan="4">Lowest Price</td>
                <td>2 Series (Rs.43.50 Lakh)</td>
            </tr>
            <tr style="text-align: center;">
                <td colspan="4">Upcoming BMW Car Models</td>
                <td>BMW M3, BMW X6, BMW i5, BMW 5 Series 2024</td>
            </tr>
            <tr style="text-align: center;">
                <td colspan="4">Fuel Type</td>
                <td>Petrol, Diesel, Electric</td>
            </tr>
            <tr style="text-align: center;">
                <td colspan="4">BMW Electric Cars</td>
                <td>BMW iX, BMW i7, BMW i4, BMW iX1</td>
            </tr>
            <tr style="text-align: center;">
                <td colspan="4">BMW Car Showrooms</td>
                <td>59 Outlets</td>
            </tr>
            <tr style="text-align: center;">
                <td colspan="4">BMW Car Service Centers</td>
                <td>37</td>
            </tr>
        </table>
    </div>
    <br>
    <div>
        <h1><i>CAR BOOKING</i></h1>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <div class="thumbnail" style="background-color: black;">
                    <img src="./folder/img9.jpg" alt="" height="300px" width="100%">
                    <div class="caption">
                        <center>
                            <a href="./userbooking.py"><input type="button" class="btn btn-primary" value="BOOKING FORM"></a>
                        </center>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="thumbnail" style="background-color: black;">
                    <img src="./folder/img1.jpg" alt="" height="300px" width="100%">
                    <div class="caption">
                        <center>
                            <a href="./testdrive.py"><input type="button" class="btn btn-primary" value="TEST DRIVE FORM"></a>
                        </center>   
                    </div>
                </div>
            </div>
        </div>
    </div><br><br>

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