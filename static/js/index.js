let warFrequency = {
  "label": "War Frequency",
  "options": [
    { label: "Any", value: "any" },
    { label: "Always", value: "always" },
    { label: "Never", value: "never" },
    { label: "Twice a week", value: "moreThanOncePerWeek" },
    { label: "Once a week", value: "oncePerWeek" },
    { label: "Rarely", value: "unknown" }]}

let warF = document.querySelector('#warFrequency');
for (var i = 0; i < warFrequency["options"].length; i++) {
  let warFOption = `<option value="${warFrequency["options"][i]['value']}">${warFrequency["options"][i]['label']}</option>`;
  warF.innerHTML += `${warFOption}`;
}

let arrow = document.querySelector('.ASButton svg')
arrow.style.transform = 'rotate(0deg)';
document.querySelector('.ASButton').addEventListener('click', ()=>{
  let taginp = document.getElementById('taginp');
  let websiteTittle = document.querySelector('#websiteTittle');
  let ASButton = document.querySelector('#ASButton')
  if (arrow.style.transform == 'rotate(0deg)') {
    arrow.style.transform = 'rotate(90deg)';
    websiteTittle.style.display = 'none';
    taginp.style.display = 'none';
    ASButton.style.display = 'none';
  }
  else{
    arrow.style.transform = 'rotate(0deg)';
    websiteTittle.style.display = 'block';
    taginp.style.display = 'block';
    ASButton.style.display = 'block';
  }
});
let CLInp = document.querySelector('#CLInp');
let plus = document.querySelector('#plus');
let minus = document.querySelector('#minus');

plus.addEventListener('click',()=>{
  let trophyValue = CLInp.value;
  let a = Number(trophyValue) + 500;
  CLInp.value = a;
});
minus.addEventListener('click', () => {
  let trophyValue = CLInp.value;
  let a = Number(trophyValue);
  if (a < 500) {
    b = a - 0;
  } else {
    b = a - 500;
  }
  CLInp.value = b;
});
let customRange1 = document.querySelector('#customRange1');
let rangeValue = document.querySelector('#rangeValue');
customRange1.addEventListener('input', ()=>{
  let value99 = customRange1.value;
  rangeValue.innerHTML = value99;
});
let customRange2 = document.querySelector('#customRange2');
let rangeValue2 = document.querySelector('#rangeValue2');
customRange2.addEventListener('input', () => {
  let value99 = customRange2.value;
  rangeValue2.innerHTML = value99;
});
let customRange3 = document.querySelector('#customRange3');
let rangeValue3 = document.querySelector('#rangeValue3');
customRange3.addEventListener('input', () => {
  if (customRange2.value > customRange3.value) {
    customRange3.min = parseInt(customRange2.value) + 1;
  }
  else if(customRange2.value < customRange3.value) {
    customRange3.min = parseInt(customRange2.value) +1;
  }
  let value99 = customRange3.value;
  rangeValue3.innerHTML = value99;
});
  
let css = `
border: 0.7px solid green;!important;
box-shadow: 0px 0px 0px 5px #18C10061;!important`;
let css2 = `
border: 0.7px solid red;!important;
box-shadow: 0px 0px 0px 5px rgba(198,40,40,0.5);!important`;

let AdvanceSbtn = document.querySelector('#AdvanceSbtn');
let ASButton = document.querySelector("#ASButton")
let taginp = document.getElementById("taginp");
let validation = document.querySelector('#validation');
window.addEventListener('DOMContentLoaded', (event) => {
AdvanceSbtn.style.display = 'block';
taginp.value = "";
    });
  
  taginp.addEventListener("input",fVelediction);
  
  function fVelediction(){
    let InpLength = taginp.value.length;
    // console.log(InpLength);
    if(InpLength <= 2){
      ASButton.disabled = true;
      taginp.setAttribute('style',css2);
    }
    else{
      ASButton.disabled = false;
      taginp.setAttribute('style',css);
    }
  }
  
 
