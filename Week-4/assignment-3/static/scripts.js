// from our index.html, it will connect to this javascript file to start these two functions
function signup() {
    let xhttp = new XMLHttpRequest();
    // xhttp.onreadystatechange = function() {
    //   if (this.readyState == 4 && this.status == 200) {
    //       //document.getElementById("demo").innerHTML = 
    //       //    this.responseText;
    //   }
    // };
    xhttp.open('POST', '/signup');
    xhttp.setRequestHeader('Content-Type',  'application/x-www-form-urlencoded');
    xhttp.send('email=' + document.querySelector("#emailInput").value + '&password=' + document.querySelector("#passwordInput").value); 
  }
  
  
  function login() {
      let xhttp = new XMLHttpRequest();
      // xhttp.onreadystatechange = function() {
      //   if (this.readyState == 4 && this.status == 200) {
      //     // document.getElementById("result").innerHTML = 
      //     //     this.responseText;
      //   }
      // };
      xhttp.open('POST', '/login');
      xhttp.setRequestHeader('Content-Type',  'application/x-www-form-urlencoded');
      xhttp.send('email=' + document.querySelector("#emailInput").value + '&password=' + document.querySelector("#passwordInput").value); 
  }

   