contract DrugTransaction {
    struct drugDetail{
        string name;
        int qty;
        uint8 price;
        bool present;
    }
    
    //drugs are refered with hash
    mapping(string => drugDetail) unboughtDrug;
    mapping(string => drugDetail) boughtDrug;
    

    function DrugTransaction() {

    }
    
    function sellDrug(string drugHash,string name,  int qty, uint8 price) returns (bool){
        unboughtDrug[drugHash]= drugDetail(name,qty,price,true);
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