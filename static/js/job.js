var MyApp = angular.module('Myapp', []).controller("HelloController", [function () {
    var ctrl = this;
    ctrl.name = "vikas";
    ctrl.toggle = false
    ctrl.clicked = function () {
        console.log(ctrl.toggle);
        ctrl.toggle = !ctrl.toggle;
    }
}]);
MyApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});