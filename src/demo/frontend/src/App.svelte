<script>
  import Navbar from "./components/Navbar.svelte";
  import Banner from "./components/Banner.svelte";
  import Demo from "./components/Demo.svelte";
  import About from "./components/About.svelte";
  import Testimonials from "./components/Testimonials.svelte";
  import Social from "./components/Social.svelte";
  import Footer from "./components/Footer.svelte";
  import DATA from "./data/data";
  console.log(DATA);
</script>

<!-- Navbar -->
<Navbar navlists={DATA.NAVBAR_DATA} header={DATA.HEADER} />
<!-- Banner -->
<Banner bannerData={DATA.BANNER_DATA} />
<!-- Demo -->
<Demo demoData={DATA.DEMO_DATA} />
<!-- About -->
<About aboutData={DATA.ABOUT_DATA} />
<!-- Testimonials -->
<Testimonials testimonialData={DATA.TESTIMONIAL_DATA} />
<!-- Social Media -->
<Social socialData={DATA.SOCIAL_DATA} />
<!-- Footer -->
<Footer footerData={DATA.FOOTER_DATA} header={DATA.HEADER} />
