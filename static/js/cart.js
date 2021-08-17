const updateBtns = document.getElementById('addToCart');
updateBtns.addEventListener('click', function () {
    const productId = this.dataset.product;
    const action = this.dataset.action;
    console.log('productId:', productId, 'action:', action)
    console.log('User:', user)
    if (user === 'AnonymousUser') {
        console.log('Not logged in')
    } else {
        console.log('User is logging')
        updateUserOrder(productId, action)
    }
})

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data..')
    const dataOrder = {'productId': productId, 'action': action}
    $.ajax({
        url: '/order/update_item/',
        headers: {"X-CSRFToken": csrftoken},
        type: 'POST',
        data: JSON.stringify(dataOrder),
        contentType: 'application/json',
        dataType: 'json'
    });

    location.reload()

}