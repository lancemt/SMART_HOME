%if acknowledged:
<tr>
	<td>{{alarm_id}}</td>
	<td>{{time_of_event}}</td>
	<td>{{description}}</td>
	<td>
		<select>
			<option {{'selected' if state == 'Non-Critical' else ''}}>Non-Critical</option>
			<option {{'selected' if state == 'Urgent' else ''}}>Urgent</option>
			<option {{'selected' if state == 'Critical' else ''}}>Critical</option>
		</select>
	</td>
	<td>{{state_history}}</td>
	<td>{{acknowledged_by}}</td>
	<td>{{acknowledged_at}}</td>
	<td><button class="waves-effect waves-light btn confirmBtn" href="#">Confirm</button></td>
</tr>
%else:
<tr>
	<td>{{alarm_id}}</td>
	<td>{{time_of_event}}</td>
	<td>{{description}}</td>
	<td>
		<select>
			<option {{'selected' if state == 'Non-Critical' else ''}}>Non-Critical</option>
			<option {{'selected' if state == 'Urgent' else ''}}>Urgent</option>
			<option {{'selected' if state == 'Critical' else ''}}>Critical</option>
		</select>
	</td>
	<td><button class="waves-effect waves-light btn confirmBtn" href="#">Confirm</button></td>
</tr>
%end