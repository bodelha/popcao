import { createService, getSettings } from '../service/api.js';

function servicesList(services) {
  const list = document.getElementById('list');
  const header = `<tr id='header'>
    <th>Nome</th>
    <th>Raças</th>
    <th>Tempo Estimado Pêlo Curto</th>
    <th>Tempo Estimado Pêlo Médio</th>
    <th>Tempo Estimado Pêlo Longo</th>
  </tr>`
  let itens = '';

  for (let service of services) {
    let _obj = ''
    for (let breed of service.breeds){
      _obj += `<p> ${breed.name_breed} </p>`
    }
    itens += `
    <tr id=${service.id_service}>
    <th>${service.name_service}</th>
    <th> ${_obj}</th>
    <th> ${service.short_fur || service.time_service}</th>
    <th> ${service.medium_fur || "Não se aplica"}</th>
    <th> ${service.long_fur || "Não se aplica"}</th>
    <th>
    <button class="update-btn" value="${service.id_service}">Editar</button>
    <button class="delete-btn" value="${service.id_service}">Deletar</button>
    </th>
    </tr>
    `
  }

  list.innerHTML = header+itens;
  console.log(list)
}

getSettings().then((data) => {
  console.log(data);
  servicesList(data);
});


document.addEventListener('click', (event) => {
	if (!event.target.matches('.update-btn')) return;

	event.preventDefault();
  location.href = `/service_detail?id=${event.target.value}`;
}, false);

document.addEventListener('click', (event) => {
	if (!event.target.matches('.delete-btn')) return;

	event.preventDefault();
  deletePet(event.target.value).then((data) => {
    console.log('pet removido');
  });
}, false);

// const form = document.getElementById('registerForm');

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
// })