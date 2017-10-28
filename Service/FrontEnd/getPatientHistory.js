function getPatientHistory(){
	patientPublicKey = $("#patientPublicKey").val();
	//console.log("asdfsd"+patientPublicKey);
	fetch("http://10.10.1.93:5000/patientHistory", {
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

		var col = [];
		for(var i=0;i<data.length;i++){
			for(var key in data[i]){
				if(col.indexOf(key) === -1){
					col.push(key);
				}
			}
		}

		var table = document.createElement("table");
		table.className="table";
		var tr=table.insertRow(-1);
		for(var i=0;i<col.length;i++){
			var th=document.createElement("th");
			th.innerHTML=col[i];
			tr.appendChild(th);
		}


		for(var i=0; i<data.length; i++){
			tr=table.insertRow(-1);
			for(var j=0;j<col.length;j++){
				var tabCell = tr.insertCell(-1);
				tabCell.innerHTML = data[i][col[j]];
			}
		}
		var divContainer = document.getElementById("showHistory");
		divContainer.innerHTML="";
		divContainer.appendChild(table );
		//do something awesome that makes the world a better place
	})
	.catch(function(res){ console.log(res) });
	return false;
}