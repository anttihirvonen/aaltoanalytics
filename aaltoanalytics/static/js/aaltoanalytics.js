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
        trackerUrl = "http://127.0.0.1:8000/analytics/log/";

        this.trackingId = "";

        this.setTrackingId = function(id) {
            this.trackingId = id;
        }

        /*
         * Makes the JSONP request to server.
         */
        function getJSONP(request) {
            /*var image = new Image(1, 1);

            image.onload = function () {};
            image.onerror = function(e) { console.log(e); }
            image.src = trackerUrl + request;*/
            var head = document.getElementsByTagName('head')[0];
            var script = document.createElement('script');
            script.type = 'text/javascript';
            script.src = trackerUrl + request;
            head.appendChild(script);
        }
        
        this.setPageviewId = function(id) {
            this.pageviewId = id;
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
        this.getUserId = function() {
            this.uniqueUserId = readCookie('uid');

            if(!this.uniqueUserId)
                this.uniqueUserId = generateUid();

            // Set the user cookie or extend it's lifetime
            setCookie('uid', this.uniqueUserId, 365);

            return this.uniqueUserId;
        }

        function getVisitId() {
            // Implement
        }
        
        /*
         * Does all the heavy lifting and actual tracking of page views
         */
        this.trackPageView = function() {
            if(!this.trackingId)
                return;

            params = {}

            params['tid']       = this.trackingId;
            // Screen info
            params['screen_width']    = screen.width;
            params['screen_height']   = screen.height;
            // Page url – no GET-parameters here
            params['url']       = document.URL ? document.URL.split('?')[0] : "";
            params['title']     = document.title;
            params['referrer']  = document.referrer;
            params['uid']       = this.getUserId();

            // Construct GET-parameter string from collected values
            paramArray = []
            for(var key in params){ paramArray.push(key+'='+encodeURIComponent(params[key])); }
            getParams = paramArray.join("&")
            // Actual request
            getJSONP("?"+getParams);

            // Circumventing the problems with objects and setInverval
            var selfobj = this;
            setInterval(function() { selfobj.lastActiveTimestampUpdate(); }, 10000);
        }

        /*
         * Keeps server informed that the user is still on the same page.
         * This is used to identify which pages are the most popular.
         *
         * This function is called every 10 seconds to update the visit's last read timestamp.
         */
        this.lastActiveTimestampUpdate = function() {
            if(this.pageviewId)
                // Append a random parameter to prevent caching
                getJSONP("updatetime/"+this.pageviewId+"/?random=" + generateUid());
        }
    }
}
