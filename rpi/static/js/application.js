$(document).ready( () =>{

    let socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', ()=>{

        socket.send('Client connected');
    });

    socket.on('message', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('take_picture', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('uploading_image', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('traffic_light_detected', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('traffic_light_not_present', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('move_forward', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('running', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('stopped', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('image_uploaded', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('analyse_image', message => {

        console.log(message);
        $('#log').append(`<p> ${message} </p>`);
    });
});