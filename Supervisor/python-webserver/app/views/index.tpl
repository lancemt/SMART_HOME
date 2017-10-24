% include('layouts/header.tpl', title='HomePage', User=User)

<h1>LOGIN</h1>

<form id="formLogin" class="col s12" action="/login" method="post">
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
						<input href="#!" class="waves-effect waves-light btn confirmBtn" type="submit" value="Submit"/>
					</div>
				</form>

</div>

<script type="text/javascript">
$(document).ready(function() {
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


% include('layouts/footer.tpl')