const BASE_URL = "http://localhost:5000/api";

function generateCupcakeHTML(cupcake) {
    return `
      <div data-cupcake-id=${cupcake.id}>
          <p>${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}</p>
        <img class="image"
              src="${cupcake.image}"
              alt="(no image provided)">
      </div>
    `;
  }

  async function showInitialCupcakes() {
    // console.log("showInitialCupcakes");
    const response = await axios.get(`${BASE_URL}/cupcakes`);
    for (let cupcakeData of response.data.cupcakes) {
      let newCupcake = $(generateCupcakeHTML(cupcakeData));
      $("#list").append(newCupcake);
    }
  }

  $("#add-cupcake").on("submit", async function (e) {
    e.preventDefault();
  
    let flavor = $("#flavor").val();
    let rating = $("#rating").val();
    let size = $("#size").val();
    let image = $("#image").val();
  
    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
      flavor,
      rating,
      size,
      image
    });
  
    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("#list").append(newCupcake);
    $("#add-cupcake").trigger("reset");
  });

  $(showInitialCupcakes);