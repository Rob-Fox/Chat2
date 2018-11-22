$(document).ready(function(){
    var roomName = 'index';

    var chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/' + roomName + '/'
    );

    chatSocket.onmessage = function (e) {
        var data = JSON.parse(e.data);
        var message = data['message'];
        var user = data['user'];
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
    var x = 0;
    document.querySelector('#c_m_submit').onclick = function (e) {
        if(x == 0){
            var messageInputDom = document.querySelector('#chat_message_input');
            var message = messageInputDom.value;

            var U_N = document.querySelector('#U_N');
            document.getElementById('user').value = U_N.value;
            U_N.parentNode.removeChild(index_name);
            U_N.parentNode.removeChild(U_N);

            var user = $('#user').val();
            chatSocket.send(JSON.stringify({
                'user': user + ': ',
                'message': message,
            }));

            messageInputDom.value = '';
            x = 1;

        }
        else{
            var messageInputDom = document.querySelector('#chat_message_input');
            var message = messageInputDom.value;

            var user = $('#user').val();
            chatSocket.send(JSON.stringify({
                'user': user + ': ',
                'message': message,
            }));

            messageInputDom.value = '';
        }
    };
})