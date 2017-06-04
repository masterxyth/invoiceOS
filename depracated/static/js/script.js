var today = new Date();
var elDate;

function todayDate(today) {
    var day, date, month, year, dayNames, monthNames, currDate;
    dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    day = dayNames[today.getDay()];
    date = today.getDate();
    month = monthNames[today.getMonth()];
    year = today.getFullYear();

    currDate = date + " " + month + " " + year;
    return currDate;
}

elDate = document.getElementById('date');
elDate.textContent = todayDate(today);
