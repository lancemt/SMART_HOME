import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';

import './main.html';

Template.hello.onCreated(function helloOnCreated() {
	// counter starts at 0
	this.counter = new ReactiveVar(0);
});

Template.hello.helpers({
	counter() {
		return Template.instance().counter.get();
	},
});

Template.hello.events({
	'click button'(event, instance) {
		// increment the counter when button is clicked
		instance.counter.set(instance.counter.get() + 1);
	},
});

// ================================

Template.register.events({
	'submit form': function(event) {
		event.preventDefault();
		console.log("Form submitted.");
	}
});

Template.register.events({
	'submit form': function(event){
		event.preventDefault();
		var emailVar = event.target.registerEmail.value;
		var passwordVar = event.target.registerPassword.value;
		Accounts.createUser({
			email: emailVar,
			password: passwordVar
		});
		console.log("Form submitted.");
	}
});

Template.login.events({
	'submit form': function(event){
		event.preventDefault();
		var emailVar = event.target.loginEmail.value;
		var passwordVar = event.target.loginPassword.value;
		Meteor.loginWithPassword(emailVar, passwordVar);
	}
});

Template.dashboard.events({
	'click .logout': function(event){
		event.preventDefault();
		Meteor.logout();
	}
});