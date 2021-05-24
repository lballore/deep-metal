
<script>
  import { onMount } from 'svelte';

  const GENERATE_BUTTON_ACTIVE = "Generate!";
  const GENERATE_BUTTON_INACTIVE = "Generating ...";
  const TOOLTIP_TEXT = "Lower temperatures result in more predictable text.\
                        With higher temperatures, the generated text becomes usually more interesting,\
                        surprising, and creative, even though the level of coherence can be affected negatively."

  let temperature = 0.95;
  let textInputs = "";
  let lyricsPayload = "";
  let generateButton = GENERATE_BUTTON_ACTIVE;
  let buttonDisabled = false;

  function handleClick() {
    toggleGenerateButton("deactivate");
    lyricsPayload = generateLyrics();
  }

  function toggleGenerateButton(action) {
    if (action == "activate") {
      generateButton = GENERATE_BUTTON_ACTIVE;
      buttonDisabled = false;
    } else {
      generateButton = GENERATE_BUTTON_INACTIVE;
      buttonDisabled = true;
    }
  }

  async function generateLyrics() {
    const response = await fetch(`/api/v1/generate`, {
      method: "POST",
      body: JSON.stringify({
        text_inputs: textInputs,
        temperature: temperature.toFixed(2),
      }),
    });
    const data = await response.json();
    toggleGenerateButton("activate");
    console.log(cleanLyrics(data["lyrics"][0]["generated_text"]))  // REMOVE!
    return cleanLyrics(data["lyrics"][0]["generated_text"])
  }

  function cleanLyrics(inputStr) {
    return inputStr.replace(/^[a-z0-9\,\.\'\n ]+/, '').trim();
  }

  onMount(() => {
    window.$('[data-toggle="tooltip"]').tooltip();
  });
</script>

<!------------------------------------------->
<!----------------MARKUP----------------------->
<!------------------------------------------->
<section id="demo" class="section grey-bgcolor">
  <div class="container text-center">

    <h2 class="title deepmetal-logo">Try the demo!</h2>

    <p class="text-left section-body">
      <i>DeepMetal</i> is a model capable of generating lyrics taylored for heavy metal songs. The model is based on the
      OpenAI GPT-2 and has been finetuned on a dataset of 141,718 heavy metal songs lyrics.<br />
      The model is capable to generate <b>explicit lyrics</b>. It is a consequence of a fine-tuning made with a dataset
      that contained such lyrics, which are part of the discography of many heavy metal bands.
      Be aware of that before you use the model, <b>the author is not liable for any emotional response and following
      consequences.</b>
    </p>

    <div class="row justify-content-md-center mt-2">
      <div class="col-md-9">
        <div class="form-group">
          <label for="temperature" class="form-label font-weight-bold">
            Temperature
            <span data-toggle="tooltip" data-placement="bottom" title={TOOLTIP_TEXT}>
              <i class="far fa-question-circle"></i>
            </span>
          </label>
          <input
            id="temperature"
            name="temperature"
            class="form-control-range gradient-range"
            type="range"
            min="0.50"
            max="1.00"
            step="0.01"
            bind:value={temperature}
          />
          <span class="rangeval">{temperature.toFixed(2)}</span>
        </div>
      </div>
    </div>

    <div class="row justify-content-md-center">
      <div class="col-md-9">
        <div class="form-group">
          <label for="text-inputs" class="form-label font-weight-bold">
            Incipit (leave blank for unconditioned generation)
          </label>
          <div class="input-group">
            <span class="input-group-text">
              <i class="fas fa-pen-fancy fa-2x"></i>
            </span>
            <input
              id="text-inputs"
              name="text-inputs"
              class="form-control form-control-lg"
              type="text"
              placeholder="Your text ..."
              bind:value={textInputs}
            >
          </div>
        </div>
      </div>
    </div>

    <div class="row justify-content-md-center mt-3 mb-3">
      <div class="col">
        <button class="btn btn-primary" type="button" disabled={buttonDisabled} on:click={handleClick}>{generateButton}</button>
      </div>
    </div>

    <div class="row justify-content-md-center section-body">
      <div class="col-md-8">
        {#await lyricsPayload}
          <p class="justify-content-center">
            <img src="/static/images/waiting.gif" class="waiting-gif" alt="waiting" />
          </p>
        {:then metalLyrics}
          <p class="metal-lyrics deepmetal-logo">{metalLyrics}</p>
        {:catch error}
          <div class="justify-content-center alert alert-danger">
            <h4 class="alert-heading">Error generating lyrics: {error.message}</h4>
          </div>
        {/await}
      </div>
    </div>

  </div>
</section>

<!------------------------------------------->
<!----------------STYLE----------------------->
<!------------------------------------------->
<style>
  .metal-lyrics {
    white-space: pre-line;
    font-size: 18px;
  }

  .waiting-gif {
    width: 50%;
    height: auto;
  }

  *[data-toggle="tooltip"] {
    cursor: pointer;
  }

  .title {
    text-transform: uppercase;
  }

  section .btn-primary {
    box-shadow: none;
    padding: 8px 25px;
    border: none;
  }
</style>
