let lastScrollTop = 0;
const header = document.querySelector('.custom-header');

header.style.position = 'fixed';
header.style.top = '0';
header.style.width = '100%';

window.addEventListener('scroll', function() {
  let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  if (scrollTop > lastScrollTop) {
    header.style.top = "-300px";
  } else {
    header.style.top = "0";
  }
  lastScrollTop = scrollTop;
});

// Seleciona os links de navegação do Header e da Navegação Lateral
const headerNavLinks = document.querySelectorAll('.header-nav-link');
const sidebarNavLinks = document.querySelectorAll('.sidebar-nav-link');

// Função para remover a classe 'active' de uma lista de links específica
function removeActiveClass(links) {
  links.forEach(link => link.classList.remove('active'));
}

// Função para ocultar todas as seções e remover as classes 'active' dos links
function hideAllSections() {
  document.querySelectorAll('.section-content').forEach(section => {
    section.style.display = 'none';
  });
  
  document.querySelectorAll('.section-articles').forEach(articles => {
    articles.style.display = 'none';
  });
}

// Evento para cada link de navegação no Header
headerNavLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    const sectionId = link.getAttribute('data-section');
    if (sectionId) {
      event.preventDefault();
      hideAllSections(); // Oculta todas as seções
      removeActiveClass(headerNavLinks); // Remove 'active' de todos os links do Header

      // Exibe a seção correspondente
      document.getElementById(sectionId).style.display = 'block';
      
      // Exibe a seção de artigos correspondente, se existir
      const articlesSectionId = sectionId + '-articles';
      const articlesSection = document.getElementById(articlesSectionId);
      if (articlesSection) {
        articlesSection.style.display = 'block';
      }

      // Adiciona a classe 'active' ao link clicado
      link.classList.add('active');
      console.log('Mostrando seção:', sectionId);
      console.log('Mostrando seção de artigos:', articlesSectionId);
    }
  });
});

// Evento para cada link de navegação na barra lateral
sidebarNavLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    const sectionId = link.getAttribute('data-section');
    if (sectionId) {
      event.preventDefault();
      hideAllSections(); // Oculta todas as seções
      removeActiveClass(sidebarNavLinks); // Remove 'active' de todos os links da barra lateral

      // Exibe a seção correspondente
      document.getElementById(sectionId).style.display = 'block';

      // Exibe a seção de artigos correspondente, se existir
      const articlesSectionId = sectionId + '-articles';
      const articlesSection = document.getElementById(articlesSectionId);
      if (articlesSection) {
        articlesSection.style.display = 'block';
      }

      // Adiciona a classe 'active' ao link clicado
      link.classList.add('active');
      console.log('Mostrando seção:', sectionId);
      console.log('Mostrando seção de artigos:', articlesSectionId);
    }
  });
});

// Função para ocultar todas as seções apenas na coluna direita
function hideAllRightSections() {
  document.querySelectorAll('.rightColumn .section-content').forEach(section => {
    section.style.display = 'none';
  });
}

// Função para mostrar os detalhes de "Casa Geriátrica Divinavó"
function showDivinavoDetails() {
  hideAllRightSections();
  document.getElementById('divinavo-info').style.display = 'block';
}

document.getElementById('learnMoreDivinavo').addEventListener('click', showDivinavoDetails);

// Função para mostrar os detalhes de "Distribuição de Quentinhas"
function showQuentinhaDetails() {
  hideAllRightSections();
  document.getElementById('quentinha-info').style.display = 'block';
}

document.getElementById('learnMoreQuentinha').addEventListener('click', showQuentinhaDetails);

// Função para mostrar os detalhes de "Semana Cultural"
function showCulturaDetails() {
  hideAllRightSections();
  document.getElementById('cultura-info').style.display = 'block';
}

document.getElementById('learnMoreCultura').addEventListener('click', showCulturaDetails);

// Função para mostrar os detalhes de "Hemório"
function showHemorioDetails() {
  hideAllRightSections();
  document.getElementById('hemorio-info').style.display = 'block';
}

document.getElementById('learnMoreHemorio').addEventListener('click', showHemorioDetails);


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