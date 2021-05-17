<script>
  export let textInputs;
  export let metalLyrics = [];
  export let demoData = {};
  const { HEADING, ALL_SERVICES } = demoData;

  async function generateLyrics() {
    const response = await fetch(`/api/v1/generate`, {
      method: "POST",
    });
    const data = await response.json();
    console.log(data)
  }
</script>

<!------------------------------------------->
<!----------------MARKUP----------------------->
<!------------------------------------------->
<section id="demo" class="section">
  <div class="container text-center">
    <h2 class="title">{HEADING}</h2>
    <div class="row section-body">
      <button class="btn btn-outline-primary" type="button" on:click={generateLyrics}>Get lyrics</button>
    </div>
    <buttom class="btn btn-primary round-border main-bgcolor">
      {ALL_SERVICES}
    </buttom>
  </div>
</section>
<!------------------------------------------->
<!----------------STYLE----------------------->
<!------------------------------------------->
<style>
  .service-img {
    width: 200px;
    height: 200px;
    margin-top: 20px;
  }

  .service h4 {
    padding: 5px;
    margin-top: 25px;
    text-transform: uppercase;
  }

  .title {
    text-transform: uppercase;
  }

  .title::before {
    content: "";
    background: linear-gradient(90deg, #0072ff 0%, #00d4ff 100%);
    height: 5px;
    width: 200px;
    margin-left: auto;
    margin-right: auto;
    display: block;
    transform: translateY(60px);
  }

  .title::after {
    content: "";
    background: linear-gradient(90deg, #0072ff 0%, #00d4ff 100%);
    height: 10px;
    width: 50px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 40px;
    display: block;
    transform: translateY(14px);
  }

  section .btn-primary {
    box-shadow: none;
    padding: 8px 25px;
    border: none;
  }
</style>