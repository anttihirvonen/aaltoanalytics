/*
 * Aalto Analytics tracking script.
 *
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
        
        this.trackPageView = function() {
            /*
             * Does all the heavy lifting and actual tracking of page views
             */
            var width = screen.width;
            var height = screen.height;

            getImage("?swidth="+width+"&sheight="+height);
        }
    }
}
