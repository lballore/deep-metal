<script>
</script>

<!------------------------------------------->
<!----------------MARKUP----------------------->
<!------------------------------------------->
<section id="project" class="section">
  <div class="container">
    <h1 class="title text-center deepmetal-logo">The project</h1>
    <div class="row section-body">
      <div class="col-md-6 my-auto">
          The research is divided in <strong>4 parts</strong>:

          <ul>
            <li>
              Brief <strong>analysis of dataset contents</strong>: quantities (amount of artists, albums, album types, songs etc.) and
              simple statistics, album releases and distribution over the years,language distribution, bands popularity etc.
            </li>
            <li>
              <strong>Readability analysis</strong>: swear words ratio and Coleman-Liau grade index, word frequence and definition of
              "metalness", POS analysis etc.
            </li>
            <li>
              Word based <strong>sentiment analysis</strong>, sentiment analysis with VADER, bands clustering based on sentiment and "metalness",
              bands emotional arcs, emotional arcs applied on literature, LDA topics modeling etc.
            </li>
            <li>
              Heavy metal <strong>lyrics generator</strong>, based on
              <a target="_blank" href="https://github.com/openai/gpt-2">OpenAI's GPT-2 generative model</a>. The model is also available
              on the HuggingFace transformer library (read more <a target="_blank" href="https://huggingface.co/lucone83/deep-metal">here</a>).
            </li>
          </ul>

          For more details you can read the related articles <a target="_blank" href="https://blog.lucaballore.com/">on my Medium blog</a>
          or visit the official <a target="_blank" href="https://github.com/lucone83/deep-metal">GitHub repository</a> of the project.
      </div>

      <div class="col-md-6 mt-5 d-none d-lg-block d-xl-block d-md-block">
        <img src=/static/images/horns.png alt="Metal horns" class="img-fluid" />
      </div>
    </div>
  </div>
</section>

<!------------------------------------------->
<!----------------STYLE----------------------->
<!------------------------------------------->
<style>
  section ul li {
    margin: 10px 0;
  }

  section ul {
    padding-left: 23px;
  }
</style>
