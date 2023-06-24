let updateBtns = document.getElementsByClassName('item');
for ( let i=0; i<updateBtns.length; i++ ){
    updateBtns[i].addEventListener('click',function (){
        let productId = this.dataset.product
        console.log()
        console.log('productId: ' + productId);

        console.log("User: ", user)
        if (user == "AnonymousUser"){
            console.log("User is not authenticated")
        }else{
             goToDetailedView(productId);
        }
    })
}

addToCart = document.getElementById("addToCart");
addToCart.addEventListener('click', function (){
    let selectedSize = document.querySelector('input[name="size"]:checked').value;
    addToCart.setAttribute('data-size',selectedSize);
    let sizeD = this.dataset.size;
    if (user == "AnonymousUser"){
            console.log("User is not authenticated")
    }else{
            updateItem(sizeD);
    }
})

function updateItem(size){
    let url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'size':size})
    })
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log('Data: ', data)
            location.reload()
        })
}

function goToDetailedView(productId){
    console.log('User is authenticated, sending data..')

    let url = '/go_to_detailed_view/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId})
    })
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log('Data: ', data)
            location.assign("http://127.0.0.1:8000/detailedView")
        })
}