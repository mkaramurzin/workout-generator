document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#email').onclick = function() {
        let address = prompt("Enter your email address")
        fetch('email', {
            method: 'POST',
            body: JSON.stringify({
                address: address,
                plan: document.querySelector('#plan').innerHTML
            })
        })
        .then(response => response.json())
        .then(result => {
            alert(result.msg)
        })
        .catch(error => {
            console.log(error)
            alert('There was an Error')
        })
    }

})