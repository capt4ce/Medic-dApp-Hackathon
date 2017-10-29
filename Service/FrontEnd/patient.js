function getPatientDetails(){
	patientPublicKey = $("#patientPublicKey").val();
	//console.log("asdfsd"+patientPublicKey);
	fetch("http://10.10.1.93:5000/patientDetails", {
	  method: "post",
	  headers: {
	    'Accept': 'application/json',
	    'Content-Type': 'application/json'
	  },

	  //make sure to serialize your JSON body
	  body: JSON.stringify({id: patientPublicKey+'' })
	})
	.then( (response) => (response.json()))
	.then(function(data){ 
		console.log(data)
		//alert("button Clicked"+data['Patient']);
		$("#age").text(data['age']);
		$("#sex").text(data['sex']);
		$("#currentDisease").text(data['currentDisease']);
		$("#currentTreatment").text(data['currentTreatment']);
		$("#treatmentConstraints").text(data['treatmentConstraints']);
		$('#details').css({'display':'block'});
		$('#getH').css({'display':'block'});
	   //do something awesome that makes the world a better place
	})
	.catch(function(res){ console.log(res) });
	return false;
}