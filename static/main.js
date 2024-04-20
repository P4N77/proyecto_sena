document.addEventListener('DOMContentLoaded', function() {
    const addButtons = document.querySelectorAll('.add-btn');
    const quantityInputs = document.querySelectorAll('.quantity-input');
    const resultSpans = document.querySelectorAll('.result');

    addButtons.forEach((button, index) => {
        button.addEventListener('click', function() {
            var input = button.parentElement.parentElement.querySelector('.quantity-input');
            const name = button.getAttribute('data-name');
            const price = button.getAttribute('data-price');
            const quantity = parseInt(quantityInputs[index].value);
            const result = quantity * parseInt(price);
            const formattedResult = "$" + result.toFixed(2);

            if (parseFloat(input.value) <= 0) {
                    alert('Por favor, ingresa un número positivo.');
                    return;
                }else{
                    if (input.value.trim() === '') {
            alert('Por favor, ingresa un número antes de añadir.');
            return;
            }else{
    const confirmAdd = confirm(`¿Quieres agregar ${quantity} unidades de ${name} a la factura?`);
    if (confirmAdd) {
                const newRow = `<tr><td>${name}</td><td>${quantity}</td><td>${formattedResult}</td></tr>`;
                document.querySelector('#added-table tbody').innerHTML += newRow;
            }
}
                }
            
            
        });
    });

    document.querySelector('#guardar-btn').addEventListener('click', function() {

    const rows = document.querySelectorAll('#added-table tbody tr');
    if (rows.length === 0) {
        alert("No hay elementos añadidos para calcular.");
        return;
    }
    let total = 0;
    rows.forEach(row => {
        const totalCell = row.querySelector('td:nth-child(3)');
        const totalValue = parseFloat(totalCell.textContent.replace('$', ''));
        total += totalValue;
    });


    const totalDiv = document.querySelector('#total-div');
    totalDiv.textContent = `Total: $${total.toFixed(2)}`;
    document.querySelector('#print-btn').removeAttribute('disabled');
});


    document.querySelector('#print-btn').addEventListener('click', function() {
        window.print();
    });
});

var fechaDeHoy = new Date();


var dia = fechaDeHoy.getDate();
var mes = fechaDeHoy.getMonth() + 1; 
var año = fechaDeHoy.getFullYear();


if (dia < 10) {
dia = '0' + dia;
}
if (mes < 10) {
mes = '0' + mes;
}

var fechaFormateada = dia + '/' + mes + '/' + año;

document.getElementById('fechaDeHoy').innerText = "Fecha: " + fechaFormateada;