export function requiredInputUpload(form, cb){
  formInputUpload(form, 'required', cb);
}

export function optionalInputUpload(form, cb){
  formInputUpload(form, 'optional', cb);
}

export function vidfileInputUpload(){
  let name = PBVD.file_upload_endpoint.url.split('/')[5].split('.')[0];
  inputUpload('vidfile', `incident[cloud_id]=${name}`, cb);
}

function formInputUpload(form, type, cb){
  let formData = new FormData(form);
  // let formObj = {};
  // for(var key of formData.keys()) {
  //   let values = formData.getAll(key);
  //   values.forEach((val, i) => {
  //     formObj[key+i] = val;
  //   });
  // }
  inputUpload(type, formData, cb);
}

function inputUpload(type, data, cb) {
  let oReq = new XMLHttpRequest();
  oReq.addEventListener("load", () => {
    cb(oReq);
  });
  if (typeof data == 'string'){
    oReq.open('POST', `/upload?input_type=${type}&${data}`);
    oReq.send();
  } else {
    oReq.open('POST', `/upload?input_type=${type}`);
    oReq.send(data);
  }
}

function serialize(obj) {
  var str = [];
  for(let p in obj)
    if (obj.hasOwnProperty(p)) {
      str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
    }
  return str.join("&");
}
