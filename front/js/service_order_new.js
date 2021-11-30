import {
  createServiceOrder,
  getTutor,
  getBreeds,
  getSettings,
} from "../service/api.js";

const getUrlParamsId = () => {
  var url = new URL(window.location.href);
  var id = url.searchParams.get("id");
  return id;
};

const tutorId = getUrlParamsId();

function insertTime(id) {}

function build(tutorDetail, breeds_data, service_data) {
  const anchor = document.getElementById("service_order");
  const { id_tutor, name_tutor, pets } = tutorDetail;
  var cont = `
  <div class="form_session">
  <div id="tutor" class="card">
      <label for="name_tutor">Nome Tutor</label>
      <input type="text" name="name_tutor" id="name_tutor" value=${name_tutor}>
      <input type="hidden" id="id_tutor" name="id_tutor" value=${id_tutor}>
    </div>
      <div></div>
      </div>
  `;
  var i = 0;
  for (let pet of pets) {
    cont =
      cont +
      `
      <div>
      <div class="form_session">
      <div class="card">
      <label for="name_pet">Nome Pet</label>
        <input type="text" name="name_pet" id=name_pet${i} value=${pet.name_pet}>
        <input type="hidden" id=pet${i} name="pet" value=${pet.id_pet}>
        <input type="hidden" id=groomable${i} name="pet" value=${pet.groomable} class=>
        <input type="hidden" id=breed${i} name="pet" value=${pet.id_breed} class="pet_breed">
      </div>
      </div>
    `;
    i++;
    var j = 0;
    for (let breed of breeds_data) {
      if (breed.id_breed == pet.breed_id) {
        let set = breed.set;
        var j = 0;
        for (let serv of set) {
          for (let service of service_data) {
            if (service.id_service == serv) {
              console.log(service);
              if (breed.groomable == false) {
                cont += `
                  <div>
                  <div class="form_session">
                  <div class="card">
                    <label for="service_duration">Estimativa ${service.name_service}</label>
                    <input type="text" name="service_duration" id="service_duration" value=${service.time_service}>
                    <input type="hidden" id="service_category${i}_${j}" name="service_category${i}_${j}" value=${serv}>
                  </div>
                  </div>
      <div></div>
      </div>
                `;
              } else {
                cont += `
                  <div class="form_session" id="gromm"${i}_${j}>
                  <div class = "card">

                  <div>Selecione <br><br>(Estimativa ${service.name_service})<br><br></div>
                  <div id=groomable${i}_${j}>
                  <div id="trio${i}_${j}" class="trio">
                    <div>
                    <label for="groom_short">Pêlo Curto</label>
                    <input type="radio" name="groomable" id="groom_short${i}_${j}" value="0" />
                    <input type="text" id="service_time0${i}_${j}" name="service_time0${i}_${j}" value=${service.short_fur}>
                    </div>
                    <div>
                    <label for="grooma_medium">Pêlo Médio</label>
                    <input type="radio" name="groomable" id="grooma_medium${i}_${j}" value="1" />
                    <input type="text" id="service_time1${i}_${j}" name="service_time1${i}_${j}" value=${service.medium_fur}>
                    </div>
                    <div>
                    <label for="groomable_long">Pêlo Longo</label>
                    <input type="radio" name="groomable" id="groomable_long${i}_${j}" value="2" />
                    <input type="text" id="service_time2${i}_${j}" name="service_time2${i}_${j}" value=${service.long_fur}>
                    </div>
                    </div>
                  <div id="time${i}_${j}"></div>
      <div></div>
      </div>
                    `;
              }
              j++;
            }
          }
        }
      }
    }
  }
  anchor.innerHTML = cont;
}

getBreeds().then((_breeds) => {
  const breeds_data = _breeds;
  getSettings().then((_sett) => {
    const service_data = _sett;
    getTutor(tutorId).then((data) => {
      const _data = data;
      build(_data, breeds_data, service_data);
      // form.addEventListener("sumit", (event) => {
      //   console.log(event);
      //   if (!arr.hasOwnPropert(event.target.id)) return;
      //   insertTime(event.target);
      // });
    });
  });
});
const form = document.getElementById("order");
form.addEventListener("click", (event) => {
  event.preventDefault();
  alert("Ordem salva com sucesso");
  window.location.href = "index.html";
});
