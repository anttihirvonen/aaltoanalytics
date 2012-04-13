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

            // Screen info
            params['swidth']    = screen.width;
            params['sheight']   = screen.height;
            // Page url – no GET-parameters here
            params['url']       = document.URL ? document.URL.split('?')[0] : "";
            params['referrer'] = document.referrer;
       
            // Construct GET-parameter string from collected values
            paramArray = []
            for(var key in params){ paramArray.push(key+'='+encodeURIComponent(params[key])); }
            getParams = paramArray.join("&")

            // Actual request
            getImage("?"+getParams);
        }

        /*
         * Keeps server informed that the user is still on the same page.
         * This is used to identify which pages are the most popular.
         *
         * This function is called every 10 seconds to update
         */
        this.bounceUpdate = function() {

        }
    }
}
