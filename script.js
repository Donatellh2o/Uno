const cardForm = document.getElementById('card');

cardForm.onsubmit = (event) => {
    event.preventDefault();
    const cardcolors = document
        .getElementById('color')
        .value
        .substring(1)
        .match(/.{1,2}/g);
    const aRgb = [
        parseInt(cardcolors[0], 16),
        parseInt(cardcolors[1], 16),
        parseInt(cardcolors[2], 16)
    ];
    const cardnumber = document.getElementById('key').value;
    console.log(aRgb);
    console.debug(cardnumber);
    const link = createLink(aRgb, cardnumber);
  
    window.open(link, "_blank");
    console.debug(link);
};

function createLink(color, cardNumber) {
    const params = new URLSearchParams();
    params.append('key', cardNumber);
    params.append('rgb', color);

    return `http://127.0.0.1:5000/with_parameters?${params.toString()}`;
}




