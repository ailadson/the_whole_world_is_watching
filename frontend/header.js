let uploadBtn = document.getElementById('header-upload');
uploadBtn.addEventListener('click', e => {
  console.log("clicked");
  location.href = `${location.href}upload`;
});
