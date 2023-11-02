//设置cookie
function setCookie(name, value, seconds) {
  seconds = seconds || 0;   //seconds有值就直接赋值，没有为0
  var expires = "";
  if (seconds != 0) {      //设置cookie生存时间
    var date = new Date();
    date.setTime(date.getTime() + (seconds * 1000));
    expires = "; expires=" + date.toGMTString();
  }
  document.cookie = name + "=" + escape(value) + expires + "; path=/";   //转码并赋值
}
function setInof(key, value) {
  localStorage.setItem(key, value);
  setCookie(key,value)//存储localStorage的同时，也存储一个cookie来监听
}
  //取得cookie
  function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';'); //把cookie分割成组
    for (var i = 0; i < ca.length; i++) {
      var c = ca[i]; //取得字符串
      while (c.charAt(0) == ' ') { //判断一下字符串有没有前导空格
        c = c.substring(1, c.length); //有的话，从第二位开始取
      }
      if (c.indexOf(nameEQ) == 0) { //如果含有我们要的name
        return unescape(c.substring(nameEQ.length, c.length)); //解码并截取我们要值
      }
    }
    return false;
  }
 if(!getCookie('Token')){
   //清除
    localStorage.setItem('a','log in');
  }
