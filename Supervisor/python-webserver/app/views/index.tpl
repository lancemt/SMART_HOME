% include('layouts/header.tpl', title='HomePage', User=User)

<h1>LOGIN</h1>

<div class="table">
		<table id="Login" class="striped highlight">
			<thead>

			  	Usernname:<br>
			  	<input type="text" name="firstname"><br>
			  	Password:<br>
			  	<input type="text" name="lastname">
			  	<td><button class="waves-effect waves-light btn confirmBtn" href="#">Confirm</button></td>
			</thead>
		</table>
</div>



<script type="text/javascript">
	$(function() 
	{
		$('.table').on('click', '.confirmBtn', function()
		{
			getElementsByTagName('')
		}
	}
</script>

% include('layouts/footer.tpl')