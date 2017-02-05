pragma solidity ^0.4.7;

contract userContract { 

	struct record {
		uint256 rec; 	//the hash
		//string link; 	//link to the database
		int hospitalID; 	//Hospital ID where the patient take the record
		int userID;		//User ID
	}
	record myrecord;
	event upload(address _from, uint256 _rec, int h_id, int u_id); 

 	
	//Create events uploadRecord
	function uploadRecords(uint256 r, int h_id, int u_id) { 
		upload(msg.sender, r, h_id, u_id); 
	}

	
	//returns the hash stored for the user
	function getHash() constant returns (uint256) {
		return myrecord.rec; 
	}
	

	//gives back the link for the database	
	//function getLink() constant returns (string) { 
	//	return myrecord.link; 
	//}	
}	
