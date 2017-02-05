pragma solidity ^0.4.7;

contract userRecord { 

	struct record {
		uint256 rec; 	//the hash
		//string link; 	//link to the database
		int hospitalID; 	//Hospital ID where the patient take the record
		int userID;		//User ID
	}
	record myrecord;
	event upload(address _from, uint256 _rec, string _link); 

 	
	//Create events uploadRecord
	function uploadRecords(uint256 r, string l) { 
		upload(msg.sender, r, l); 
	}

	
	//returns the hash stored for the user
	function getHash() constant returns (uint256) {
		return myrecord.rec; 
	}
	

	//gives back the link for the database	
	function getLink() constant returns (string) { 
		return myrecord.link; 
	}	
}	
