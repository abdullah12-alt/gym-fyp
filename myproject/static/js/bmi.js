const calculateBMI = () => {
    const weight = document.getElementById("weight").value;
    const height = document.getElementById("height").value;
    const bmi = (weight / ((height/100) ** 2)).toFixed(2);
    let result = "";
    if (weight == 0 && height == 0) {
        result = `Please Enter the Required Fields`;}
    else if (bmi < 18.5) {
        result = `Underweight: ${bmi}`;
    } else if (bmi >= 18.5 && bmi <= 24.9) {
        result = `Normal weight: ${bmi}`;
    } else if (bmi >= 25 && bmi <= 29.9) {
        result = `Overweight: ${bmi}`;
    } else if(bmi >= 30 && bmi <= 65){
        result = `Obesity: ${bmi}`;
    }else {
        result = `Went Something Wrong `;
    }

    document.getElementById("result").innerHTML = result;
}

document.getElementById("calculate-btn").addEventListener("click", calculateBMI);
