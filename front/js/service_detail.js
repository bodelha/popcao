import { createService, getService, updateService } from '../service/api.js';


const getUrlParamsId = () => {
  var url = new URL(window.location.href);
  var id = url.searchParams.get('id');
  return id;
}

const serviceId = getUrlParamsId();

getService(serviceId).then((data) => {
  console.log(data, serviceId);
  const {
    name_service,
    short_fur,
    medium_fur,
    long_fur,
    time_service,
    breeds
  } = data;
  document.getElementById('name').value=name_service
  document.getElementById('breeds').value=breeds
  if (short_fur){
    document.getElementById('short_fur').value=short_fur
    document.getElementById('medium_fur').value=medium_fur
    document.getElementById('long_fur').value=long_fur
    document.getElementById('time_service').value='Não se aplica'
  }
  else{
  document.getElementById('time_service').value=time_service
  document.getElementById('short_fur').value='Não se aplica'
  document.getElementById('medium_fur').value='Não se aplica'
  document.getElementById('long_fur').value='Não se aplica'
}
});

// function formSubmit(event) {
//   const data = {
//     name_service: document.getElementById('name').value,
//     small_time: document.getElementById('small_time').value,
//     medium_time: document.getElementById('medium_time').value,
//     large_time: document.getElementById('large_time').value,
//   };
//   createService(data).then((response) => {
//     if (response.ok) {
//       return response.json();
//     }
//     return Promise.reject(response);
//   }).then((data) => {
//     console.log(data);
//   }).catch((error) => {
//     console.warn(error);
//   });
// }

// form.addEventListener('submit', (event) => {
//   event.preventDefault();
//   formSubmit();


const form = document.getElementById('registerForm');

function formSubmit() {

  const data = {
    name_service: document.getElementById('name').value,
    time_service: document.getElementById('time_service').value,
    short_fur: document.getElementById('short_fur').value,
    medium_fur: document.getElementById('medium_fur').value,
    long_fur: document.getElementById('long_fur').value,
    // set: document.getElementById('breeds').value,
  };
  for (const item in data){
    if (data[item] == 'Não se aplica'){
      delete data[item]
    }
  }
  updateService(serviceId, data).then((response) => {
    if (response.ok) {
      return response.json();
    }
    return Promise.reject(response);
  }).then((data) => {
    console.log(data);
  }).catch((error) => {
    console.warn(error);
  });
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  formSubmit();
})