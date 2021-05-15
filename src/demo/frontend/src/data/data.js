const HEADER = "DeepMetal";

const NAVBAR_DATA = [
  { id: 1, url: "/", label: "Home" },
  { id: 2, url: "#demo", label: "Demo" }, // services
  { id: 3, url: "#project", label: "Project" }, // about-us
  { id: 4, url: "#about-me", label: "About me" }, // testimonials
  { id: 5, url: "#footer", label: "Contacts" } // contacts
];

const BANNER_DATA = {
  HEADING: "DeepMetal",
  DECRIPTION:
    "AI-generated heavy metal lyrics, based on OpenAI GPT-2 model.",
};

const DEMO_DATA = {
  HEADING: "Try the demo!",
  ALL_SERVICES: "All Services",
};

const ABOUT_DATA = {
  HEADING: "Why choose us?",
  TITLE: "Why we're different",
  IMAGE_URL: "/static/images/network.png",
  WHY_CHOOSE_US_LIST: [
    "We provides Cost-Effective Digital Marketing than Others.",
    "High customer statisfaction and experience.",
    "Marketing efficiency and quick time to value.",
    "Clear & transparent fee structure.",
    "We provides Marketing automation which is an integral platform that ties all of your digital marketing together.",
    "A strong desire to establish long lasting business partnerships.",
    "Provide digital marketing to mobile consumer.",
    "We provides wide range to services in reasonable prices"
  ]
};

const TESTIMONIAL_DATA = {
  HEADING: "What clients say?",
  TESTIMONIAL_LIST: [
    {
      DESCRIPTION:
        "Nixalar has made a huge difference to our business with his good work and knowledge of SEO and business to business marketing techniques. Our search engine rankings are better than ever and we are getting more people contacting us thanks to Jomer’s knowledge and hard work.",
      IMAGE_URL: "/static/images/user1.jpg",
      NAME: "Julia hawkins",
      DESIGNATION: "Co-founder at ABC"
    },
    {
      DESCRIPTION:
        "Nixalar and his team have provided us with a comprehensive, fast and well planned digital marketing strategy that has yielded great results in terms of content, SEO, Social Media. His team are a pleasure to work with, as well as being fast to respond and adapt to the needs of your brand.",
      IMAGE_URL: "/static/images/user2.jpg",
      NAME: "John Smith",
      DESIGNATION: "Co-founder at xyz"
    }
  ]
};

const SOCIAL_DATA = {
  HEADING: "Find us on social media",
  IMAGES_LIST: [
    "/static/images/facebook-icon.png",
    "/static/images/instagram-icon.png",
    "/static/images/whatsapp-icon.png",
    "/static/images/twitter-icon.png",
    "/static/images/linkedin-icon.png",
    "/static/images/snapchat-icon.png"
  ]
};

const FOOTER_DATA = {
  DESCRIPTION:
    "We are typically focused on result-based maketing in the digital world. Also, we evaluate your brand’s needs and develop a powerful strategy that maximizes profits.",
  CONTACT_DETAILS: {
    HEADING: "Contact us",
    ADDRESS: "La trobe street docklands, Melbourne",
    MOBILE: "+1 61234567890",
    EMAIL: "nixalar@gmail.com"
  },
  SUBSCRIBE_NEWSLETTER: "Subscribe newsletter",
  SUBSCRIBE: "Subscribe"
};

const MOCK_DATA = {
  HEADER,
  NAVBAR_DATA,
  BANNER_DATA,
  DEMO_DATA,
  ABOUT_DATA,
  TESTIMONIAL_DATA,
  SOCIAL_DATA,
  FOOTER_DATA
};
export default MOCK_DATA;
