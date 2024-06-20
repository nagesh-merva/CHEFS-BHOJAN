let Discount = 10

const HAT = document.getElementById('Chefshat')
const DISCOUNT = document.getElementById('discount')

document.getElementById('discountForm').addEventListener('submit', function (event) {
    event.preventDefault()

    const name = document.getElementById('name').value
    const phone = document.getElementById('phone').value

    const formData = {
        name: name,
        phone: phone
    };

    fetch('https://chefs-bhojan-mlz6.vercel.app/save_form_data', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData),

        credentials: 'include',
    })
        .then(response => response.text())
        .then(data => {
            fetchWeightedValue()
        })
        .catch((error) => {
            console.error('Error:', error)
            alert('ERROR, Please try again')
        })
});

function fetchWeightedValue() {
    fetch('https://chefs-bhojan-mlz6.vercel.app/get_discount_value', {
        method: 'GET',
        mode: 'cors',
        credentials: 'include',
    })
        .then(response => response.json())
        .then(data => {
            Discount = data.value
            console.log(Discount)
            updateElements()
        })
        .catch((error) => {
            console.error('Error fetching weighted value:', error)
        })
}


function updateElements() {
    HAT.classList.remove('hidden')
    HAT.classList.add('animate-translate-scale')
    setTimeout(() => {
        DISCOUNT.innerText += Discount + "% Discount"
        DISCOUNT.classList.add('animate-scale')
        DISCOUNT.classList.remove('hidden')
    }, 1000)
}
