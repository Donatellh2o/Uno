const cardForm = document.getElementById('card');

cardForm.onsubmit = (event) => {
    event.preventDefault();

    const cardcolors = document
        .getElementById('color')
        .value
        .substring(1)
        .match(/.{1,2}/g);

    const chosen_color = [
        parseInt(cardcolors[0], 16),
        parseInt(cardcolors[1], 16),
        parseInt(cardcolors[2], 16)
    ];
    
    aRgb = [8,6,240];
    
    cardcolor_b = document.getElementById('color_b').value;
``
    if (document.querySelector('#togg1').checked === true) {
      aRgb = chosen_color;
    }

    if (document.querySelector('#togg2').checked === true){

        if (cardcolor_b == "red") aRgb = [200, 75, 51];

        if (cardcolor_b == "yellow") aRgb = [246, 214, 89];

        if (cardcolor_b == "blue") aRgb = [51, 116, 181];

        if (cardcolor_b == "green") aRgb = [146, 190, 83];
    }
    
    if (document.querySelector('#togg3').checked === true) {
      cardnumber = 'complete'
      aRgb = [0,0,0]
      const link = createLink(aRgb, cardnumber);
      window.open(link, "_blank");
    }

    if (document.querySelector('#togg3').checked === false) {
      cardnumber = document.getElementById('key').value;
      const link = createLink(aRgb, cardnumber);
      window.open(link, "_blank");
    }
}

function createLink(color, cardNumber) {
    const params = new URLSearchParams();
    params.append('key', cardNumber);
    params.append('rgb', color);

    return `http://127.0.0.1:5000/with_parameters?${params.toString()}`;
}







document.addEventListener('DOMContentLoaded', function() {
    const radioInputs = document.querySelectorAll('input[type="radio"]');
  
    radioInputs.forEach(function(radioInput) {
      radioInput.addEventListener('click', function() {
        const val = radioInput.getAttribute('value');
        const target = document.querySelector(`.${val}`);
        const messages = document.querySelectorAll('.msg');
  
        messages.forEach(function(message) {
          if (message !== target) {
            message.style.display = 'none';
          }
        });
  
        target.style.display = 'block';
      });
    });
  }); 