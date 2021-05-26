<script>
 const ABOUT_ME = [
    {
      DESCRIPTION: "Sardinian born software engineer, based in Stockholm, Sweden 🇸🇪",
      ICON: "fa-home"
    },
    {
      DESCRIPTION:"Software Engineer at EA DICE",
      ICON: "fa-laptop-code"
    },
    {
      DESCRIPTION:"Proud metalhead, football lover and gamer",
      ICON: "fa-bolt"
    },
    {
      DESCRIPTION: "History nerd, polyglot, bassist",
      ICON: "fa-book-reader"
    }
  ];
</script>
<!------------------------------------------->
<!----------------MARKUP----------------------->
<!------------------------------------------->

<section id="testimonials" class="section">
  <div class="container">
    <h1 class="title text-center deepmetal-logo mb-3">About me</h1>
    <div class="row justify-content-md-center section-body">
      <div class="col-md-5 my-pic text-center">
        <img class="img-fluid" src="/static/images/my-picture.jpg" alt="luca" />
      </div>
      <div class="col-md-7 my-details my-auto">
        <h2 class="deepmetal-logo mb-3">Luca Ballore</h2>
        <ul class="fa-ul">
          {#each ABOUT_ME as aboutMe}
            <li><span class="fa-li"><i class="fas {aboutMe.ICON}"></i></span>{aboutMe.DESCRIPTION}</li>
          {/each}
      </div>
    </div>
  </div>
</section>

<!------------------------------------------->
<!----------------STYLE----------------------->
<!------------------------------------------->
<style>
  .my-details ul li {
    margin-bottom: 16px;
  }

  .my-pic img {
    width: 90%;
    height: auto;
    border-radius: 50%;
  }

  .my-details {
    border-left: 4px solid black;
  }
</style>
