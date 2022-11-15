$(function()
{
    let arr = $('.PriceDesc');
    let clearArr = new Array();
    for(let i = 0;i<arr.length;i++){
        let price = $(arr[i]).html();
        price = price.replace('$','');
        price = price.replace('.','');
        clearArr.push(price);
    };
    let arrNewValues = new Array();
    for(let i = 0;i<arr.length;i++){
        arrNewValues.push('$'+Math.round(parseInt(clearArr[i])*0.95));
        $('.PriceDesc').text(arrNewValues[i]);
        arr[i].classList.replace('PriceDesc','Price');
    }
});