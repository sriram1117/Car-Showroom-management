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

            .ig {
                margin-top: -35px;
                width: 100%;
            }

""")
print("""    
            
        </style>
            <script>
                $(function () {
                    $(document).scroll(function () {
                        var $nav = $(".navbar-fixed-top");
                        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
                    });
                });
            </script>
    </head>
""")
print("""
    <body id="mybage" data-spy="scroll" data-target="navbar" data-offset="60">


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
                    <li><a href="./userCARS.py"> <span class="glyphicon glyphicon-info-sign"></span> CARS</a></li>
                    <li><a href="./userSERVICE.py"> <span class="glyphicon glyphicon-wrench"></span> SERVICE</a></li>
                    <li><a href="./userCONTACT.py"> <span class="glyphicon glyphicon-phone"></span> CONTACT</a></li>
                </ul>
            </div>
        </nav>
        <div class="">
            <img src="./folder/img2.jpg" alt="" style="width: 100%; height: 500px;margin-top: -35px;">
        </div>

        <div>
            <h1><i>CAR DETAILS</i></h1>
        </div><br>
""")
print("""
        <!-- Page Content -->
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <div class="thumbnail">
                        <img src="./New folder/bmw x1.jpg" alt="BMW Car 1">
                        <div class="caption">
                            <h3>BMW X1</h3>
                            <p>Price: ₹ 4,590,000</p>
                            <p>STARTING FROM</p>
                            <p>
                                <center>
                                    <a href="#" class="btn btn-primary" role="button" data-toggle="modal"
                                        data-target="#carModal1">Details <span
                                            class="glyphicon glyphicon-info-sign"></span></a>
                                </center>
                            </p>
                        </div>
                    </div>
                </div>
""")
print("""
                <div class="col-md-4">
                    <div class="thumbnail">
                        <img src="./New folder/bmw x3.jpg" alt="BMW Car 1">
                        <div class="caption">
                            <h3>BMW X3</h3>
                            <p>Price: ₹ 6,850,000</p>
                            <p>STARTING FROM</p>
                            <p>
                                <center>
                                    <a href="#" class="btn btn-primary" role="button" data-toggle="modal"
                                        data-target="#carModal2">Details <span class="glyphicon glyphicon-info-sign"></span>
                                    </a>
                                </center>
                            </p>
                        </div>
                    </div>
                </div>
""")
print("""
                <div class="col-md-4">
                    <div class="thumbnail">
                        <img src="./New folder/bmw x4.jpg" alt="BMW Car 1">
                        <div class="caption">
                            <h3>BMW X4</h3>
                            <p>Price: ₹ 9,620,000</p>
                            <p>STARTING FROM</p>
                            <p>
                                <center>
                                    <a href="#" class="btn btn-primary" role="button" data-toggle="modal"
                                        data-target="#carModal3">Details <span
                                            class="glyphicon glyphicon-info-sign"></span></a>
                                </center>
                            </p>
                        </div>
                    </div>
                </div>
""")
print("""
                <div class="col-md-4">
                    <div class="thumbnail">
                        <img src="./New folder/bmw x5.jpg" alt="BMW Car 1">
                        <div class="caption">
                            <h3>BMW X5</h3>
                            <p>Price: ₹ 9,520,000</p>
                            <p>STARTING FROM</p>
                            <p>
                                <center>
                                    <a href="#" class="btn btn-primary" role="button" data-toggle="modal"
                                        data-target="#carModal4">Details <span
                                            class="glyphicon glyphicon-info-sign"></span></a>
                                </center>
                            </p>
                        </div>
                    </div>
                </div>
""")
print("""
                <div class="col-md-4">
                    <div class="thumbnail">
                        <img src="./New folder/bmw x7.png" alt="BMW Car 1">
                        <div class="caption">
                            <h3>BMW X7</h3>
                            <p>Price: ₹ 12,370,000</p>
                            <p>STARTING FROM</p>
                            <p>
                                <center>
                                    <a href="#" class="btn btn-primary" role="button" data-toggle="modal"
                                        data-target="#carModal5">Details <span
                                            class="glyphicon glyphicon-info-sign"></span></a>
                                </center>
                            </p>
                        </div>
                    </div>
                </div>
""")
print("""
                <div class="col-md-4">
                    <div class="thumbnail">
                        <img src="./New folder/bmw xi.jpg" alt="BMW Car 1">
                        <div class="caption">
                            <h3>BMW iX</h3>
                            <p>Price: ₹ 12,100,000</p>
                            <p>STARTING FROM</p>
                            <p>
                                <center>
                                    <a href="#" class="btn btn-primary" role="button" data-toggle="modal"
                                        data-target="#carModal6">Details <span
                                            class="glyphicon glyphicon-info-sign"></span></a>
                                </center>
                            </p>
                        </div>
                    </div>
                </div>
""")
print("""
                <div class="col-md-4">
                    <div class="thumbnail">
                        <img src="./New folder/bmw xm.png" alt="BMW Car 1">
                        <div class="caption">
                            <h3>BMW XM</h3>
                            <p>Price: ₹ 26,000,000</p>
                            <p>STARTING FROM</p>
                            <p>
                                <center>
                                    <a href="#" class="btn btn-primary" role="button" data-toggle="modal"
                                        data-target="#carModal7">Details <span
                                            class="glyphicon glyphicon-info-sign"></span></a>
                                </center>
                            </p>
                        </div>
                    </div>
                </div>
""")
print("""
                <div class="col-md-4">
                    <div class="thumbnail">
                        <img src="./New folder/bmw z4.jpg" alt="BMW Car 1">
                        <div class="caption">
                            <h3>BMW Z4</h3>
                            <p>Price: ₹ 5,04,999</p>
                            <p>STARTING FROM</p>
                            <p>
                                <center>
                                    <a href="#" class="btn btn-primary" role="button" data-toggle="modal"
                                        data-target="#carModal8">Details <span
                                            class="glyphicon glyphicon-info-sign"></span></a>
                                </center>
                            </p>
                        </div>
                    </div>
                </div>
""")
print("""
                <div class="col-md-4">
                    <div class="thumbnail">
                        <img src="./New folder/bmw m8.jpg" alt="BMW Car 1">
                        <div class="caption">
                            <h3>BMW M8</h3>
                            <p>Price:₹ 24,400,000</p>
                            <p>STARTING FROM</p>
                            <p>
                                <center>
                                    <a href="#" class="btn btn-primary" role="button" data-toggle="modal"
                                        data-target="#carModal9">Details <span
                                            class="glyphicon glyphicon-info-sign"></span></a>
                                </center>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
""")
print("""
            <!-- Modals for Car Details <span class="glyphicon glyphicon-info-sign"></span> -->
            <div class="modal fade" id="carModal1" tabindex="-1" role="dialog" aria-labelledby="carModal1Label">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" id="carModal1Label" style="text-align: center;">BMW X1 Details</h4>
                        </div>
                        <div class="modal-body">
                            <p>Price: ₹ 4,590,000</p>
                            <h3>12.04 Km/l</h3>
                            <p>Fuel consumption,combained</p>
                            <h3>Petrol Diesel</h3>
                            <p>Engine and Fuel Type</p>
                            <h4>The new BMW X1 impresses with its comprehensive versatility and functionality:</h4>
                            <ul>
                                <li>Clearly structured design language on the exterior for a sporty and self-assured
                                    presence</li>
                                <li>Available with combustion engine, in petrol and diesel</li>
                                <li>The modern interior is equipped with high-quality materials and innovations such as the
                                    BMW Curved Display
                                </li>
                            </ul>
                            <h3>BMW X1 sDrive18d:</h3>
                            <p>
                            <ul>
                                <li>Fuel consumption, combined km/L: 20.37</li>
                                <li>CO2 emissions, combined in g/km: 130</li>
                            </ul>
                            </p>
                            <h3>BMW X1 sDrive18i:</h3>
                            <p>
                            <ul>
                                <li>Fuel consumption, combined km/L: 16.35</li>
                                <li>CO2 emissions, combined in g/km: 145</li>
                            </ul>
                            </p>
                            <!-- Add more car details <span class="glyphicon glyphicon-info-sign"></span> here -->
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
""")
print("""
            <div class="modal fade" id="carModal2" tabindex="-1" role="dialog" aria-labelledby="carModal1Label">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" id="carModal1Label" style="text-align: center;">BMW X3 Details</h4>
                        </div>
                        <div class="modal-body">
                            <p>Price: ₹ 6,850,000</p>
                            <h3>12.04 Km/l</h3>
                            <p>Fuel consumption,combained</p>
                            <h3> Diesel</h3>
                            <p>Engine and Fuel Type</p>
                            <h4>The exquisite feel of luxury finally meets the exhilarating zeal of performance. With
                                interiors so grand, features so
                                advanced and performance so powerful, the BMW X3 is ready to serve an experience that’s
                                nothing like you’ve felt before.</h4>
                            <ul>

                                <!-- Add more car details <span class="glyphicon glyphicon-info-sign"></span> here -->
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
""")
print("""
            <div class="modal fade" id="carModal3" tabindex="-1" role="dialog" aria-labelledby="carModal1Label">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" id="carModal1Label" style="text-align: center;">BMW X4 Details</h4>
                        </div>
                        <div class="modal-body">
                            <p>Price: ₹ 9,620,000</p>
                            <h3>Up to 360 hp (265 kW)</h3>
                            <p>Engine Type</p>
                            <h3>Petrol</h3>
                            <p>Fuel Type</p>
                            <h4>The first-ever BMW X4 xDrive M40i combine BMW M TwinPower Turbo engines with M-specific
                                elements to give the Sports
                                Activity Coupé (SAC) class new levels of performance.</h4>
                            <!-- Add more car details <span class="glyphicon glyphicon-info-sign"></span> here -->
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
""")
print("""
            <div class="modal fade" id="carModal4" tabindex="-1" role="dialog" aria-labelledby="carModal1Label">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" id="carModal1Label" style="text-align: center;">BMW X5 Details</h4>
                        </div>
                        <div class="modal-body">
                            <p>Price:₹ 9,520,000</p>
                            <h3>12.04 Km/l</h3>
                            <p>Fuel consumption,combained</p>
                            <h3>Petrol Diesel</h3>
                            <p>Engine and Fuel Type</p>
                            <h4>With the BMW X5,you experience exceptional interior comfort and innovative functionality in
                                a
                                sporty design:</h4>
                            <ul>
                                <li>Powerful BMW TwinPower Turbo 6-cylinder combustion engine with 280 kW (381 hp)</li>
                                <li>Adaptive 2-Axle Air Suspension</li>
                                <li>Glowing BMW kidney “Iconic Glow”</li>
                                <li>Innovative BMW Curved Display with touch-based operating concept</li>
                                <li>BMW Live Cockpit Professional: with head-up display, Augmented Reality Navigation and
                                    more</li>
                            </ul>
                            <h3>BMW X5 xDrive40i:</h3>
                            <p>
                            <ul>
                                <li>Fuel consumption, combined WLTP in km/l: 12.04 km/l</li>
                                <li> CO2 emissions, combined WLTP in g/km: 197.0 g/km</li>
                            </ul>
                            </p>
                            <h3>BMW X5 xDrive30d:</h3>
                            <p>
                            <ul>
                                <li>Fuel consumption, combined WLTP in km/l: 11.98 km/l</li>
                                <li>CO2 emissions, combined WLTP in g/km: 198.0 g/km</li>
                            </ul>
                            </p>
                            <!-- Add more car details <span class="glyphicon glyphicon-info-sign"></span> here -->
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
""")
print("""
            <div class="modal fade" id="carModal5" tabindex="-1" role="dialog" aria-labelledby="carModal1Label">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" id="carModal1Label" style="text-align: center;">BMW X7 Details </h4>
                        </div>
                        <div class="modal-body">
                            <p>Price: ₹ 12,370,000</p>
                            <h3>11.29 km/L</h3>
                            <p>Fuel consumption,combained</p>
                            <h3>Petrol Diesel</h3>
                            <p>Engine and Fuel Type</p>
                            <h4>The new BMW X7 xDrive40i fascinates from the very first encounter with its combination of
                                uncompromising power,
                                luxurious comfort and expressive design language:</h4>
                            <ul>
                                <li>The lively BMW TwinPower Turbo 6-cylinder petrol engine delivers 280 kW (381 hp) onto
                                    the road.</li>
                                <li>The standard series 2-axle air suspension makes every journey especially comfortable.
                                </li>
                                <li>Comfort seats wrapped in BMW Individual Extended Leather Trim Merino.</li>
                                <li>The new face of the BMW luxury class: split headlights, redesigned kidney grille (with
                                    optional illumination) and front
                                    apron.</li>
                            </ul>
                            <h3>BMW X7 xDrive40i*:</h3>
                            <p>
                            <ul>
                                <li>Fuel consumption in km/L (combined): 11.29 </li>
                                <li> CO2 emissions in g/km (combined): 210</li>
                            </ul>
                            </p>
                            <h3>BMW X7 xDrive40d*: </h3>
                            <p>
                            <ul>
                                <li>FFuel consumption in km/L (combined): 14.31</li>
                                <li>CO2 emissions in g/km (combined): 185</li>
                            </ul>
                            </p>
                            <h3>BMW X7 xDrive40d DPE 7 Seater*: </h3>
                            <p>
                            <ul>
                                <li>Fuel consumption in km/L (combined): 14.31</li>
                                <li>CO2 emissions in g/km (combined): 185</li>
                            </ul>
                            </p>
                            <!-- Add more car details <span class="glyphicon glyphicon-info-sign"></span> here -->
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
""")
print("""
            <div class="modal fade" id="carModal6" tabindex="-1" role="dialog" aria-labelledby="carModal1Label">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" id="carModal1Label" style="text-align: center;">BMW iX Details </h4>
                        </div>
                        <div class="modal-body">
                            <p>Price: ₹ 12,100,000</p>
                            <h3>Full-Electric</h3>
                            <p>Engine and Fuel Type</p>
                            <h4>THE FIRST ALL-ELECTRIC BMW iX: JOY. BORN AGAIN.</h4>
                            <ul>
                                <li>The first all-electric BMW iX is a first of its kind in a future-oriented generation of
                                    automobiles. With fully-electric
                                    driving pleasure and newly-developed, precise and minimalist monolithic design, the BMW
                                    iX is a vision turned into
                                    reality. Discover the emblem of new era of mobility and electrify your sheer driving
                                    pleasure.
                                </li>
                            </ul>
                            <!-- Add more car details <span class="glyphicon glyphicon-info-sign"></span> here -->
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
""")
print("""
            <div class="modal fade" id="carModal7" tabindex="-1" role="dialog" aria-labelledby="carModal1Label">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" id="carModal1Label" style="text-align: center;">BMW XM Details</h4>
                        </div>
                        <div class="modal-body">
                            <p>Price: ₹ 26,000,000/p>
                            <h3>480 kW (653 hp)</h3>
                            <p>Performance</p>
                            <h3>Plug-in Hybrid</h3>
                            <p>Engine and Fuel Type</p>
                            <h4>THE FIRST-EVER BMW XM.</h4>
                            <ul>
                                <li>Exclusive, expressive, electrified: The new BMW XM combines impressive presence with the
                                    high performance of a BMW M and
                                    powerful plug-in hybrid technology of the latest generation.</li>
                            </ul>
                            <h3>BMW XM*:</h3>
                            <p>
                            <ul>
                                <li>FFuel Consumption, Combined km/l: 61.9 </li>
                                <li>CO2 emissions, Combined g/km: 36.5</li>
                                <li>Energy consumption, combined WLTP in kWh/100 km: 30.1–28.9</li>
                            </ul>
                            </p>
                            <!-- Add more car details <span class="glyphicon glyphicon-info-sign"></span> here -->
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
""")
print("""
            <div class="modal fade" id="carModal8" tabindex="-1" role="dialog" aria-labelledby="carModal1Label">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" id="carModal1Label" style="text-align: center;">BMW Z4 Details </h4>
                        </div>
                        <div class="modal-body">
                            <p>Price: ₹ 5,04,999</p>
                            <h3>12.095 Km/l</h3>
                            <p>Fuel consumption,combained</p>
                            <h3>Petrol</h3>
                            <p>Engine and Fuel Type</p>
                            <h4>The BMW Z4 combines the dynamics of a sports car with the freedom of a roadster. Explore for
                                yourself:</h4>
                            <ul>
                                <li>Progressive aesthetics in an iconic roadster design</li>
                                <li>Powerful driving dynamics with up to 250 kW (340 hp)* and high-precision handling</li>
                                <li>M aerodynamics package for optimised efficiency and dynamics</li>
                            </ul>
                            <!-- Add more car details <span class="glyphicon glyphicon-info-sign"></span> here -->
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
""")
print("""
            <div class="modal fade" id="carModal9" tabindex="-1" role="dialog" aria-labelledby="carModal1Label">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h4 class="modal-title" id="carModal1Label" style="text-align: center;">BMW M8 Details
                            </h4>
                        </div>
                        <div class="modal-body">
                            <p>Price: ₹ 24,400,000</p>
                            <h3>Up to 625 hp (460 kW)</h3>
                            <p>Performance</p>
                            <h3>Petrol</h3>
                            <p>Engine and Fuel Type</p>
                            <h4>NEW BMW M8 Competition Coupé.</h4>
                            <ul>
                                <li>With its distinguished motorsport legacy, BMW M has long been all about
                                    racetrack-inspired engineering and performance.
                                    On the 50th anniversary of this unmatched automotive journey, we commend our community
                                    of fans, drivers, and M
                                    enthusiasts for upholding the ethos of M. The past 50 years have been about providing
                                    pure JOY to our customers - faster
                                    heartbeats, surging adrenaline and unbridled excitement. Now, to celebrate BMW M's
                                    fascinating history, we're launching
                                    some exciting '50 Jahre M' editions through the year.</li>
                                <li>As part of the celebrations, we now present the new BMW M8 Competition Coupé 50 Jahre M'
                                    Edition. The M8 badge itself
                                    leaves no doubt that the ultimate experience of M is imminent. Built for the racetrack,
                                    it's the embodiment of pure
                                    performance and represents the essence of what we have learned and developed over the
                                    last 50 years. And despite its
                                    sports car genes, the lavishly designed interior of the BMW M8 Competition Coupé '50
                                    Jahre M' Edition sets new standards
                                    in luxury. This car is the cutting edge of BMW M, pushing the limits of driving physics
                                    for that ultimate adrenaline
                                    thrill.</li>
                            </ul>
                            <h3>BMW M8 Competition Coupé:</h3>
                            <p>
                            <ul>
                                <li>uel consumption in km/l (combined): 8.77 </li>
                                <li> CO2 emissions in g/km (combined): 262</li>
                            </ul>
                            </p>
                            <!-- Add more car details <span class="glyphicon glyphicon-info-sign"></span> here -->
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br><br>


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
                                    <a href="./userSERVICE.py" style="text-decoration: none; color:white;"> <span
                                            class="glyphicon  glyphicon-wrench"></span>
                                        SERVICE</a><br>
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
    </body>

</html>
""")