// Under the MIT license. See LICENSE file at project root for info.

function theme() {
    if (document.getElementById("style").getAttribute("href") == "styles/default.css") {
        document.getElementById("style").setAttribute("href", "styles/light.css"); 
        document.getElementById("logo").setAttribute("src", "assets/logolight.svg"); 
        document.getElementById("ts").setAttribute("src", "assets/light.svg"); 
    } else if (document.getElementById("style").getAttribute("href") == "styles/light.css") {
        document.getElementById("style").setAttribute("href", "styles/none.css"); 
        document.getElementById("logo").setAttribute("src", "assets/logolight.svg"); 
        document.getElementById("ts").setAttribute("src", "assets/none.svg"); 
    } else {
        document.getElementById("style").setAttribute("href", "styles/default.css"); 
        document.getElementById("logo").setAttribute("src", "assets/logo.svg"); 
        document.getElementById("ts").setAttribute("src", "assets/dark.svg"); 
    }
}