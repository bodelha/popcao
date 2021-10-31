
import { getServices } from '../service/api.js';

function servicesList(services) {
  const list = document.getElementById('list');
  let itens = '';

  for (let service of services) {;
    itens += `<li>${service.name_service} - ${small_time.breed}</li>`
  }

  list.innerHTML = itens;
}

getServices().then((data) => {
  console.log(data.services);
  servicesList(data.services);
});