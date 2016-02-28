"use strict";

require("angular");
require("angular-route");

var app = angular.module("teamworkConsole",
                         [
                            "ngRoute",
                         ]);
app
.service('ConfigService', require("./service/configure"))
.service('UserService', require("./service/userservice"))
.controller('entrance', require("./pages/entrance.js"))
;

app.config(function($routeProvider, $locationProvider) {
    $routeProvider
    .when("/entrance", 
          {
            controller: "entrance",
            template: require("../v/pages/entrance.html"),
          })
    .when("/",
          {
            redirectTo: "/entrance",
          })
    ;
})
;

module.exports = app;