import { getSettings, deleteService, createService } from '../service/api.js';

function servicesList(services) {
  const list = document.getElementById('list');
  const header = `<tr id='header'>
    <th id='name'>Nome</th>
    <th id='breed'>Raças</th>
    <th>Tempo Estimado<br>Pêlo Curto</th>
    <th>Tempo Estimado<br>Pêlo Médio</th>
    <th>Tempo Estimado<br>Pêlo Longo</th>
    <th><button class="create-btn">Novo Serviço</button></th>
  </tr>`
  let itens = '';

  for (let service of services) {
    let _obj = ''
    for (let breed of service.breeds){
      _obj += `<p class=breed> ${breed.name_breed} </p>`
    }
    itens += `
    <tr id=${service.id_service}>
    <th id='name'>${service.name_service}</th>
    <th id='breed'> ${_obj}</th>
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
  console.log(event);
	if (!event.target.matches('.create-btn')) return;

	event.preventDefault();
  createService().then((data)=>{
    console.log(data);
  });
  location.href = `/new_service.html`;
}, false);


document.addEventListener('click', (event) => {
	if (!event.target.matches('.delete-btn')) return;

	event.preventDefault();
  deleteService(event.target.value).then((data) => {
    document.location.reload(true);
  });
}, false);

document.addEventListener('click', (event) => {
	if (!event.target.matches('.update-btn')) return;

	event.preventDefault();
  location.href = `/service_detail.html?id=${event.target.value}`;
}, false);
