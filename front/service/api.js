const BASE_URL_API = 'http://127.0.0.1:8000/api';

export async function createService(data) {
  const response = await fetch(`${BASE_URL_API}/service`, {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-type': 'application/json; charset=UTF-8'
    }
  });
  return response;
}

export async function getServices() {
  const response = await fetch(`${BASE_URL_API}/services`);
  const services = await response.json();
  return services;
}

export async function getService(id) {
  const response = await fetch(
    `${BASE_URL_API}/service/${id}`,
    {
      method: 'GET',
      body: JSON.stringify(data),
      headers: {
      'Content-type': 'application/json; charset=UTF-8'
    }
    }
    );
  const service = await response.json();
  return service;
}

export async function updateService(id, data) {
  const response = await fetch(
    `${BASE_URL_API}/service/${id}`,
    {
      method: 'PUT',
      body: JSON.stringify(data),
      headers: {
      'Content-type': 'application/json; charset=UTF-8'
    }
    }
    );
  return response;
}


export async function deleteService(id, data) {
  const response = await fetch(
    `${BASE_URL_API}/service/${id}`,
    {
      method: 'DELETE',
      body: JSON.stringify(data),
      headers: {
      'Content-type': 'application/json; charset=UTF-8'
    }
    }
    );
  return response;
}