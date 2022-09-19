function accessSCADA() {
    var controlCode = prompt("Enter Access Code:");
    if (controlCode == "5678") {
        return;
    } else {
        alert("Invalid Code") /*displays error message*/
        window.history.back();
    }
}

var clockElement = document.getElementById('clock');

function clock() {
    clockElement.textContent = new Date().toLocaleString();
}
setInterval(clock, 1000);

// Find the right method, call on correct element
function launchFullScreen(element) {
    if (element.requestFullScreen) {
        element.requestFullScreen();
    } else if (element.mozRequestFullScreen) {
        element.mozRequestFullScreen();
    } else if (element.webkitRequestFullScreen) {
        element.webkitRequestFullScreen();
    }
}



// object literal holding data for option elements
var Select_List_Data = {
    'facility': // name of associated select box
    {
        // names match option values in controlling select box
        Area1: {
            text: ['[Facility]', 'Gate', 'Ground', 'Lobby', 'Office1', 'Office2', 'Office3', 'Office4', 'Office5', 'Office6', 'Office7', 'Office8', 'Office9'],
            value: ['#', 'gate', 'ground', 'lobby', 'control-office1.html', 'control-office2.html', 'OFC3', 'OFC4', 'OFC5', 'OFC6', 'OFC7', 'OFC8', 'OFC9']
        },
        Area2: {
            text: ['[Facility]', 'Rm 201', 'Rm 202', 'Rm 203', 'Rm 204', 'Rm 205', 'Rm 206', 'Rm 207', 'Rm 208', 'Rm 209', 'Rm 210', 'Rm 211', 'Rm 212'],
            value: ['#', 'R201', 'R202', 'R203', 'R204', 'R205', 'R206', 'R207', 'R208', 'R209', 'R210', 'R211', 'R212']
        },
        Area3: {
            text: ['[Facility]', 'Rm 301', 'Rm 302', 'Rm 303', 'Rm 304', 'Rm 305', 'Rm 306', 'Rm 307', 'Rm 308', 'Rm 309', 'Rm 310', 'Rm 311', 'Rm 312'],
            value: ['#', 'R301', 'R302', 'R303', 'R304', 'R305', 'R306', 'R307', 'R308', 'R309', 'R310', 'R311', 'R312']
        },
        Area4: {
            text: ['[Facility]', 'Rm 401', 'Rm 402', 'Rm 403', 'Rm 404', 'Rm 405', 'Rm 406', 'Rm 407', 'Rm 408', 'Rm 409', 'Rm 410', 'Rm 411', 'Rm 412'],
            value: ['#', 'R401', 'R402', 'R403', 'R404', 'R405', 'R406', 'R407', 'R408', 'R409', 'R410', 'R411', 'R412']
        },
        AreaEtc: {
            text: ['[Facility]', 'Rooftop 1', 'Rooftop 2', 'Rooftop 3', '---', '---', '---', '---', '---', '---', '---', '---', '---', ],
            value: ['#', 'etc1', 'etc2', 'etc3', 'etc4', 'etc5', 'etc6', 'etc7', 'etc8', 'etc9', 'etc10', 'etc11', 'etc12']
        },
        Default: {
            text: ['[Facility]'],
            value: ['#', ]
        }
    }
};

// removes all option elements in select box 
// removeGrp (optional) boolean to remove optgroups
function removeAllOptions(sel, removeGrp) {
    var len, groups, par;
    if (removeGrp) {
        groups = sel.getElementsByTagName('optgroup');
        len = groups.length;
        for (var i = len; i; i--) {
            sel.removeChild(groups[i - 1]);
        }
    }

    len = sel.options.length;
    for (var i = len; i; i--) {
        par = sel.options[i - 1].parentNode;
        par.removeChild(sel.options[i - 1]);
    }
}

function appendDataToSelect(sel, obj) {
    var f = document.createDocumentFragment();
    var labels = [],
        group, opts;

    function addOptions(obj) {
        var f = document.createDocumentFragment();
        var o;

        for (var i = 0, len = obj.text.length; i < len; i++) {
            o = document.createElement('option');
            o.appendChild(document.createTextNode(obj.text[i]));

            if (obj.value) {
                o.value = obj.value[i];
            }

            f.appendChild(o);
        }
        return f;
    }

    if (obj.text) {
        opts = addOptions(obj);
        f.appendChild(opts);
    } else {
        for (var prop in obj) {
            if (obj.hasOwnProperty(prop)) {
                labels.push(prop);
            }
        }

        for (var i = 0, len = labels.length; i < len; i++) {
            group = document.createElement('optgroup');
            group.label = labels[i];
            f.appendChild(group);
            opts = addOptions(obj[labels[i]]);
            group.appendChild(opts);
        }
    }
    sel.appendChild(f);
}

// anonymous function assigned to onchange event of controlling select box
document.forms['demoForm'].elements['area'].onchange = function(e) {
    // name of associated select box
    var relName = 'facility';

    // reference to associated select box 
    var relList = this.form.elements[relName];

    // get data from object literal based on selection in controlling select box (this.value)
    var obj = Select_List_Data[relName][this.value];

    // remove current option elements
    removeAllOptions(relList, true);

    // call function to add optgroup/option elements
    // pass reference to associated select box and data for new options
    appendDataToSelect(relList, obj);
};


// populate associated select box as page loads
(function() { // immediate function to avoid globals

    var form = document.forms['demoForm'];

    // reference to controlling select box
    var sel = form.elements['area'];
    sel.selectedIndex = 0;

    // name of associated select box
    var relName = 'facility';
    // reference to associated select box
    var rel = form.elements[relName];

    // get data for associated select box passing its name
    // and value of selected in controlling select box
    var data = Select_List_Data[relName][sel.value];

    // add options to associated select box
    appendDataToSelect(rel, data);

}());



function gotoPage(select) {
    var code = prompt("Enter Access Code:");
    if (code === null) {
        return;
    }
    if (code == "5678") {
        window.location.replace('control-office1.html')
    } else {
        alert("Invalid Code") /*displays error message*/
    }
}


function openArea(evt, areaName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(areaName).style.display = "block";
    evt.currentTarget.className += "active";
}


$(function() {
    $('#searchKeyword').keyup(filter);

    function filter() {
        var rex = new RegExp($('#searchKeyword').val(), 'i');
        var rows = $('.searchable tr');

        rows.hide();

        rows.filter(function() {

            var tester = true;

            tester = rex.test($(this).text());

            tester = tester && filterOnTable(this);

            return tester;
        }).show();
    }

    function filterOnTable(selector) {
        var tester = true;
        return tester;
    }
});


function download_csv(csv, filename) {
    var csvFile;
    var downloadLink;

    // CSV FILE
    csvFile = new Blob([csv], { type: "text/csv" });

    // Download link
    downloadLink = document.createElement("a");

    // File name
    downloadLink.download = filename;

    // We have to create a link to the file
    downloadLink.href = window.URL.createObjectURL(csvFile);

    // Make sure that the link is not displayed
    downloadLink.style.display = "none";

    // Add the link to your DOM
    document.body.appendChild(downloadLink);

    // Lanzamos
    downloadLink.click();
}

function toggleMenu() {
    var x = document.getElementById("sidebar");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

function showPreviewOne(event) {
    if (event.target.files.length > 0) {
        let src = URL.createObjectURL(event.target.files[0]);
        let preview = document.getElementById("uploadImage");
        preview.src = src;
        preview.style.display = "block";
    }
}

function myImgRemoveFunctionOne() {
    document.getElementById("uploadImage").src = "assets/img/placeholder.png";
}

function viewDevice() {
    var accessCode = prompt("Enter Access Code:");
    if (accessCode == null) {
        return;
    }
    if (accessCode == "5678") {
        window.open('view-device.html') /*opens the target page while Id & password matches*/
    } else {
        alert("Invalid Code") /*displays error message*/
    }
}