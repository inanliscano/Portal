function searchRecords() {
    let input = document.getElementById("search").value.toLowerCase();
    let table = document.getElementById("records-body");
    let rows = table.getElementsByTagName("tr");

    for (let row of rows) {
        let cells = row.getElementsByTagName("td");
        let found = false;

        for (let cell of cells) {
            if (cell.innerText.toLowerCase().includes(input)) {
                found = true;
                break;
            }
        }

        row.style.display = found ? "" : "none";
    }
}