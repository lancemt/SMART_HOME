import { Meteor } from 'meteor/meteor';

var db = new MongoInternals.RemoteCollectionDriver('mongodb://localhost:27017/test')

Meteor.startup(() => {
  // code to run on server at startup
  console.log(db.open('users').find().fetch())
});
