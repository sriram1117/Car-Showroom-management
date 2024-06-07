#!C:/Users/JJ/AppData/Local/Programs/Python/Python310/Python.exe

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- Latest compiled and minified CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Latest compiled JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">

    <style>
        .nav-link {
            color: red !important;
            border-bottom: 1px solid transparent;
            font-weight: bolder;
        }
    
        a {
            font-size: 15px;

        }

        .logo {
            border-radius: 50%;
            position: absolute;
            margin-left: 100px;
            margin-top: -40px;
        }
        body{
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
        }
    </style>
</head>

<body>
    <nav class="navbar navbar-expand-sm bg-dark navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#"><img class="logo" src="./caro/600px-BMW.svg.png"
                    style="height: 100px;width: 100px;" alt=""></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="collapsibleNavbar">
                <!-- <div class="collapse navbar-collapse" id="navbarNav"> -->
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="./adminloginform.py">
                            ADMIN</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./emploginform.py">LOGIN</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./userregform.py">REGESTER</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="./userloginform.py">USER LOGIN</a>
                    </li>
                    <!-- Add more navigation items as needed -->
                </ul>
            </div>

        </div>
        </div>
    </nav>

    <div class="f1">
        <img style="height: 600px;width: 100%;" src="./image/peakpx.jpg" alt="">
    </div>

</body>

</html>
      """)