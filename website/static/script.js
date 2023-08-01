var d = new Date();
var n = d.toLocaleString(); // toLocaleString() returns the date and time in a localized format
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('generated-time').innerHTML = 'Generated on: ' + n;
});
