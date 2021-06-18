var elements = document.getElementsByClassName("sidebar");

for (e in elements) {
  if (elements[e].innerHTML == "") {
    elements[e].innerHTML = "→ Announcements";
    break;
  }
}
