pragma solidity ^0.4.0;

// import "./helper/stringUtils.sol";
// import "./helper/jsmnSolLib.sol";

contract Doctor {
    // struct doctorDetail {
    //     bytes32 sex;
    //     int8 age;
    //     // string[] specialityList;
    // }
    struct Bank {
    address owner;
    uint balance;
}

    // mapping (address => doctorDetail) public doctorList;

    function Doctor() {
        // doctorDetail a = doctorDetail("m" , 30);
        //  a.sex="f";
        c = Bank({
    owner: msg.sender,
    balance: 5
});
        c.balance = 5;
    }

    // function getDetail(address key) returns (bytes1, int8, string[]) {
    //     doctorDetail d = doctorList[key];
    //     return d.sex,d.age,d.specialityList;
    // }

    function testOutput() returns (string){
        return "aaa";
    }

}