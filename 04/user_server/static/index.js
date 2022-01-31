var addUserSubmit = document.getElementById('add-user-submit');
addUserSubmit.addEventListener('click', function(e) {
    e.preventDefault();
    var username = document.getElementById('add-user-username').value;
    var password = document.getElementById('add-user-password').value;
    var data = {
        username: username,
        password: password
    };
    var request = new XMLHttpRequest();
    request.open('POST', '/add-user');
    request.setRequestHeader('Content-Type', 'application/json');
    request.addEventListener('load', function() {
        if (request.status === 200) {
            alert('User ' + username + ' added successfully!');
            window.location.href = '/';
        } else {
            // print the error
            alert('Error: ' + request.responseText);
        }
    });
    request.send(JSON.stringify(data));
});

var loginSubmit = document.getElementById('login-submit');
loginSubmit.addEventListener('click', function(e) {
    e.preventDefault();
    var username = document.getElementById('login-username').value;
    var password = document.getElementById('login-password').value;
    var data = {
        username: username,
        password: password
    };
    var request = new XMLHttpRequest();
    request.open('POST', '/login');
    request.setRequestHeader('Content-Type', 'application/json');
    request.addEventListener('load', function() {
        if (request.status === 200) {
            alert('User ' + username + ' logged in successfully!');
            window.location.href = '/';
        } else {
            // print the error
            alert('Error: ' + request.responseText);
        }
    });
    request.send(JSON.stringify(data));
});
