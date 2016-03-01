/**
 * http://usejsdoc.org/
 */
"use strict";
require("angular");
require("angular-route");
require("angular-translate");
require("angular-ui-bootstrap");

var app = angular.module("teamworkWeb",
                         [
                            "ngRoute",
                            "pascalprecht.translate",
                            "ui.bootstrap",
                         ]);

app
.service('ConfigService', require("../m/service/configure"))
.service('UserService', require("../m/service/userservice"))
.controller('entrance', require("./pages/entrance"))
.controller("login", require("./pages/login"))
/* forms */
.controller("loginForm", require("./forms/login"))
;

app.config(function($routeProvider, $locationProvider) {
    $routeProvider
    .when("/entrance", 
          {
            controller: "entrance",
            template: require("../v/pages/entrance.html"),
          })
    .when("/login",
          {
            controller: "login",
            templateUrl: "view/pages/login.html",
          })
    .when("/",
          {
            redirectTo: "/entrance",
          })
    ;
})
;

module.exports = app;