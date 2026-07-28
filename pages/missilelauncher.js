var assignedWindow = document.querySelector(`#${document.currentScript.dataset.window}`);
var assignedContext = assignedWindow.querySelector("iframe").contentWindow.document;

var bigRedButton = assignedContext.querySelector("canvas");

bigRedButton.addEventListener("click", () => {
    // create explosion image and set things
    var explosionImage = document.createElement("div");
    explosionImage.style.width = "424px"; // rounded
    explosionImage.style.height = "408px";
    explosionImage.style.position = "absolute";
    explosionImage.style.pointerEvents = "none";
    explosionImage.style.zIndex = "999";
    explosionImage.style.imageRendering = "pixelated";
    explosionImage.style.backgroundImage = "url('pages/assets/kaboom-sprites.png')"; // relative to index
    explosionImage.style.backgroundPositionX = "6840px";
    explosionImage.style.backgroundSize = "6840px";
    explosionImage.style.top = `${Math.floor(Math.random() * (window.innerHeight - 408))}px`;
    explosionImage.style.left = `${Math.floor(Math.random() * (window.innerWidth - 424))}px`;
    document.body.insertAdjacentElement("beforeend", explosionImage);
    var explosionFrame = 0;
    setInterval(() => {
        if (explosionFrame == 16) {
            explosionImage.remove();
        };
        explosionImage.style.backgroundPositionX = `${6840 - explosionFrame * 424}px`;
        explosionFrame += 1;
    }, 80)
})