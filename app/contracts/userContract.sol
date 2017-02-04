pragma solidity ^0.4.7;

contract userRecord { 
	struct record {
		uint256 rec; 
		string link; 
	}
	record myrecord; 
	function uploadRecords(uint256 r, string l) { 
		myrecord = record(r, l);
	}
	
	function getHash() constant returns (uint256) {
		return myrecord.rec; 
	}
	
	function getLink() constant returns (string) { 
		return myrecord.link; 
	}	
}	
