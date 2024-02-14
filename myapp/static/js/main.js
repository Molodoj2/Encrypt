function clearText() {
    document.getElementById("input_for_encrypt").value = "";
}

function copyText() {
    var textarea = document.getElementById("encrypted");
    textarea.select();
    document.execCommand("copy");
    window.getSelection().removeAllRanges();
    alert("Текст скопійовано!");
}

function copyKey() {
    var textarea = document.getElementById("encryption_key");
    textarea.select();
    document.execCommand("copy");
    window.getSelection().removeAllRanges();
    alert("Текст скопійовано!");
}

