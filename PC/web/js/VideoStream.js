document.addEventListener("DOMContentLoaded", function() {
    var url = "http://192.168.3.1:8080/stream/webrtc"; 
    var iframe = document.getElementById("videoStream");
    iframe.src = url;
});