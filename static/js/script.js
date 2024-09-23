let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");
let searchBtn = document.querySelector(".bx-search");

btn.onclick = function () {
    sidebar.classList.toggle("active");
}
searchBtn.onclick = function () {
    sidebar.classList.toggle("active");
}

// function myFunction() {
//     document.getElementById("mybtn").style.visibility = "hidden";
// }

// function myFunction2() {
//     document.getElementById("mybtn2").style.visibility = "visible";
// }

// document.getElementById('mybtn_cor').addEventListener('click', function () {
//     var table2excel = new Table2Excel();
//     table2excel.export(document.querySelectorAll("#stud_table"));
// });

document.getElementById('mybtn_cor').addEventListener('click', function () {
    var table2excel = new Table2Excel();
    table2excel.export(document.querySelectorAll("#stud_table"));
});