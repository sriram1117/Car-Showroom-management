#!C:/Users/JJ/AppData/Local/Programs/Python/Python310/Python.exe
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

        .caro {
            margin-top: -35px;
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
            visibility: visible;
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
    <nav class="navbar navbar-inverse navbar-fixed-center active" method="post">
        <div class="container-fluid">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar"></button>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </div>
        <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#"> <span class="glyphicon glyphicon-home"></span> HOME</a></li>
                <li><a href="./userABOUT_US.py"> <span class="glyphicon glyphicon-globe"></span> ABOUT_US</a></li>
                <li><a href="./userCARS.py"> <span class="glyphicon glyphicon-info-sign"></span> CARS</a></li>
                <li><a href="./userSERVICE.py"> <span class="glyphicon glyphicon-wrench"></span> SERVICE</a></li>
                <li><a href="./userCONTACT.py"> <span class="glyphicon glyphicon-phone"></span> CONTACT</a></li>
            </ul>
        </div>
    </nav>

    <!-- carousel -->
    <div class="caro">
        <div id="mycarousel" class="carousel slide" data-ride="carousel">
            <!-- indicatores -->
            <ol class="carousel-indicators">
                <li data-target-="#mycarousel" data-slide-to="0" class="active"></li>
                <li data-target-="#mycarousel" data-slide-to="1"></li>
                <li data-target-="#mycarousel" data-slide-to="2"></li>
                <!-- <li data-target-="#mycarousel" data-slide-to="3"></li> -->
            </ol>
            <!-- wrapper for slides -->
            <div class="carousel-inner">

                <div class="item active">
                    <img src="./new/p90399176_highres_the-new-bmw-m3-compe.webp" alt=""
                        style="height: 500px;width: 100%;">
                </div>

                <div class="item">
                    <img src="./new/bmw-i4-m50-bmw-ix-stage-teaser.jpg" alt="" style="height: 500px;width: 100%;">
                </div>

                <div class="item">
                    <img src="./new/p90416614-highres-1618598278.jpg" alt="" style="height: 500px;width: 100%;">
                </div>

                <!-- <div class="item">
                        <img src="./front-left-side-47.jpg" alt="" style="height: 500px;width: 100%;">
                    </div> -->
            </div>

            <!-- left and right control -->

            <a class="left carousel-control" href="#mycarousel" data-slide="prev">
                <span class="glyphicon glyphicon-chevron-left"></span>
                <span class="sr-only">previous</span>
            </a>

            <a class="right carousel-control" href="#mycarousel" data-slide="next">
                <span class="glyphicon glyphicon-chevron-right"></span>
                <span class="sr-only">next</span>
            </a>
        </div>

    </div><br><br>

    <div class="container">
        <h3 style="text-align: center;">BYERISCHE MOTOREN WERKE AG[BMW]</h3>
        <p class="container" style="text-align: justify;">Bayerische Motoren Werke AG, abbreviated as BMW (German
            pronunciation), is a German
            multinational
            manufacturer of luxury vehicles and motorcycles headquartered in Munich, Bavaria, Germany. The company
            was
            founded in
            1916 as a manufacturer of aircraft engines, which it produced from 1917 to 1918 and again from 1933 to
            1945.
            Automobiles are marketed under the brands BMW, Mini and Rolls-Royce, and motorcycles are marketed under the
            brand BMW
            Motorrad. In 2017, BMW was the world's fourteenth-largest producer of motor vehicles, with 2,279,503
            vehicles
            produced and in 2022 the 7th largest by revenue. The company has significant motor-sport history,
            especially in
            touring cars, sports cars, and the Isle of Man TT.

            BMW is headquartered in Munich and produces motor vehicles in Germany, Brazil, China, India, Mexico, the
            Netherlands,
            South Africa, the United Kingdom, and the United States. The Quandt family is a long-term shareholder of the
            company,
            following investments by the brothers Herbert and Harald Quandt in 1959 that saved BMW from bankruptcy, with
            the
            remaining shares owned by the public.
        </p>
    </div><br><br><br>


    <div class="container">
        <div class="row">
            <div class="column slideanim">
                <div class="col-md-4">
                    <div class="thumbnail" style="background-color: black;">
                        <img src="./folder/img12.jpg" alt="" height="300px" width="100%">
                    </div>
                </div>
            </div>
            <div class="column slideanim">
                <div class="col-md-4">
                    <div class="thumbnail" style="background-color: black;">
                        <img src="./folder/img13.jpg" alt="" height="300px" width="100%">
                    </div>
                </div>
            </div>
            <div class="column slideanim">
                <div class="col-md-4">
                    <div class="thumbnail" style="background-color: black;">
                        <img src="./folder/img6.jpg" alt="" height="300px" width="100%">
                    </div>
                </div>
            </div>
            <div class="column slideanim">
                <div class="col-md-4">
                    <div class="thumbnail" style="background-color: black;">
                        <img src="./folder/img8.jpg" alt="" height="300px" width="100%">
                    </div>
                </div>
            </div>
            <div class="column slideanim">
                <div class="col-md-4">
                    <div class="thumbnail" style="background-color: black;">
                        <img src="./folder/img3.jpg" alt="" height="300px" width="100%">
                    </div>
                </div>
            </div>
            <div class="column slideanim">
                <div class="col-md-4">
                    <div class="thumbnail" style="background-color: black;">
                        <img src="./folder/img4.jpg" alt="" height="300px" width="100%">
                    </div>
                </div>
            </div>
        </div>
    </div>
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
                                <a href="./userCARS.py" style="text-decoration: none; color:white;"> <span
                                        class="glyphicon glyphicon-info-sign"></span> CARS</a><br>
                                <a href="./userSERVICE.py" style="text-decoration: none; color:white;"> <span
                                        class="glyphicon  glyphicon-wrench"></span> SERVICE</a><br>
                                <a href="./userCONTACT.py" style="text-decoration: none; color:white;"> <span
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