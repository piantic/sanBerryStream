streaming = document.querySelector('.jsStreaming');
status = document.querySelector('.jsStatusValue');
btnStream = document.querySelector('.jsStreamBtn');
btnGetData = document.querySelector('.jsGetDataBtn');

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