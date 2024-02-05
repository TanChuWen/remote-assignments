function ajax(src, callback){
    // your code here
    let xhr = new XMLHttpRequest(); //define an XMLHttpRequest (XHR) variable -> build an XHR object to get data from remote
    xhr.onreadystatechange = function() { // step 3
        if (xhr.readyState === 4 && xhr.status === 200) {
            // if it succeeds, call the callback function and give back the data
            callback(xhr.responseText); // step 4
        }
    };
    xhr.open("GET", src, true); //step 2
    xhr.send(); //
}

function render(data) { //step 6
    // define a new div element
    let divElement = document.createElement("div");
    // put the data into the div element
    divElement.innerHTML = data; //data is the response that rendered
    // put the div element into the div and web page
    document.body.appendChild(divElement);
}

ajax("https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products", function(response) { // step 1
// call the callback function-render and show the data on the browser
    render(response); // step 5
});


