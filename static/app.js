const $list = $('ul')
const $form = $('form')

async function getCupcakes(){
    const res = await axios.get('/api/cupcakes')
    cupcakes = res.data.cupcakes

    cupcakes.forEach(cake => {
        let li = $(`<li>${cake.flavor}</li>`)
        let img = $(`<img src="${cake.image} >`)
        li.append(img)
        $list.append(li)
    });
}

getCupcakes()

$form.on('submit', async (e) => {
   e.preventDefault()

    let flavor = $('#flavor').val()
    let size = $('#size').val()
    let rating = $('#rating').val()
    let image = $('#image').val()

    console.log(flavor, size, rating, image)

    const addCupcake = await axios.post('http://localhost:5000/api/cupcakes', { flavor, size, rating, image})

    

    $list.empty()
    getCupcakes()
    
})

