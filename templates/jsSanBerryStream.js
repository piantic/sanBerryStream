streaming = document.querySelector('.jsStreaming');
//status = document.getElementById('statusValue');
btnStream = document.querySelector('.jsStreamBtn');
btnGetData = document.querySelector('.jsGetDataBtn');

function startStream() {
    streaming.src = `/video_feed`;
    console.log("startStream");
}

function stopStream() {
    streaming.src = "resources/image2.jpg";
    console.log("stop Stream");
}


function init() {
    btnStream.addEventListener("click", startStream);
    btnGetData.addEventListener("click", stopStream);
}

init();