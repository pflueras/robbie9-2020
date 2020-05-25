$(document).ready( () =>{

    let socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', ()=>{

        socket.send('Client connected');
    });

    socket.on('message', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });
});