function getDoctorDetails(){
	doctorPublicKey = $("#doctorPrimaryKey").val();
	//console.log("asdfsd"+doctorPublicKey);
	fetch("http://10.10.1.93:5000/doctorDetails", {
	  method: "post",
	  headers: {
	    'Accept': 'application/json',
	    'Content-Type': 'application/json'
	  },

	  //make sure to serialize your JSON body
	  body: JSON.stringify({id: doctorPublicKey+'' })
	})
	.then( (response) => (response.json()))
	.then(function(data){ 
		console.log(data)
		//alert("button Clicked"+data['Doctor']);
		$("#age").text(data['age']);
		$("#sex").text(data['sex']);
		$("#Speciality").text(data['speciality']);
		$('#details').css({'display':'block'});
		$('#prescrib').css({'display':'block'});
	   //do something awesome that makes the world a better place
	})
	.catch(function(res){ console.log(res) });
	return false;
}