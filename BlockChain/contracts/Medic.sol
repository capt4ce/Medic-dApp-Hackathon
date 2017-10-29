pragma solidity ^0.4.11;


contract Medic {
    event Treatment(address doctor, address patient, string treatments, string status, string disease);
    
    struct doctorDetail {
        uint8 age;
        string sex;
        string specialities;
    }

    struct patientDetail {
        uint8 age;
        string sex;
        string currentDiseases;
        string currentTreatments;
        string treatmentRestrictions;
    }

    mapping (address => doctorDetail) doctors;
    mapping (address => patientDetail) patients;
    mapping (string => string) diseases;   //string of disease symptoms 

    
    function Medic() {
        // doctorDetail storage d = doctorDetail(8,"m");
        
    }
    

    // ==========================================
    // Doctor Methods
    // ==========================================
    function getDoctorDetail(address doctor) returns (doctorDetail) {
        return doctors[doctor];
    }
    
    function addDoctor(uint8 age, string sex, string specialities) returns (bool) {
        doctors[msg.sender]=doctorDetail(age,sex,specialities);
        return true;
    }
    
    function changeAge(uint8 age) {
        doctors[msg.sender].age=age;
    }
    
    function changeSex(string sex) {
        doctors[msg.sender].sex=sex;
    }
    
    function changeSpecialities(string specialities) {
        doctors[msg.sender].specialities=specialities;
    }
    
    // can we filter element inside array in the event?
    function issueTreatmentRecord(address patient, string treatments, string treatmentStatus, string disease) {
        Treatment(msg.sender,patient,treatments, treatmentStatus,disease);
    }


    // ==========================================
    // Patient Methods
    // ==========================================    
    function getPatientDetail(address patient) returns (patientDetail) {
        return patients[patient];
    }
    
    function addPatient(uint8 age, string sex, string currentDiseases, string currentTreatments, string treatmentRestrictions) returns (bool) {
        patients[msg.sender] = patientDetail(age,sex,currentDiseases,currentTreatments,treatmentRestrictions);
        return true;
    }
    
    function changePatientAge(address patient, uint8 age) {
        patients[patient].age=age;
    }
    
    function changePatientSex(address patient, string sex) {
        patients[patient].sex=sex;
    }
    
    function changePatientCurrentDiseases(address patient, string currentDiseases) {
        patients[patient].currentDiseases=currentDiseases;
    }
    
    function changePatientCurrentTreatments(address patient, string currentTreatments) {
        patients[patient].currentTreatments=currentTreatments;
    }
    
    function changePatientTreatmentRestrictions(address patient, string treatmentRestrictions) {
        patients[patient].treatmentRestrictions=treatmentRestrictions;
    }

    function addDisease(string disease, string symptomList) {
        diseases[disease]=symptomList;
    }
    
}