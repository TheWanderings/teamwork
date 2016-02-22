"use strict";

angular.module("teamworkConsole")
.controller('loginForm', function($scope, $http, ConfigService, $routeParams, $location){
  $scope.formData = {};
  var next = $routeParams["next"] || "/";
  $scope.error = {
    account: null,
    password: null,
  };
  $scope.$watch("formData.account",
                function(newVal) {
                  $scope.error.account = null;
                });
  $scope.$watch("formData.password",
                function(newVal) {
                  $scope.error.password = null;
                });
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
      $location.path(next).search({});
    })
    .catch(function(response) {
      if (response.status === 401) {
        if (response.data.error === "wrongPassword") {
          $scope.error.password = response.data.error;
        }
        else if (response.data.error === "userMissing") {
          $scope.error.account = response.data.error;
        }
      }
      else {
        console.error(response);
      }
    })
    return false;
  };
});