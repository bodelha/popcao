import { getService, updateService } from "../service/api.js";

const getUrlParamsId = () => {
  var url = new URL(window.location.href);
  var id = url.searchParams.get("id");
  console.log(id);
  return id;
};

const serviceId = getUrlParamsId();

getService(serviceId).then((data) => {
  console.log(data, serviceId);
  const {
    name_service,
    short_fur,
    medium_fur,
    long_fur,
    time_service,
    breeds,
  } = data;
  document.getElementById("name_service").value = name_service;
  if (short_fur) {
    const time = document.getElementById("time");
    time.innerHTML = `<div class="form_session">
      <label for="short_fur">Tempo estimado para pet de pêlo curto</label>
      <input type="text" class="duration-input" name="short_fur" id="short_fur" required pattern="[0-9]{2}:[0-9]{2}:[0-9]{2}" value=${short_fur}>
    </div>
    <div class="form_session">
      <label for="medium_fur">Tempo estimado para pet de pêlo médio</label>
      <input type="text" class="duration-input" name="medium_fur" id="medium_fur" required pattern="[0-9]{2}:[0-9]{2}:[0-9]{2}" value=${medium_fur}>
    </div>
    <div class="form_session">
      <label for="long_fur">Tempo estimado para pet de pêlo longo</label>
      <input type="text" class="duration-input" name="long_fur" id="long_fur" required pattern="[0-9]{2}:[0-9]{2}:[0-9]{2}" value=${long_fur}>
    </div>
      <div>`;
    const rdb = document.getElementById("groomable1");
    rdb.checked = true;
  } else {
    const time = document.getElementById("time");
    time.innerHTML = `<div class="form_session">
      <label for="time_service">Tempo estimado</label>
      <input class="duration-input" type="text" id="time_service" required pattern="[0-9]{2}:[0-9]{2}" value=${time_service}>
    </div>`;
    const rdb = document.getElementById("groomable0");
    rdb.checked = true;
  }
  const b_class = document.getElementById("breedSession");
  var contend = ``;
  var i = 0;
  for (const item in breeds) {
    console.log(breeds[item]);
    contend =
      contend +
      `<div id=${breeds[item].id_breed}><label for="name">Nome</label>
          <input type="text" name="breed_input" alt="${breeds[item].id_breed}" class="name_breed" id="name${i}" value=${breeds[item].name_breed} ></div>`;
    i++;
  }
  b_class.innerHTML = contend;
});

document.addEventListener("click", (event) => {
  if (!event.target.matches("#new_breed")) return;

  event.preventDefault();
  const b_class = document.getElementById("breedSession");
  const new_b = b_class.getElementsByClassName("breed_input");
  console.log(b_class, new_b);
  var cont = b_class.innerHTML;
  cont =
    cont +
    `<div><label for="name">Nome</label>
  <input type="text" name="breed_input" class="name_breed" id="name${new_b.length}" autocomplete="on"></div>`;
  b_class.innerHTML = cont;
});

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

const form = document.getElementById("registerForm");

function formSubmit() {
  const data = {
    name_service: document.getElementById("name_service"),
    time_service: document.getElementById("time_service"),
    short_fur: document.getElementById("short_fur"),
    medium_fur: document.getElementById("medium_fur"),
    long_fur: document.getElementById("long_fur")
  };
  const groomable = document.getElementById("groomable1").checked;
  const parsed_data = {};
  for (const item in data) {
    if (data[item]) {
      var d = data[item];
      parsed_data[d.id] = d.value;
    }
  }
  const breeds = [];
  const set = document.getElementsByName("breed_input");
  for (var i = 0; i < set.length; i++) {
    breeds.push({
      id_breed: set[i].alt,
      name_breed: set[i].value,
      groomable: groomable == 1,
    });
  }
  parsed_data["set"] = breeds;
  console.log(parsed_data, breeds);
  updateService(serviceId, parsed_data)
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

form.addEventListener("submit", (event) => {
  event.preventDefault();
  formSubmit();
});
