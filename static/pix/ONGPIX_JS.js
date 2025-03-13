let currentImageIndex = 0; // Índice da imagem atual
const images = [
    'static/pix/ONG_IMG/c_kid1.png', // Imagem 1
    'static/pix/ONG_IMG/c_kid2.png', // Imagem 2
    'static/pix/ONG_IMG/c_kid3.png' // Imagem 3
];

function changeImage(imageIndex) {
    const image = document.getElementById('image');
    currentImageIndex = imageIndex; // Atualiza o índice da imagem atual
    image.src = images[currentImageIndex]; // Altera a imagem
    updateActiveCircle(); // Atualiza o círculo ativo
}

function startSlideshow() {
    const image = document.getElementById('image');
    setInterval(() => {
        currentImageIndex = (currentImageIndex + 1) % images.length; 
        image.src = images[currentImageIndex]; 
        updateActiveCircle();
    }, 2500); // Muda a imagem a cada 3 segundos
}

function updateActiveCircle() {
    const circles = document.querySelectorAll('.circle');
    circles.forEach((circle, index) => {
        circle.classList.remove('active');
        if (index === currentImageIndex) {
            circle.classList.add('active');
        }
    });
}

window.onload = startSlideshow;

    let lastScrollTop = 0;
    const header = document.querySelector('.custom-header');

    window.addEventListener('scroll', function() {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        if (scrollTop > lastScrollTop) {
            // Esconde o header quando o usuário rolar para baixo
            header.style.top = "-100px"; // ajuste o valor com base na altura do seu header
        } else {
            // Mostra o header quando o usuário rolar para cima
            header.style.top = "0";
        }

        lastScrollTop = scrollTop;
    });

  // Função para armazenar o valor da doação no Local Storage e redirecionar
  function setDonationValue(value) {
    // Salva o valor da doação no Local Storage
    localStorage.setItem("donationValue", value);

    // Redireciona para a página de doação (ONGPIX2_HTML)
    window.location.href = "pix2"
  }

  // Pega o valor da doação armazenado no Local Storage
  const donationValue = localStorage.getItem("donationValue");

  // Se houver valor armazenado, exibe no campo correto
  if (donationValue) {
    document.getElementById("donationValue").innerText = "R$ " + donationValue;
  } else {
    document.getElementById("donationValue").innerText = "R$ 30,00"; // Valor padrão caso não haja nada no Local Storage
  }
