﻿"use strict";

angular.module("teamworkConsole",
               [
                "ngRoute",
                "pascalprecht.translate",
                "ui.bootstrap",
               ])
.config(function($routeProvider, $locationProvider) {
  $routeProvider
  .when("/entrance", {
    templateUrl: "view/pages/entrance.html",
    controller: "entrance",
  })
  .when("/login", {
    templateUrl: "view/pages/login.html",
    controller: "login",
  })
  .when("/", {
    redirectTo: "/entrance",
  });
});