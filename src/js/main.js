
const HAT = document.getElementById('Chefshat')
const DISCOUNT = document.getElementById('discount')

document.getElementById('discountForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const name = document.getElementById('name').value
    const phone = document.getElementById('phone').value

    const formData = {
        name: name,
        phone: phone
    }

    try {
        await saveFormData(formData)
        await fetchWeightedValue()
    } catch (error) {
        console.error('Error:', error)
        alert('ERROR, Please try again')
    }
});

async function saveFormData(formData) {
    try {
        const response = await fetch('https://chefs-bhojan-backend.vercel.app/api/save_form_data', {
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
        updateElements()
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