/*
 * Aalto Analytics tracking script.
 *
 * This script should be loaded in head-section of the page.
 * Call AaltoAnalytics.trackPageview() in the end of the body
 * tag to actually track a pageview.
 */

var AaltoAnalytics;

if(!this.AaltoAnalytics) {
    AaltoAnalytics = new function() {

        // Hardcoded for now, needs to be configurable
        trackerUrl = "http://127.0.0.1:8000/analytics/log/"

        /*
         * Requests the 1x1 image from the server. 
         */
        function getImage(request) {
            var image = new Image(1, 1);

            image.onload = function () {};
            image.onerror = function(e) { console.log(e); }
            image.src = trackerUrl + request;
        }
        
        function getUserId() {
            // Implement
        }

        function getVisitId() {
            // Implement
        }
        
        /*
         * Does all the heavy lifting and actual tracking of page views
         */
        this.trackPageView = function() {
            params = {}
            params['swidth'] = screen.width;
            params['sheight'] = screen.height;

            // Construct GET-parameter string from collected values
            paramArray = []
            for(var key in params){ paramArray.push(key+'='+params[key]); }
            getParams = paramArray.join("&")

            // Actual request
            getImage("?"+getParams);
        }
    }
}
