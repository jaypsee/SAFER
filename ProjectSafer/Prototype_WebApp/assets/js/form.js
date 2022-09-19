var selectedRow = null

function onFormSubmit() {
    if (validateNews()) {
        var formNews = readformNews();
        if (selectedRow == null)
            insertNewNews(formNews);
        else
            updateNews(formNews);
        resetNews();
    }
    if (validatePost()) {
        var formPost = readformPost();
        if (selectedRow == null)
            insertNewPost(formPost);
        else
            updatePost(formPost);
        resetPost();
    }
}

function readformNews() {
    var formNews = {};
    formNews["contentNews"] = document.getElementById("contentNews").value;
    return formNews;
}

function readformPost() {
    var formPost = {};
    formPost["contentPost"] = document.getElementById("contentPost").value;
    return formPost;
}

function insertNewNews(data) {
    var tableNews = document.getElementById("savedNews").getElementsByTagName('tbody')[0];
    var newNews = tableNews.insertRow(tableNews.length);
    cell1 = newNews.insertCell(0);
    cell1.innerHTML = data.contentNews;
    cell2 = newNews.insertCell(1);
    cell2.innerHTML = `<a class="buttonAction" id="savedNews" onClick="onEditNews(this)">Edit</a>
                       <a class="buttonAction" id="savedNews" onClick="onDeleteNews(this)">Delete</a>`;
    cell3 = newNews.insertCell(2);
    cell3.innerHTML = `<div class="dropdown action-label">
                       <a class="btn btn-white btn-sm rounded dropdown-toggle" href="#" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-dot-circle-o text-success"></i> Active <i class="caret"></i></a>
                       <ul class="dropdown-menu pull-right">
                           <li><a href="#"><i class="fa fa-dot-circle-o text-success"></i> Active</a></li>
                           <li><a href="#"><i class="fa fa-dot-circle-o text-danger"></i> Inactive</a></li>
                       </ul>
                   </div>`
}

function insertNewPost(data) {
    var tablePost = document.getElementById("savedPosts").getElementsByTagName('tbody2')[1];
    var newPost = tablePost.insertRow(tablePost.length);
    cell3 = newPost.insertCell(0);
    cell3.innerHTML = data.contentPost;
    cell4 = newPost.insertCell(1);
    cell4.innerHTML = `<div class="dropdown action-label">
                        <a class="btn btn-white btn-sm rounded dropdown-toggle" href="#" data-toggle="dropdown" aria-expanded="false"><i class="fa fa-dot-circle-o text-success"></i> Active <i class="caret"></i></a>
                        <ul class="dropdown-menu pull-right">
                            <li><a href="#"><i class="fa fa-dot-circle-o text-success"></i> Active</a></li>
                            <li><a href="#"><i class="fa fa-dot-circle-o text-danger"></i> Inactive</a></li>
                        </ul>
                    </div>`
}


function resetNews() {
    document.getElementById("contentNews").value = "";
    selectedRow = null;
}

function resetPost() {
    document.getElementById("contentPost").value = "";
    selectedRow = null;
}

function onEditNews(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("contentNews").value = selectedRow.cells[0].innerHTML;
}

function onEditPost(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("contentPost").value = selectedRow.cells[0].innerHTML;
}

function updateNews(formNews) {
    selectedRow.cells[0].innerHTML = formNews.contentNews;
}

function updatePost(formPost) {
    selectedRow.cells[0].innerHTML = formPost.contentNews;
}

function onDeleteNews(td) {
    if (confirm('Are you sure to delete this record ?')) {
        row = td.parentElement.parentElement;
        document.getElementById("savedNews").deleteRow(row.rowIndex);
        resetNews();
    }
}

function onDeletePost(td) {
    if (confirm('Are you sure to delete this record ?')) {
        row = td.parentElement.parentElement;
        document.getElementById("savedPosts").deleteRow(row.rowIndex);
        resetNews();
    }
}

function validateNews() {
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

function validatePost() {
    isValid = true;
    if (document.getElementById("contentPost").value == "") {
        isValid = false;
        document.getElementById("contentPostValidationError").classList.remove("hide");
    } else {
        isValid = true;
        if (!document.getElementById("contentPostValidationError").classList.contains("hide"))
            document.getElementById("contentPostValidationError").classList.add("hide");
    }
    return isValid;
}