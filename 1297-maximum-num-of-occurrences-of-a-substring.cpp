class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        int start = 0,result = 0;
        unordered_map<int,int> count; 
        unordered_map<string,int> occurence;     

        for(int i  =0; i < s.length(); i++) { //Sliding window
            count[s[i]]++;						
            if(i - start + 1 > minSize) {//Reduce the size of the window if increased to size.
                if(--count[s[start]] == 0)//Remove the letter from map if count 0 to track unique letters.
                    count.erase(s[start]);
                start++;
            }
            if(i - start + 1 == minSize && count.size() <= maxLetters) //When the substring in the window matches the constraints.
                result = max(result,++occurence[s.substr(start,i - start + 1)]); //Increase the occurence count of the string and get the max.
        }
        return result;
    }
};
