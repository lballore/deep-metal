<script>
  const SOCIAL_LIST = [
    {
      ICON: "fa-linkedin",
      NAME: "LinkedIn",
      PROFILE_URL: "https://www.linkedin.com/in/lucaballore/"
    },
    {
      ICON: "fa-github",
      NAME: "GitHub",
      PROFILE_URL: "https://github.com/lucone83"
    },
    {
      ICON: "fa-medium",
      NAME: "Medium",
      PROFILE_URL: "https://blog.lucaballore.com"
    },
    {
      ICON: "fa-twitter",
      NAME: "Twitter",
      PROFILE_URL: "https://twitter.com/LBallore"
    }
  ]
</script>

<!------------------------------------------->
<!----------------MARKUP----------------------->
<!------------------------------------------->
<section id="social-media" class="section grey-bgcolor">
  <div class="container text-center">
    <h1 class="title text-center deepmetal-logo">Find me on social media</h1>
    <div class="social-icons section-body">
      {#each SOCIAL_LIST as social}
        <a
          class="mr-3"
          title={social.NAME}
          href={social.PROFILE_URL}
          target="_blank">
          <i class="fa fab fa-3x {social.ICON}"></i>
        </a>
      {/each}
    </div>
  </div>
</section>

<!------------------------------------------->
<!----------------STYLE----------------------->
<!------------------------------------------->
<style>
  .social-icons a {
    text-decoration: none;
    transition: 0.5s;
    color: #212529;
  }

  .social-icons a:hover {
    text-decoration: none;
    color: rgb(66, 66, 66) !important;
  }
</style>
