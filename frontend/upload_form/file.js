let file = document.querySelector('#file-input');

file.addEventListener('change', (e)=>{
  let reader  = new FileReader();
  reader.addEventListener('load', (e)=>{
    let endpoint = window.PBVD.file_upload_endpoint;
    let oReq = new XMLHttpRequest();
    oReq.addEventListener("load", () => {
      console.log(oReq.responseText);
    });
    oReq.open(endpoint.method, `${endpoint.url}?${serialize(endpoint.params)}`);
    for(let h in endpoint.headers) {
      oReq.setRequestHeader((h), (endpoint.headers[h]))
    }
    oReq.send(reader.result);
  })
  reader.readAsDataURL(file.files[0]);
});

function serialize(obj) {
  var str = [];
  for(let p in obj)
    if (obj.hasOwnProperty(p)) {
      str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
    }
  return str.join("&");
}
