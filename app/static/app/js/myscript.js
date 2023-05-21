$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 2,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 4,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 6,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})
const n = ({ path: e }) => {
    if (e && Array.isArray(e)) {
      return e.map((e) => e.className).join(" ").includes("css-inspector-cta");
    }
    return false; // or handle the case where `e` is not defined or not an array
  };
  
  if ("HTML" === t.tagName || "BODY" === t.tagName || n(e)) {
    // Rest of your code
  }
  

$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2] 
    console.log("pid =", id)
    $.ajax({
        type:"GET",
        url:"/pluscart/",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data =", data);
            eml.innerText=data.quantity 
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2] 
    $.ajax({
        type:"GET",
        url:"/minuscart/",
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText=data.quantity;
            document.getElementById("amount").innerText=data.amount;
            document.getElementById("totalamount").innerText=data.totalamount;
        }
    })
})


$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("amount").innerText=data.amount; 
            document.getElementById("totalamount").innerText=data.totalamount;
            eml.parentNode.parentNode.parentNode.parentNode.remove() ;
        }
    })
})


$('.plus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/pluswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            //alert(data.message)
            window.location.href = `http://localhost:8000/product-detail/${id}`
        }
    })
})


$('.minus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/minuswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            window.location.href = `http://localhost:8000/product-detail/${id}`
        }
    })
})