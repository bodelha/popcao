import { createPet } from '../service/api.js';

const form = document.getElementById('registerForm');

function formSubmit(event) {
  const data = {
    name: document.getElementById('name').value,
    breed: document.getElementById('breed').value,
  };
  createPet(data).then((response) => {
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