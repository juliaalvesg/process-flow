var processos = JSON.parse(localStorage.getItem('processos')) || [];

function loadScript() {
    displayProcessList();
}

document.getElementById('infoForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var data = document.getElementById('data').value;
    var cliente = document.getElementById('cliente').value;
    var causa = document.getElementById('causa').value;
    var numeroProcesso = generateProcessNumber();
    var processo = {
        numero: numeroProcesso,
        data: data,
        cliente: cliente,
        causa: causa
    };
    processos.push(processo);
    saveProcessosToLocalStorage();
    displayProcessList();
    document.getElementById('advogado').value = '';
    document.getElementById('cliente').value = '';
    document.getElementById('causa').value = '';
});

document.getElementById('searchBtn').addEventListener('click', function() {
    var searchValue = document.getElementById('search').value.trim();
    var foundProcess = processos.find(function(processo) {
        return processo.numero === searchValue;
    });
    if (foundProcess) {
        alert('Processo encontrado! Número do processo: ' + foundProcess.numero);
    } else {
        alert('Processo não encontrado.');
    }
});

function displayProcessList() {
    var processList = document.getElementById('processList');
    processList.innerHTML = '';
    processos.forEach(function(processo) {
        var listItem = document.createElement('li');
        listItem.textContent = 'Processo: ' + processo.numero + ', Cliente: ' + processo.cliente + ', Causa: ' + processo.causa + ', Data: ' + processo.data;
        
        var downloadBtn = document.createElement('button');
        downloadBtn.textContent = 'Baixar PDF';
        downloadBtn.addEventListener('click', function() {
            downloadProcessAsPDF(processo);
        });
        
        listItem.appendChild(downloadBtn);
        processList.appendChild(listItem);
    });
}

function generateProcessNumber() {
    // Vai gerar um número aleatório de 6 dígitos
    return Math.floor(Math.random() * 900000) + 100000;
}

function saveProcessosToLocalStorage() {
    localStorage.setItem('processos', JSON.stringify(processos));
}

function downloadProcessAsPDF(processo) {
    window.jsPDF = window.jspdf.jsPDF;
    var doc = new jsPDF();
    doc.text(20, 20, 'Processo: ' + processo.numero);
    doc.text(20, 30, 'Data: ' + processo.data);
    doc.text(20, 40, 'Cliente: ' + processo.cliente);
    doc.text(20, 50, 'Causa: ' + processo.causa);

    try {
        doc.save('processo_' + processo.numero + '.pdf');
    } catch (error) {
        console.error('Erro ao baixar o PDF:', error);
    }
}

document.getElementById('clearBtn').addEventListener('click', function() {
    clearProcessList(); 
});