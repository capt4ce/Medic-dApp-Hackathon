pragma solidity ^0.4.11;

contract Patient {

    struct patientDetail{
        uint8 age;
        string sex;
        string currentDiseases;
        string currentTreatments;
        string treatmentRestrictions;
    }
    
    mapping (address => patientDetail) patients;

    
    function Patient() {
        // doctorDetail storage d = doctorDetail(8,"m");
        
    }
    
    function getDetail(address patient) returns (patientDetail) {
        return patients[patient];
    }
    
    function addPatient(address patient, uint8 age, string sex, string currentDiseases, string currentTreatments, string treatmentRestrictions) returns (bool) {
        patients[patient]=patientDetail(age,sex,currentDiseases,currentTreatments,treatmentRestrictions);
        return true;
    }
    
    function changeAge(address patient, uint8 age) {
        patients[patient].age=age;
    }
    
    function changeSex(address patient, string sex) {
        patients[patient].sex=sex;
    }
    
    function changeCurrentDiseases(address patient, string currentDiseases) {
        patients[patient].currentDiseases=currentDiseases;
    }
    
    function changeCurrentTreatments(address patient, string currentTreatments) {
        patients[patient].currentTreatments=currentTreatments;
    }
    
    function changeTreatmentRestrictions(address patient, string treatmentRestrictions) {
        patients[patient].treatmentRestrictions=treatmentRestrictions;
    }
    
    
}