function sendEmail() {
    var recipient = "contato@henriquesebastiao.com";
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;
    var mailtoLink = "mailto:" + recipient + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(message);
    window.location.href = mailtoLink;
}