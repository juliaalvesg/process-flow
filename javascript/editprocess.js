var modal = document.getElementById('myModal');
var form = document.getElementById("processForm");


window.onload = function() {
    var tipoCliente = localStorage.getItem("tipoCliente");
    var nomeCliente = localStorage.getItem("nomeCliente");
    var causaProcesso = localStorage.getItem("causaProcesso");
    var dataHora = localStorage.getItem("dataHora");
    var andamento = localStorage.getItem("andamento");
    var infoAdicionais = localStorage.getItem("infoAdicionais");

    document.getElementById("tipoCliente").value = tipoCliente || "fisica";
    document.getElementById("nomeCliente").value = nomeCliente || "";
    document.getElementById("causaProcesso").value = causaProcesso || "";
    document.getElementById("dataHora").value = dataHora || "";
    document.getElementById("andamento").value = andamento || "";
    document.getElementById("infoAdicionais").value = infoAdicionais || "";

    
    modal.style.display = "block";
}


form.onsubmit = function(event) {
    event.preventDefault(); 

   
    var tipoCliente = document.getElementById("tipoCliente").value;
    var nomeCliente = document.getElementById("nomeCliente").value;
    var causaProcesso = document.getElementById("causaProcesso").value;
    var dataHora = document.getElementById("dataHora").value;
    var andamento = document.getElementById("andamento").value;
    var infoAdicionais = document.getElementById("infoAdicionais").value;

 
    localStorage.setItem("tipoCliente", tipoCliente);
    localStorage.setItem("nomeCliente", nomeCliente);
    localStorage.setItem("causaProcesso", causaProcesso);
    localStorage.setItem("dataHora", dataHora);
    localStorage.setItem("andamento", andamento);
    localStorage.setItem("infoAdicionais", infoAdicionais);

   
    location.reload();

    
    modal.style.display = "none";
}
