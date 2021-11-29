import { getBreeds, createTutor } from "../service/api.js";

function formSubmit() {
  const data = {
    name_tutor: document.getElementById("nome").value,
    cellphone1: document.getElementById("celular1").value,
    cellphone2: document.getElementById("celular2").value,
    adress: document.getElementById("adress").value,
  };
  var parsed_pets = [];
  const pets = document.getElementsByClassName("pet_group");
  for (var i = 0; i < pets.length; i++) {
    parsed_pets.push({
      name_pet: document.getElementById(`pet_name${i}`).value,
      breed_id: document.getElementById(`id_breed_hidden${i}`).value,
      sex: document.getElementById(`sex${i}`).value,
    });
  }
  data["pets"] = parsed_pets;
  console.log(data, parsed_pets);
  createTutor(data)
    .then((response) => {
      if (response.ok) {
        return response.json();
      }
      return Promise.reject(response);
    })
    .then((data) => {
      console.log(data);
      alert("Cadastrado com sucesso");
      window.location.href = "index.html";
    })
    .catch((error) => {
      console.warn(error);
    });
}

function dataList(breeds) {
  var header = `
    <label for="id_breed">Raça</label>
    <input list="breed_list" id="id_breed0" name="breed" oninput="onInput(0)" autocomplete=false>
    <input type="hidden" name="breed" id="id_breed_hidden0" oninput="onInput(0)">
    <datalist id="breed_list">
        `;
  for (const breed in breeds) {
    header = header.concat(
      `<option class="option" value=${breeds[breed].name_breed} id=${breeds[breed].id_breed}>
      `
    );
  }
  header = header.concat(`</datalist>`);
  const anchor = document.getElementById("anchor0");
  anchor.innerHTML = header;
  globalThis.header = header;
}

document.addEventListener("click", (event) => {
  if (!event.target.matches("#new_pet")) return;
  event.preventDefault();
  const p_class = document.getElementsByClassName("pet_group");
  let i = p_class.length;
  var cont = p_class[0].innerHTML;
  cont = cont.replace("pet0", `pet${i}`);
  cont = cont.replace("pet_name0", `pet_name${i}`);
  cont = cont.replace("anchor0", `anchor${i}`);
  cont = cont.replace("id_breed0", `id_breed${i}`);
  cont = cont.replace("id_breed_hidden0", `id_breed_hidden${i}`);
  cont = cont.replaceAll("onInput(0)", `onInput(${i})`);
  cont = cont.replaceAll("sex0", `sex${i}`);
  let sector = document.getElementById("pet_sector");
  let sectortxt = sector.innerHTML;
  sectortxt.trim();
  sector.innerHTML = `
  ${sectortxt.slice(0, -6)}
  <div class="pet_group" id="pet${i}">
  ${cont}</div><div></div>`;
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
