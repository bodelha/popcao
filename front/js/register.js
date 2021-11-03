import { createService, getServices } from '../service/api.js';

function servicesList(services) {
  const list = document.getElementById('list');
  let itens = '';

  for (let service of services) {;
    itens += `<li>${service.name_service} - ${service.small_time}</li>`
  }

  list.innerHTML = itens;
}

getServices().then((data) => {
  console.log(data);
  servicesList(data);
});

const form = document.getElementById('registerForm');

function formSubmit(event) {
  const data = {
    name_service: document.getElementById('name').value,
    small_time: document.getElementById('small_time').value,
    medium_time: document.getElementById('medium_time').value,
    large_time: document.getElementById('large_time').value,
  };
  createService(data).then((response) => {
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