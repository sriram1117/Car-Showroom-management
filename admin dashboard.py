#!C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
<style>
    .a1{
       padding-right:300px; 
       margin-top:100px;
    }
    
    .container-fluid{
        position:fixed;
        overflow: auto;

    }
</style>
</head>

<body>
    <div class="container-fluid">
        <div class="row flex-nowrap">
            <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
                <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-100">
                    <a href="/"
                        class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-white text-decoration-none">
                        <span class="fs-5 d-none d-sm-inline"></span>
                    </a>
                    <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start"
                        id="menu">
                        <li class="nav-item">
                            <a href="./admin dashboard.py" class="nav-link align-middle px-0">
                                <i class="fas fa-home"></i> <span class="ms-1 d-none d-sm-inline">DASHBOARD</span>
                            </a>
                        </li>
                        <li>
                            <a href="#submenu2" data-bs-toggle="collapse" class="nav-link px-0 align-middle ">
                                <i class="fab fa-black-tie"></i> <span
                                    class="ms-1 d-none d-sm-inline">EMPLOYEE DETAILS </span></a>
                            <ul class="collapse nav flex-column ms-1" id="submenu2" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./adminempaddform.py" class="nav-link px-0"> <i class="fas fa-ankh"></i> <span class="d-none d-sm-inline">NEW</span>
                                        </a>
                                </li>
                                <li>
                                    <a href="./adminempdataview.py" class="nav-link px-0"> <i class="fas fa-eye"></i> <span class="d-none d-sm-inline">VIEW</span>
                                        </a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="./admininventrystatus.py" class="nav-link px-0 align-middle">
                                <i class="fas fa-car-crash"></i> <span class="ms-1 d-none d-sm-inline">INVENTRY & ASSET</span></a>
                        </li>
                        <li>
                            <a href="#submenu3" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                                <i class="fas fa-comment-medical"></i> <span class="ms-1 d-none d-sm-inline">LEAVE REQUEST</span> </a>
                            <ul class="collapse nav flex-column ms-1" id="submenu3" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./adminleavedataview.py" class="nav-link px-0"> <i class="fas fa-ankh"></i> <span class="d-none d-sm-inline">NEW</span>
                                        </a>
                                </li>
                                <li>
                                    <a href="./adminleavedatatable.py" class="nav-link px-0"> <i class="fas fa-backspace"></i> <span class="d-none d-sm-inline">EXIST</span>
                                        </a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="./salary.py" class="nav-link px-0 align-middle">
                                <i class="fas fa-hand-holding-usd"></i> <span class="ms-1 d-none d-sm-inline">SALARY CALCULATION</span>
                            </a>
                        </li>
                    </ul>
                    <hr>
                    <div class="dropdown pb-4">
                        <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle"
                            id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                            <img src="./image/WhatsApp Image 2023-12-07 at 11.22.08 AM.jpeg" alt="hugenerd" width="30" height="30"
                                class="rounded-circle">
                            <span class="d-none d-sm-inline mx-1">MORE</span>
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark text-small shadow">

                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="./home.py">Sign out</a></li>
                        </ul>
                    </div>
                </div>
            </div>
    <div class="active a1">
        <center>
            <h2>WELCOME ADMIN</h2>
            <img class="user" src="./image/WhatsApp Image 2023-12-07 at 11.22.08 AM.jpeg" alt="" height="200px"
                width="200px">
        </center>
    </div>

</body>

</html>
      """)