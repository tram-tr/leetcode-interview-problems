class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int>hashMap;
        vector<int> ans {0,0};
        int diff = 0;

        for (size_t i = 0; i < nums.size(); i++) {
            if (hashMap.count(nums[i]) > 0) {
                ans[0] = hashMap[nums[i]];
                ans[1] = i;
                break;
            }

            diff = target - nums[i];
            hashMap[diff] = i;
        }

        return ans;
    }
};
