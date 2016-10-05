var MyApp = angular.module('Myapp', []).controller("HelloController", [function(){
    var ctrl = this;
    ctrl.name = "vikas";
    ctrl.clicked = function() {
        console.log(ctrl.toggle);
        ctrl.toggle = !ctrl.toggle;
    }
    }]);3
    MyApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});