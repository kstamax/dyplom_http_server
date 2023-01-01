const lst = document.getElementById("itemsList");
const chatSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/main/devicelog'
);
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data)
    lst.innerHTML = `${data.message}`;
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
buildTable();

function buildTable() {
    const message = 'hello world';
    chatSocket.send(JSON.stringify({
        'message': message
    }));
}