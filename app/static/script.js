const btnGenerate = document.querySelector("#generate-pdf");

btnGenerate.addEventListener("click", () => {

    //conteudo do pdf
    const content = document.querySelector("#content")

    //configuração do arquivo final
    const options = {
        margin: [2, 3, 3, 2],
        filename: "Pedido.pdf",
        html2canvas: {scale: 1},
        jsPDF: {unit:"mm", format: "a4", orientation: "portrait"}
    }

    // Gerar e baixar o pdf
    html2pdf().set(options).from(content).save();

})