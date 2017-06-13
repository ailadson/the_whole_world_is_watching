let file = document.querySelector('#file-input');

file.addEventListener('change', (e)=>{
  let reader  = new FileReader();
  reader.addEventListener('load', (e)=>{
    upload_data_to_gcs(reader.result);
  });
  reader.readAsDataURL(file.files[0]);
});

function upload_data_to_gcs(data) {
  let endpoint = window.PBVD.file_upload_endpoint;
  let oReq = new XMLHttpRequest();

  oReq.addEventListener("load", () => {
    vidfile_input_upload();
  });

  oReq.open(endpoint.method, `${endpoint.url}?${serialize(endpoint.params)}`);
  for(let h in endpoint.headers)
    oReq.setRequestHeader((h), (endpoint.headers[h]));
  oReq.send(data);
}

function vidfile_input_upload(){
  let name = PBVD.file_upload_endpoint.url.split('/')[5].split('.')[0];
  let oReq = new XMLHttpRequest();
  oReq.addEventListener("load", () => {
    console.log(oReq.responseText);
  });
  oReq.open('POST', `/upload?input_type=vidfile&incident[cloud_id]=${name}}`);
  oReq.send();
}

function serialize(obj) {
  var str = [];
  for(let p in obj)
    if (obj.hasOwnProperty(p)) {
      str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
    }
  return str.join("&");
}
