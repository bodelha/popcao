const button = document.getElementById("fetch-btn");

button.addEventListener("click", function() {
    try {
        fetch("http://127.0.0.1:8000/api/services")
        .then(response => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
        })
        .then(json => buildList(json));
    } catch (error) {
        return {
            "serviços": [
                "Tosa Higiênica",
                "Tosa Tesoura",
                "Tosa máquina",
                "Banho"
            ],
            "porte":[
                "pequeno",
                "médio",
                "grande"
            ]
        }
    }

});

/*
Build the user's list
 */
function buildList(data) {
  console.log(data);
}