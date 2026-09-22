function previewImage(input, previewId) {
    const preview = document.getElementById(previewId);
    const defaultIcon = document.getElementById('defaultIcon');
    
    if (input.files && input.files[0]) {
        
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
            defaultIcon.style.display = 'none';
        }
        reader.readAsDataURL(input.files[0]);
    }
}

//get state and city from pincode
function getPincodeDetails() {
    const pincode = document.getElementById('pincode').value;
    if (pincode.length === 6 || (pincode.length > 0 && pincode.length < 6)) {
        fetch(`https://api.postalpincode.in/pincode/${pincode}`)
            .then(response => response.json())
            .then(data => {
                if (data[0].Status === "Success") {
                    const postOffice = data[0].PostOffice[0];
                    document.getElementById('state').value = postOffice.State;
                    document.getElementById('city').value = postOffice.District;
                } else {
                    Swal.fire({
                        icon: "error",
                        title: "Invalid Pincode...",
                        text: "Please Enter Correct Pincode!"
                    });
                    clearAddressFields();
                }
            })
            .catch(error => {
                console.error("Error fetching pincode data:", error);
                clearAddressFields();
            });
    }
}

function clearAddressFields() {
    document.getElementById('state').value = '';
    document.getElementById('city').value = '';
}
