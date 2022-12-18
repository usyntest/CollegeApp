const alert_type = document.querySelector('#alert')
const confession_type = document.querySelector('#confession')
const speciality_type = document.querySelector('#speciality')
const speciality = document.querySelector('.speciality')
const submitBtn = document.querySelector('.submit-btn')
const cloutInput = document.querySelector('.clout-input')

let cloutCount = 0

alert_type.addEventListener('change', () => {
    speciality.classList.remove('hidden')
    clout_count = 5
})

confession_type.addEventListener('change', () => {
    speciality.classList.add('hidden')
    speciality_type.checked = false
})

speciality.addEventListener('change', () => {
    if (speciality_type.checked === true) {
        clout_count = 10;
    } else {
        clout_count = 5
    }
})

submitBtn.addEventListener('click', () => {
    cloutInput.value = cloutCount
})
