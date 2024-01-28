// Assignment 3-3 get http://localhost:3000/data?number=10 的值55
function showResult() {
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML = 
            this.responseText;
    }
  };
  xhttp.open("GET", "http://localhost:3000/data?number=10", true);
  xhttp.send();
}

// Assignment 3-4 http://localhost:3000/updatedURL 
function calculateSum() {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("result").innerHTML = 
            this.responseText;
      }
    };
    updatedURL= "http://localhost:3000/data?number="+document.getElementById('numberInput').value
    xhttp.open("GET", updatedURL, true);
    xhttp.send();
  }


