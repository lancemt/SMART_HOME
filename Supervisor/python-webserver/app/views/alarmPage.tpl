% include('layouts/header.tpl', title='HomePage', User=User)

	<h2>Unacknowledged Alarms</h2>
	<table id="unacknowledged" class="striped highlight">
		<thead>
			<tr>
				<th>AlarmID</th>
				<th>Description</th>
				<th>State</th>
				<th>Acknowledge</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>TEST</td>
				<td>TEST</td>
				<td>TEST</td>
				<td>TEST</td>
			</tr>
			<tr>
				<td>TEST</td>
				<td>TEST</td>
				<td>TEST</td>
				<td>TEST</td>
			</tr>
		</tbody>
	</table>

% include('layouts/footer.tpl')