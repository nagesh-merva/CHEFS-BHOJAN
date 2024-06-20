let Discount = 10

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
        return response.json()
    } catch (error) {
        throw error;
    }
}

async function fetchWeightedValue() {
    try {
        const response = await fetch('https://chefs-bhojan-backend.vercel.app/api/get_discount_value', {
            method: 'GET',
            credentials: 'include'
        });
        if (!response.ok) {
            throw new Error('Failed to fetch weighted value')
        }
        const data = await response.json();
        Discount = data.value;
        console.log(Discount);
        updateElements();
    } catch (error) {
        throw error;
    }
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
