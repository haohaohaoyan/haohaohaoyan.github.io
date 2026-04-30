// stuff

const windowTemplate = document.querySelector("#window-template")
const taskbarItemTemplate = document.querySelector("#taskbar-item-template")
const fullscreenContainer = document.querySelector("#fullscreen-container")
const taskbar = document.querySelector("#taskbar")
const rightClickMenu = document.querySelector("#rightclickmenu")
var windowList = []

const clamp = (num, min, max) => Math.min(Math.max(num, min), max) // i miss gdscript

async function createWindow(link, atCursor = false, posX = null, posY = null, width = "400px", height = "300px") { // make a window (iframes and embeds and such for content, cors tries to kill me every now and then but it's ok)
    let newWindow = document.body.appendChild(windowTemplate.content.cloneNode(true).firstElementChild);
    // setup 
    addDrag(newWindow);
    if (atCursor) { // atCursor is a mouse event if true bc js kinda sucks
        newWindow.style.left = `${atCursor.clientX}px`, newWindow.style.top = `${atCursor.clientY}px`;
    } else if (posX && posY) {
        newWindow.style.left = posX, newWindow.style.top = posY;
    };
    newWindow.style.width = width || "400px", newWindow.style.height = height || "300px";
    newWindow.style.animation = "0.3s ease-out open-window";
    // add content
    let content = newWindow.appendChild(document.createElement("iframe"));
    content.style.overflow = "hidden";
    content.scrolling = "yes"; 
    content.src = link;
    await new Promise((resolve, reject) => {
        content.addEventListener("load", function() {
            try {
                resolve();
            } catch (e) {
                console.log("god damn it")
                reject();
            };
        });
    });
    // Attach proper open window things to buttons that need it (could have been a global script but this is fineeee)
    content.contentWindow.document.querySelectorAll(".openwindow").forEach((windowOpener) => {
        windowOpener.onclick = () => {
            event.preventDefault();
            createWindow(windowOpener.dataset.windowpath);
        }; 
    });

    while (windowList.includes(newWindow.id)) {
        newWindow.id = String(Math.floor(Math.random() * 1000)).padStart(3, "0");
    };
    windowList.push(newWindow.id);

    // header bar funcs
    let windowHeader = newWindow.querySelector(".headerbar");
    try {
        windowHeader.querySelector("p").innerText = content.contentWindow.document.querySelector('title').innerText
    } catch (SecurityError) {
        windowHeader.querySelector("p").innerText = link;
    };
    windowHeader.querySelector("p").title = link;
    windowHeader.querySelector(".close").onclick = closeWindow;
    windowHeader.querySelector(".toggle-window").onclick = toggleWindow;

    function closeWindow(event) {
        newWindow.style.animation = "0.3s ease-out close-window";
        newWindow.style.pointerEvents = "none";
        newWindow.addEventListener("animationend", function() {
            taskbar.querySelector(`[data-window="${newWindow.id}"]`).remove();
            newWindow.remove();
        });
    };

    function toggleWindow(event) {
        if (!newWindow.className.includes("fullscreen")) {
            newWindow.className += " fullscreen";
            newWindow.style.top = 0; newWindow.style.left = 0;
        } else {
            newWindow.className = newWindow.className.replace(" fullscreen", '');
        };
    };

    // enable stretching 

    addStretch(newWindow.querySelector(".stretch-horizontal"), "X");
    addStretch(newWindow.querySelector(".stretch-vertical"), "Y");

    // create linked taskbar item

    var newTaskbarItem = taskbar.appendChild(taskbarItemTemplate.content.cloneNode(true).firstElementChild);
    newTaskbarItem.dataset.window = newWindow.id;
    newTaskbarItem.innerText = windowHeader.querySelector("p").innerText;

    return newWindow;
};

function addDrag(element) { // based on the w3 example AGAIN bc i'm a dumbass
    var locX, locY, changeX, changeY;
    element.querySelector(".headerbar").onmousedown = startDrag;

    function startDrag(event) {
        event.preventDefault();
        if (event.target.nodeName != "BUTTON") {
            document.onmousemove = drag, document.onmouseup = endDrag;
            document.querySelectorAll('iframe').forEach((element) => element.style.pointerEvents = "none");
            locX = event.clientX, locY = event.clientY;
            element.querySelector(".headerbar").style.cursor = "grabbing";
            if (element.className.includes("fullscreen")) {
                element.className = element.className.replace(" fullscreen", '');
                element.style.left = `${event.clientX}px`, element.style.top = `${event.clientY, 0}px`;
                document.body.appendChild(element);
            };
        };
    };

    function drag(event) {
        event.preventDefault();
        changeX = locX - event.clientX, changeY = locY - event.clientY, locX = event.clientX, locY = event.clientY;
        element.style.left = `${Math.max(element.offsetLeft - changeX, 0)}px`, element.style.top = `${Math.max(element.offsetTop - changeY, 0)}px`;
    };

    function endDrag() {
        document.onmousemove = null, document.onmouseup = null, element.querySelector(".headerbar").style.cursor = "grab";
        document.querySelectorAll('iframe').forEach((element) => element.style.pointerEvents = "all");
    };

};

function addStretch(element, axis) { // practically the same as above. pretty unreadable too but it's the exact same logic as above
    var n, changeN;
    element.onmousedown = function(event) {
        event.preventDefault();
        n = event[`client` + axis];
       document.querySelectorAll('iframe').forEach((element) => element.style.pointerEvents = "none");
        document.onmousemove = function(event) {
            event.preventDefault();
            changeN = n - event['client' + axis], n = event['client' + axis];
            element.parentNode.style[{"X": "width", "Y": "height"}[axis]] = `${Math.max(Number(element.parentNode.style[{"X": "width", "Y": "height"}[axis]].replace('px', '')) - changeN, 300)}px`;
        };
        document.onmouseup = function() {
            document.onmousemove = null, document.onmouseup = null;
            document.querySelectorAll('iframe').forEach((element) => element.style.pointerEvents = "all");
        };
    };

};

function openMenu(event) {
    rightClickMenu.style.display = 'flex';
    rightClickMenu.style.left = `${event.clientX}px`, rightClickMenu.style.top = `${event.clientY}px`;
    document.onclick = function(event) {
        if (event.target.parentNode.id != "rightclickmenu") {
            rightClickMenu.style.display = 'none';
        };
    };
};

document.oncontextmenu = function(event) {
    event.preventDefault();
    openMenu(event);
};

rightClickMenu.querySelector('#rightclickmenu-openfile').onclick = async function(event) {
    let fileWindow = await createWindow("pages/openfile.html", event);
    fileWindow.querySelector('iframe').contentWindow.document.querySelector('#runbutton').onclick = function(event) {
        const path = fileWindow.querySelector('iframe').contentWindow.document.querySelector('#filepathinput').value || "pages/start.html";
        createWindow(path, event);
        taskbar.querySelector(`[data-window="${fileWindow.id}"]`).remove();
        fileWindow.remove();
    };
    rightClickMenu.style.display = "none";
};

createWindow("pages/start.html", false, "calc(50vw - 400px)", "calc(50vh - 300px)", "800px", "600px");

document.querySelector("#open-start-page-button").onclick = () => createWindow("pages/start.html");

function setTime() {
    let now = new Date;
    document.querySelector("#clock").innerText = `${now.getHours() % 12}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2,'0')} ${["AM", "PM"][Math.floor(now.getHours() / 12)]}`;
};

setInterval(setTime, 1000);

if (window.innerWidth <= 800) {
    alert("The whole webOS thing works pretty badly on small or thin screens. The website will be opened in page mode instead.");
    location.href = "pages/start.html";
}
