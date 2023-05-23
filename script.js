const cardForm = document.getElementById('card');

cardForm.onsubmit = (event) => {
    event.preventDefault();
    
    aRgb = [];

    if (document.querySelector('#choice1').checked === true) {
        cardNumber = 'complete'
        aRgb = [0,0,0]
    }
    
    if (document.querySelector('#choice2').checked === true) {

        if (document.querySelector('#choice3').checked === true) {
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

            aRgb = chosen_color
            cardNumber = document.getElementById('key1').value;

        }

        else if (document.querySelector('#choice4').checked === true){

            cardcolor_b = document.getElementById('color_b').value;

            if (cardcolor_b == "red") {
            aRgb = [200, 75, 51];
            }

            if (cardcolor_b == "yellow") {
            aRgb = [246, 214, 89];
            }

            if (cardcolor_b == "blue") {
            aRgb = [51, 116, 181];
            }

            if (cardcolor_b == "green") {
            aRgb = [146, 190, 83];
            }

            cardNumber = document.getElementById('key2').value;
        }
        
        if (document.querySelector('#choice5').checked === true){
            
            cardNumber = document.getElementById('key3').value;
            aRgb = [0, 0, 0]

        }
    }

    const link = createLink(aRgb, cardNumber);
    window.open(link, "_blank");
}

function createLink(color, cardNumber) {
    const params = new URLSearchParams();
    params.append('key', cardNumber);
    params.append('rgb', color);

    return `http://10.66.10.71:5000/with_parameters?${params.toString()}`;
}







document.addEventListener('DOMContentLoaded', function() {
    const radioInputs = document.querySelectorAll('input[name="checkbox_1"]');
  
    radioInputs.forEach(function(radioInput) {
      radioInput.addEventListener('click', function() {
        const val = radioInput.getAttribute('value');
        const target = document.querySelector(`.${val}`);
        const messages = document.querySelectorAll('.msg1');
  
        messages.forEach(function(message) {
          if (message !== target) {
            message.style.display = 'none';
          }
        });
  
        target.style.display = 'block';
      });
    });
  }); 





  document.addEventListener('DOMContentLoaded', function() {
    const radioInputs = document.querySelectorAll('input[name="checkbox_2"]');
  
    radioInputs.forEach(function(radioInput) {
      radioInput.addEventListener('click', function() {
        const val = radioInput.getAttribute('value');
        const target = document.querySelector(`.${val}`);
        const messages = document.querySelectorAll('.msg2');
  
        messages.forEach(function(message) {
          if (message !== target) {
            message.style.display = 'none';
          }
        });
  
        target.style.display = 'block';
      });
    });
  }); 

  once();

  function once(){
    const messages1 = document.querySelectorAll('.msg1');
    messages1.forEach(function(message) {
        message.style.display = 'none';
    })
    
    const messages2 = document.querySelectorAll('.msg2');
    messages2.forEach(function(message) {
        message.style.display = 'none';
    })
    
  }