function showContent(sectionId) {
    // Esconder todos os containers de conteúdo
    document.querySelectorAll('.content').forEach(function(content) {
        content.style.display = 'none';
    });

    // Mostrar o container correspondente ao menu clicado
    document.getElementById(sectionId).style.display = 'block';

    // Atualizar a classe 'active' dos links do menu
    document.querySelectorAll('.nav-link').forEach(function(link) {
        link.classList.remove('active');
        link.classList.add('link-body-emphasis');
    });

    // Adicionar a classe 'active' ao link clicado
    event.currentTarget.classList.add('active');
    event.currentTarget.classList.remove('link-body-emphasis');
}
