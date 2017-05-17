var analyzer = angular.module('analyzer', [
  'ngRoute'
]);

analyzer.config([
  '$routeProvider',
  '$locationProvider',
  function($routeProvider, $locationProvider) {
    $routeProvider.when('/components-definition', {
      templateUrl: 'components-definition.html'
    }).when('/documents-processing', {
      templateUrl: 'documents-processing.html',
      controller: 'docCtrl'
    }).when('/basic-analysis', {
      templateUrl: 'basic-analysis.html'
    }).when('/advanced-analysis', {
      templateUrl: 'advanced-analysis.html'
    }).when('/user-guide', {
      templateUrl: 'user-guide.html'
    }).otherwise(function (injector, location) {
      // var path = location.path();
      // window.location = path;
    });

    $locationProvider.html5Mode({
      // enabled: true
    });
  }
]);

analyzer.run(function($rootScope, $location) {
  $rootScope.$on('$routeChangeStart', function(event, next, current) {
    if (current != null) {
    }
  });
});

// Controllers
analyzer.controller(
  'navbar',
  [
    '$scope',
    '$location',
    function($scope, $location) {
      $scope.isActive = function(viewLocation) {
        return viewLocation === $location.path();
      };
    }
  ]
);

analyzer.controller(
  'docCtrl',
  [
    '$scope',
    function($scope) {
      var viewer = ace.edit('document-view');
      Require('./renderer/documents-processing')
    }
  ]
)
