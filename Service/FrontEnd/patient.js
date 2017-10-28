function getPatientDetails(){
	patientPublicKey = $("#patientPrimaryKey").val();
	//console.log("asdfsd"+patientPublicKey);
	fetch("http://10.10.1.93:5000/patientDetails", {
	  method: "post",
	  headers: {
	    'Accept': 'application/json',
	    'Content-Type': 'application/json'
	  },

	  //make sure to serialize your JSON body
	  body: JSON.stringify({id: patientPublicKey })
	})
	.then( (response) => (response.json()))
	.then(function(data){ 
		console.log(data)
		//alert("button Clicked"+data['Patient']);
		$("#patientName").text(data['Patient']);
		$("#age").text(data['Patient']);
		$("#sex").text(data['Patient']);
		$("#currentDisease").text(data['Disease']);
		$("#currentTreatment").text(data['Patient']);
		$("#treatmentConstraints").text(data['Patient']);
		$('#details').css({'display':'block'});
	   //do something awesome that makes the world a better place
	})
	.catch(function(res){ console.log(res) });
	return false;
}