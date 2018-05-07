// Karma configuration

module.exports = function(config) {
    config.set({

        // base path, that will be used to resolve files and exclude
        basePath: '/home/web/django_project/',

        // frameworks to use
        frameworks: ['jasmine', 'requirejs'],
        //
        plugins: [
            require('karma-jasmine'),
            require('karma-chrome-launcher'),
            require('karma-requirejs'),
        ],

        // list of files / patterns to load in the browser
        files: [
            'bims/static/test-main.js',
            {pattern: 'bims/static/js/libs/jquery/*', included: false},
            {pattern: 'bims/static/js/libs/bootstrap-4.0.0/js/*.js', included: false},
            {pattern: 'bims/static/js/libs/openlayers-4.6.4/*.js', included: false},
            {pattern: 'bims/static/js/libs/requirejs-2.3.5/*.js', included: false},
            {pattern: 'bims/static/js/libs/underscore-1.8.3/*', included: false},
            {pattern: 'bims/static/js/libs/backbone-1.3.3/*.js', included: false},
            {pattern: 'bims/static/js/libs/jquery-ui-1.12.1/*.js', included: false},
            {pattern: 'bims/static/js/collections/*.js', included: false},
            {pattern: 'bims/static/js/forms/*.js', included: false},
            {pattern: 'bims/static/js/models/*.js', included: false},
            {pattern: 'bims/static/js/views/*.js', included: false},
            {pattern: 'bims/static/tests/*Spec.js', included: false}
        ],

        // list of files to exclude
        exclude: [
            'bims/static/js/app.js',
            'bims/static/js/views/donut-chart.js',
            'bims/static/js/views/generate-donut-chart.js'
        ],

        // test results reporter to use
        // possible values: 'dots', 'progress', 'junit', 'growl', 'coverage'
        reporters: ['progress'],

        // web server port
        port: 9876,

        // enable / disable colors in the output (reporters and logs)
        colors: true,

        // level of logging
        // possible values: config.LOG_DISABLE || config.LOG_ERROR || config.LOG_WARN || config.LOG_INFO || config.LOG_DEBUG
        logLevel: config.LOG_INFO,

        // enable / disable watching file and executing tests whenever any file changes
        autoWatch: true,

        // Start these browsers, currently available:
        // - Chrome
        // - ChromeCanary
        // - Firefox
        // - Opera
        // - Safari (only Mac)
        // - PhantomJS
        // - IE (only Windows)
        browsers: ['ChromeNoSandboxHeadless'],
        customLaunchers: {
            ChromeNoSandboxHeadless: {
                base: 'Chromium',
                flags: [
                    '--no-sandbox',
                    // See https://chromium.googlesource.com/chromium/src/+/lkgr/headless/README.md
                    '--headless',
                    '--disable-gpu',
                    // Without a remote debugging port, Google Chrome exits immediately.
                    ' --remote-debugging-port=9222'
                ]
            }
        },

        // If browser does not capture in given timeout [ms], kill it
        captureTimeout: 60000,

        // Continuous Integration mode
        // if true, it capture browsers, run tests and exit
        singleRun: false
    });
};