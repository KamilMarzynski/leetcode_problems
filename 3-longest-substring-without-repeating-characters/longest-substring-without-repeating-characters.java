class Solution {
    public int lengthOfLongestSubstring(String s) {
        String subString = "";
        int longest = 0;

        for (char c : s.toCharArray()) {
            int index = subString.indexOf(c);
            if (index == -1) {
                subString += c;
                System.out.println(subString);
                int length = subString.length();
                if(length > longest) {
                    longest = length;
                }
            } else {
                subString = subString.substring(index + 1);
                subString += c;
            }
        }

        return longest;
    }
}