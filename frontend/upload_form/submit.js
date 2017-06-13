const SUBMIT_BTNS = {
  // vidfile : 'vidfile-submit-btn',
  required : 'required-submit-btn',
  optional : 'optional-submit-btn'
}

let form = document.querySelector('form');

for (let key in SUBMIT_BTNS) {
  if (SUBMIT_BTNS.hasOwnProperty(key)) {
    let id = SUBMIT_BTNS[key];
    let btn = document.querySelector(`#${id}`);
    btn.addEventListener('click', (e) => {
      console.log('btn, first.');
    });
  }
}

form.addEventListener('submit', (e) => {
  console.log('form, first.');
  e.preventDefault();
});
