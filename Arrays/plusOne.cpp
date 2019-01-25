class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool carry = true; 
        for (int i=digits.size()-1; i>=0 && carry; i--){
            digits[i] = (++digits[i])%10;
            if (digits[i] == 0)
                carry = 1;
            else
                carry = 0;
        }
        
        if (carry)
             digits.insert(digits.begin(), 1);
        
        return digits;
    }
};
