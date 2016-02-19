"use strict";

angular.module("teamworkConsole",
               [
                "ngRoute",
                "pascalprecht.translate",
                "ui.bootstrap",
               ])
.config(function($routeProvider, $locationProvider) {
  $routeProvider
  .when("/entrance", {
    templateUrl: "view/partial/entrance.html",
    controller: "entrance",
  })
  .when("/", {
    redirectTo: "/entrance",
  });
});