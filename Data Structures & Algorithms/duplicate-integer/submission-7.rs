
impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut uniques = Vec::new();

        for num in nums.iter(){
            if uniques.contains(num) {
                return true;
            }
            uniques.push(*num);
        }
        false
    }
}
