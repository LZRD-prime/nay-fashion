// JS pour Nay Fashion – élégance fluide

// Scroll fluide vers les sections
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) target.scrollIntoView({ behavior: 'smooth' });
  });
});

// Apparition des sections au scroll
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('show');
  });
});
document.querySelectorAll('.section').forEach(section => observer.observe(section));

// Animation sur le bouton de formulaire
document.querySelectorAll('form button').forEach(button => {
  button.addEventListener('click', () => {
    button.textContent = "Redirection...";
    button.classList.add("added");

    // Réinitialisation du bouton après 2 secondes
    setTimeout(() => {
      if (button.classList.contains("added")) {
        button.textContent = "Envoyer";
        button.classList.remove("added");
      }
    }, 2000);
  });
});
// Validation du formulaire
document.querySelector('form').addEventListener('submit', function (e) {
  e.preventDefault();
  const name = this.querySelector('input[name="name"]').value;
  const email = this.querySelector('input[name="email"]').value;

  if (name && email) {
    alert(`Merci ${name}, votre message a été envoyé !`);
    this.reset();
  } else {
    alert("Veuillez remplir tous les champs.");
  }
});
// Gestion de la navigation mobile
document.querySelector('.menu-toggle').addEventListener('click', () => {
  document.querySelector('.nav-links').classList.toggle('active');

  document.querySelector('.menu-toggle').classList.toggle('active');
  document.body.classList.toggle('no-scroll');
});