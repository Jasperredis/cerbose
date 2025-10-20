// Under the MIT license. See LICENSE file at project root for info.

function theme() {
    if (document.getElementById("style").getAttribute("href") == "styles/default.css") {
        document.getElementById("style").setAttribute("href", "styles/light.css"); 
        document.getElementById("logo").setAttribute("src", "assets/logodocslight.svg"); 
        document.getElementById("ts").setAttribute("src", "assets/light.svg"); 
    } else if (document.getElementById("style").getAttribute("href") == "styles/light.css") {
        document.getElementById("style").setAttribute("href", "styles/none.css"); 
        document.getElementById("logo").setAttribute("src", "assets/logodocslight.svg"); 
        document.getElementById("ts").setAttribute("src", "assets/none.svg"); 
    } else {
        document.getElementById("style").setAttribute("href", "styles/default.css"); 
        document.getElementById("logo").setAttribute("src", "assets/logodocs.svg"); 
        document.getElementById("ts").setAttribute("src", "assets/dark.svg"); 
    }
}

function dash2slash(fromm, str) {
    let spl = str.split(fromm)
    if (fromm == "-") {
        return spl.join("/")
    }
    else {
        return spl.join("-")
    }
}

function loadu(ite) {
    console.log("aaa");
    let url = "https://raw.githubusercontent.com/Jasperredis/cerbose/refs/heads/main/" + ite;
    fetch(url)
    .then(res => {
        if (!res.ok) {
        alert("Could not fetch docs. Try again later.");
        throw new Error("Failed to fetch docs");
        }
        return res.text();
    })
    .then(md => {
        document.getElementById("content").innerHTML = marked.parse(md);
        document.getElementById("copylink").innerHTML = `LINK: https://jasperredis.github.io/cerbose/docs.html?page=${dash2slash("/", ite)}`
    })
    .catch(err => {
        document.getElementById("content").innerHTML = `<p>Error loading docs: ${err.message}</p>`;
    });
}

// Load provided page
const urlParams = new URLSearchParams(window.location.search);
const page = urlParams.get('page');
const pages = [
    "docs-1.md", 
    "docs-2.md", 
    "docs-3.md", 
    "docs-4.md", 
    "docs-internal_subsitute.md", 
    "docs-cprint.md", 
    "docs-cerbar.md", 
    "docs-cin.md", 
    "docs-config.md", 
    "docs-issues.md", 
    "CONTRIBUTING.md", 
    "docs-8-12.md"
];
if (pages.includes(page)) {
    loadu(dash2slash("-", page));
}
