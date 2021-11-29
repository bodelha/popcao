import { getTutors, createServiceOrder} from "../service/api.js";

function tutorList(tutors) {
  const anchor = document.getElementById("tutor_list");
  var cont = `<tr id='header'>
  <th id='name_tutor'>Tutor</th>
  <th id='name_tutor'>Pets</th>
</tr>`

  for (let tutor of tutors) {
    let obj=''
    for(let pet of tutor.pets){
      obj += `<p class=pet> ${pet.name_pet} </p>`
    }
    console.log(tutor)
    cont = cont.concat(
      `
    <tr id=${tutor.id_tutor}>
    <th id='name_tutor'>${tutor.name_tutor}</th>
    <th id='pets'>${obj}</th>
    <th>
    <button class="order-btn" value="${tutor.id_tutor}">Iniciar</button>
    </th>
    </tr>
    `
    );
  }
  anchor.innerHTML = cont;
}

getTutors().then((data) => {
  console.log(data);
  tutorList(data);
});


document.addEventListener('click', (event) => {
  console.log(event);
	if (!event.target.matches('.order-btn')) return;

	event.preventDefault();
  location.href = `/service_order_new.html?id=${event.target.value}`;
}, false);
