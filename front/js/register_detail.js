import { createService, getService } from '../service/api.js';

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

function serviceDetail(service) {
  const register = document.getElementById('registerForm')
  console.log(register)
  item = '';
  item += `
    <div>
      <label for="name">Nome do serviço</label>
        <input type="text" name="name" id="name" value="${register.name_service}">
    </div>
    <br>
    <div>
      <label for="small_time">Tempo estimado para pet de pequeno porte</label>
      <input type="text" name="small_time" id="small_time" value="${service.small_time}">
    </div>
    <br>
    <div>
      <label for="medium_time">Tempo estimado para pet de médio porte</label>
      <input type="text" name="medium_time" id="medium_time" value="${service.medium_time}">
    </div>
    <br>
    <div>
      <label for="large_time">Tempo estimado para pet de grande porte</label>
      <input type="text" name="large_time" id="large_time" value="${service.large_time}">
    </div>
    <br>
    <button type="submit" id="submit-btn">Salvar</button>
    `
}

getService(pk).then((data) => {
  console.log(data, pk);
  serviceDetail(data)
}

);