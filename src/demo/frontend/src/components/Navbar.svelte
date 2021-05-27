<script>
  const NAVBAR_DATA = [
    { id: 1, url: "/", label: "Home" },
    { id: 2, url: "#project", label: "Project" },
    { id: 3, url: "#demo", label: "Demo" },
    { id: 4, url: "#about-me", label: "About me" },
    { id: 5, url: "#social-media", label: "Contacts" }
  ];

  function autoToggleNavbar() {
    window.$(".navbar-collapse").collapse('hide');
  }
</script>

<!------------------------------------------->
<!----------------MARKUP----------------------->
<!------------------------------------------->
<section id="nav-bar">
  <nav class="navbar main-bgcolor navbar-expand-md navbar-dark">
    <a class="navbar-brand deepmetal-logo" href="/">
      DeepMetal
    </a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation">
      <span class="navbar-toggler-icon" />
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ml-auto">
        {#each NAVBAR_DATA as section}
          <li class="nav-item">
            <a class="nav-link" on:click="{autoToggleNavbar}" href={section.url}>{section.label}</a>
          </li>
        {/each}
      </ul>
    </div>
  </nav>
</section>

<!------------------------------------------->
<!----------------STYLE----------------------->
<!------------------------------------------->
<style>
  #nav-bar {
    position: sticky;
    top: 0;
    z-index: 10;
  }

  .navbar {
    padding: 5px 20px !important;
  }

  .navbar-nav li {
    padding: 0 0 0 20px;
  }

  .navbar-nav li a {
    font-family: "MetalMania";
    text-transform: uppercase;
    float: right;
    text-align: left;
  }
</style>