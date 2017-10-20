import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';


import './main.html';

Template.loginBtn.helpers({
	userEmail:function(){
		if (Meteor.user().emails && Meteor.user().emails.length > 0) {
				return Meteor.user().emails[0].address;
			}
			return 'no email';
	}
});

// $('.collapsible').collapsible();
// Template.loginBtn.onCreated(function () {
// 	this.collapsible();
// });

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

Template.loginBtn.events({
	'click' : function(event, instance) {
		event.preventDefault();
		console.log("TEST");
	},
		'click #logout': function(event){
		event.preventDefault();
		Meteor.logout();
	}
});
	
Meteor.startup(function () {
	$('.modal').modal();
});