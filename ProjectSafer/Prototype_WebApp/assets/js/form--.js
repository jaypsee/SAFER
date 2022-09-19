var selectedRow = null

function onFormSubmit() {
    if (validate()) {
        var formData = readFormData();
        if (selectedRow == null)
            insertNewRecord(formData);
        else
            updateRecord(formData);
        resetForm();
    }
}

function readFormData() {
    var formData = {};
    formData["contentNews"] = document.getElementById("contentNews").value;
    return formData;
}

function insertNewRecord(data) {
    var table = document.getElementById("savedNews").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.contentNews;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = `<a class="buttonPrev" onClick="onEdit(this)">Edit</a>
                       <a class="buttonPrev" onClick="onDelete(this)">Delete</a>`;
}

function resetForm() {
    document.getElementById("contentNews").value = "";
    selectedRow = null;
}

function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("contentNews").value = selectedRow.cells[0].innerHTML;
}
function updateRecord(formData) {
    selectedRow.cells[0].innerHTML = formData.contentNews;
}

function onDelete(td) {
    if (confirm('Are you sure to delete this record ?')) {
        row = td.parentElement.parentElement;
        document.getElementById("savedNews").deleteRow(row.rowIndex);
        resetForm();
    }
}
function validate() {
    isValid = true;
    if (document.getElementById("contentNews").value == "") {
        isValid = false;
        document.getElementById("contentNewsValidationError").classList.remove("hide");
    } else {
        isValid = true;
        if (!document.getElementById("contentNewsValidationError").classList.contains("hide"))
            document.getElementById("contentNewsValidationError").classList.add("hide");
    }
    return isValid;
}