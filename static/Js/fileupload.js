var fileuploadsrc = document.getElementById('file-upload-src');
var filenamesrc = document.getElementById('filename-src')

var fileuploadtarget = document.getElementById('file-upload-target');
var filenametarget = document.getElementById('filename-target')

fileuploadsrc.addEventListener('change',function() {
    
    var filepath = this.value;
    var m = filepath.match(/([^\/\\]+)$/);   
    var filename = m[1];    
    filenamesrc.textContent=filename
});

fileuploadtarget.addEventListener('change',function() {
    var filepath = this.value;
    var m = filepath.match(/([^\/\\]+)$/);
    var filename = m[1];
    filenametarget.textContent=filename
});