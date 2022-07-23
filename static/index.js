iconcode = document.getElementById("icon").innerHTML;
icon_url = "http://openweathermap.org/img/wn/" + iconcode + "@2x.png";
document.getElementById("image").setAttribute("src", icon_url);