% include('layouts/header.tpl', title='HomePage', User=User)

	<h2>Unacknowledged Alarms</h2>
	<div class="table">
		<table id="unacknowledged" class="striped highlight">
			<thead>
				<tr>
					<th>Alarm ID</th>
					<th>Time Of Event</th>
					<th>Description</th>
					<th>State</th>
					<th>Acknowledge</th>
				</tr>
			</thead>
			<tbody  style="color:red;">
				{{!data}}
			</tbody>
		</table>
	</div>
	<div class="divider"></div>
	<h2>Acknowledged Alarms</h2>
	<div class="table">
		<table id="acknowledged" class="striped highlight">
			<thead>
				<tr>
					<th>Alarm ID</th>
					<th>Time Of Event</th>
					<th>Description</th>
					<th>State</th>
					<th>State History</th>
					
					<th>Acknowledged At</th>
				</tr>
			</thead>
			<tbody  style="color:green;">
				{{!ack_data}}
			</tbody>
		</table>
	</div>

<script type="text/javascript">
	$(function() {
		$('.table').on('click', '.confirmBtn', function(){
			// row = $(this).closest('tr').clone();
			// $("#acknowledged").children('tbody').last('tr').append(row);
			row = $(this).closest('tr')
			$.ajax({
				type: 'POST',
				url: '/ackConfirm',
				data: {
					id:row.children().html(),
					state: row.find('.select-dropdown').val()
					// table:row.closest('table').attr('id') === 'unacknowledged'
				},
				success : function (response) {
						// Materialize.toast(response, 1000);
						row.remove();
						$("#acknowledged").children('tbody').last('tr').append(response);
						$('select').material_select();
				}
			});
			$.ajax({
				type: 'POST',
				url: '/generateReport',
				data: {
					id:row.children().html(),
					state: row.find('.select-dropdown').val()
					// table:row.closest('table').attr('id') === 'unacknowledged'
				},
				success : function (response) {
						// Materialize.toast(response, 1000);
						row.remove();
						$("#acknowledged").children('tbody').last('tr').append(response);
						$('select').material_select();
				}
			});
		});
	});
	function refTable(){
		$.ajax({
			type: 'POST',
			url: '/refreshTables',
			// data: {'latestDate': latestDate},
			statusCode: {
				200: function(response) {
					// Materialize.toast(response['data'][0], 1000);
					// console.log(response);
					$('#unacknowledged>tbody').append(response);	
					$('select').material_select();
					refTable();
				},
				299: function(response){
					// Materialize.toast("No. of timeouts: " + ++timeoutNo, 1000);
					console.log("Test: timeout reached, retrying...")
					refTable();
				}	
			}
		});
	}

	$(document).ready(function() {
		$('select').material_select();
		refTable();
	});
</script>

% include('layouts/footer.tpl')
