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

        /*
         * Returns unique identifier of length 8.
         *
         */
        function generateUid()
        {
            var text = "";
            var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

            for( var i=0; i < 8; i++ )
                text += possible.charAt(Math.floor(Math.random() * possible.length));

            return text;
        }
        
        /*
         * Sets cookie name=value that expires is given number of days.
         */
        function setCookie(name, value, days) {
            if (days) {
                var date = new Date();
                date.setTime(date.getTime() + (days*24*60*60*1000));
                var expires = "; expires=" + date.toGMTString();
            }
            else var expires = "";
            document.cookie = name + "=" + value + expires + "; path=/";
        }
        
        /*
         * Reads value associated with given name from cookie.
         */
        function readCookie(name) {
            var nameEQ = name + "=";
            var ca = document.cookie.split(';');

            for(var i = 0; i < ca.length; i++) {
                var c = ca[i];
                while (c.charAt(0 )== ' ') c = c.substring(1, c.length);
                if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
            }
            return null;
        }
        
        /*
         * Returns unique id of the user.
         *
         * If no such id is found, we try to create one and save
         * it into cookie for later use.
         */
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
            document.cookie = "test=kis";
            document.cookie = "val=fd";
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
