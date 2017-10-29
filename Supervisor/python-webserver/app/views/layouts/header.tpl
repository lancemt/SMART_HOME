<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="description" content="template for python 3.3+ web applications or web API server">
	<meta name="author" content="bottleplate">
	<!-- <link rel="shortcut icon" href="/img/favicon.ico"> -->

	<title>{{title}}</title>
	<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

	<link href="/css/materialize.min.css" rel="stylesheet" type="text/css">
	<script src="/js/jquery.min.js"></script>
	<script src="/js/materialize.min.js"></script>
	<link href="/css/main.css" rel="newest stylesheet" type="text/css">
</head>

<body>
	
	<nav>
		<div class="nav-wrapper">
			<a href="/" class="brand-logo">Smart Home System</a>
			<a href="#" data-activates="mobile-demo" class="button-collapse"><i class="material-icons">menu</i></a>
			<ul id="nav-mobile" class="right hide-on-med-and-down">
				%if User:
				<li><div class="userEmail">{{User}}</div></li>
				<li><a class="waves-effect waves-light btn" id="logout" href="#">Logout</a></li>
				%end
			</ul>
			<ul class="side-nav" id="mobile-demo">
				%if User:
				<li><a class="userEmail">{{User}}</a></li>
				<li><a class="waves-effect waves-light btn" id="logout" href="#">Logout</a></li>
				%end
			</ul>
		</div>
	</nav>

<script type="text/javascript">
$(document).ready(function() {
    $(".button-collapse").sideNav();
    $('#formLogin').submit(function(e) {
        $.ajax({
            type: 'POST',
            url: $('#formLogin').attr('action'),
            data: $(this).serialize(),
            success : function (response) {
                Materialize.toast(response, 1000);
                    // TODO: tell the user why the login failed
                    // on success then the server will redirect.
            }
        });
        e.preventDefault();
    });
});
</script>

	<!-- Wrap all page content here -->
	<div class="container">
