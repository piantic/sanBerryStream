const streaming = document.querySelector('.jsStreaming');
let status = document.querySelector('.jsStatusValue');
const btnStream = document.querySelector('.jsStreamBtn');
const btnStop = document.querySelector('.jsStopBtn');
const btnGetData = document.querySelector('.jsGetDataBtn');


function setStreamBtn(isClick) {
    btnStream.disabled = isClick;
    btnStop.disabled = !isClick;
}

function startStream() {
    streaming.src = `/video_feed`;
    setStreamBtn(true);
}

function getData() {
    console.log("getData");
    const query = '{ sanBerryStatus(name: "San") }';
    fetch(
        `/graphql?query=${query}`
    ).then(function(response){
        console.log(response);
        return response.json();
    }).then(function(result){
        console.log(result);
        status.value = result.data["sanBerryStatus"];
    });
}

function stopStream() {
    streaming.src = "/resources/dummy.jpg";
    setStreamBtn(false);
}

function init() {
    streaming.src = "/resources/dummy.jpg";
    setStreamBtn(false);

    btnStream.addEventListener("click", startStream);
    btnStop.addEventListener("click", stopStream);
    btnGetData.addEventListener("click", getData);
}

init();