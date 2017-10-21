% include('layouts/header.tpl', title='HomePage', User=User)

	<h2>Unacknowledged Alarms</h2>
	<table id="unacknowledged" class="striped highlight" style="height: 300px; overflow-y: scroll;">
		<thead>
			<tr>
				<th>Alarm ID</th>
				<th>Time Of Event</th>
				<th>Description</th>
				<th>State</th>
				<th>Acknowledge</th>
			</tr>
		</thead>
		<tbody>
			{{!data}}
		</tbody>
	</table>
	<h2>Acknowledged Alarms</h2>
	<table id="acknowledged" class="striped highlight">
		<thead>
			<tr>
				<th>Alarm ID</th>
				<th>Time Of Event</th>
				<th>Description</th>
				<th>State</th>
				<th>State History</th>
				<th>Acknowledged By</th>
				<th>Acknowledged At</th>
			</tr>
		</thead>
		<tbody>
			{{!ack_data}}
		</tbody>
	</table>

<script type="text/javascript">
	$(function() {
		$(".confirm").click( function(){
			// row = $(this).closest('tr').clone();
			$(this).closest('tr').remove();
			// $("#acknowledged").children('tbody').last('tr').append(row);
		});
	});

	$(document).ready(function() {
		$('#acknowledged').DataTable( {
			columnDefs: [
			{
				targets: [ 0, 1, 2 ],
				className: 'mdl-data-table__cell--non-numeric'
			}
			]
		});
	});
</script>

% include('layouts/footer.tpl')