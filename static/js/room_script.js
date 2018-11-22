$(document).ready(function () {
    var roomName = window.location.href.split('/');
    roomName = roomName[roomName.length-1];
    // roomName = roomName.split('/')
    // console.log(roomName.split('/'));
    // console.log(roomName);
    // console.log(roomName);
    // var roomName = {{ room_name_json }};

    var chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/' + roomName + '/'
    );

    chatSocket.onmessage = function (e) {
        var data = JSON.parse(e.data);
        // console.log(e);
        var message = data['message'];
        var user = data['user'];
        // console.log(user, message);
        // document.querySelector('#chat_log').value += (user + message + '\n');
        $('#chat_log').append("<span class='user'>" + user + "</span><span class = 'message'>" + message + "</span><br>");
    };

    chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly');
        console.error(e);
    };

    document.querySelector('#chat_message_input').focus();
    document.querySelector('#chat_message_input').onkeyup = function (e) {
        if (e.keyCode === 13) { // check if return is pressed on submit button
            document.querySelector('#c_m_submit').click();
        }
    };

    document.querySelector('#c_m_submit').onclick = function (e) {
        var messageInputDom = document.querySelector('#chat_message_input');
        var message = messageInputDom.value;
        var user = $('#user').val();
        console.log(user);
        chatSocket.send(JSON.stringify({
            'user': user + ': ',
            'message': message,
        }));

        messageInputDom.value = '';
    };
})