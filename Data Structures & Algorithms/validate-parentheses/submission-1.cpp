class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        unordered_map<char, char> closeOpen = {{')', '('}, {'}', '{'}, {']', '['}};

        for (char c : s){
            if (closeOpen.count(c)){
                if(!stack.empty() && stack.top() == closeOpen[c]){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stack.push(c);
            }
        }

        if(!stack.empty()){
            return false;
        }
        return true;
    }
};
