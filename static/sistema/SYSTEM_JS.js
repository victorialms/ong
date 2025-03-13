function login(event) {
    event.preventDefault(); // Evita o recarregamento da página

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "admin" && password === "ong1124") {
        window.location.href = "/sistema2"; // Redireciona para a rota Flask
    } else {
        alert("Nome de usuário ou senha incorretos!");
    }
}