/**
 * This function makes a call to the backend API.
 * @param {*} data Contains all the values to feed to the algorithm
 * @returns An api response containing algorithm related data
 */
const findRoute = async (data) => {
    console.log("Inside PostGetPath");

    let api_response = await fetch('http://localhost:5000//find_route', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': String.valueOf(data.length),
            'Host': 'localhost:5000'
        },
        body: data
    }).then(response => response.json())
        .then(sucess_msg => {
            console.log('Successful:', sucess_msg);
            return sucess_msg
        })
        .catch((error_msg) => { 
            console.error('Unsuccessful:', error_msg);
            return error_msg.message
        });

    return api_response
}

export default findRoute