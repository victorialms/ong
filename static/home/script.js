let count = 1;
document.getElementById("radio1").checked = true;

let interval = setInterval(nextImage, 5000);

function nextImage() {
    count++;
    if (count > 4) {
        count = 1;
    }
    document.getElementById("radio" + count).checked = true;
}

// Função para resetar o intervalo ao selecionar uma nova imagem
function resetInterval(selectedCount) {
    count = selectedCount;
    clearInterval(interval);
    document.getElementById("radio" + count).checked = true;
    interval = setInterval(nextImage, 5000);
}

// Adicione eventos de clique aos botões de seleção
for (let i = 1; i <= 4; i++) {
    document.getElementById("radio" + i).addEventListener("click", function() {
        resetInterval(i);
    });
}



// header 
let lastScrollTop = 0;
const header = document.querySelector('.custom-header');

window.addEventListener('scroll', function() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
        // Esconde o header quando o usuário rolar para baixo
        header.style.top = "-200px"; // ajuste o valor com base na altura do seu header
    } else {
        // Mostra o header quando o usuário rolar para cima
        header.style.top = "0";
    }

    lastScrollTop = scrollTop;
});

function inscreverEmail() {
    const emailInput = document.getElementById("email");
    const email = emailInput.value.trim();
  
    if (email && email.includes("@")) {
      // Simula uma inscrição e exibe uma mensagem de confirmação
      alert("Inscrição realizada com sucesso! Obrigado por se inscrever.");
      emailInput.value = "";  // Limpa o campo após a inscrição
    } else {
      alert("Por favor, insira um e-mail válido.");
    }
  }

// Botão que scrolla pro topo da página:
const scrollUpBtn = document.getElementById('scrollUpBtn');

window.addEventListener('scroll', () => {
  if (window.scrollY === 0) {
    scrollUpBtn.classList.add('hidden');
  } else {
    scrollUpBtn.classList.remove('hidden');
  }
});

scrollUpBtn.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});
