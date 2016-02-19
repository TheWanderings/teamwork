"use strict";

angular.module("teamworkConsole")
.service("ConfigService", function($http, $q){
  this.configs = null;
  var svc = this;
  // this.getConfigs = function(success, error) {
  //   if (svc.configs !== null) {
  //     success(svc.configs);
  //   }
  //   else {
  //     var req = {
  //       url: "config/config.json",
  //       method: "GET",
  //     };
  //     $http(req).then(
  //       function(response) {
  //         console.log(response);
  //         svc.configs = response.data;
  //         success(svc.configs);
  //       },
  //       function(response) {
  //         if (error)
  //           error(response);
  //       }
  //     );
  //   }
  // };
  this.getConfigs = function() {
    var defer = $q.defer();
    if (svc.configs) {
      defer.resolve(svc.configs);
    }
    else {
      var req = {
        url: "config/config.json",
        method: "GET",
      };
      $http(req)
      .then(
        function(response) {
          svc.configs = response.data;
          defer.resolve(svc.configs);
        },
        function(response) {
          defer.reject(response);
        }
      );
    }
    return defer.promise;
  };

})
;