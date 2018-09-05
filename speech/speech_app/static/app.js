var recognizeMic = require('watson-speech/speech-to-text/recognize-microphone');

window.onload = () =>{
var start= document.getElementById("start");
start.onclick = onListenClick;
};

function onListenClick(){
    fetch('/api/speech-to-text/token')
    .then(function(response) {
        return response.text();
    }).then( (token) => {
      var stream = recognizeMic({
          token: token,
          objectMode: true,
          extractResults: true,
          format: false
      });
      stream.on('data', (data) => {
        console.log(data);
        document.getElementById("ans").innerHTML = data.alternatives[0].transcript;
      });
      stream.on('error', function(err) {
          console.log(err);
      });
      document.querySelector('#stop').onclick = stream.stop.bind(stream);
    }).catch(function(error) {
        console.log(error);
    });
  }

