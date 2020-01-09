streaming = document.getElementsByClassName('.jsStreaming');
status = document.getElementById('statusValue');
btnStream = document.getElementsByClassName('jsStreamBtn');
btnGetData = document.getElementsByClassName('jsGetDataBtn');

function startStream() {
    // fetch(
    //     `/video_feed`
    // ).then(function(response){
    //     console.log(response);
    //     return response.json();
    // }).then(function(numRecords){
    //     console.log(numRecords);
    //     setNextPageNumberForImage(numRecords, n);
    // });
    streaming.src = `/video_feed`;

}

function nextPage(n) {

}

function init() {
    btnStream.addEventListener("click", startStream);
}

init();