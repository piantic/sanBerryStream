const streaming = document.querySelector('.jsStreaming');
const status = document.getElementById("statusValue");
const btnStream = document.querySelector('.jsStreamBtn');
const btnGetData = document.querySelector('.jsGetDataBtn');

function startStream() {
    streaming.src = `/video_feed`;
    status.value = "Streaming";
    status.style ="color:red";
    console.log("startStream");
}

function stopStream() {
    status.value = "Ready";
    status.style ="color:black";
    streaming.src = "resources/image2.jpg";
    console.log("stop Stream");
}


function init() {
    btnStream.addEventListener("click", startStream);
    btnGetData.addEventListener("click", stopStream);

}

init();