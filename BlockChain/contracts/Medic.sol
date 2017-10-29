pragma solidity ^0.4.11;


contract Medic {
    event Treatment(address doctor, address patient, string treatments, string status, string disease);
    event RenalTest(address patient, uint8 Creatinine, uint8 Sodium, uint8 Potassium, uint8 eGFR, uint8 Urea);
    
    struct doctorDetail {
        string identityHash;
        uint8 age;
        string sex;
        string specialities;
    }

    struct patientDetail {
        string identityHash;
        uint8 age;
        string sex;
        string currentDiseases;
        string currentTreatments;
        string treatmentRestrictions;
        uint8 diseaseSeverity;
    }

    struct patientRenalProfile{
        uint8 Creatinine;
        uint8 Sodium;
        uint8 Potassium;
        uint8 eGFR;
        uint8 Urea;
    }

    struct diseaseDetail{
        string name;
        string symptoms;
    }

    struct drugDetail{
        string name;
        int qty;
        uint8 price;
        bool present;
    }

    mapping (address => doctorDetail) doctors;
    mapping (address => patientDetail) patients;
    mapping(address => patientRenalProfile) patientRenalProfiles;

    //drugs are refered with hash
    mapping (string => diseaseDetail) diseases;   //string of disease symptoms 

    //drugs are refered with hash
    mapping(string => drugDetail) unboughtDrug;
    mapping(string => drugDetail) boughtDrug;
    mapping(string => drugDetail) drugs;

    
    function Medic() {
        // doctorDetail storage d = doctorDetail(8,"m");
        
    }

    function test() returns (string) {
        return "aaa";
    }
    

    // ==========================================
    // Doctor Methods
    // ==========================================
    function getDoctorDetail(address doctor) returns (string,uint8,string,string) {
        return (doctors[doctor].identityHash,doctors[doctor].age,doctors[doctor].sex,doctors[doctor].specialities);
    }

    function addDoctor(string identityHash, uint8 age, string sex, string specialities) returns (address) {
        doctors[msg.sender]=doctorDetail(identityHash,age,sex,specialities);
        return msg.sender;
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
    function getPatientDetail(address patient) returns (string,uint8,string,string,string,string,uint8) {
        return (patients[patient].identityHash,patients[patient].age,patients[patient].sex,patients[patient].currentDiseases,patients[patient].currentTreatments,patients[patient].treatmentRestrictions,patients[patient].diseaseSeverity);
    }

    function addPatient(string identityHash,uint8 age, string sex, string currentDiseases, string currentTreatments, string treatmentRestrictions, uint8 diseaseSeverity) returns (address) {
        patients[msg.sender] = patientDetail(identityHash, age,sex,currentDiseases,currentTreatments,treatmentRestrictions,diseaseSeverity);
        return msg.sender;
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

    // Patient's Renal profiles
    function getPatientRenalProfile(address patient) returns (uint8,uint8,uint8,uint8,uint8) {
        return (patientRenalProfiles[patient].Creatinine,patientRenalProfiles[patient].Sodium,patientRenalProfiles[patient].Potassium,patientRenalProfiles[patient].eGFR,patientRenalProfiles[patient].Urea);
    }
    
    function setPatientRenalProfile(address patient, uint8 Creatinine, uint8 Sodium, uint8 Potassium, uint8 eGFR, uint8 Urea) returns (bool) {
        patientRenalProfiles[patient]= patientRenalProfile(Creatinine,Sodium,Potassium,eGFR,Urea);
        RenalTest(patient,Creatinine,Sodium,Potassium,eGFR,Urea);
        return true;
    }

    
    
    


    // ==========================================
    // Disesase Methods
    // ==========================================
    function getDiseaseDetail(string diseaseHash) returns (string,string){
        return(diseases[diseaseHash].name,diseases[diseaseHash].symptoms);
    }
    function addDisease(string diseaseHash, string name, string symptomList) {
        diseases[diseaseHash]=diseaseDetail(name,symptomList);
    }


    // ==========================================
    // Drugs methods
    // ==========================================
    function getDrugDetails(string drugHash) returns (string,int,uint8,bool){
        return (drugs[drugHash].name,drugs[drugHash].qty,drugs[drugHash].price,drugs[drugHash].present);
    }

    function sellDrug(string drugHash,string name,  int qty, uint8 price) returns (bool){
        unboughtDrug[drugHash]= drugDetail(name,qty,price,true);
        drugs[drugHash]= drugDetail(name,qty,price,true);
        return true;
    }

    function drugBuy(string drugHash) returns (bool){
        if (unboughtDrug[drugHash].present) {
            boughtDrug[drugHash]=unboughtDrug[drugHash];
            delete unboughtDrug[drugHash];
            return true;
        }
        return false;
    }
    
}