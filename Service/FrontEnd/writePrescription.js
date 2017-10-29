function prescribe(){
	patientPublicKey = $("#patientPublicKey").val();
	doctorPublicKey = $("#doctorPrimaryKey").val();
	disease = $("#disease").val();
	treatment = $("#treatment").val();
	treatmentStatus = $("#treatmentStatus").val();
	$("#doctorPublicKey").text(doctorPublicKey);
	//console.log("asdfsd"+patientPublicKey);
	fetch("http://10.10.1.93:5000/createPrescription", {
	  method: "post",
	  headers: {
	    'Accept': 'application/json',
	    'Content-Type': 'application/json'
	  },

	  //make sure to serialize your JSON body
		  body: JSON.stringify(
		  	{
		  		patientPublicKey: patientPublicKey,
		  		doctorPublicKey: doctorPublicKey,
		  		disease: disease,
		  		treatment: treatment,
		  		treatmentStatus: treatmentStatus,
		  	})
	})
	.then( (response) => (response.json()))
	.then(function(data){alert(data['status'])})
	.catch(function(res){ console.log(res) });
	return false;
}