"use strict";

angular.module("teamworkConsole")
.controller('loginForm', function($scope, $http, ConfigService){
  $scope.formData = {};
  $scope.login = function() {
    var fd = new FormData();
    for (var k in $scope.formData) {
      fd.append(k, $scope.formData[k]);
    }
    var req = {
      url: "/login",
      method: "POST",
      data: fd,
      headers: {"Content-Type": undefined},
    };
    ConfigService.wrappedHttp(req)
    .then(function(response) {
      console.log(response);
    })
    .catch(function(response) {
      console.log(response);
    })
    return false;
  };
});