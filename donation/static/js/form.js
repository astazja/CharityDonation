console.log('form js');
const institutionInputs = document.querySelectorAll('.institution input');
document.querySelectorAll('.institution').forEach(input => input.style.display = 'none');

document.querySelectorAll('.category input').forEach(input => {
    input.addEventListener('change', function (e) {
        const isChecked = e.target.checked;
        const institutionsToPrint = categories[e.target.value];
        for (let value of institutionsToPrint) {
            for (let input of institutionInputs) {
                if (Number(input.value) === Number(value)) {
                    if (isChecked) {
                        input.parentElement.parentElement.style.display = 'block'
                    } else {
                        input.parentElement.parentElement.style.display = 'none'
                    }
                }
            }
        }
    })
});

var summaryData = document.querySelectorAll('.summary--text');
var btnsNext = document.querySelectorAll('.next-step');

institutionInputs.forEach(input => {
    input.addEventListener('change', (e) => {
        if (e.target.checked) {
            var text = input.parentElement.querySelector('.title');
            summaryData[1].textContent = `Dla ${text.textContent}`;
        }
    })
});

var bagsAmount = document.querySelector('.bags label input');
btnsNext[1].addEventListener('click', (e) => {
    if (bagsAmount.value) {
        summaryData[0].textContent = `Liczba oddanych worków: ${bagsAmount.value}`
    } else {
        summaryData[0].textContent = 'Nie oddano żadnych worków.'
    }
});

var deliveryData = [...document.querySelectorAll('.delivery-data input'), document.querySelector('.delivery-data textarea')];
var deliverySummary = document.querySelectorAll('.delivery-summary li');

btnsNext[3].addEventListener('click', (e) => {
    for (var i = 0; i < deliveryData.length; i++) {
        if (deliveryData[i].value) {
            deliverySummary[i].textContent = deliveryData[i].value
        } else {
            deliverySummary[i].textContent = 'Nie podano';
        }
    }
});