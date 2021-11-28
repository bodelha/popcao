import { createService} from '../service/api.js';

function formSubmit() {

  const data = {
    name_service: document.getElementById('name_service'),
    time_service: document.getElementById('time_service'),
    short_fur: document.getElementById('short_fur'),
    medium_fur: document.getElementById('medium_fur'),
    long_fur: document.getElementById('long_fur')
  };
  const groomable = document.getElementById('groomable1').checked;
  const parsed_data = {};
  for (const item in data){
    if (data[item]){
      var d = data[item]
      parsed_data[d.id] = d.value;
    };
  };
  const breeds = [];
  const set = document.getElementsByName("breed_input");
  for (var i=0; i<set.length;i++){
  console.log('set[i].value',set[i].value)
    breeds.push({
      'name_breed': set[i].value,
      'groomable': groomable==1
    })
    console.log(breeds)
  }
  parsed_data['breeds'] = breeds
  console.log(parsed_data, breeds)
  createService(parsed_data).then((response) => {
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

const form = document.getElementById('registerForm');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  formSubmit();
});