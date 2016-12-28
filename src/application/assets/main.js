var size = 12;
document.body.style.fontSize = "" + size + "pt";


function expandText() {
  size += 2;
  console.log(size);
  document.body.style.fontSize = "" + size + "pt";
}

setInterval(expandText, 1000);
