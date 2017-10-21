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
			<a href="/" class="brand-logo">Logo</a>
			<ul id="nav-mobile" class="right hide-on-med-and-down">
				<li><a href="alarmpage">Alarm Page</a></li>
				<!-- <li><a href="badges.html">Components</a></li> -->
				%if User:
				<li><div class="userEmail">{{User}}</div></li>
				<li><a class="waves-effect waves-light btn" id="logout" href="#">Logout</a></li>
				%else:
				<li><a class="waves-effect waves-light btn modal-trigger" id="login" href="#modal1">Login</a></li>
				%end
			</ul>
		</div>
	</nav>


<!-- Modal Structure -->
	<div id="modal1" class="modal">
		<div class="modal-content">
			<h4 style="text-align:center">Log in</h4>
			<div class="row">
				<form class="col s12" action="/login" method="post">
					<div class="row">
						<div class="input-field col s12">
							<input name="email" type="email" class="validate">
							<label for="email">Email</label>
						</div>
					</div>
					<div class="row">
						<div class="input-field col s12">
							<input name="password" type="password" class="validate">
							<label for="password">Password</label>
						</div>
					</div>
					<div class="modal-footer">
						<input href="#!" class="modal-action modal-close waves-effect waves-green btn-flat" type="submit" value="Submit"/>
					</div>
				</form>
			</div>
		</div>
	</div>

	<!-- Wrap all page content here -->
	<div class="container">