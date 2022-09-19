var video3 = document.querySelector("#videoConference");
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ audio: true, video: true })
        .then(function(stream) {
            video1.srcObject = stream;
        })
        .catch(function(err0r) {
            console.log("Something went wrong!");
        });
}


var video1 = document.querySelector("#videoElement1");
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ audio: true, video: true })
        .then(function(stream) {
            video1.srcObject = stream;
        })
        .catch(function(err0r) {
            console.log("Something went wrong!");
        });
}
var video2 = document.querySelector("#videoElement2");
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ audio: true, video: { width: 950, height: 960 } })
        .then(function(stream) {
            video2.srcObject = stream;
        })
        .catch(function(err0r) {
            console.log("Something went wrong!");
        });
}
/*var video3 = document.querySelector("#videoElement3");
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ audio: true, video: { width: 950, height: 720 } })
        .then(function(stream) {
            video3.srcObject = stream;
        })
        .catch(function(err0r) {
            console.log("Something went wrong!");
        });
}
var video4 = document.querySelector("#videoElement4");
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ audio: true, video: { width: 950, height: 720 } })
        .then(function(stream) {
            video4.srcObject = stream;
        })
        .catch(function(err0r) {
            console.log("Something went wrong!");
        });
}
var video5 = document.querySelector("#videoElement5");
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ audio: true, video: { width: 950, height: 720 } })
        .then(function(stream) {
            video5.srcObject = stream;
        })
        .catch(function(err0r) {
            console.log("Something went wrong!");
        });
}
var video6 = document.querySelector("#videoElement6");
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ audio: true, video: { width: 950, height: 720 } })
        .then(function(stream) {
            video6.srcObject = stream;
        })
        .catch(function(err0r) {
            console.log("Something went wrong!");
        });
}*/

/*
function toggleFullScreen1() {
  if (!document.fullscreenElement) {

    var elem1 = document.getElementById("videoElement1");
    if (elem1.requestFullscreen) {
      elem1.requestFullscreen();
    } else if (elem1.mozRequestFullScreen) {
      elem1.mozRequestFullScreen();
    } else if (elem1.webkitRequestFullscreen) {
      elem1.webkitRequestFullscreen();
    } else if (elem1.msRequestFullscreen) {
      elem1.msRequestFullscreen();
    }

  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}
function toggleFullScreen2() {
  if (!document.fullscreenElement) {

    var elem2 = document.getElementById("videoElement2");
    if (elem2.requestFullscreen) {
      elem2.requestFullscreen();
    } else if (elem2.mozRequestFullScreen) {
      elem2.mozRequestFullScreen();
    } else if (elem2.webkitRequestFullscreen) {
      elem2.webkitRequestFullscreen();
    } else if (elem2.msRequestFullscreen) {
      elem2.msRequestFullscreen();
    }    

  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}
function toggleFullScreen3() {
  if (!document.fullscreenElement) {

    var elem3 = document.getElementById("videoElement3");
    if (elem3.requestFullscreen) {
      elem3.requestFullscreen();
    } else if (elem3.mozRequestFullScreen) {
      elem3.mozRequestFullScreen();
    } else if (elem3.webkitRequestFullscreen) {
      elem3.webkitRequestFullscreen();
    } else if (elem3.msRequestFullscreen) {
      elem3.msRequestFullscreen();
    }    

  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}
function toggleFullScreen4() {
  if (!document.fullscreenElement) {

    var elem4 = document.getElementById("videoElement4");
    if (elem4.requestFullscreen) {
      elem4.requestFullscreen();
    } else if (elem4.mozRequestFullScreen) {
      elem4.mozRequestFullScreen();
    } else if (elem4.webkitRequestFullscreen) {
      elem4.webkitRequestFullscreen();
    } else if (elem4.msRequestFullscreen) {
      elem4.msRequestFullscreen();
    }    

  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}
function toggleFullScreen5() {
  if (!document.fullscreenElement) {

    var elem5 = document.getElementById("videoElement5");
    if (elem5.requestFullscreen) {
      elem5.requestFullscreen();
    } else if (elem5.mozRequestFullScreen) {
      elem5.mozRequestFullScreen();
    } else if (elem5.webkitRequestFullscreen) {
      elem5.webkitRequestFullscreen();
    } else if (elem5.msRequestFullscreen) {
      elem5.msRequestFullscreen();
    }    

  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}
function toggleFullScreen6() {
  if (!document.fullscreenElement) {

    var elem6 = document.getElementById("videoElement6");
    if (elem6.requestFullscreen) {
      elem6.requestFullscreen();
    } else if (elem6.mozRequestFullScreen) {
      elem6.mozRequestFullScreen();
    } else if (elem6.webkitRequestFullscreen) {
      elem6.webkitRequestFullscreen();
    } else if (elem6.msRequestFullscreen) {
      elem6.msRequestFullscreen();
    }    

  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}

document.addEventListener("keydown", function(e) {
  if (e.keyCode == 13) {
    console.log('enter')
    toggleFullScreen();
  }
}, false);     */