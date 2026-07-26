var assignedWindow = document.querySelector(`#${document.currentScript.dataset.window}`);
var assignedContext = assignedWindow.querySelector("iframe").contentWindow.document


var bigRedButton = assignedContext.querySelector("#bigredbutton");

bigRedButton.addEventListener("click", () => {
    var explosionImage = document.createElement("img");
    explosionImage.style.position = "absolute";
    explosionImage.style.pointerEvents = "none";
    explosionImage.src = `pages/assets/kaboom.gif?${Math.random()}`; // relative to index, randomized link forces loading multiple
    explosionImage.style.top = `${Math.floor(Math.random() * window.innerHeight)}px`;
    explosionImage.style.left = `${Math.floor(Math.random() * window.innerWidth)}px`;
    document.body.insertAdjacentElement("beforeend", explosionImage);
    setTimeout(() => {
        explosionImage.remove();
    }, 1360)
})