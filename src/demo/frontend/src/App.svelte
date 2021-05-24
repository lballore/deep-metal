<script>
  import Navbar from "./components/Navbar.svelte";
  import Banner from "./components/Banner.svelte";
  import Project from "./components/Project.svelte";
  import Demo from "./components/Demo.svelte";
  import About from "./components/About.svelte";
  import Social from "./components/Social.svelte";
  import Footer from "./components/Footer.svelte";
  import DATA from "./data/data";
  console.log(DATA);
</script>

<!-- Navbar -->
<Navbar />
<!-- Banner -->
<Banner />
<!-- Project -->
<Project />
<!-- Demo -->
<Demo />
<!-- Testimonials -->
<About />
<!-- Social Media -->
<Social socialData={DATA.SOCIAL_DATA} />
<!-- Footer -->
<Footer footerData={DATA.FOOTER_DATA} header={DATA.HEADER} />
