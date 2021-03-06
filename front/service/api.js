const BASE_URL_API = "http://127.0.0.1:8000";

export async function getSettings() {
  const response = await fetch(`${BASE_URL_API}/settings`);
  const settings = await response.json();
  return settings;
}

export async function createService(data) {
  console.log(JSON.stringify(data));
  const response = await fetch(`${BASE_URL_API}/service/new`, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
  return response;
}

export async function getService(id) {
  const response = await fetch(`${BASE_URL_API}/service/${id}`, {
    method: "GET",
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
  const service = await response.json();
  return service;
}

export async function updateService(id, data) {
  const response = await fetch(`${BASE_URL_API}/service/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
  return response;
}

export async function deleteService(id, data) {
  const response = await fetch(`${BASE_URL_API}/service/${id}`, {
    method: "DELETE",
    body: JSON.stringify(data),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
  return response;
}

export async function getBreeds() {
  const response = await fetch(`${BASE_URL_API}/breeds`);
  const breeds = await response.json();
  return breeds;
}
export async function getBreed(id) {
  const response = await fetch(`${BASE_URL_API}/breed/${id}`, {
    method: "GET",
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
  const breed = await response.json();
  return breed;
}
export async function createTutor(data) {
  console.log(JSON.stringify(data));
  const response = await fetch(`${BASE_URL_API}/tutor/new`, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
  return response;
}
export async function getTutors() {
  const response = await fetch(`${BASE_URL_API}/tutors`);
  const breeds = await response.json();
  return breeds;
}
export async function getTutor(id) {
  const response = await fetch(`${BASE_URL_API}/tutor/${id}`);
  const breeds = await response.json();
  return breeds;
}
export async function createServiceOrder(data){
  console.log(JSON.stringify(data));
  const response = await fetch(`${BASE_URL_API}/service_order`, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  });
  return response;  
}