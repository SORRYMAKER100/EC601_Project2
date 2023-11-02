window.onload = function() {
    var studentid = JSON.parse(localStorage.getItem('a'))
    document.getElementById('demo').innerHTML = studentid

    var student = JSON.parse(localStorage.getItem('b'))
    document.getElementById('demo2').innerHTML = student


}
