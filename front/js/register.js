import { getBreeds, createTutor } from "../service/api.js";

function formSubmit() {
  const data = {
    name_tutor: document.getElementById("nome"),
    cellphone1: document.getElementById("celular1"),
    cellphone2: document.getElementById("celular2"),
    adress: document.getElementById("adress"),
    name_pet: document.getElementById("pet_name0"),
    breed_id: document.getElementById("id_breed"),
    sex: document.getElementById("sex0"),
  };
  console.log(document.getElementById("id_breed"));
  console.log(document.getElementById("sex0"));
  var parsed_data = {};
  for (const item in data) {
    if (data[item]) {
      var d = data[item];
      parsed_data[d.id] = d.value;
    }
  }
  var parsed_pets = {};
  const pets = document.getElementsByClassName("pet_group");
  for (var i = 0; i < pets.length; i++) {
    var group = document.getElementById(`pet${i}`);
    console.log(group.firstChild.nodeValue);

    // parsed_pets[i]={
    //   name_pet: pets[i].getElementById("pet_name").value,
    //   breed_id: pets[i].getElementById("id_breed").value,
    //   sex:pets[i].getElementById("sex").value
    // };
  }
  console.log(parsed_pets);
  parsed_data["pets"] = parsed_pets;
  console.log(parsed_data, parsed_pets);
  createTutor(parsed_data)
    .then((response) => {
      if (response.ok) {
        return response.json();
      }
      return Promise.reject(response);
    })
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.warn(error);
    });
}

function dataList(breeds) {
  var header = `
    <label for="id_breed">Raça</label>
    <input list="breed_list" id="id_breed" name="breed"/>
    <datalist id="breed_list">
        `;
  for (const breed in breeds) {
    header = header.concat(
      `<option value=${breeds[breed].name_breed} value=${breeds[breed].id_breed}>`
    );
  }
  header = header.concat(
    `</datalist><input type="hidden" name="breed" id="id_breed-hidden">`
  );
  const anchor = document.getElementById("anchor0");
  anchor.innerHTML = header;
  globalThis.header = header;
  
}

document.addEventListener('click', (event)=>{
  if (!event.target.matches("#id_breed")) return;
  event.preventDefault();
  console.log(event)
})

document.addEventListener("click", (event) => {
  if (!event.target.matches("#new_pet")) return;
  event.preventDefault();
  const p_class = document.getElementsByClassName("pet_sector")[0];
  var cont = p_class.innerHTML;
  cont =
    cont +
    `<div class="pet_group" id="pet1">
  <div class="form_session">
    <label for="pet_name">Nome do Pet</label>
    <input type="text" name="pet_name" id="pet_name1" required />
  </div>
  <div class="form_session" id="anchor1">
  ${globalThis.header}
  </div>
  <div class="form_session" id="sex1">
    <div>Sexo</div>
    <div id="pair">
      <label for="sex1">Macho</label>
      <input type="radio" name="sex1" id="male" value="M" />
      <label for="sex1">Fêmea</label>
      <input type="radio" name="sex1" id="female" value="F" />
    </div>
  </div>
  $(function(){
    $('#id_breed').change(function(){
        console.log($("#breed_list[value='" + $('#id_breed').val() + "']").attr('id_breed'));
    });
  });
  <div id="pet_group_to_be"></div>`;
  p_class.innerHTML = cont;
});


var header;
const form = document.getElementById("register_form");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  formSubmit();
});

getBreeds().then((data) => {
  // console.log(data);
  dataList(data);
});
