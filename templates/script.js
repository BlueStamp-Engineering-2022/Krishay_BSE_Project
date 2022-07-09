let isOn = true;

function turnOff() {
    console.log("off");
    const popup = document.getElementById("turnOffPopup");
    popup.classList.toggle("show");
    setTimeout(() => {
        popup.classList.toggle("show");
    }, 2000);
    // TODO: Stop python script

    // Overwrite powerData.txt with "off"
    writeToFile("off");

    // Read and print powerData.txt
    readFile();
}

function turnOn() {
    console.log("on");
    const popup = document.getElementById("turnOnPopup");
    popup.classList.toggle("show");
    setTimeout(() => {
        popup.classList.toggle("show");
    }, 2000);
    // TODO: Start python script

    // Overwrite powerData.txt with "on'
    writeToFile("on");

    // Read and print powerData.txt
    readFile();
}

function writeToFile(text) {

}

function readFile() {
    fetch('powerData.txt')
        .then(response => response.text())
        .then(text => console.log(`File content: ${text}`))
}