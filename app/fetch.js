var formdata = new FormData();
formdata.append("input_value", "https://stackoverflow.com/questions/42011100/how-can-i-pass-post-parameters-in-fetch-request-react-native");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("http://127.0.0.1:8080/test_post", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));