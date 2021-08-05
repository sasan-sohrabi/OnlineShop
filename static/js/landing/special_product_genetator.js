function special_product_genetator(data) {
    console.log("Im Here")
    for (let drink in data) {
        let cardGenerator = document.getElementById('cardGenerator')

        let divCol = document.createElement('div')
        divCol.classList.add("col-12")
        divCol.classList.add("col-sm-6")
        divCol.classList.add("col-md-6")
        divCol.classList.add("col-lg-4")
        divCol.classList.add("filter")
        divCol.classList.add("col-12")
        divCol.style.marginTop="20px";
        divCol.style.borderRadius= "30%";
        divCol.classList.add(data[drink]["category"])
        divCol = cardGenerator.appendChild(divCol)

        let divCard = document.createElement('div')
        divCard.classList.add("card")
        divCard.classList.add("bg-nav")
        divCard.classList.add("h-100")
        divCard.style.padding = "5%"
        divCard = divCol.appendChild(divCard)

        let img = document.createElement('img')
        img.classList.add("card-img")
        img.style.borderRadius="80%"
        img.src = "/static/images/" + data[drink]['img']

        img = divCard.appendChild(img)

        let divCarBody = document.createElement('div')
        divCarBody.classList.add("card-body")
        divCarBody = divCard.appendChild(divCarBody)

        let title_h4 = document.createElement('h4')
        title_h4.classList.add("card-title")
        title_h4 = divCarBody.appendChild(title_h4)

        let spanTitle = document.createElement('span')
        spanTitle.classList.add("shop-item-title")
        spanTitle.innerText = data[drink]["name"]
        spanTitle = title_h4.appendChild(spanTitle)

        let idData = document.createElement('span')
        idData.classList.add("data-id")
        idData.setAttribute("type", "hidden")
        idData.innerText = drink
        idData = divCarBody.appendChild(idData)

        let divBuy = document.createElement('div')
        divBuy.classList.add("buy")
        divBuy.classList.add("d-flex")
        divBuy.classList.add("justify-content-between")
        divBuy.classList.add("align-items-center")
        divBuy = divCarBody.appendChild(divBuy)

        let divPrice = document.createElement('div')
        divPrice.classList.add("price")
        divPrice.classList.add("text-success")
        divPrice.classList.add("text-center")
        divPrice = divBuy.appendChild(divPrice)

        let spanPrice = document.createElement('span')
        spanPrice.classList.add("shop-item-price")
        spanPrice.innerText = data[drink]["price"] + "$"
        spanPrice = divPrice.appendChild(spanPrice)

        let btnCart = document.createElement('btn')
        btnCart.classList.add("btn")
        btnCart.style.backgroundColor ="rgba(80, 61, 43, 0.68)"
        btnCart.classList.add("HoverClass1")
        btnCart.classList.add("btn-large")
        btnCart.classList.add("shop-item-button")
        btnCart.setAttribute('aria-hidden', 'true')
        btnCart.setAttribute('type', 'button')
        btnCart.innerText = "Add to cart"
        let i = document.createElement('i')
        i.classList.add("fa");
        i.classList.add("fa-shopping-cart");
        i = btnCart.appendChild(i);
        btnCart = divBuy.appendChild(btnCart);
    }
}


