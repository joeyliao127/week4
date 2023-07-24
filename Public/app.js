const checkbox = document.querySelector("#contract");
const submit = document.querySelector("#submit");
const alert = document.querySelector(".alert p");
const calculator = document.querySelector(".calculator button");
const num = document.querySelector(".calculator input");
const num_alert_text = document.querySelector(".calcu_alert");
console.log(`checkbox=  ${checkbox}`);
console.log(checkbox.checked);
submit.addEventListener("click", (event) => {
  if (checkbox.checked) {
    console.log("checkbox已勾選");
  } else {
    console.log("checkbox未勾選");
    alert.style.display = "block";
    event.preventDefault();
  }
});

calculator.addEventListener("click", (event) => {
  if (num.value % 1 != 0) {
    event.preventDefault();
    num_alert_text.textContent = "(請輸入正整數)";
    num_alert_text.style.display = "block";
  } else if (!num.value) {
    event.preventDefault();
    num_alert_text.textContent = "(請輸入數字)";
    num_alert_text.style.display = "block";
  } else if (num.value < 0) {
    event.preventDefault();
    num_alert_text.textContent = "(請輸入大於0的整數)";
    num_alert_text.style.display = "block";
  }
});
