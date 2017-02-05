pragma solidity ^0.4.7;

contract userRecord { 
	struct record {
		uint256 rec; 
		string link; 
	}
	record myrecord;
	event upload(address _from, uint256 _rec, string _link); 
 
	function uploadRecords(uint256 r, string l) { 
		upload(msg.sender, r, l); 
	}
	
	function getHash() constant returns (uint256) {
		return myrecord.rec; 
	}
	
	function getLink() constant returns (string) { 
		return myrecord.link; 
	}	
}	
