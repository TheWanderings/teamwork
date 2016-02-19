"use strict";

angular.module("teamworkConsole")
.controller('entrance', function(UserService, ConfigService){
  UserService.getMe()
  .then(function(me) {
    console.log(me);
  })
  .catch(function(res) {
    console.log(res);
  });
})
;