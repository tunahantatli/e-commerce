// Get references to the elements
const minusButtons = document.querySelectorAll('.minus-cart');
const plusButtons = document.querySelectorAll('.plus-cart');
const removeButtons = document.querySelectorAll('.remove-cart');
const quantityElements = document.querySelectorAll('#quantity');
const amountElement = document.getElementById('amount');
const totalAmountElement = document.getElementById('totalamount');

// Add event listeners to minus buttons
minusButtons.forEach(button => {
  button.addEventListener('click', function() {
    const productId = button.getAttribute('pid');
    const quantityElement = document.querySelector(`#quantity[pid="${productId}"]`);
    let quantity = parseInt(quantityElement.textContent);
    if (quantity > 1) {
      quantity--;
      quantityElement.textContent = quantity;
      updateTotalAmount();
    }
  });
});

// Add event listeners to plus buttons
plusButtons.forEach(button => {
  button.addEventListener('click', function() {
    const productId = button.getAttribute('pid');
    const quantityElement = document.querySelector(`#quantity[pid="${productId}"]`);
    
    let quantity = parseInt(quantityElement.textContent);
    quantity++;
    quantityElement.textContent = quantity;
    updateTotalAmount();
  });
});

// Add event listeners to remove buttons
removeButtons.forEach(button => {
  button.addEventListener('click', function() {
    const productId = button.getAttribute('pid');
    const rowElement = button.closest('.row');
    rowElement.remove();
    updateTotalAmount();
  });
});

// Function to update the total amount
function updateTotalAmount() {
  let totalAmount = 0;
  quantityElements.forEach(element => {
    const quantity = parseInt(element.textContent);
    const priceElement = element.closest('.row').querySelector('strong');
    const price = parseFloat(priceElement.textContent.replace('$ ', ''));
    totalAmount += quantity * price;
  });

  amountElement.textContent = '$ ' + totalAmount.toFixed(2);
  totalAmountElement.textContent = '$ ' + totalAmount.toFixed(2);
}
