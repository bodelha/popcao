import { getTutors } from "../service/api.js";

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
