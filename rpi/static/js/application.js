$(document).ready( () =>{

    let socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

    socket.on('take_picture', (event) => {

        console.log('Event: ' + event);
        $('#log').html('<p>' + 'Event: ' + event + '</p>');
    });

    socket.on('uploading_image', (event) => {

        console.log('Event: ' + event);
        $('#log').html('<p>' + 'Event: ' + event + '</p>');
    });

    socket.on('traffic_light_detected', (event) => {

        console.log('Event: ' + event);
        $('#log').html('<p>' + 'Event: ' + event + '</p>');
    });

    socket.on('traffic_light_not_present', (event) => {

        console.log('Event: ' + event);
        $('#log').html('<p>' + 'Event: ' + event + '</p>');
    });

    socket.on('move_forward', (event) => {

        console.log('Event: ' + event);
        $('#log').html('<p>' + 'Event: ' + event + '</p>');
    });

    socket.on('running', (event) => {

        console.log('Event: ' + event);
        $('#log').html('<p>' + 'Event: ' + event + '</p>');
    });

    socket.on('stopped', (event) => {

        console.log('Event: ' + event);
        $('#log').html('<p>' + 'Event: ' + event + '</p>');
    });

    socket.on('image_uploaded', (event) => {

        console.log('Event: ' + event);
        $('#log').html('<p>' + 'Event: ' + event + '</p>');
    });

    socket.on('analyse_image', (event) => {

        console.log('Event: ' + event);
        $('#log').html('<p>' + 'Event: ' + event + '</p>');
    });
})