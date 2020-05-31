$(document).ready( () => {
    let socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', () => {
        socket.send('Client connected');
    });

    socket.on('TAKING_IMAGE', message => {
        console.log('TAKING_IMAGE: ' + message);
        // $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('IMAGE_TAKEN', message => {
        console.log('IMAGE_TAKEN: ' + JSON.stringify(message));
        // $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('UPLOADING_IMAGE', message => {
        console.log('UPLOADING_IMAGE: ' + message);
        // $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('IMAGE_UPLOADED', message => {
        console.log('IMAGE_UPLOADED: ' + JSON.stringify(message));
        // $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('ANALYSING_IMAGE', message => {
        console.log('ANALYSING_IMAGE: ' + message);
        // $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('TRAFFIC_LIGHT_DETECTED', message => {
        console.log('TRAFFIC_LIGHT_DETECTED: ' + message);
        // $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('TRAFFIC_LIGHT_NOT_PRESENT', message => {
        console.log('TRAFFIC_LIGHT_NOT_PRESENT: ' + message);
        // $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('MOVING_FORWARD', message => {
        console.log('MOVING_FORWARD: ' + message);
        // $('#log').append(`<p> ${message} </p>`);
    });

    socket.on('STOPPED', message => {
        console.log('STOPPED: ' + message);
        // $('#log').append(`<p> ${message} </p>`);
    });
});