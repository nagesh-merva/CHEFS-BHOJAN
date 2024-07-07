
const HAT = document.getElementById('Chefshat')
const DISCOUNT = document.getElementById('discount')
const submitbtn = document.getElementById('BTN')

document.getElementById('discountForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const name = document.getElementById('name').value
    const phone = document.getElementById('phone').value

    const formData = {
        name: name,
        phone: phone
    }

    try {
        const response = await saveFormData(formData)
        if (response.status === 'exists') {
            displayMessage(response.message)
        } else {
            submitbtn.classList.add('hidden')
            updateElements()
        }
    } catch (error) {
        console.error('Error:', error)
    }
});

async function saveFormData(formData) {
    try {
        const response = await fetch('http://localhost:8000/api/save_form_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData),
            credentials: 'include'
        });
        if (!response.ok) {
            throw new Error('Failed to save form data')
        }
        return response.json()
    } catch (error) {
        throw error
    }
}

function getRandomDiscount() {
    const values = [10, 20, 30, 40]
    const probabilities = [0.3, 0.5, 0.1, 0.1]

    let random = Math.random()
    let cumulativeProbability = 0

    for (let i = 0; i < values.length; i++) {
        cumulativeProbability += probabilities[i]
        if (random < cumulativeProbability) {
            return values[i]
        }
    }
}

function updateElements() {
    const Discount = getRandomDiscount()

    HAT.classList.remove('hidden')
    HAT.classList.add('animate-translate-scale')

    setTimeout(() => {
        DISCOUNT.innerText += Discount + "% Discount"
        DISCOUNT.classList.add('animate-scale')
        DISCOUNT.classList.remove('hidden')
    }, 1000)
}


function displayMessage(message) {
    const messageElement = document.createElement('div')
    messageElement.innerText = message
    messageElement.className = 'error-message px-8 absolute inset-0 h-screen w-screen flex items-center justify-center bg-amber-500 font-bold text-3xl text-white z-50'
    document.body.appendChild(messageElement)
}
