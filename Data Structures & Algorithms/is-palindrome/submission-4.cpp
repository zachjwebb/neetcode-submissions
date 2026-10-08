class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size()-1;

        while (l < r){

            if(l < r and !isalnum(s[l])){
                l++;
                continue;
            }
            if(tolower(r) > l and !isalnum(s[r])){
                r--;
                continue;
            }
            if(tolower(s[l]) != tolower(s[r])){
                return false;
            }

            l++;
            r--;

        }

        return true;
    }
};
