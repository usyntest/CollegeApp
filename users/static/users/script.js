const crossBtnMessage = document.querySelector('.single-message-close-btn')
const singleMsg = document.querySelector('.single-message')

crossBtnMessage?.addEventListener('click', () => {
    singleMsg.classList.add('hidden')
})