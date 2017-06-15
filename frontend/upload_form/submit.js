import { requiredInputUpload, optionalInputUpload } from './api_util';

const SUBMIT_BTNS = [
  // vidfile : 'vidfile-submit-btn',
  'required',
  'optional'
]

let inputType = null;
let form = document.querySelector('form');

SUBMIT_BTNS.forEach(key => {
  let id = `${key}-submit-btn`;
  let btn = document.querySelector(`#${id}`);
  btn.addEventListener('click', (e) => {
    inputType = key;
  });
});

form.addEventListener('submit', (e) => {
  e.preventDefault();
  if (inputType === 'required') {
    requiredInputUpload(form, (req) => {
      console.log("REQUIRED DATA UPLOADED");
    });
  } else if (inputType === 'optional'){
    optionalInputUpload(form, (req) => {
      console.log("OPTIONAL DATA UPLOADED");
      window.location.href = `${window.location.origin}?thankyou=1`;
    });
  }
});
