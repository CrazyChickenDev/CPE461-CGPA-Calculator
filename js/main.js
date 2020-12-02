// Insert the input fields for a new class into the table.
function addNewRow() {
    const tableBody = document.getElementById("tableBody");
    const tr = document.createElement("tr");

    const td = document.createElement("td");
    const td1 = document.createElement("td");
    const td2 = document.createElement("td");
    const input = document.createElement("input");
    const select1 = document.createElement("select");
    const select2 = document.createElement("select");

    const option11 = document.createElement("option");
    const option12 = document.createElement("option");
    const option13 = document.createElement("option");
    const option14 = document.createElement("option");
    const option15 = document.createElement("option");
    const option16 = document.createElement("option");
    const option21 = document.createElement("option");
    const option22 = document.createElement("option");
    const option23 = document.createElement("option");
    const option24 = document.createElement("option");
    const option25 = document.createElement("option");
    const option26 = document.createElement("option");

    input.type = "text";
    input.name = "courseCode";
    input.classList.add("code-input");

    select1.name = "creditUnit";
    select2.name = "grade";
    select1.classList.add("select");
    select2.classList.add("select");
    select1.setAttribute("onchange", "addUpCreditsGpa()");
    select2.setAttribute("onchange", "addUpCreditsGpa()");
    option11.innerHTML = "6";
    option12.innerHTML = "5";
    option13.innerHTML = "4";
    option14.innerHTML = "3";
    option15.innerHTML = "2";
    option16.innerHTML = "1";
    option21.innerHTML = "A";
    option22.innerHTML = "B";
    option23.innerHTML = "C";
    option24.innerHTML = "D";
    option25.innerHTML = "E";
    option26.innerHTML = "F";

    select1.appendChild(option11);
    select1.appendChild(option12);
    select1.appendChild(option13);
    select1.appendChild(option14);
    select1.appendChild(option15);
    select1.appendChild(option16);
    select2.appendChild(option21);
    select2.appendChild(option22);
    select2.appendChild(option23);
    select2.appendChild(option24);
    select2.appendChild(option25);
    select2.appendChild(option26);

    td.appendChild(input);
    td1.appendChild(select1);
    td2.appendChild(select2);
    tr.appendChild(td);
    tr.appendChild(td1);
    tr.appendChild(td2);

    tableBody.appendChild(tr);
}

function addUpCreditsGpa() {
    const creditUnit = document.querySelectorAll('[name = creditUnit]');
    const grade = document.querySelectorAll('[name = grade]');
    let totalUnit = document.querySelector("[name = totalUnit]").value = "";
    let gpa = document.querySelector("[name = gpa]").value = "";
    let option1 = "";
    let option2 = "";
    let a  = [];
    for (let i = 0; i < creditUnit.length; ++i) {
        option1 = creditUnit[i].options[creditUnit[i].selectedIndex].text;
        let totalUnit = document.querySelector("[name = totalUnit]").value;
        totalUnit = Number(totalUnit) + Number(option1);
        a.push(totalUnit);
    }
    let asum = a.reduce((partial_sum, a) => partial_sum + a,0); 

    let b = [];
    for (let i = 0; i < grade.length; ++i) {
        option2 = grade[i].options[grade[i].selectedIndex].text;
        let gpa = document.querySelector("[name = gpa]").value;
        let letterPoint = gradeToPoints(option2);
        let totalPoint = letterPoint;
        b.push(totalPoint);
    }
    let addAB = a.reduce(function(r,a,i){return r+a*b[i]},0);
    

    let gpaScore = parseFloat(addAB / asum).toFixed(2);
    document.querySelector("[name = totalUnit]").value = asum;
    document.querySelector("[name = gpa]").value = gpaScore;
}

//Return the points corresponding to the given letter
function gradeToPoints(grade) {   
    if ("A" == grade) {
        return 5.0;
    }
    else if ("B" == grade) {
        return 4.0;
    }
    else if ("C" == grade) {
        return 3.0;
    }
    else if ("D" == grade) {
        return 2.0;
    }
    else if ("E" == grade) {
        return 1.0;
    }
    else if ("F" == grade) {
        return 0.0;
    }
    else {
        //Guess we should we throw an exception here?
        return Invalid;
    }
}