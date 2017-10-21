%if acknowledged:
<tr>
	<td>{{alarm_id}}</td>
	<td>{{time_of_event}}</td>
	<td>{{description}}</td>
	<td>{{state}}</td>
	<td>{{state_history}}</td>
	<td>{{acknowledged_by}}</td>
	<td>{{acknowledged_at}}</td>
</tr>
%else:
<tr>
	<td>{{alarm_id}}</td>
	<td>{{time_of_event}}</td>
	<td>{{description}}</td>
	<td>{{state}}</td>
	<td><a class="waves-effect waves-light btn confirm" href="#">Confirm</a></td>
</tr>
%end